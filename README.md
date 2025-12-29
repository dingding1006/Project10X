# Project10X

다양한 주제로 10개의 프로젝트를 진행.

포트폴리오 작성 및 성장과정

# 📊 Customer Usage & Membership EDA Project

## 1. Project Overview

본 프로젝트는 **회원 마스터 데이터, 이용 로그 데이터, 클래스 및 캠페인 정보**를 활용하여  
회원의 이용 패턴과 유지 기간을 분석하는 **Exploratory Data Analysis (EDA)** 프로젝트입니다.

데이터 정제 → 집계 → 파생 변수 생성 → 통계 분석의 흐름을 통해  
정기 이용 고객과 탈퇴/유지 회원의 차이를 분석합니다.

---

## 2. Project Structure
```text
.
├── data/
│ ├── use_log.csv
│ ├── customer_master.csv
│ ├── class_master.csv
│ └── campaign_master.csv
├── customer_join.csv
└── src/
└── customer_eda.py

```
---

## 3. Dataset Overview

### use_log.csv (이용 로그 데이터)
- log_id : 이용 로그 ID
- customer_id : 고객 ID
- usedate : 이용 날짜

### customer_master.csv (회원 마스터 데이터)
- customer_id : 고객 ID
- gender : 성별
- class : 수강 클래스 코드
- campaign_id : 캠페인 ID
- start_date : 가입일
- end_date : 탈퇴일
- is_deleted : 탈퇴 여부 (1: 탈퇴, 0: 유지)

### class_master.csv
- class : 클래스 코드
- class_name : 클래스명

### campaign_master.csv
- campaign_id : 캠페인 ID
- campaign_name : 캠페인명

---

## 4. Tech Stack

- Python
- pandas
- matplotlib
- python-dateutil (relativedelta)

---

## 5. Data Processing Flow

### 5.1 데이터 로드
- 이용 로그, 회원 마스터, 클래스, 캠페인 데이터 로드
- 데이터 건수 및 기본 구조 확인

### 5.2 마스터 데이터 결합
- 회원 마스터 + 클래스 정보 (Left Join)
- 회원 마스터 + 캠페인 정보 (Left Join)
- 결합 후 결측치 확인

### 5.3 기본 집계
- 클래스별 회원 수
- 캠페인별 회원 수
- 성별 회원 수
- 탈퇴/유지 회원 수

### 5.4 최근 회원 기준 분석
- 종료일 기준 최근 시점 이후 유지 회원 필터링
- 최근 회원의 클래스/캠페인/성별 분포 확인

---

## 6. Usage Log Aggregation

### 6.1 월별 이용 횟수 집계
- 이용 날짜를 기준으로 연월(YYYYMM) 생성
- 고객별 · 월별 이용 횟수 집계

### 6.2 고객별 이용 통계 생성
- 평균 이용 횟수 (mean)
- 중앙값 (median)
- 최대 이용 횟수 (max)
- 최소 이용 횟수 (min)

---

## 7. Routine Customer Flag 생성

- 이용 날짜에서 요일 정보 추출
- 고객 · 월 · 요일별 이용 횟수 집계
- 특정 요일 월 최대 이용 횟수 ≥ 4 인 경우
  - routine_flg = 1
  - 그 외 = 0

---

## 8. Membership Period 계산

- 종료일이 없는 회원은 기준일로 대체
- 가입일과 종료일 간의 차이를 개월 단위로 계산
- relativedelta를 사용하여 정확한 기간 산출

---

## 9. Statistical Analysis & Visualization

- 고객별 이용 통계 요약
- 정기 이용 여부 분포 확인
- 회원 유지 기간 히스토그램 시각화

---

## 10. Churn vs Retention Analysis

### 탈퇴 회원
- is_deleted = 1
- 이용 패턴 및 유지 기간 분석

### 지속 회원
- is_deleted = 0
- 이용 패턴 및 유지 기간 비교

---

## 11. Output

- 최종 분석 데이터: customer_join.csv
- 추가 분석 및 모델링을 위한 Feature Dataset으로 활용 가능

---

## 12. Key Takeaways

- 이용 빈도와 정기성은 회원 유지와 강한 상관관계가 있음
- 반복 이용 패턴은 장기 유지 고객의 주요 특징
- EDA 전형 흐름(정제 → 집계 → 파생 변수 → 분석) 경험

---

## 13. Future Improvements

- 코호트 분석
- 이탈 예측 모델링
- 클래스/캠페인별 LTV 분석
- 시계열 기반 이용 패턴 분석
