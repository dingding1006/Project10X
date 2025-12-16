# Sales EDA Project (Pandas)

이 프로젝트는 고객/상품 마스터와 거래(헤더/디테일) 데이터를 결합해,
월별 매출 및 상품별 매출 트렌드를 분석(EDA)하고 간단한 시각화를 수행합니다.

## 📁 Project Structure
```text
project-folder/
├── data/
│   ├── customer_master.csv
│   ├── item_master.csv
│   ├── transaction_1.csv
│   ├── transaction_2.csv
│   ├── transaction_detail_1.csv
│   └── transaction_detail_2.csv
└── src/
    └── eda_web_orders.py
```   

> `data/` 폴더 내 CSV 파일이 필수입니다.

## 🧩 Dataset Overview

- `customer_master.csv`: 고객 마스터(고객 정보)
- `item_master.csv`: 상품 마스터(상품 정보 및 단가)
- `transaction_1.csv`, `transaction_2.csv`: 거래 헤더 데이터(결제일, 고객, 거래금액 등)
- `transaction_detail_1.csv`, `transaction_detail_2.csv`: 거래 상세 데이터(상품, 수량 등)

## 🛠️ Tech Stack

- Python
- pandas
- matplotlib

## ✅ What This EDA Does

### 1) 데이터 로드
여러 CSV 파일을 읽어들인 후 데이터 형태를 확인합니다.

### 2) 거래/거래상세 데이터 유니언(Concat)
`transaction_1 + transaction_2`  
`transaction_detail_1 + transaction_detail_2`  
→ 각각 하나의 테이블로 통합합니다.

### 3) 거래상세 + 거래헤더 조인(Merge)
`transaction_id` 기준으로 거래상세에 `payment_date`, `customer_id`를 붙입니다.

### 4) 마스터 데이터 조인
- 고객 마스터: `customer_id` 기준 조인
- 상품 마스터: `item_id` 기준 조인

### 5) 파생 변수 생성
- `price = quantity * item_price`

### 6) 데이터 검산(Validation)
파생 변수로 만든 상세 매출 합계(`join_data["price"].sum()`)와  
거래헤더의 매출 합계(`transaction["price"].sum()`)가 같은지 확인합니다.

### 7) 기본 통계/결측 확인
- 결측치 개수 확인: `isnull().sum()`
- 기술통계: `describe()`
- 결제일 범위: `payment_date` min/max

### 8) 월별 매출 집계
- `payment_date`를 datetime으로 변환
- `payment_month(YYYYMM)` 생성
- 월별 매출 합계 집계

### 9) 월별/상품별 매출 및 수량 집계
- groupby로 월/상품 단위 집계
- pivot_table로 월별 상품 매출/수량 테이블 생성

### 10) 시각화(상품별 월 매출 트렌드)
상품 `PC-A ~ PC-E`의 월별 매출(price)을 라인 차트로 시각화합니다.

## 🚀 How to Run

### Option 1) Python script 실행
```bash
pip install pandas matplotlib
python src/eda_web_orders.py
