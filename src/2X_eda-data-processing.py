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
# 6. 