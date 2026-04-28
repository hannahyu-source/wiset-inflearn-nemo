"""
Nemo 앱 상점 목록 스크래핑 스크립트
- API: https://www.nemoapp.kr/api/store/search-list
- 수집된 데이터는 data/nemo_stores.db 에 저장
"""

import requests
import sqlite3
import json
import os
from datetime import datetime

# ─────────────────────────────────────────────
# 설정
# ─────────────────────────────────────────────
BASE_URL = "https://www.nemoapp.kr/api/store/search-list"

# 프롬프트에서 제공된 파라미터 (PageIndex 만 변경하여 페이지 반복)
DEFAULT_PARAMS = {
    "CompletedOnly": "false",
    "NELat": "37.51582615800965",
    "NELng": "127.05411349575468",
    "SWLat": "37.483292587284524",
    "SWLng": "127.01958275998645",
    "Zoom": "15",
    "SortBy": "29",
    "PageIndex": "0",
}

# 프롬프트에서 제공된 헤더
HEADERS = {
    "referer": "https://www.nemoapp.kr/store",
    "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/147.0.0.0 Safari/537.36"
    ),
}

# 저장 경로 (소스코드 기준 상대경로)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DB_PATH = os.path.join(DATA_DIR, "nemo_stores.db")

os.makedirs(DATA_DIR, exist_ok=True)


# ─────────────────────────────────────────────
# DB 초기화
# ─────────────────────────────────────────────
def init_db(conn: sqlite3.Connection) -> None:
    """테이블이 없으면 생성"""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS stores (
            id                             TEXT PRIMARY KEY,
            article_type                   INTEGER,
            number                         INTEGER,
            building_management_serial     TEXT,
            agent_id                       TEXT,
            title                          TEXT,
            business_large_code            INTEGER,
            business_large_code_name       TEXT,
            business_middle_code           INTEGER,
            business_middle_code_name      TEXT,
            price_type                     INTEGER,
            price_type_name                TEXT,
            deposit                        INTEGER,
            monthly_rent                   INTEGER,
            premium                        INTEGER,
            sale                           INTEGER,
            maintenance_fee                INTEGER,
            floor                          INTEGER,
            ground_floor                   INTEGER,
            size                           REAL,
            area_price                     REAL,
            first_deposit                  INTEGER,
            first_monthly_rent             INTEGER,
            first_premium                  INTEGER,
            is_priority                    INTEGER,
            is_premium_closed              INTEGER,
            is_move_in_date                INTEGER,
            move_in_date                   TEXT,
            near_subway_station            TEXT,
            view_count                     INTEGER,
            favorite_count                 INTEGER,
            state                          INTEGER,
            preview_photo_url              TEXT,
            small_photo_urls               TEXT,  -- JSON 배열
            origin_photo_urls              TEXT,  -- JSON 배열
            confirmed_date_utc             TEXT,
            created_date_utc               TEXT,
            edited_date_utc                TEXT,
            completion_confirmed_date_utc  TEXT,
            scraped_at                     TEXT
        )
    """)
    conn.commit()


# ─────────────────────────────────────────────
# 아이템 저장
# ─────────────────────────────────────────────
def save_items(conn: sqlite3.Connection, items: list) -> int:
    """items 리스트를 DB에 UPSERT 하고, 신규 저장 건수를 반환"""
    saved = 0
    scraped_at = datetime.utcnow().isoformat()

    for item in items:
        try:
            conn.execute("""
                INSERT INTO stores (
                    id, article_type, number, building_management_serial,
                    agent_id, title,
                    business_large_code, business_large_code_name,
                    business_middle_code, business_middle_code_name,
                    price_type, price_type_name,
                    deposit, monthly_rent, premium, sale, maintenance_fee,
                    floor, ground_floor, size, area_price,
                    first_deposit, first_monthly_rent, first_premium,
                    is_priority, is_premium_closed, is_move_in_date, move_in_date,
                    near_subway_station, view_count, favorite_count, state,
                    preview_photo_url, small_photo_urls, origin_photo_urls,
                    confirmed_date_utc, created_date_utc, edited_date_utc,
                    completion_confirmed_date_utc, scraped_at
                ) VALUES (
                    :id, :article_type, :number, :building_management_serial,
                    :agent_id, :title,
                    :business_large_code, :business_large_code_name,
                    :business_middle_code, :business_middle_code_name,
                    :price_type, :price_type_name,
                    :deposit, :monthly_rent, :premium, :sale, :maintenance_fee,
                    :floor, :ground_floor, :size, :area_price,
                    :first_deposit, :first_monthly_rent, :first_premium,
                    :is_priority, :is_premium_closed, :is_move_in_date, :move_in_date,
                    :near_subway_station, :view_count, :favorite_count, :state,
                    :preview_photo_url, :small_photo_urls, :origin_photo_urls,
                    :confirmed_date_utc, :created_date_utc, :edited_date_utc,
                    :completion_confirmed_date_utc, :scraped_at
                )
                ON CONFLICT(id) DO UPDATE SET
                    title               = excluded.title,
                    monthly_rent        = excluded.monthly_rent,
                    deposit             = excluded.deposit,
                    view_count          = excluded.view_count,
                    favorite_count      = excluded.favorite_count,
                    state               = excluded.state,
                    edited_date_utc     = excluded.edited_date_utc,
                    scraped_at          = excluded.scraped_at
            """, {
                "id":                            item.get("id"),
                "article_type":                  item.get("articleType"),
                "number":                        item.get("number"),
                "building_management_serial":    item.get("buildingManagementSerialNumber"),
                "agent_id":                      item.get("agentId"),
                "title":                         item.get("title"),
                "business_large_code":           item.get("businessLargeCode"),
                "business_large_code_name":      item.get("businessLargeCodeName"),
                "business_middle_code":          item.get("businessMiddleCode"),
                "business_middle_code_name":     item.get("businessMiddleCodeName"),
                "price_type":                    item.get("priceType"),
                "price_type_name":               item.get("priceTypeName"),
                "deposit":                       item.get("deposit"),
                "monthly_rent":                  item.get("monthlyRent"),
                "premium":                       item.get("premium"),
                "sale":                          item.get("sale"),
                "maintenance_fee":               item.get("maintenanceFee"),
                "floor":                         item.get("floor"),
                "ground_floor":                  item.get("groundFloor"),
                "size":                          item.get("size"),
                "area_price":                    item.get("areaPrice"),
                "first_deposit":                 item.get("firstDeposit"),
                "first_monthly_rent":            item.get("firstMonthlyRent"),
                "first_premium":                 item.get("firstPremium"),
                "is_priority":                   int(bool(item.get("isPriority"))),
                "is_premium_closed":             int(bool(item.get("isPremiumClosed"))),
                "is_move_in_date":               int(bool(item.get("isMoveInDate"))),
                "move_in_date":                  item.get("moveInDate"),
                "near_subway_station":           item.get("nearSubwayStation"),
                "view_count":                    item.get("viewCount"),
                "favorite_count":                item.get("favoriteCount"),
                "state":                         item.get("state"),
                "preview_photo_url":             item.get("previewPhotoUrl"),
                "small_photo_urls":              json.dumps(item.get("smallPhotoUrls", []), ensure_ascii=False),
                "origin_photo_urls":             json.dumps(item.get("originPhotoUrls", []), ensure_ascii=False),
                "confirmed_date_utc":            item.get("confirmedDateUtc"),
                "created_date_utc":              item.get("createdDateUtc"),
                "edited_date_utc":               item.get("editedDateUtc"),
                "completion_confirmed_date_utc": item.get("completionConfirmedDateUtc"),
                "scraped_at":                    scraped_at,
            })
            saved += 1
        except Exception as e:
            print(f"  [저장 오류] id={item.get('id')} → {e}")

    conn.commit()
    return saved


# ─────────────────────────────────────────────
# 1 페이지 수집
# ─────────────────────────────────────────────
def fetch_page(page_index: int) -> dict | None:
    """지정된 페이지를 API에서 가져와 JSON 응답을 반환"""
    params = DEFAULT_PARAMS.copy()
    params["PageIndex"] = str(page_index)

    try:
        resp = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f"  [요청 오류] 페이지={page_index} → {e}")
        return None


# ─────────────────────────────────────────────
# 메인
# ─────────────────────────────────────────────
def main() -> None:
    print("=" * 55)
    print("  Nemo 스크래핑 시작 (전체 페이지 수집)")
    print(f"  DB 경로: {DB_PATH}")
    print("=" * 55)

    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    total_saved = 0
    page = 0

    # ── items 가 빈 배열로 올 때까지 반복 ─────────────
    while True:
        print(f"\n[페이지 {page}] 요청 중...")
        data = fetch_page(page)

        # 요청 자체가 실패한 경우
        if data is None:
            print("  응답 없음. 수집 종료.")
            break

        items = data.get("items", [])
        print(f"  items 건수: {len(items)}")

        # items 가 빈 배열 → 더 이상 데이터 없음
        if not items:
            print("  더 이상 데이터가 없습니다. 수집 완료.")
            break

        saved = save_items(conn, items)
        total_saved += saved
        print(f"  저장 완료: {saved} 건  (누적: {total_saved} 건)")

        page += 1  # 다음 페이지로

    # ── 수집 결과 요약 ─────────────────────────────────
    cur = conn.execute("SELECT COUNT(*) FROM stores")
    db_total = cur.fetchone()[0]
    print("\n" + "=" * 55)
    print(f"  수집 페이지 수: {page} 페이지")
    print(f"  이번 실행 저장: {total_saved} 건")
    print(f"  DB 총 저장 건수: {db_total} 건")
    print("=" * 55)

    # ── 샘플 출력 ─────────────────────────────────────
    print("\n[샘플 데이터 상위 3건]")
    cur = conn.execute(
        "SELECT number, title, price_type_name, deposit, monthly_rent, near_subway_station "
        "FROM stores ORDER BY rowid LIMIT 3"
    )
    for row in cur.fetchall():
        print(f"  #{row[0]} | {row[1]} | {row[2]} | 보증금:{row[3]}만 | 월세:{row[4]}만 | {row[5]}")

    conn.close()
    print("\n완료! DB 파일:", DB_PATH)


if __name__ == "__main__":
    main()
