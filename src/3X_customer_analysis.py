# %%
# 1. 데이터 읽기
import pandas as pd
uselog = pd.read_csv('data/use_log.csv')
print(len(uselog))
uselog.head()

customer = pd.read_csv('data/customer_master.csv')
print(len(customer))
customer.head()

class_master = pd.read_csv('data/class_master.csv')
print(len(class_master))
class_master.head()

campaign_master = pd.read_csv('data/campaign_master.csv')
print(len(campaign_master))
campaign_master.head()
# %%
# 2. 데이터 가공
customer.isnull().sum()

customer_join = pd.merge(customer, class_master, on="class", how="left")
customer_join = pd.merge(customer_join, campaign_master, on="campaign_id", how="left")
customer_join.head()

print(len(customer))
print(len(customer_join))

customer_join.isnull().sum()
# %%
# 3. 데이터 집계
customer_join.groupby("class_name").count()["customer_id"]
customer_join.groupby("campaign_name").count()["customer_id"]
customer_join.groupby("gender").count()["customer_id"]
customer_join.groupby("is_deleted").count()["customer_id"]

customer_join["start_date"] = pd.to_datetime(customer_join["start_date"])
customer_start = customer_join.loc[customer_join["start_date"]>pd.to_datetime("20180401")]
print(len(customer_start))
# %%
# 4. 최근 데이터 집계
customer_join["end_date"] = pd.to_datetime(customer_join["end_date"])
customer_newer = customer_join.loc[(customer_join["end_date"]>=pd.to_datetime("20190331"))|(customer_join["end_date"].isna())]
print(len(customer_newer))
customer_newer["end_date"].unique()

customer_newer.groupby("class_name").count()["customer_id"]
customer_newer.groupby("campaign_name").count()["customer_id"]
customer_newer.groupby("gender").count()["customer_id"]
# %%
# 5. 이용 이력 데이터 집계
uselog["usedate"] = pd.to_datetime(uselog["usedate"])
uselog["연월"] = uselog["usedate"].dt.strftime("%Y%m")
uselog_months = uselog.groupby(["연월","customer_id"],as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]
uselog_months.head()
# %%
