
# %% 
# 1. 데이터 읽기 및 출력
import pandas as pd
customer_master=pd.read_csv('data/customer_master.csv')
item_master = pd.read_csv('data/item_master.csv')
transaction_1 = pd.read_csv('data/transaction_1.csv')
transaction_2 = pd.read_csv('data/transaction_2.csv')
transaction_detail_1 = pd.read_csv('data/transaction_detail_1.csv')
transaction_detail_2 = pd.read_csv('data/transaction_detail_2.csv')

display(customer_master.head())

# %%
# 2. 데이터 결합(유니언)
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

transaction_detail.describe()
# %%
# 3. 데이터 결합(조인)
join_data = pd.merge(transaction_detail, transaction[["transaction_id","payment_date","customer_id"]], on= "transaction_id", how = "left")

join_data.head()
# %%
# 4. 마스터 데이터 결합(조인)
join_data = pd.merge(join_data, customer_master, on= "customer_id", how = "left")
join_data = pd.merge(join_data, item_master, on= "item_id", how = "left")

join_data.head()
# %%
# 5. 필요한 데이터 칼럼 생성
join_data["price"]=join_data["quantity"]*join_data["item_price"]

join_data.head()

# %%
# 6. 데이터 검산(price)
join_data["price"].sum() == transaction["price"].sum()

# %%
# 7. 각종 통계량 확인
join_data.isnull().sum()
join_data.describe()

join_data["payment_date"].min()
join_data["payment_date"].max()

join_data.head()
# %%
# 8. 월별 데이터 집계
join_data["payment_date"] = pd.to_datetime(join_data["payment_date"])
join_data["payment_month"] = join_data["payment_date"].dt.strftime("%Y%m")
join_data[["payment_date","payment_month"]].head()

join_data.groupby("payment_month")["price"].sum()

# %%
# 9. 월별, 상품별 데이터 집계
join_data.groupby(["payment_month","item_name"])[["price","quantity"]].sum()
pd.pivot_table(join_data, index='item_name',columns='payment_month',values=['price','quantity'],aggfunc='sum')
# %%
# 10. 가시화

graph_data = pd.pivot_table(join_data, index='payment_month',columns='item_name',values='price',aggfunc='sum')

import matplotlib.pyplot as plt
#%matplotlib inline
plt.plot(list(graph_data.index),graph_data["PC-A"],label='PC-A')
plt.plot(list(graph_data.index),graph_data["PC-B"],label='PC-B')
plt.plot(list(graph_data.index),graph_data["PC-C"],label='PC-C')
plt.plot(list(graph_data.index),graph_data["PC-D"],label='PC-D')
plt.plot(list(graph_data.index),graph_data["PC-E"],label='PC-E')

plt.legend()
