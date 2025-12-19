# %%
# 1. 데이터 읽기
import pandas as pd

uriage_data = pd.read_csv('data/uriage.csv')
kokyaku_data = pd.read_excel('data/kokyaku_daicho.xlsx')


# %%
# 2. 데이터 오류 파악
uriage_data.head()
kokyaku_data.head()

# %%
# 3. 오류 있는 채로 집계
uriage_data['purchase_date'] = pd.to_datetime(uriage_data['purchase_date'])
uriage_data['purchase_month'] = uriage_data['purchase_date'].dt.strftime("%Y%m")
res = uriage_data.pivot_table(index = 'purchase_month', columns = 'item_name', values = 'item_price', aggfunc = 'sum', fill_value = 0)
res
# %%
# 4. 오류 수정
uriage_data['item_name'] = uriage_data['item_name'].str.upper()
uriage_data['item_name'] = uriage_data['item_name'].str.replace(" ","")

uriage_data.sort_values(by=['item_name'], ascending=True)
print(len(pd.unique(uriage_data.item_name)))
# %%
# 5. 결측치 수정
uriage_data.isnull().any(axis=0)

flg_is_null = uriage_data['item_price'].isnull()

for trg in list(uriage_data.loc[flg_is_null, 'item_name'].unique()):    
    price = uriage_data.loc[(~flg_is_null) & (uriage_data['item_name']==trg), 'item_price'].max()
    uriage_data['item_price'].loc[(flg_is_null)&(uriage_data['item_name']==trg)] = price
    print(trg,price)

uriage_data.head()
uriage_data.isnull().any(axis=0)

for trg in list(uriage_data['item_name'].sort_values().unique()):
    print(trg + '의 최고가 : ' + str(uriage_data.loc[uriage_data['item_name']==trg]['item_price'].max()) 
          + '의 최저가 : ' + str(uriage_data.loc[uriage_data['item_name']==trg]['item_price'].min(skipna=False)))

# %%
# 6. 고객 이름 오류 수정
kokyaku_data["고객이름"].head
uriage_data["customer_name"].head()

kokyaku_data['고객이름'] = kokyaku_data['고객이름'].str.replace(" ","")
kokyaku_data['고객이름'] = kokyaku_data['고객이름'].str.replace("  ","")

kokyaku_data["고객이름"].head

# %%
# 7. 날짜 오류 수정
flg_is_serial = kokyaku_data["등록일"].astype('str').str.isdigit()
flg_is_serial.sum()

fromSerial = pd.to_timedelta(kokyaku_data.loc[flg_is_serial, '등록일'].astype('float'),unit='D') + pd.to_datetime('1900/01/01')
fromSerial

fromString = pd.to_datetime(kokyaku_data.loc[~flg_is_serial,'등록일'])
fromString

kokyaku_data["등록일"] = pd.concat([fromSerial, fromString])
kokyaku_data

flg_is_serial = kokyaku_data["등록일"].astype('str').str.isdigit()
flg_is_serial.sum()
# %%
# 8. 고객이름을 키로 데이터 결합(조인)
join_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on="고객이름", how="left")
join_data = join_data.drop("customer_name", axis=1)
join_data
# %%
# 9. 정제한 데이터 덤프
dump_data = join_data[["purchase_date", "purchase_month", "item_name", "item_price", "고객이름", "지역", "등록일"]]
dump_data

dump_data.to_csv("dump_data.csv", index=False)
# %%
# 10. 데이터 집계
import_data = pd.read_csv("dump_data.csv")
import_data

byItem = import_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
byItem

byPrice = import_data.pivot_table(index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
byPrice

byCustomer = import_data.pivot_table(index="purchase_month", columns="고객이름", aggfunc="size", fill_value=0)
byCustomer

byRegion = import_data.pivot_table(index="purchase_month", columns="지역", aggfunc="size", fill_value=0)
byRegion

away_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on="고객이름", how="right")
away_data[away_data["purchase_date"].isnull()][["고객이름", "등록일"]]
