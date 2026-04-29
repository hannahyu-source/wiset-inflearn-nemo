---
marp: true
theme: default
paginate: true
backgroundColor: #FAF9F6
header: "네모 상가 데이터 심층 분석 : 리소그래프 에디션"
footer: "아날로그 데이터 랩 발행"
style: |
  section {
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    background-color: #FAF9F6;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.15'/%3E%3C/svg%3E");
    padding: 80px 70px 110px 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #222;
    word-break: keep-all;
  }
  h1 {
    font-size: 48px;
    color: #FF48B0;
    text-transform: uppercase;
    margin: 0 0 15px 0;
    mix-blend-mode: multiply;
    letter-spacing: -1px;
    line-height: 1.1;
    font-weight: 900;
  }
  h2, h3 {
    font-size: 30px;
    color: #0078BF;
    margin: 5px 0;
    mix-blend-mode: multiply;
    font-weight: 900;
  }
  p, li {
    font-size: 18px;
    color: #333;
    font-weight: 600;
    line-height: 1.5;
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

# 네모 상가 데이터 보고서
### 리소그래프 에디션

<!-- 
발표자 노트 (2분):
안녕하십니까. 네모 데이터 분석 팀입니다. 이번 보고서는 아날로그 인쇄 기법인 리소그래프 스타일을 적용하여, 데이터가 가진 날것의 통찰을 시각적으로 구현했습니다. 핑크와 블루 잉크가 겹치며 만들어내는 독특한 시각적 흐름 속에서, 강남 상권의 핵심 지표들을 함께 살펴보시겠습니다.
-->

---

# 00. 목차

- 01. 데이터 개요 및 품질
- 02. 핵심 통계 요약
- 03. 데이터 시각화 인사이트
- 04. 매물 제목 키워드 분석
- 05. 비즈니스 전략 제안

<!-- 
발표자 노트 (2분):
오늘의 분석 순서입니다. 데이터의 신뢰성을 확인하는 개요부터 시작하여, 핵심 수치 요약, 그리고 총 10가지의 정교한 시각화 분석을 통해 시장의 맥락을 짚어내겠습니다. 마지막으로는 AI 기반의 키워드 분석과 전략적 제안으로 마무리하겠습니다.
-->

---

# 01. 데이터 개요

- 전체 데이터 수: 2,169건 (높은 신뢰도)
- 컬럼 수: 40개 (심층 분석 가능)
- 중복 데이터: 0건 (완벽한 정제)
- 분석 중심: 강남권 상업용 부동산

<!-- 
발표자 노트 (2분):
우리가 분석한 데이터는 강남권을 중심으로 한 2,169건의 실제 매물입니다. 중복이나 오류가 없는 깨끗한 데이터셋을 바탕으로 했기에, 여기서 도출된 인사이트들은 실제 시장의 흐름을 매우 정확하게 반영하고 있습니다.
-->

---

# 02. 핵심 지표 요약

- 평균 보증금: 5,761만 원
- 평균 월세: 440만 원
- 평균 권리금: 3,862만 원
- 평균 면적: 136㎡ (약 41평)

<!-- 
발표자 노트 (2분):
강남 상가 시장을 대표하는 숫자들입니다. 평균 보증금 5,760만 원, 월세 440만 원 수준입니다. 이 지표들은 강남이라는 특수 상권이 가진 높은 가치와 그에 따른 진입 장벽을 동시에 보여줍니다.
-->

---

# 03. 업종별 분포
![center](images/01_large_code_freq.png)
- 주요 업종: 기타, 음식점, 서비스업 순
- 시사점: 전통적인 먹거리 상권의 높은 경쟁 강도

<!-- 
발표자 노트 (2분):
대분류 업종분포입니다. 음식점과 서비스업의 비중이 압도적으로 높습니다. 이는 상가 시장이 얼마나 치열한 레드오션인지를 보여주는 지표이며, 차별화된 전략 없이는 생존이 어려움을 시사합니다.
-->

---

# 03. 보증금 분포 분석
![center](images/02_deposit_dist.png)
- 전형적인 롱테일(Long-tail) 분포
- 중앙값(50%): 4,000만 원 선 형성

<!-- 
발표자 노트 (2분):
보증금의 분포를 보십시오. 대부분의 매물이 왼쪽 하단 가격대에 밀집해 있지만, 상위권 매물은 기하급수적으로 높은 보증금을 형성하고 있습니다. 이는 상가 시장의 양극화 현상을 여실히 드러냅니다.
-->

---

# 03. 면적 대비 월세
![center](images/03_size_rent_scatter.png)
- 상관관계: 0.15 (매우 낮음)
- 인사이트: 면적보다 '입지'가 임대료의 핵심

<!-- 
발표자 노트 (2분):
면적과 월세의 상관관계 분석 결과입니다. 0.15라는 낮은 수치는 상가 임대료가 단순히 면적에 비례하지 않음을 뜻합니다. 평수보다 '어디에 위치하느냐'가 가격 결정의 80% 이상을 차지합니다.
-->

---

# 03. 층수별 임대료 차이
![center](images/04_floor_rent_avg.png)
- 1층 매물의 압도적 우위 확인
- 접근성 프리미엄이 가격에 그대로 반영

<!-- 
발표자 노트 (2분):
층수별 임대료입니다. 1층의 가치가 데이터로 명확히 증명됩니다. 하지만 배달 중심이나 목적형 방문 업종이라면, 월세가 훨씬 저렴한 2층이나 지하층을 선택하는 것이 영리한 전략이 될 수 있습니다.
-->

---

# 03. 권리금 현황
![center](images/05_state_premium_box.png)
- 상가 상태에 따른 극단적 이상치 존재
- 진입 시 권리금 리스크 검토 필수

<!-- 
발표자 노트 (2분):
권리금의 분포입니다. 권리금은 법적 보호가 어려운 만큼 리스크가 큽니다. 데이터에 나타난 극단적인 고액 권리금 매물들은 해당 입지의 가치를 반영하지만, 동시에 투자 회수 가능성을 냉정히 따져봐야 함을 경고합니다.
-->

---

# 03. 거래 형태 비중
![center](images/06_price_type_pie.png)
- 월세 매물이 전체의 99% 이상 차지
- 현금 흐름 중심의 사업 계획 필요

<!-- 
발표자 노트 (2분):
거래 형태입니다. 전세는 거의 존재하지 않으며 월세가 시장을 지배합니다. 이는 임차인에게 매달 고정적인 비용 지출을 강요하므로, 철저한 매출 목표와 현금 흐름 관리가 사업 성공의 열쇠입니다.
-->

---

# 03. 인기 업종 TOP 20
![center](images/07_middle_code_top20.png)
- 카페 및 한식 업종이 시장 주도
- 높은 교체율을 보이는 과열 경쟁 섹션

<!-- 
발표자 노트 (2분):
중분류 업종 순위입니다. 카페와 한식당이 가장 많습니다. 인기가 많은 만큼 폐업률도 높은 구간이기에, 자신만의 독보적인 킬러 콘텐츠가 없다면 이 거대한 차트의 한 칸으로 사라질 위험이 큽니다.
-->

---

# 03. 조회수와 찜 수
![center](images/08_view_favorite_scatter.png)
- 온라인 노출도가 실제 관심도로 직결
- 마케팅 데이터 기반의 매칭 효율성 증명

<!-- 
발표자 노트 (2분):
디지털 마케팅 데이터입니다. 조회수가 높은 매물이 찜 수도 비례해서 높습니다. 매물을 빨리 처분하거나 좋은 임차인을 구하고 싶다면, 플랫폼 내 노출 최적화가 필수적임을 데이터가 증명합니다.
-->

---

# 03. 월세와 관리비 관계
![center](images/09_rent_maintenance_scatter.png)
- 두 변수 간의 독립적 상관관계 확인
- 총 점유 비용(Total Cost) 산출의 중요성

<!-- 
발표자 노트 (2분):
월세와 관리비의 관계입니다. 월세가 높다고 무조건 관리비가 높은 것은 아닙니다. 임차인은 겉으로 보이는 임대료만 볼 것이 아니라, 숨은 관리비를 포함한 실제 총 지출액을 반드시 확인해야 합니다.
-->

---

# 04. 핵심 키워드 분석
![center](images/11_text_keyword_tfidf.png)
- 주요 키워드: 무권리, 역세권, 대로변
- 고객 유입을 결정짓는 핵심 언어 추출

<!-- 
발표자 노트 (2분):
제목 키워드 분석 결과입니다. '무권리', '역세권' 같은 단어들이 고객의 마음을 움직입니다. 매물 등록 시 이러한 핵심 키워드를 어떻게 전략적으로 배치하느냐가 노출과 전환의 성패를 가릅니다.
-->

---

# 05. 종합 전략 제안

- [1] 데이터 기반 정밀 가치 평가 도입
- [2] 단계별 타겟 마케팅 최적화
- [3] 총비용 투명성 강화를 통한 신뢰 확보
- [4] 실시간 상권 트렌드 모니터링

<!-- 
발표자 노트 (2분):
마지막 결론입니다. 데이터 기반의 정교한 가치 평가, 키워드 중심의 레이어드 마케팅, 그리고 비용 최적화가 필요합니다. 리소그래프의 선명한 색감처럼, 데이터 기반의 명확한 전략으로 비즈니스의 성공을 이끄시기 바랍니다.
-->

---

# Q & A

### 감사합니다.
### 리소그래프 에디션 종료.

<!-- 
발표자 노트 (2분):
발표를 마칩니다. 리소그래프 특유의 감각적인 스타일로 풀어낸 이번 분석 결과가 여러분의 의사결정에 큰 도움이 되었기를 바랍니다. 질문이 있으시면 편하게 말씀해 주세요. 감사합니다.
-->
