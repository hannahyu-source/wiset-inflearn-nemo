# -*- coding: utf-8 -*-
"""DB 저장 결과 확인 스크립트"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "nemo_stores.db")

conn = sqlite3.connect(DB_PATH)

# 총 건수
total = conn.execute("SELECT COUNT(*) FROM stores").fetchone()[0]
print(f"총 저장 건수: {total}건\n")

# 샘플 5건 출력
rows = conn.execute(
    "SELECT number, title, deposit, monthly_rent, near_subway_station FROM stores LIMIT 5"
).fetchall()

print("=== 샘플 데이터 (상위 5건) ===")
for r in rows:
    print(f"  #{r[0]} | {r[1]} | 보증금:{r[2]}만 | 월세:{r[3]}만 | {r[4]}")

conn.close()
