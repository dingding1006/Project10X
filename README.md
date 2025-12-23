# Sales & Customer Data EDA Project

## Project Overview
이 프로젝트는 매출 데이터(uriage)와 고객 마스터 데이터(kokyaku)를 활용하여  
데이터 오류를 정제하고, 월별·상품별·고객별·지역별 매출 현황을 분석하는  
Exploratory Data Analysis(EDA) 프로젝트입니다.

---

## Project Structure

.
├── data/
│   ├── uriage.csv
│   └── kokyaku_daicho.xlsx
├── dump_data.csv
└── src/
    └── 2X_eda-data-processing.py

- uriage.csv : 매출(거래) 데이터
- kokyaku_daicho.xlsx : 고객 마스터 데이터
- dump_data.csv : 정제 완료 후 분석용 데이터
- 2X_eda-data-processing.py : 전체 EDA 및 데이터 정제 코드

---

## Dataset Overview

### uriage.csv
- purchase_date : 구매 일시
- item_name : 상품명
- item_price : 상품 단가
- customer_name : 고객 이름

### kokyaku_daicho.xlsx
- 고객이름
- 지역
- 등록일

---

## Tech Stack
- Python
- pandas
- openpyxl

---

## EDA Process
- 데이터 로드
- 데이터 오류 확인
- 상품명 정제
- 상품 단가 결측치 보정
- 고객 이름 정제
- 고객 등록일 정제
- 매출 데이터 기준 고객 정보 Left Join
- 정제 데이터 CSV 저장

---

## Aggregation & Analysis
- 월별·상품별 판매 건수
- 월별·상품별 매출 합계
- 고객별 구매 빈도
- 지역별 구매 빈도

---

## Non-Purchasing Customer Analysis
고객 마스터 기준 Right Join을 수행하여  
구매 이력이 없는 고객을 식별합니다.

---

## Key Takeaways
- 데이터 정제의 중요성 이해
- 데이터 오류가 집계 결과에 미치는 영향 확인
- Left Join과 Right Join의 차이 이해
- 실무형 EDA 흐름 경험

---

## Future Improvements
- 매출 시각화
- 고객 세그먼트 분석
- 재구매율 분석
