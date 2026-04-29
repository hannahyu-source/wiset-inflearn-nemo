---
marp: true
theme: default
paginate: true
backgroundColor: #0f0c29
header: "NEMO EDA : PREMIUM GLASSMORPHISM"
footer: "© 2026 DATA INSIGHT DASHBOARD"
style: |
  section {
    font-family: 'Malgun Gothic', sans-serif;
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    padding: 60px 50px 140px 50px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    color: #ffffff;
    word-break: keep-all;
    overflow: hidden;
  }
  section::before {
    content: "";
    position: absolute;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(157, 80, 187, 0.3) 0%, rgba(0, 0, 0, 0) 70%);
    top: -100px; right: -100px;
    border-radius: 50%;
    z-index: 0;
  }
  .glass-card {
    position: relative;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    z-index: 1;
    width: 100%;
  }
  h1 {
    font-size: 40px;
    color: #00d2ff;
    margin: 0 0 10px 0;
    font-weight: 800;
  }
  h2, h3 {
    font-size: 26px;
    color: #9d50bb;
    margin: 5px 0;
    font-weight: 700;
  }
  p, li {
    font-size: 17px;
    color: #f0f0f0;
    margin: 3px 0;
  }
  img {
    max-height: 250px; /* 10% 확대 반영 */
    width: auto;
    display: block;
    margin: 10px auto;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.2);
  }
  /* 슬라이드 하단 발표자 노트 스타일 */
  .script-box {
    position: absolute;
    bottom: 20px;
    left: 50px;
    right: 50px;
    background: rgba(0, 0, 0, 0.4);
    border-left: 4px solid #00d2ff;
    padding: 10px 20px;
    font-size: 14px;
    color: #cccccc;
    border-radius: 0 8px 8px 0;
    z-index: 2;
    line-height: 1.4;
  }
  header, footer {
    font-size: 10px;
    color: rgba(255, 255, 255, 0.4);
  }
---

<div class="glass-card">

# 네모 상가 데이터 보고서
### 프리미엄 글래스모피즘 에디션

</div>

<div class="script-box">
<b>발표자 노트:</b> 안녕하십니까. 네모 데이터 분석 팀입니다. 이번 보고서는 시각적 몰입감을 극대화한 글래스모피즘 스타일로 제작되었습니다. 데이터의 투명성과 비즈니스의 미래지향적인 가치를 담아내고자 했습니다.
</div>

---

<div class="glass-card">

# 00. 목차

- 01. 데이터 개요 및 품질
- 02. 핵심 통계 요약
- 03. 데이터 시각화 인사이트
- 04. 매물 제목 키워드 분석
- 05. 비즈니스 전략 제안

</div>

<div class="script-box">
<b>발표자 노트:</b> 오늘 발표는 데이터 개요부터 핵심 통계, 그리고 10가지 시각화 분석을 거쳐 최종 전략 제안으로 마무리하겠습니다. 각 슬라이드의 데이터와 시각적 흐름에 주목해 주시기 바랍니다.
</div>

---

<div class="glass-card">

# 01. 데이터 개요

- 전체 데이터 수: 2,169건 (높은 신뢰도)
- 컬럼 수: 40개 (심층 분석 가능)
- 중복 데이터: 0건 (완벽한 정제)
- 분석 중심: 강남권 상업용 부동산

</div>

<div class="script-box">
<b>발표자 노트:</b> 분석의 토대가 된 데이터는 강남권을 중심으로 한 2,169건의 실제 매물입니다. 중복이나 오류가 없는 완벽하게 정제된 데이터셋으로 분석의 신뢰성을 확보했습니다.
</div>

---

<div class="glass-card">

# 02. 핵심 지표 요약

- 평균 보증금: 5,761만 원
- 평균 월세: 440만 원
- 평균 권리금: 3,862만 원
- 평균 면적: 136㎡ (약 41평)

</div>

<div class="script-box">
<b>발표자 노트:</b> 강남 상가 시장의 4대 지표입니다. 보증금 5,760만 원, 월세 440만 원이 평균적입니다. 이 숫자들은 강남이라는 특수 상권이 가진 높은 가치와 진입 장벽을 수치로 보여줍니다.
</div>

---

<div class="glass-card">

# 03. 업종별 분포
![center](images/01_large_code_freq.png)
- 주요 업종: 기타, 음식점, 서비스업 순
- 시사점: 전통적인 먹거리 상권의 높은 경쟁 강도

</div>

<div class="script-box">
<b>발표자 노트:</b> 업종별 분포를 보면 음식점과 서비스업이 압도적입니다. 이는 상가 시장이 얼마나 치열한 레드오션인지를 보여주며, 차별화된 전략 없이는 생존이 어려움을 시사합니다.
</div>

---

<div class="glass-card">

# 03. 보증금 분포 분석
![center](images/02_deposit_dist.png)
- 전형적인 롱테일(Long-tail) 분포
- 중앙값(50%): 4,000만 원 선 형성

</div>

<div class="script-box">
<b>발표자 노트:</b> 보증금 분포입니다. 대부분의 매물이 낮은 가격대에 밀집해 있지만, 상위권으로 갈수록 가격이 급격히 치솟는 양극화 현상을 보실 수 있습니다.
</div>

---

<div class="glass-card">

# 03. 면적 대비 월세
![center](images/03_size_rent_scatter.png)
- 상관관계: 0.15 (매우 낮음)
- 인사이트: 면적보다 '입지'가 임대료의 핵심

</div>

<div class="script-box">
<b>발표자 노트:</b> 면적과 월세의 상관관계는 고작 0.15입니다. 즉, 면적이 넓다고 비싼 것이 아니라 입지와 동선이 월세를 결정하는 압도적인 변수임을 뜻합니다.
</div>

---

<div class="glass-card">

# 03. 층수별 임대료 차이
![center](images/04_floor_rent_avg.png)
- 1층 매물의 압도적 우위 확인
- 접근성 프리미엄이 가격에 그대로 반영

</div>

<div class="script-box">
<b>발표자 노트:</b> 층수별 가치입니다. 1층의 가치가 명확히 증명됩니다. 접근성이 임대료로 직결되는 시장이지만, 업종에 따라서는 고층이나 지하층을 통한 비용 절감 전략도 유효합니다.
</div>

---

<div class="glass-card">

# 03. 권리금 현황
![center](images/05_state_premium_box.png)
- 상가 상태에 따른 극단적 이상치 존재
- 진입 시 권리금 리스크 검토 필수

</div>

<div class="script-box">
<b>발표자 노트:</b> 권리금의 분포입니다. 상가 상태에 따라 극단적인 차이를 보입니다. 권리금 리스크가 큰 만큼, 데이터 기반의 객관적인 가치 평가가 반드시 선행되어야 합니다.
</div>

---

<div class="glass-card">

# 03. 거래 형태 비중
![center](images/06_price_type_pie.png)
- 월세 매물이 전체의 99% 이상 차지
- 현금 흐름 중심의 사업 계획 필요

</div>

<div class="script-box">
<b>발표자 노트:</b> 강남 상권은 철저히 월세 중심입니다. 99% 이상의 매물이 월세로 거래되므로, 매달의 현금 흐름 관리가 사업의 생명선임을 알 수 있습니다.
</div>

---

<div class="glass-card">

# 03. 인기 업종 TOP 20
![center](images/07_middle_code_top20.png)
- 카페 및 한식 업종이 시장 주도
- 높은 교체율을 보이는 과열 경쟁 섹션

</div>

<div class="script-box">
<b>발표자 노트:</b> 카페와 한식당이 시장을 주도하지만, 동시에 가장 빈번하게 폐업하고 바뀌는 구간이기도 합니다. 시장의 인기와 생존은 별개의 문제임을 명심해야 합니다.
</div>

---

<div class="glass-card">

# 03. 조회수와 찜 수
![center](images/08_view_favorite_scatter.png)
- 온라인 노출도가 실제 관심도로 직결
- 마케팅 데이터 기반의 매칭 효율성 증명

</div>

<div class="script-box">
<b>발표자 노트:</b> 조회수가 높은 매물이 찜 수도 높습니다. 온라인 마케팅의 기본 공식이 상가 매물 시장에서도 그대로 적용되고 있음을 보여주는 아주 정직한 데이터입니다.
</div>

---

<div class="glass-card">

# 03. 월세와 관리비 관계
![center](images/09_rent_maintenance_scatter.png)
- 두 변수 간의 독립적 상관관계 확인
- 총 점유 비용(Total Cost) 산출의 중요성

</div>

<div class="script-box">
<b>발표자 노트:</b> 월세와 관리비는 독립적으로 움직입니다. 임대료만 보고 계약했다가는 관리비 폭탄을 맞을 수 있으므로, 반드시 합산된 '총 점유 비용'을 따져봐야 합니다.
</div>

---

<div class="glass-card">

# 04. 핵심 키워드 분석
![center](images/11_text_keyword_tfidf.png)
- 주요 키워드: 무권리, 역세권, 대로변
- 고객 유입을 결정짓는 핵심 언어 추출

</div>

<div class="script-box">
<b>발표자 노트:</b> 고객을 움직이는 3대 키워드는 무권리, 역세권, 대로변입니다. 이 핵심 단어들을 전략적으로 활용하는 것이 마케팅 효율을 높이는 가장 빠른 길입니다.
</div>

---

<div class="glass-card">

# 05. 종합 전략 제안

- [1] 데이터 기반 정밀 가치 평가 도입
- [2] 단계별 타겟 마케팅 최적화
- [3] 총비용 투명성 강화를 통한 신뢰 확보
- [4] 실시간 상권 트렌드 모니터링

</div>

<div class="script-box">
<b>발표자 노트:</b> 결론입니다. 객관적인 데이터 가치 평가와 키워드 중심의 마케팅, 그리고 투명한 비용 관리가 필요합니다. 데이터가 가리키는 방향으로 비즈니스를 정렬하십시오.
</div>

---

<div class="glass-card">

# Q & A

### 감사합니다.
### 글래스모피즘 에디션 종료.

</div>

<div class="script-box">
<b>발표자 노트:</b> 발표를 마칩니다. 세련된 스타일만큼이나 명확한 데이터 분석이 여러분의 의사결정에 영감을 주었기를 바랍니다. 질문이 있으시면 말씀해 주십시오. 감사합니다.
</div>
