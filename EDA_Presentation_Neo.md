---
marp: true
theme: default
paginate: true
backgroundColor: #FAF9F6
header: "NEMO EDA : RISOGRAPH AUTHENTIC"
footer: "PRINTED BY ANALOG DATA LAB"
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background-color: #FAF9F6;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.15'/%3E%3C/svg%3E");
    padding: 80px 70px 110px 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #222;
  }
  h1 {
    font-size: 55px;
    color: #FF48B0;
    text-transform: uppercase;
    margin: 0 0 15px 0;
    mix-blend-mode: multiply;
    letter-spacing: -1px;
    line-height: 1.0;
  }
  h2, h3 {
    font-size: 32px;
    color: #0078BF;
    margin: 5px 0;
    mix-blend-mode: multiply;
    font-weight: 900;
  }
  p, li {
    font-size: 18px;
    color: #333;
    font-weight: 600;
    line-height: 1.4;
    margin: 5px 0;
  }
  ul {
    margin-left: 25px;
    list-style: none;
  }
  li::before {
    content: "■";
    color: #FF48B0;
    display: inline-block;
    width: 1.2em;
    margin-left: -1.2em;
    font-size: 0.8em;
  }
  img {
    max-height: 220px;
    width: auto;
    display: block;
    margin: 15px auto;
    filter: contrast(1.2) sepia(0.2);
    mix-blend-mode: multiply;
    border: none;
    box-shadow: 10px 10px 0px rgba(0, 120, 191, 0.2);
  }
  header {
    top: 30px;
    font-size: 12px;
    font-weight: 900;
    color: #FF48B0;
    letter-spacing: 2px;
    opacity: 0.7;
  }
  footer {
    bottom: 30px;
    font-size: 11px;
    font-weight: 900;
    color: #0078BF;
    letter-spacing: 1px;
    opacity: 0.7;
  }
  /* 리소그래프 겹침 효과 레이어 */
  section::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(#FF48B0 0.5px, transparent 0.5px);
    background-size: 3px 3px;
    opacity: 0.03;
    pointer-events: none;
  }
---

# NEMO EDA REPORT
### RISOGRAPH AUTHENTIC

<!-- 
발표자 노트 (2분):
네모 데이터 분석 팀입니다. 이번 리소그래프 에디션은 인쇄상의 불완전함이 주는 미학을 강조했습니다. 핑크와 블루 잉크가 겹치며 만들어내는 독특한 색감을 즐기시며, 데이터 이면에 숨겨진 비즈니스 인사이트를 탐구해 보시기 바랍니다.
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
오늘의 분석 여정입니다. 깨끗하게 정제된 데이터 개요부터, 리소그래프의 강렬한 색감으로 재탄생한 10가지 시각화 인사이트를 차례로 만나보시겠습니다.
-->

---

# 01. DATA QUALITY

- TOTAL ROWS: 2,169
- TOTAL COLS: 40
- DUPES: 0 (CLEAN PRINT)
- FOCUS: GANGNAM COMMERCIAL

<!-- 
발표자 노트 (2분):
우리의 분석 기반은 탄탄합니다. 강남권 2,169건의 실제 데이터를 정교하게 인쇄하듯 분석했습니다. 데이터의 선명함이 곧 전략의 선명함입니다.
-->

---

# 02. THE NUMBERS

- DEPOSIT AVG: 5,761M KRW
- RENT AVG: 4.4M KRW
- PREMIUM AVG: 38.6M KRW
- SIZE AVG: 136 SQM

<!-- 
발표자 노트 (2분):
숫자로 보는 시장입니다. 보증금 5,760만 원, 월세 440만 원. 이 숫자들이 의미하는 경제적 중량감을 리소그래프의 묵직한 잉크 질감으로 표현했습니다.
-->

---

# 03. SECTOR FREQ
![center](images/01_large_code_freq.png)
- TOP: OTHER, FOOD, SERVICE
- MARKET SATURATION ANALYSIS

<!-- 
발표자 노트 (2분):
업종별 분포입니다. 선명한 잉크가 겹치듯, 다양한 업종들이 밀집해 있습니다. 특히 음식점과 서비스업의 비중은 시장의 치열함을 보여줍니다.
-->

---

# 03. DEPOSIT DIST
![center](images/02_deposit_dist.png)
- LONG TAIL DISTRIBUTION
- 50% MEDIAN: 4,000M KRW

<!-- 
발표자 노트 (2분):
보증금 분포 히스토그램입니다. 대부분의 기회는 왼쪽의 밀집 구간에 있지만, 오른쪽으로 갈수록 하이엔드 시장의 문턱이 급격히 높아짐을 알 수 있습니다.
-->

---

# 03. SIZE VS RENT
![center](images/03_size_rent_scatter.png)
- CORR: 0.15 (LOW)
- LOCATION > SQUARE FOOTAGE

<!-- 
발표자 노트 (2분):
면적과 월세의 상관관계입니다. 잉크가 흩뿌려진 듯한 산점도를 보십시오. 면적보다는 입지 프리미엄이 월세를 결정하는 핵심 변수임이 드러납니다.
-->

---

# 03. FLOOR VS RENT
![center](images/04_floor_rent_avg.png)
- 1ST FLOOR IS THE KING
- GROUND ACCESS PREMIUM

<!-- 
발표자 노트 (2분):
층수별 가치입니다. 1층 상가의 압도적인 접근성이 핑크색 바 차트로 강조되어 있습니다. 비즈니스 성격에 맞는 최적의 층수를 선택하는 것이 고정비 절감의 핵심입니다.
-->

---

# 03. PREMIUM BY STATE
![center](images/05_state_premium_box.png)
- EXTREME OUTLIERS DETECTED
- ENTRY BARRIER RISK CHECK

<!-- 
발표자 노트 (2분):
권리금 박스플롯입니다. 극단적인 이상치들이 존재하는 상급 매물 시장의 문턱을 확인하십시오. 철저한 리스크 관리가 필요한 영역입니다.
-->

---

# 03. PRICE TYPE
![center](images/06_price_type_pie.png)
- RENT DOMINANCE (99%)
- CASH FLOW STRATEGY

<!-- 
발표자 노트 (2분):
거래 형태 비중입니다. 월세 중심의 시장 구조는 매달의 현금 흐름 관리가 사업의 생명선임을 시사합니다.
-->

---

# 03. TOP 20 CATEGORY
![center](images/07_middle_code_top20.png)
- CAFE & KOREAN FOOD LEAD
- HIGH TURNOVER SECTORS

<!-- 
발표자 노트 (2분):
세부 업종 순위입니다. 가장 인기가 많은 업종일수록 차별화된 마케팅 키워드가 필수적입니다.
-->

---

# 03. VIEW VS FAV
![center](images/08_view_favorite_scatter.png)
- HIGH ENGAGEMENT PROPERTIES
- CONVERSION PROBABILITY UP

<!-- 
발표자 노트 (2분):
디지털 지표 분석입니다. 조회수가 높은 매물이 찜 수도 높다는 정직한 데이터를 통해 온라인 노출의 중요성을 다시 확인합니다.
-->

---

# 03. RENT VS MAINT
![center](images/09_rent_maintenance_scatter.png)
- TOTAL COST MANAGEMENT
- HIDDEN EXPENSES CHECK

<!-- 
발표자 노트 (2분):
월세와 관리비의 상관관계입니다. 겉으로 보이는 임대료뿐만 아니라 숨은 관리비까지 포함한 '총 점유 비용'을 산출하는 것이 스마트한 임차인의 자세입니다.
-->

---

# 04. TOP KEYWORDS
![center](images/11_text_keyword_tfidf.png)
- NO PREMIUM, SUBWAY, MAIN ROAD
- CUSTOMER ATTRACTION PHRASES

<!-- 
발표자 노트 (2분):
텍스트 분석 결과입니다. '무권리', '역세권' 등 고객의 시선을 끄는 핵심 키워드들이 리소그래프 스타일로 선명하게 추출되었습니다.
-->

---

# 05. STRATEGY

- [1] DATA-DRIVEN VALUATION
- [2] LAYERED MARKETING
- [3] COST OPTIMIZATION
- [4] TREND ADAPTABILITY

<!-- 
발표자 노트 (2분):
종합 전략입니다. 데이터에 기반한 가치 평가와 레이어드 마케팅, 그리고 비용 최적화. 이 세 가지가 리소그래프처럼 선명한 비즈니스 성공을 보장할 것입니다.
-->

---

# Q & A

### THANKS.
### RISOGRAPH OUT.

<!-- 
발표자 노트 (2분):
발표를 마칩니다. 리소그래프 특유의 따뜻하면서도 강렬한 느낌이 여러분의 비즈니스에 새로운 영감이 되었기를 바랍니다. 감사합니다.
-->
