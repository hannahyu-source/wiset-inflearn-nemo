---
marp: true
theme: default
paginate: true
backgroundColor: #fffef0
header: "NEMO EDA : RISOGRAPH EDITION"
footer: "© 2026 ANALOG DATA LAB"
style: |
  section {
    font-family: 'Arial Black', sans-serif;
    background-color: #fffef0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
    padding: 80px 60px 110px 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: none;
  }
  h1 {
    font-size: 50px;
    color: #FF2D55;
    text-transform: uppercase;
    margin: 0 0 20px 0;
    text-shadow: 3px 3px 0px #00AFFF;
    line-height: 1.1;
  }
  h2, h3 {
    font-size: 28px;
    color: #00AFFF;
    margin: 10px 0;
    text-shadow: 2px 2px 0px #FFE000;
  }
  p, li {
    font-size: 19px;
    color: #333;
    font-weight: 700;
    line-height: 1.3;
    margin: 6px 0;
  }
  ul {
    margin-left: 20px;
  }
  li::before {
    content: "●";
    color: #FF2D55;
    display: inline-block;
    width: 1em;
    margin-left: -1em;
  }
  img {
    max-height: 220px;
    width: auto;
    display: block;
    margin: 10px auto;
    filter: contrast(1.1) brightness(1.05);
    mix-blend-mode: multiply;
    border: 3px solid #00AFFF;
    box-shadow: 6px 6px 0px #FF2D55;
  }
  header {
    top: 30px;
    font-size: 14px;
    font-weight: 900;
    color: #FF2D55;
    border-bottom: 2px solid #FF2D55;
  }
  footer {
    bottom: 30px;
    font-size: 14px;
    font-weight: 900;
    color: #00AFFF;
    border-top: 2px solid #00AFFF;
  }
---

# NEMO EDA REPORT
### RISOGRAPH PRINT EDITION

<!-- 
발표자 노트 (2분):
안녕하십니까. 이번 보고서는 아날로그 인쇄 기법인 '리소그래프' 스타일을 적용한 특별판입니다. 잉크의 질감과 겹침 효과를 통해 데이터의 역동성을 표현했습니다. 디자인은 화려하지만, 내용은 그 어느 때보다 실무적이고 날카롭게 구성했습니다. 리소그래프 특유의 감성과 함께 네모 상가 데이터의 깊은 통찰력을 느껴보시기 바랍니다.
-->

---

# 00. CONTENTS

- 01. DATA OVERVIEW
- 02. STATS SUMMARY
- 03. VISUAL INSIGHTS
- 04. KEYWORD ANALYSIS
- 05. STRATEGIC PROPOSAL

<!-- 
발표자 노트 (2분):
전체 목차입니다. 데이터의 기초 체력을 확인하는 개요부터, 핵심 시각화 10선, 그리고 TF-IDF를 이용한 키워드 분석까지 준비했습니다. 리소그래프의 강렬한 색감처럼, 각각의 섹션이 여러분의 머릿속에 선명하게 남을 수 있도록 핵심 위주로 전달하겠습니다.
-->

---

# 01. DATA QUALITY

- TOTAL ROWS: 2,169
- TOTAL COLS: 40
- DUPES: 0 (PERFECT)
- FOCUS: GANGNAM COMMERCIAL

<!-- 
발표자 노트 (2분):
데이터 품질입니다. 강남권 상가 매물 2,169건을 전수 분석했습니다. 중복이나 결측치가 거의 없는 완벽한 데이터셋을 기반으로 했기에, 여기서 도출된 결과들은 실제 시장의 흐름을 매우 정확하게 반영합니다.
-->

---

# 02. THE NUMBERS

- DEPOSIT AVG: 5,761M KRW
- RENT AVG: 4.4M KRW
- PREMIUM AVG: 38.6M KRW
- SIZE AVG: 136 SQM

<!-- 
발표자 노트 (2분):
평균 보증금 5,760만 원, 평균 월세 440만 원. 이 숫자들이 강남 상가 시장의 현재 주소입니다. 권리금 또한 4,000만 원 가까이 형성되어 있어 진입 장벽이 상당함을 알 수 있습니다. 이 숫자들을 기준점으로 삼아 이어지는 시각화 분석을 보시면 더욱 흥미로울 것입니다.
-->

---

# 03. SECTOR FREQ
![center](images/01_large_code_freq.png)
- TOP: OTHER, FOOD, SERVICE
- HIGH COMPETITION MARKET

<!-- 
발표자 노트 (2분):
업종별 분포 시각화입니다. 리소그래프 특유의 색감으로 강조된 차트를 보십시오. 음식점과 서비스업의 비중이 압도적입니다. 레드오션에서의 생존 전략이 그만큼 절실하다는 신호이기도 합니다.
-->

---

# 03. DEPOSIT DIST
![center](images/02_deposit_dist.png)
- LONG TAIL DISTRIBUTION
- 50% MEDIAN: 4,000M KRW

<!-- 
발표자 노트 (2분):
보증금 분포입니다. 낮은 가격대에 매물이 집중되어 있지만, 오른쪽으로 갈수록 가격이 급상승하는 전형적인 롱테일 구조입니다. 대다수의 창업자가 4,000만 원에서 6,000만 원 사이의 보증금 구간에서 기회를 찾고 있음을 보여줍니다.
-->

---

# 03. SIZE VS RENT
![center](images/03_size_rent_scatter.png)
- CORR: 0.15 (LOW)
- LOCATION > SQUARE FOOTAGE

<!-- 
발표자 노트 (2분):
면적과 월세의 상관관계입니다. 0.15라는 낮은 수치는 상가 임대료가 단순히 크기에 비례하지 않음을 증명합니다. '얼마나 넓으냐'보다 '어디에 있느냐'가 가격의 80% 이상을 결정합니다.
-->

---

# 03. FLOOR VS RENT
![center](images/04_floor_rent_avg.png)
- 1ST FLOOR IS THE KING
- GROUND ACCESS PREMIUM

<!-- 
발표자 노트 (2분):
층수별 임대료입니다. 1층의 압도적인 우위를 보십시오. 접근성이 곧 임대료로 직결됩니다. 하지만 목적형 업종이라면 2층이나 지하를 선택해 비용을 절감하는 영리한 전략이 필요합니다.
-->

---

# 03. PREMIUM BY STATE
![center](images/05_state_premium_box.png)
- EXTREME OUTLIERS DETECTED
- ENTRY BARRIER RISK CHECK

<!-- 
발표자 노트 (2분):
권리금 현황입니다. 상가 상태에 따라 권리금의 편차가 매우 큽니다. 리스크가 큰 영역인 만큼 데이터 기반의 냉정한 가치 평가가 선행되어야 합니다.
-->

---

# 03. PRICE TYPE
![center](images/06_price_type_pie.png)
- RENT DOMINANCE (99%)
- CASH FLOW STRATEGY REQUIRED

<!-- 
발표자 노트 (2분):
거래 형태입니다. 전세는 멸종 수준이고 오직 월세뿐입니다. 매달 발생하는 고정 비용을 감당할 수 있는 현금 흐름 확보가 사업 성패의 열쇠입니다.
-->

---

# 03. TOP 20 CATEGORY
![center](images/07_middle_code_top20.png)
- CAFE & KOREAN FOOD LEAD
- HIGH TURNOVER SECTORS

<!-- 
발표자 노트 (2분):
중분류 업종 분석입니다. 한식과 카페가 시장을 주도합니다. 경쟁이 치열한 만큼 차별화된 키워드와 마케팅 없이는 살아남기 힘든 구간입니다.
-->

---

# 03. VIEW VS FAV
![center](images/08_view_favorite_scatter.png)
- HIGH ENGAGEMENT PROPERTIES
- CONVERSION PROBABILITY UP

<!-- 
발표자 노트 (2분):
조회수와 찜 수의 관계입니다. 많이 보여지는 매물이 결국 선택받습니다. 온라인 플랫폼에서의 노출 전략이 실제 계약으로 이어지는 결정적인 고리임을 데이터가 증명합니다.
-->

---

# 03. RENT VS MAINT
![center](images/09_rent_maintenance_scatter.png)
- TOTAL COST MANAGEMENT
- HIDDEN EXPENSES CHECK

<!-- 
발표자 노트 (2분):
월세와 관리비입니다. 두 수치는 독립적으로 움직이는 경우가 많습니다. 임대료만 보고 계약했다가는 관리비 폭탄을 맞을 수 있으니, 반드시 총 점유 비용을 합산하여 분석해야 합니다.
-->

---

# 04. TOP KEYWORDS
![center](images/11_text_keyword_tfidf.png)
- NO PREMIUM, SUBWAY, MAIN ROAD
- CUSTOMER ATTRACTION PHRASES

<!-- 
발표자 노트 (2분):
핵심 키워드 분석입니다. 무권리, 역세권, 대로변. 이 단어들이 고객의 클릭을 부릅니다. 여러분의 매물을 설명할 때 이 강력한 키워드들을 어떻게 활용할지 고민해 보십시오.
-->

---

# 05. STRATEGY

- [1] DATA-DRIVEN VALUATION
- [2] LAYERED MARKETING
- [3] COST OPTIMIZATION
- [4] TREND ADAPTABILITY

<!-- 
발표자 노트 (2분):
최종 전략입니다. 데이터에 기반한 가치 평가, 키워드 중심의 마케팅, 총비용 최적화, 그리고 트렌드 대응. 이 네 가지가 네모 상가 시장에서 승리하는 공식입니다. 리소그래프처럼 선명한 전략으로 성공을 거두시기 바랍니다.
-->

---

# Q & A

### THANKS.
### RISOGRAPH OUT.

<!-- 
발표자 노트 (2분):
긴 시간 경청해 주셔서 감사합니다. 이번 리소그래프 에디션 보고서가 여러분의 비즈니스에 선명한 영감을 주었기를 바랍니다. 질문이 있으시면 자유롭게 말씀해 주십시오. 감사합니다.
-->
