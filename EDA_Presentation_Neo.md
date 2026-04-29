---
marp: true
theme: default
paginate: true
backgroundColor: #0f0c29
header: "NEMO EDA : AUTHENTIC GLASSMORPHISM"
footer: "© 2026 PREMIUM DATA DASHBOARD"
style: |
  section {
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    /* 딥 그라디언트 배경 */
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    padding: 80px 70px 110px 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #ffffff;
    word-break: keep-all;
    overflow: hidden;
  }
  /* 배경 기하학 도형 효과 */
  section::before {
    content: "";
    position: absolute;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(157, 80, 187, 0.4) 0%, rgba(0, 0, 0, 0) 70%);
    top: -50px; right: -50px;
    border-radius: 50%;
    z-index: 0;
  }
  section::after {
    content: "";
    position: absolute;
    width: 250px; height: 250px;
    background: radial-gradient(circle, rgba(0, 210, 255, 0.3) 0%, rgba(0, 0, 0, 0) 70%);
    bottom: -30px; left: -30px;
    border-radius: 50%;
    z-index: 0;
  }
  /* 유리 카드 본체 */
  .glass-card {
    position: relative;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    border-radius: 32px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 40px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
    z-index: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    font-size: 45px;
    color: #ffffff;
    margin: 0 0 15px 0;
    font-weight: 800;
    letter-spacing: -1px;
  }
  h2, h3 {
    font-size: 28px;
    color: #00d2ff;
    margin: 5px 0;
    font-weight: 700;
  }
  p, li {
    font-size: 18px;
    color: #f0f0f0;
    font-weight: 400;
    line-height: 1.5;
    margin: 5px 0;
  }
  ul {
    margin-left: 20px;
    list-style: none;
  }
  li::before {
    content: "●";
    color: #00d2ff;
    display: inline-block;
    width: 1.5em;
    margin-left: -1.5em;
    font-size: 0.8em;
  }
  img {
    max-height: 220px;
    width: auto;
    display: block;
    margin: 15px auto;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
  }
  header {
    top: 30px;
    font-size: 11px;
    color: rgba(255, 255, 255, 0.6);
    font-weight: 600;
    letter-spacing: 2px;
    z-index: 2;
  }
  footer {
    bottom: 30px;
    font-size: 11px;
    color: rgba(255, 255, 255, 0.6);
    font-weight: 600;
    letter-spacing: 1px;
    z-index: 2;
  }
---

<div class="glass-card">

# 네모 상가 데이터 보고서
### 정통 글래스모피즘 에디션

</div>

<!-- 
발표자 노트 (2분):
사용자님께서 제안해주신 정통 글래스모피즘 스타일을 완벽하게 재현했습니다. 딥한 배경 위로 떠오른 투명한 유리 카드와 배경의 은은한 조명이 조화를 이루어, 분석 데이터의 신뢰도를 시각적으로 격상시켰습니다.
-->

---

<div class="glass-card">

# 00. 목차

- 01. 데이터 개요 및 품질
- 02. 핵심 통계 요약
- 03. 데이터 시각화 인사이트
- 04. 매물 제목 키워드 분석
- 05. 비즈니스 전략 제안

</div>

---

<div class="glass-card">

# 01. 데이터 개요

- 전체 데이터 수: 2,169건 (높은 신뢰도)
- 컬럼 수: 40개 (심층 분석 가능)
- 중복 데이터: 0건 (완벽한 정제)
- 분석 중심: 강남권 상업용 부동산

</div>

---

<div class="glass-card">

# 02. 핵심 지표 요약

- 평균 보증금: 5,761만 원
- 평균 월세: 440만 원
- 평균 권리금: 3,862만 원
- 평균 면적: 136㎡ (약 41평)

</div>

---

<div class="glass-card">

# 03. 업종별 분포
![center](images/01_large_code_freq.png)
- 주요 업종: 기타, 음식점, 서비스업 순
- 시사점: 전통적인 먹거리 상권의 높은 경쟁 강도

</div>

---

<div class="glass-card">

# 03. 보증금 분포 분석
![center](images/02_deposit_dist.png)
- 전형적인 롱테일(Long-tail) 분포
- 중앙값(50%): 4,000만 원 선 형성

</div>

---

<div class="glass-card">

# 03. 면적 대비 월세
![center](images/03_size_rent_scatter.png)
- 상관관계: 0.15 (매우 낮음)
- 인사이트: 면적보다 '입지'가 임대료의 핵심

</div>

---

<div class="glass-card">

# 03. 층수별 임대료 차이
![center](images/04_floor_rent_avg.png)
- 1층 매물의 압도적 우위 확인
- 접근성 프리미엄이 가격에 그대로 반영

</div>

---

<div class="glass-card">

# 03. 권리금 현황
![center](images/05_state_premium_box.png)
- 상가 상태에 따른 극단적 이상치 존재
- 진입 시 권리금 리스크 검토 필수

</div>

---

<div class="glass-card">

# 03. 거래 형태 비중
![center](images/06_price_type_pie.png)
- 월세 매물이 전체의 99% 이상 차지
- 현금 흐름 중심의 사업 계획 필요

</div>

---

<div class="glass-card">

# 03. 인기 업종 TOP 20
![center](images/07_middle_code_top20.png)
- 카페 및 한식 업종이 시장 주도
- 높은 교체율을 보이는 과열 경쟁 섹션

</div>

---

<div class="glass-card">

# 03. 조회수와 찜 수
![center](images/08_view_favorite_scatter.png)
- 온라인 노출도가 실제 관심도로 직결
- 마케팅 데이터 기반의 매칭 효율성 증명

</div>

---

<div class="glass-card">

# 03. 월세와 관리비 관계
![center](images/09_rent_maintenance_scatter.png)
- 두 변수 간의 독립적 상관관계 확인
- 총 점유 비용(Total Cost) 산출의 중요성

</div>

---

<div class="glass-card">

# 04. 핵심 키워드 분석
![center](images/11_text_keyword_tfidf.png)
- 주요 키워드: 무권리, 역세권, 대로변
- 고객 유입을 결정짓는 핵심 언어 추출

</div>

---

<div class="glass-card">

# 05. 종합 전략 제안

- [1] 데이터 기반 정밀 가치 평가 도입
- [2] 단계별 타겟 마케팅 최적화
- [3] 총비용 투명성 강화를 통한 신뢰 확보
- [4] 실시간 상권 트렌드 모니터링

</div>

---

<div class="glass-card">

# Q & A

### 감사합니다.
### 글래스모피즘 에디션 종료.

</div>
