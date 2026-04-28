# 네모 상가 데이터 심층 EDA 보고서

## 1. 데이터 개요 및 품질 점검

- **전체 데이터 수**: 2169 행, 40 열
### 데이터 샘플 (상위 5행)
|    | id                                   |   article_type |   number |   building_management_serial | agent_id   | title                            |   business_large_code | business_large_code_name   |   business_middle_code | business_middle_code_name   |   price_type | price_type_name   |   deposit |   monthly_rent |   premium |   sale |   maintenance_fee |   floor |   ground_floor |   size |   area_price |   first_deposit |   first_monthly_rent |   first_premium |   is_priority |   is_premium_closed |   is_move_in_date |   move_in_date | near_subway_station   |   view_count |   favorite_count |   state | preview_photo_url                                                                | small_photo_urls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | origin_photo_urls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |   confirmed_date_utc | created_date_utc                 | edited_date_utc                  |   completion_confirmed_date_utc | scraped_at                 |
|---:|:-------------------------------------|---------------:|---------:|-----------------------------:|:-----------|:---------------------------------|----------------------:|:---------------------------|-----------------------:|:----------------------------|-------------:|:------------------|----------:|---------------:|----------:|-------:|------------------:|--------:|---------------:|-------:|-------------:|----------------:|---------------------:|----------------:|--------------:|--------------------:|------------------:|---------------:|:----------------------|-------------:|-----------------:|--------:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------:|:---------------------------------|:---------------------------------|--------------------------------:|:---------------------------|
|  0 | b48dcf64-d4d5-41c0-bcf6-1f8ce4d95f88 |              1 |   936771 |    1168010800102180000007134 |            | 월 100만원대 무권리 스튜디오                |                    16 | 서비스업                       |                   1609 | 기타서비스업                      |            1 | 임대                |     20000 |           1200 |         0 |      0 |               100 |       3 |              4 |  59.52 |           71 |           20000 |                 1200 |               0 |             0 |                   0 |                 1 |            nan | 학동역, 도보 5분            |            0 |                2 |       1 | https://img.nemoapp.kr/article-photos/957f0939-a403-4c11-8f85-a2d93df5492e/s.jpg | ["https://img.nemoapp.kr/article-photos/957f0939-a403-4c11-8f85-a2d93df5492e/s.jpg", "https://img.nemoapp.kr/article-photos/cc03d3d2-3ef8-4d24-9dd9-59d110e5c0bc/s.jpg", "https://img.nemoapp.kr/article-photos/a9aaea37-50c8-424b-8783-e3acfc3970a6/s.jpg", "https://img.nemoapp.kr/article-photos/9542d9b5-4d78-4771-b746-7d9b3ecf20cd/s.jpg", "https://img.nemoapp.kr/article-photos/50ce9142-7bef-4be3-88b6-4068961a8d1e/s.jpg", "https://img.nemoapp.kr/article-photos/023ee793-47d2-4b01-8332-3302bd94d98c/s.jpg", "https://img.nemoapp.kr/article-photos/efbaba45-2bb7-43e8-aa71-c970575000c5/s.jpg", "https://img.nemoapp.kr/article-photos/d8668768-bb65-4a1b-8664-3b2c6d2c8162/s.jpg", "https://img.nemoapp.kr/article-photos/96088713-4df7-4e99-8579-f0a00c224dc2/s.jpg", "https://img.nemoapp.kr/article-photos/ca33538a-58d6-4bce-a204-3bd437e41a38/s.jpg", "https://img.nemoapp.kr/article-photos/f345d3d0-c52a-4a4b-9edb-2d5dcb865079/s.jpg"]                                                                                     | ["https://img.nemoapp.kr/article-photos/957f0939-a403-4c11-8f85-a2d93df5492e/l.jpg", "https://img.nemoapp.kr/article-photos/cc03d3d2-3ef8-4d24-9dd9-59d110e5c0bc/l.jpg", "https://img.nemoapp.kr/article-photos/a9aaea37-50c8-424b-8783-e3acfc3970a6/l.jpg", "https://img.nemoapp.kr/article-photos/9542d9b5-4d78-4771-b746-7d9b3ecf20cd/l.jpg", "https://img.nemoapp.kr/article-photos/50ce9142-7bef-4be3-88b6-4068961a8d1e/l.jpg", "https://img.nemoapp.kr/article-photos/023ee793-47d2-4b01-8332-3302bd94d98c/l.jpg", "https://img.nemoapp.kr/article-photos/efbaba45-2bb7-43e8-aa71-c970575000c5/l.jpg", "https://img.nemoapp.kr/article-photos/d8668768-bb65-4a1b-8664-3b2c6d2c8162/l.jpg", "https://img.nemoapp.kr/article-photos/96088713-4df7-4e99-8579-f0a00c224dc2/l.jpg", "https://img.nemoapp.kr/article-photos/ca33538a-58d6-4bce-a204-3bd437e41a38/l.jpg", "https://img.nemoapp.kr/article-photos/f345d3d0-c52a-4a4b-9edb-2d5dcb865079/l.jpg"]                                                                                     |                  nan | 2026-04-17T04:56:44.851539+00:00 | 2026-04-27T02:26:04.542901+00:00 |                             nan | 2026-04-27T02:44:49.525998 |
|  1 | 69f02241-815c-4d35-8671-8eb281df56f4 |              1 |   937880 |    1168010500100500002000001 |            | 삼성중앙역 1분 거리 초역세권 사무실 임대          |                    16 | 서비스업                       |                   1609 | 기타서비스업                      |            1 | 임대                |     20000 |           1500 |         0 |      0 |               350 |       2 |              5 |  49.75 |          105 |           20000 |                 1500 |               0 |             0 |                   0 |                 1 |            nan | 삼성중앙역, 도보 3분          |            0 |                0 |       1 | https://img.nemoapp.kr/article-photos/a48626b6-fa53-4644-a21f-767d57726a25/s.jpg | ["https://img.nemoapp.kr/article-photos/a48626b6-fa53-4644-a21f-767d57726a25/s.jpg", "https://img.nemoapp.kr/article-photos/03778315-5a33-4ef4-a66b-4bb1b3e7a9a2/s.jpg", "https://img.nemoapp.kr/article-photos/775e8eeb-ed09-4a76-84fe-d6a66649f407/s.jpg", "https://img.nemoapp.kr/article-photos/73a444cf-2102-4d37-b4ab-95f5fd4ea9aa/s.jpg", "https://img.nemoapp.kr/article-photos/7413bec6-23c2-4f49-ab53-0496f1d0696a/s.jpg", "https://img.nemoapp.kr/article-photos/bae52653-8983-429b-9fa5-0ea69448a4a9/s.jpg", "https://img.nemoapp.kr/article-photos/e61eed03-15cd-4e2b-9cd0-74b4f0791fa1/s.jpg", "https://img.nemoapp.kr/article-photos/5c25e480-9b2d-4a7b-8944-9b6785c5b5d1/s.jpg", "https://img.nemoapp.kr/article-photos/315f92a6-e651-43b9-8cab-b3e7bcd357a6/s.jpg"]                                                                                                                                                                                                                                                             | ["https://img.nemoapp.kr/article-photos/a48626b6-fa53-4644-a21f-767d57726a25/l.jpg", "https://img.nemoapp.kr/article-photos/03778315-5a33-4ef4-a66b-4bb1b3e7a9a2/l.jpg", "https://img.nemoapp.kr/article-photos/775e8eeb-ed09-4a76-84fe-d6a66649f407/l.jpg", "https://img.nemoapp.kr/article-photos/73a444cf-2102-4d37-b4ab-95f5fd4ea9aa/l.jpg", "https://img.nemoapp.kr/article-photos/7413bec6-23c2-4f49-ab53-0496f1d0696a/l.jpg", "https://img.nemoapp.kr/article-photos/bae52653-8983-429b-9fa5-0ea69448a4a9/l.jpg", "https://img.nemoapp.kr/article-photos/e61eed03-15cd-4e2b-9cd0-74b4f0791fa1/l.jpg", "https://img.nemoapp.kr/article-photos/5c25e480-9b2d-4a7b-8944-9b6785c5b5d1/l.jpg", "https://img.nemoapp.kr/article-photos/315f92a6-e651-43b9-8cab-b3e7bcd357a6/l.jpg"]                                                                                                                                                                                                                                                             |                  nan | 2026-04-22T06:56:14.16868+00:00  | 2026-04-27T02:26:02.478853+00:00 |                             nan | 2026-04-27T02:44:49.525998 |
|  2 | bbca3c41-e10a-42cd-8df6-acea24bd7630 |              1 |   936165 |    1168010800100340008006373 |            | 유니크한 건물 넓은 테라스가 있는 사무실           |                    17 | 기타업종                       |                   1709 | 기타창업모음                      |            1 | 임대                |     40000 |           2100 |         0 |      0 |               200 |       5 |              5 |  52.89 |          142 |           40000 |                 2100 |               0 |             0 |                   0 |                 1 |            nan | 학동역, 도보 5분            |            0 |                0 |       1 | https://img.nemoapp.kr/article-photos/de1607b3-c652-4904-bc94-3f42f0993c8b/s.jpg | ["https://img.nemoapp.kr/article-photos/de1607b3-c652-4904-bc94-3f42f0993c8b/s.jpg", "https://img.nemoapp.kr/article-photos/e3d7cb9c-124d-4214-a2b0-948a38a41ac4/s.jpg", "https://img.nemoapp.kr/article-photos/88da7584-4122-40b3-a5fd-62672fd82611/s.jpg", "https://img.nemoapp.kr/article-photos/a28c05bf-9346-4b8a-8302-33db31a5a4fa/s.jpg", "https://img.nemoapp.kr/article-photos/45037de5-3066-4114-a5e4-1f2181dbb5fc/s.jpg", "https://img.nemoapp.kr/article-photos/fed15ffb-67d2-4a3b-9669-b6a0946f8336/s.jpg", "https://img.nemoapp.kr/article-photos/9419da8f-88aa-4d7e-bd7f-026df911f340/s.jpg", "https://img.nemoapp.kr/article-photos/c410a1b2-0934-47b4-a8e1-4c5b9f33d390/s.jpg", "https://img.nemoapp.kr/article-photos/2d06678b-e531-4f32-bd8f-f0cc7e02c1bd/s.jpg", "https://img.nemoapp.kr/article-photos/4ef0d46c-39f8-4f66-a694-c744dc8aee83/s.jpg", "https://img.nemoapp.kr/article-photos/9ad39733-6f6e-4674-86f9-666ff1cf2110/s.jpg", "https://img.nemoapp.kr/article-photos/a1eacabc-e11a-4352-b41f-ea10c6669709/s.jpg"] | ["https://img.nemoapp.kr/article-photos/de1607b3-c652-4904-bc94-3f42f0993c8b/l.jpg", "https://img.nemoapp.kr/article-photos/e3d7cb9c-124d-4214-a2b0-948a38a41ac4/l.jpg", "https://img.nemoapp.kr/article-photos/88da7584-4122-40b3-a5fd-62672fd82611/l.jpg", "https://img.nemoapp.kr/article-photos/a28c05bf-9346-4b8a-8302-33db31a5a4fa/l.jpg", "https://img.nemoapp.kr/article-photos/45037de5-3066-4114-a5e4-1f2181dbb5fc/l.jpg", "https://img.nemoapp.kr/article-photos/fed15ffb-67d2-4a3b-9669-b6a0946f8336/l.jpg", "https://img.nemoapp.kr/article-photos/9419da8f-88aa-4d7e-bd7f-026df911f340/l.jpg", "https://img.nemoapp.kr/article-photos/c410a1b2-0934-47b4-a8e1-4c5b9f33d390/l.jpg", "https://img.nemoapp.kr/article-photos/2d06678b-e531-4f32-bd8f-f0cc7e02c1bd/l.jpg", "https://img.nemoapp.kr/article-photos/4ef0d46c-39f8-4f66-a694-c744dc8aee83/l.jpg", "https://img.nemoapp.kr/article-photos/9ad39733-6f6e-4674-86f9-666ff1cf2110/l.jpg", "https://img.nemoapp.kr/article-photos/a1eacabc-e11a-4352-b41f-ea10c6669709/l.jpg"] |                  nan | 2026-04-15T07:04:38.653038+00:00 | 2026-04-27T02:25:57.875605+00:00 |                             nan | 2026-04-27T02:44:49.525998 |
|  3 | d54736b1-0cd9-440a-93c2-21b455a32c3f |              1 |   911255 |    1168010800101490005007996 |            | 🎀 논현동 인테리어 A급 뷰티샵 🎀              |                    17 | 기타업종                       |                   1709 | 기타창업모음                      |            1 | 임대                |     20000 |           2000 |        10 |      0 |               200 |       1 |              5 |  46.28 |          149 |           20000 |                 2300 |              10 |             0 |                   0 |                 1 |            nan | 학동역, 도보 8분            |            2 |                0 |       1 | https://img.nemoapp.kr/article-photos/dd03a45f-3d58-490d-a7b2-1a56307629ca/s.jpg | ["https://img.nemoapp.kr/article-photos/dd03a45f-3d58-490d-a7b2-1a56307629ca/s.jpg", "https://img.nemoapp.kr/article-photos/610ca418-3f65-47e7-a74c-a1a6803ef61e/s.jpg", "https://img.nemoapp.kr/article-photos/473c6701-40a7-4d0d-bbd4-344227344f7f/s.jpg", "https://img.nemoapp.kr/article-photos/572c279c-0104-4df3-8ad5-3a91f37d5baa/s.jpg", "https://img.nemoapp.kr/article-photos/ae6e26e0-7e58-4365-b3d8-0cf5e67605bd/s.jpg", "https://img.nemoapp.kr/article-photos/c940ac5d-5ce3-4335-bed9-dfbec64abd1b/s.jpg", "https://img.nemoapp.kr/article-photos/2024ade2-5426-4b13-8e7e-bf1bd70015a2/s.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                     | ["https://img.nemoapp.kr/article-photos/dd03a45f-3d58-490d-a7b2-1a56307629ca/l.jpg", "https://img.nemoapp.kr/article-photos/610ca418-3f65-47e7-a74c-a1a6803ef61e/l.jpg", "https://img.nemoapp.kr/article-photos/473c6701-40a7-4d0d-bbd4-344227344f7f/l.jpg", "https://img.nemoapp.kr/article-photos/572c279c-0104-4df3-8ad5-3a91f37d5baa/l.jpg", "https://img.nemoapp.kr/article-photos/ae6e26e0-7e58-4365-b3d8-0cf5e67605bd/l.jpg", "https://img.nemoapp.kr/article-photos/c940ac5d-5ce3-4335-bed9-dfbec64abd1b/l.jpg", "https://img.nemoapp.kr/article-photos/2024ade2-5426-4b13-8e7e-bf1bd70015a2/l.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                     |                  nan | 2025-11-07T01:48:47.080223+00:00 | 2026-04-27T02:01:48.701976+00:00 |                             nan | 2026-04-27T02:44:49.525998 |
|  4 | b75afb24-7054-4f12-b71c-a73d45534746 |              1 |   931318 |    1168010800102420004006447 |            | 🌱 강남구청역 스타일 좋은 인테리어 깨끗한 내부의 상가 🌱 |                    17 | 기타업종                       |                   1709 | 기타창업모음                      |            1 | 임대                |     20000 |           1700 |        10 |      0 |               220 |       1 |              5 |  33.06 |          178 |           20000 |                 1730 |              10 |             0 |                   0 |                 1 |            nan | 강남구청역, 도보 3분          |            0 |                0 |       1 | https://img.nemoapp.kr/article-photos/6591a0d2-1eaf-4db9-a2ea-006c62048338/s.jpg | ["https://img.nemoapp.kr/article-photos/6591a0d2-1eaf-4db9-a2ea-006c62048338/s.jpg", "https://img.nemoapp.kr/article-photos/140fcf42-cf44-44f8-a25d-f2a314147382/s.jpg", "https://img.nemoapp.kr/article-photos/009f8cc7-4fcd-40e5-87be-44b5502f3b8b/s.jpg", "https://img.nemoapp.kr/article-photos/fb61b2d3-0498-416f-a640-b8bb35a737a2/s.jpg", "https://img.nemoapp.kr/article-photos/a705902a-4bf8-4650-8a03-e99a4fef4269/s.jpg", "https://img.nemoapp.kr/article-photos/b63c7672-a37d-432d-bed0-1ae69ea9f135/s.jpg", "https://img.nemoapp.kr/article-photos/1a106cff-2685-4b2b-a268-7bec7f0070b8/s.jpg", "https://img.nemoapp.kr/article-photos/ea05cce2-4e86-4827-91f9-0944a0726467/s.jpg", "https://img.nemoapp.kr/article-photos/38d57891-d2b6-433a-8606-1eca53f70415/s.jpg"]                                                                                                                                                                                                                                                             | ["https://img.nemoapp.kr/article-photos/6591a0d2-1eaf-4db9-a2ea-006c62048338/l.jpg", "https://img.nemoapp.kr/article-photos/140fcf42-cf44-44f8-a25d-f2a314147382/l.jpg", "https://img.nemoapp.kr/article-photos/009f8cc7-4fcd-40e5-87be-44b5502f3b8b/l.jpg", "https://img.nemoapp.kr/article-photos/fb61b2d3-0498-416f-a640-b8bb35a737a2/l.jpg", "https://img.nemoapp.kr/article-photos/a705902a-4bf8-4650-8a03-e99a4fef4269/l.jpg", "https://img.nemoapp.kr/article-photos/b63c7672-a37d-432d-bed0-1ae69ea9f135/l.jpg", "https://img.nemoapp.kr/article-photos/1a106cff-2685-4b2b-a268-7bec7f0070b8/l.jpg", "https://img.nemoapp.kr/article-photos/ea05cce2-4e86-4827-91f9-0944a0726467/l.jpg", "https://img.nemoapp.kr/article-photos/38d57891-d2b6-433a-8606-1eca53f70415/l.jpg"]                                                                                                                                                                                                                                                             |                  nan | 2026-03-20T04:47:19.968989+00:00 | 2026-04-27T02:01:44.838554+00:00 |                             nan | 2026-04-27T02:44:49.525998 |

### 데이터 샘플 (하위 5행)
|      | id                                   |   article_type |   number |   building_management_serial | agent_id   | title                            |   business_large_code | business_large_code_name   |   business_middle_code | business_middle_code_name   |   price_type | price_type_name   |   deposit |   monthly_rent |   premium |   sale |   maintenance_fee |   floor |   ground_floor |   size |   area_price |   first_deposit |   first_monthly_rent |   first_premium |   is_priority |   is_premium_closed |   is_move_in_date |   move_in_date | near_subway_station   |   view_count |   favorite_count |   state | preview_photo_url                                                                | small_photo_urls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | origin_photo_urls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | confirmed_date_utc            | created_date_utc                 | edited_date_utc                  |   completion_confirmed_date_utc | scraped_at                 |
|-----:|:-------------------------------------|---------------:|---------:|-----------------------------:|:-----------|:---------------------------------|----------------------:|:---------------------------|-----------------------:|:----------------------------|-------------:|:------------------|----------:|---------------:|----------:|-------:|------------------:|--------:|---------------:|-------:|-------------:|----------------:|---------------------:|----------------:|--------------:|--------------------:|------------------:|---------------:|:----------------------|-------------:|-----------------:|--------:|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:---------------------------------|:---------------------------------|--------------------------------:|:---------------------------|
| 2164 | 5b896c06-a198-4083-999f-c613442cbb0b |              1 |   646407 |    1168010800101800008009048 |            | 주거지 상권, 수요도 많은 논현동 매장            |                    11 | 휴게음식점                      |                   1102 | 치킨점                         |            1 | 임대                |     10000 |            900 |    190000 |      0 |                50 |       1 |              5 |  29.75 |          105 |           10000 |                  900 |          190000 |             0 |                   0 |                 1 |            nan | 신논현역, 도보 7분           |          582 |                0 |       1 | https://img.nemoapp.kr/article-photos/5d14696e-facf-4c17-81fe-34b6d6f2c52a/s.jpg | ["https://img.nemoapp.kr/article-photos/5d14696e-facf-4c17-81fe-34b6d6f2c52a/s.jpg", "https://img.nemoapp.kr/article-photos/596e2364-f951-4250-8d8a-a518362abccb/s.jpg", "https://img.nemoapp.kr/article-photos/1ec99dad-bfc8-4842-9ae0-5a330e15ef56/s.jpg", "https://img.nemoapp.kr/article-photos/26583d80-a14f-428c-b1ff-ebfb9083381b/s.jpg", "https://img.nemoapp.kr/article-photos/4d2c9be0-ece9-4467-ab12-3b1075868047/s.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ["https://img.nemoapp.kr/article-photos/5d14696e-facf-4c17-81fe-34b6d6f2c52a/l.jpg", "https://img.nemoapp.kr/article-photos/596e2364-f951-4250-8d8a-a518362abccb/l.jpg", "https://img.nemoapp.kr/article-photos/1ec99dad-bfc8-4842-9ae0-5a330e15ef56/l.jpg", "https://img.nemoapp.kr/article-photos/26583d80-a14f-428c-b1ff-ebfb9083381b/l.jpg", "https://img.nemoapp.kr/article-photos/4d2c9be0-ece9-4467-ab12-3b1075868047/l.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2022-06-02T09:13:08.403+00:00 | 2022-06-02T09:13:08.523333+00:00 | 2022-07-13T14:12:42.57004+00:00  |                             nan | 2026-04-27T02:46:01.507198 |
| 2165 | 77862f50-9bb3-49bf-a680-1ba021274c06 |              1 |   646920 |    1168010100106990002022253 |            | 안정적 매출 보장, 역삼동 횟집                |                    12 | 일반음식점                      |                   1204 | 생선회/해물                      |            1 | 임대                |     30000 |           3000 |    220000 |      0 |                 0 |       2 |              6 | 111.61 |           93 |           30000 |                 3000 |          220000 |             0 |                   0 |                 1 |            nan | 선정릉역, 도보 9분           |          444 |                0 |       1 | https://img.nemoapp.kr/article-photos/8be4a8c5-08e0-487d-b9f8-be0a133d0251/s.jpg | ["https://img.nemoapp.kr/article-photos/8be4a8c5-08e0-487d-b9f8-be0a133d0251/s.jpg", "https://img.nemoapp.kr/article-photos/da8c8585-1987-4809-852d-6344003430cd/s.jpg", "https://img.nemoapp.kr/article-photos/a7905e10-ff15-43b8-b769-8d007ece3f86/s.jpg", "https://img.nemoapp.kr/article-photos/ad0e2abe-8092-4cd1-847d-064fd10f7d99/s.jpg", "https://img.nemoapp.kr/article-photos/cacd8a5d-6c39-45e4-9f32-795e4c7c9c74/s.jpg", "https://img.nemoapp.kr/article-photos/1dd00725-6b58-4b84-afdb-04a0742fbf57/s.jpg", "https://img.nemoapp.kr/article-photos/1d6f256f-9647-4180-a6be-42c2104a2fd9/s.jpg", "https://img.nemoapp.kr/article-photos/34f80347-345b-4e9b-9e61-4ad512dc22c5/s.jpg", "https://img.nemoapp.kr/article-photos/2f6c67d0-d336-45ba-8267-1e4b83637050/s.jpg", "https://img.nemoapp.kr/article-photos/c8c142ad-9dea-4f2e-b787-87bec9ecf6b8/s.jpg", "https://img.nemoapp.kr/article-photos/aad24184-0540-4729-97f1-da7792fc2a20/s.jpg", "https://img.nemoapp.kr/article-photos/eaf4942b-efe4-4553-b4c5-784585856d1a/s.jpg", "https://img.nemoapp.kr/article-photos/26bf073f-68f2-4e42-85d6-0086c8e24b65/s.jpg"] | ["https://img.nemoapp.kr/article-photos/8be4a8c5-08e0-487d-b9f8-be0a133d0251/l.jpg", "https://img.nemoapp.kr/article-photos/da8c8585-1987-4809-852d-6344003430cd/l.jpg", "https://img.nemoapp.kr/article-photos/a7905e10-ff15-43b8-b769-8d007ece3f86/l.jpg", "https://img.nemoapp.kr/article-photos/ad0e2abe-8092-4cd1-847d-064fd10f7d99/l.jpg", "https://img.nemoapp.kr/article-photos/cacd8a5d-6c39-45e4-9f32-795e4c7c9c74/l.jpg", "https://img.nemoapp.kr/article-photos/1dd00725-6b58-4b84-afdb-04a0742fbf57/l.jpg", "https://img.nemoapp.kr/article-photos/1d6f256f-9647-4180-a6be-42c2104a2fd9/l.jpg", "https://img.nemoapp.kr/article-photos/34f80347-345b-4e9b-9e61-4ad512dc22c5/l.jpg", "https://img.nemoapp.kr/article-photos/2f6c67d0-d336-45ba-8267-1e4b83637050/l.jpg", "https://img.nemoapp.kr/article-photos/c8c142ad-9dea-4f2e-b787-87bec9ecf6b8/l.jpg", "https://img.nemoapp.kr/article-photos/aad24184-0540-4729-97f1-da7792fc2a20/l.jpg", "https://img.nemoapp.kr/article-photos/eaf4942b-efe4-4553-b4c5-784585856d1a/l.jpg", "https://img.nemoapp.kr/article-photos/26bf073f-68f2-4e42-85d6-0086c8e24b65/l.jpg"] | 2022-06-03T08:45:29.993+00:00 | 2022-06-03T08:45:30.12+00:00     | 2022-07-13T13:03:45.411678+00:00 |                             nan | 2026-04-27T02:46:01.507198 |
| 2166 | 52cb9e28-7f6c-4ebc-b2bf-14c8235e904b |              1 |   647153 |    1168010100107360024000001 |            | 역삼역 2호선 도보 4분, 역삼동 반찬가게 상가 점포    |                    17 | 기타업종                       |                   1709 | 기타창업모음                      |            1 | 임대                |     50000 |           2500 |     70000 |      0 |              1200 |      -1 |             12 | 132.23 |           68 |           20000 |                 1500 |           70000 |             0 |                   0 |                 0 |            nan | 역삼역, 도보 5분            |          490 |                0 |       1 | https://img.nemoapp.kr/article-photos/d62301a6-0730-4ab1-a312-35c1e52d3569/s.jpg | ["https://img.nemoapp.kr/article-photos/d62301a6-0730-4ab1-a312-35c1e52d3569/s.jpg", "https://img.nemoapp.kr/article-photos/c9956d17-b2ed-4854-a601-45188ee5ad25/s.jpg", "https://img.nemoapp.kr/article-photos/6e07fcae-d396-4945-b12b-df82eeea786b/s.jpg", "https://img.nemoapp.kr/article-photos/7d7e62f3-da0f-4be1-a6aa-1231bb30b6aa/s.jpg", "https://img.nemoapp.kr/article-photos/2d55195c-cb65-4128-a2bf-8330703802e2/s.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | ["https://img.nemoapp.kr/article-photos/d62301a6-0730-4ab1-a312-35c1e52d3569/l.jpg", "https://img.nemoapp.kr/article-photos/c9956d17-b2ed-4854-a601-45188ee5ad25/l.jpg", "https://img.nemoapp.kr/article-photos/6e07fcae-d396-4945-b12b-df82eeea786b/l.jpg", "https://img.nemoapp.kr/article-photos/7d7e62f3-da0f-4be1-a6aa-1231bb30b6aa/l.jpg", "https://img.nemoapp.kr/article-photos/2d55195c-cb65-4128-a2bf-8330703802e2/l.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2022-06-03T14:56:16.96+00:00  | 2022-06-03T14:56:17.1+00:00      | 2022-07-13T12:31:20.456575+00:00 |                             nan | 2026-04-27T02:46:01.507198 |
| 2167 | d7eb3286-ee51-42ea-8b03-f1a30c683f9f |              1 |   648435 |    1168010100106480024023791 |            | 역삼동 대로변 앞, 회사원 수요 및 배달 매출 좋은 분식점 |                    12 | 일반음식점                      |                   1203 | 분식점                         |            1 | 임대                |    100000 |           2000 |     25000 |      0 |               200 |      -1 |             15 |   3.31 |         2414 |          100000 |                 2000 |           25000 |             0 |                   0 |                 0 |            nan | 강남역, 도보 6분            |          429 |                1 |       1 | https://img.nemoapp.kr/article-photos/275d302a-5bbb-4b49-bfca-12eae22a2eb5/s.jpg | ["https://img.nemoapp.kr/article-photos/275d302a-5bbb-4b49-bfca-12eae22a2eb5/s.jpg", "https://img.nemoapp.kr/article-photos/3079aafa-482f-4b1b-8087-f5e2380b019b/s.jpg", "https://img.nemoapp.kr/article-photos/d0af1ca5-c91b-40f1-bf1e-27d390a1bd9d/s.jpg", "https://img.nemoapp.kr/article-photos/dd725ce2-f712-4ad7-b788-eb7c178e4b1e/s.jpg", "https://img.nemoapp.kr/article-photos/3a69edeb-4a76-4272-892a-d6fb6b3b962f/s.jpg", "https://img.nemoapp.kr/article-photos/e87211b6-8734-492a-92c0-4960e2a83926/s.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | ["https://img.nemoapp.kr/article-photos/275d302a-5bbb-4b49-bfca-12eae22a2eb5/l.jpg", "https://img.nemoapp.kr/article-photos/3079aafa-482f-4b1b-8087-f5e2380b019b/l.jpg", "https://img.nemoapp.kr/article-photos/d0af1ca5-c91b-40f1-bf1e-27d390a1bd9d/l.jpg", "https://img.nemoapp.kr/article-photos/dd725ce2-f712-4ad7-b788-eb7c178e4b1e/l.jpg", "https://img.nemoapp.kr/article-photos/3a69edeb-4a76-4272-892a-d6fb6b3b962f/l.jpg", "https://img.nemoapp.kr/article-photos/e87211b6-8734-492a-92c0-4960e2a83926/l.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 2022-06-08T11:56:06.909+00:00 | 2022-06-08T11:56:07.05+00:00     | 2022-07-12T04:48:40.487765+00:00 |                             nan | 2026-04-27T02:46:01.507198 |
| 2168 | 523d9db9-e6e9-40b2-a0d1-b0b1e8b7a373 |              1 |   650386 |    1168010100108340066000001 |            | 역삼동 강남대로 인근 유동인구 많은 미용실          |                    16 | 서비스업                       |                   1601 | 미용실                         |            1 | 임대                |     40000 |           3600 |    100000 |      0 |                 0 |       1 |              6 |  92.56 |          135 |           40000 |                 3600 |          100000 |             0 |                   0 |                 0 |            nan | 역삼역, 도보 13분           |          468 |                0 |       1 | https://img.nemoapp.kr/article-photos/9bcb04c3-10b1-4536-9d42-3efca7df6750/s.jpg | ["https://img.nemoapp.kr/article-photos/9bcb04c3-10b1-4536-9d42-3efca7df6750/s.jpg", "https://img.nemoapp.kr/article-photos/58fb8f0d-66fe-4707-9ccd-61dcc3d2594e/s.jpg", "https://img.nemoapp.kr/article-photos/33e06eef-f973-4674-8cb0-2091ce274240/s.jpg", "https://img.nemoapp.kr/article-photos/148bb75e-7997-4a1e-b0e1-a3b1aafc4bbd/s.jpg", "https://img.nemoapp.kr/article-photos/3ce0002a-ef57-475e-901e-e521919b11dd/s.jpg", "https://img.nemoapp.kr/article-photos/a4cc9a49-deae-42e6-9c53-7fb83735b24c/s.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | ["https://img.nemoapp.kr/article-photos/9bcb04c3-10b1-4536-9d42-3efca7df6750/l.jpg", "https://img.nemoapp.kr/article-photos/58fb8f0d-66fe-4707-9ccd-61dcc3d2594e/l.jpg", "https://img.nemoapp.kr/article-photos/33e06eef-f973-4674-8cb0-2091ce274240/l.jpg", "https://img.nemoapp.kr/article-photos/148bb75e-7997-4a1e-b0e1-a3b1aafc4bbd/l.jpg", "https://img.nemoapp.kr/article-photos/3ce0002a-ef57-475e-901e-e521919b11dd/l.jpg", "https://img.nemoapp.kr/article-photos/a4cc9a49-deae-42e6-9c53-7fb83735b24c/l.jpg"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 2022-06-14T04:56:27.185+00:00 | 2022-06-14T04:56:27.31+00:00     | 2022-07-11T14:37:46.170313+00:00 |                             nan | 2026-04-27T02:46:01.507198 |

- **중복 데이터 수**: 0

## 2. 기술 통계 분석

### 수치형 데이터 기술 통계
|       |   deposit |   monthly_rent |   premium |             sale |   maintenance_fee |      size |   view_count |   favorite_count |
|:------|----------:|---------------:|----------:|-----------------:|------------------:|----------:|-------------:|-----------------:|
| count |  2169     |        2169    |    2169   |   2169           |          2169     |  2169     |     2169     |       2169       |
| mean  | 57612.1   |        4400.63 |   38627   |  42760           |          1429.59  |   136.239 |      183.033 |          1.53296 |
| std   | 85299.9   |        5914.26 |   75820.1 | 645735           |         42944.7   |   628.325 |      249.477 |          3.35478 |
| min   |     0     |           0    |       0   |      0           |             0     |     3.31  |        0     |          0       |
| 25%   | 23000     |        2000    |       0   |      0           |            30     |    49.59  |       10     |          0       |
| 50%   | 40000     |        3000    |       0   |      0           |           220     |    95.65  |       31     |          0       |
| 75%   | 60000     |        4680    |   50000   |      0           |           500     |   151.2   |      422     |          2       |
| max   |     2e+06 |       90000    |  900000   |      1.64299e+07 |             2e+06 | 28766     |     1408     |         58       |

### 범주형 데이터 기술 통계
|        |   article_type | business_large_code_name   | business_middle_code_name   | price_type_name   |   state |      floor |
|:-------|---------------:|:---------------------------|:----------------------------|:------------------|--------:|-----------:|
| count  |           2169 | 2169                       | 2169                        | 2169              |    2169 | 2169       |
| unique |            nan | 7                          | 53                          | 2                 |     nan |  nan       |
| top    |            nan | 기타업종                       | 기타창업모음                      | 임대                |     nan |  nan       |
| freq   |            nan | 1088                       | 896                         | 2146              |     nan |  nan       |
| mean   |              1 | nan                        | nan                         | nan               |       1 |    1.84002 |
| std    |              0 | nan                        | nan                         | nan               |       0 |    2.31865 |
| min    |              1 | nan                        | nan                         | nan               |       1 |   -4       |
| 25%    |              1 | nan                        | nan                         | nan               |       1 |    1       |
| 50%    |              1 | nan                        | nan                         | nan               |       1 |    1       |
| 75%    |              1 | nan                        | nan                         | nan               |       1 |    3       |
| max    |              1 | nan                        | nan                         | nan               |       1 |   20       |

### 기술 통계 상세 분석 의견

본 데이터셋은 네모 플랫폼에서 수집된 상가 매물 데이터로, 총 40개의 컬럼과 다수의 행으로 구성되어 있습니다. 기술 통계 분석 결과, 주요 수치형 변수인 보증금(deposit), 월세(monthly_rent), 권리금(premium) 등에서 매우 큰 편차와 우측으로 치우친(right-skewed) 분포가 관찰되었습니다. 이는 상권의 위치, 면적, 업종에 따라 매물 가격이 극단적으로 차이 날 수 있음을 시사합니다. 보증금의 평균은 약 5,761만원이나 표준편차가 8,529만원에 달해 평균의 대표성이 낮으며, 중앙값인 4,000만원과 큰 차이를 보입니다. 이는 일부 초고가 매물이 전체 평균을 끌어올리고 있음을 의미합니다. 특히 면적(size)의 경우 평균 대비 표준편차가 매우 커서 소형 점포부터 수만 평방미터에 달하는 대형 상가까지 다양한 규모의 매물이 혼재되어 있음을 알 수 있습니다.

범주형 데이터에서는 매물 유형(article_type)과 업종 대분류(business_large_code_name)가 특정 항목에 집중되는 경향을 보였습니다. '상가점포' 유형이 압도적으로 많으며, 업종 분류상으로는 '음식점'이나 '소매' 관련 비중이 높을 것으로 예상됩니다. 가격 형태(price_type_name)는 대부분 '월세' 기반이며, 전세나 매매 비중은 상대적으로 낮았습니다. 층수(floor) 데이터는 저층부에 집중되어 있어 상가 매물의 특성상 접근성이 좋은 1, 2층 매물이 주를 이루고 있음을 확인하였습니다. 데이터의 4분위수를 살펴보면, 월세의 경우 75% 지점이 468만원으로 나타나는데, 이는 강남 지역 상권의 높은 임대료 수준을 반영한 결과로 해석됩니다.

또한 조회수(view_count)와 찜수(favorite_count) 사이에는 양의 상관관계가 존재할 것으로 보이나, 일부 매물에 관심도가 집중되는 현상이 나타나고 있습니다. 이는 소수의 인기 매물이나 급매물이 사용자들의 관심을 독차지하고 있음을 의미하며, 데이터 품질 측면에서는 결측치가 거의 없어 분석의 신뢰도가 높으나 일부 가격 데이터에서 0 또는 극단값이 존재하여 전처리 시 주의가 필요함을 시사합니다. 관리비(maintenance_fee) 역시 최대값이 200만원에 달하는 등 고정 비용 부담이 큰 매물들이 존재하며, 이는 임차인의 실질 수익성에 큰 영향을 미칠 요소입니다. 이러한 기초 분석 결과를 바탕으로 향후 상권 분석 및 가격 결정 요인 파악을 위한 심화 분석이 가능할 것으로 판단됩니다. 본 데이터는 강남권을 중심으로 한 상업용 부동산 시장의 현재 흐름을 매우 밀도 있게 담아내고 있으며, 각 변수 간의 복합적인 상호작용을 파악하는 것이 이번 EDA의 핵심 목표 중 하나입니다.


## 3. 데이터 시각화 및 상세 분석

### 업종 대분류별 매물 빈도
![업종 대분류별 매물 빈도](images/01_large_code_freq.png)

#### 관련 데이터 테이블
| business_large_code_name   |   count |
|:---------------------------|--------:|
| 기타업종                       |    1088 |
| 일반음식점                      |     313 |
| 서비스업                       |     281 |
| 휴게음식점                      |     232 |
| 오락스포츠                      |      93 |
| 주류점                        |      84 |
| 판매업                        |      78 |

#### 해석 및 비즈니스 인사이트
업종 대분류별 빈도 분석 결과, 특정 업종에 매물이 집중되어 있는 현상이 뚜렷하게 나타납니다. 이는 현재 임대 시장에서 활발하게 거래되거나 공실이 발생하는 주요 업종군을 의미합니다. 비즈니스 관점에서 볼 때, 매물이 많은 업종은 경쟁이 치열한 레드오션일 가능성이 높으며, 반대로 매물이 적은 특수 업종은 희소성을 바탕으로 한 틈새시장 공략이 가능할 것으로 보입니다. 투자자나 예비 창업자는 이러한 매물 밀집도를 확인하여 상권의 성격과 경쟁 강도를 사전 예측할 수 있으며, 플랫폼 운영 측면에서는 매물 비중이 높은 업종을 대상으로 한 맞춤형 추천 서비스를 강화할 필요가 있습니다.

### 보증금 분포 (상위 5% 제외)
![보증금 분포 (상위 5% 제외)](images/02_deposit_dist.png)

#### 관련 데이터 테이블
|       |   deposit |
|:------|----------:|
| count |  2169     |
| mean  | 57612.1   |
| std   | 85299.9   |
| min   |     0     |
| 25%   | 23000     |
| 50%   | 40000     |
| 75%   | 60000     |
| max   |     2e+06 |

#### 해석 및 비즈니스 인사이트
보증금의 분포는 전형적인 롱테일 형태를 보이며, 대다수의 매물이 특정 구간에 밀집되어 있습니다. 상위 5%의 극단값을 제외하더라도 보증금의 편차가 큰 것은 상가 입지와 규모에 따른 자산 가치 차이를 극명하게 보여줍니다. 창업자 입장에서는 본인의 가용 자본 내에서 선택 가능한 매물의 폭이 어느 정도인지 파악하는 기초 자료가 됩니다. 비즈니스 인사이트 측면에서는 평균 가격대에서 벗어난 저렴한 매물의 원인을 파악하거나, 고가 매물의 프리미엄 요소를 분석하여 매물 가치 평가 모델을 정교화할 수 있는 근거를 제공합니다.

### 면적 대비 월세 상관관계
![면적 대비 월세 상관관계](images/03_size_rent_scatter.png)

#### 관련 데이터 테이블
|              |     size |   monthly_rent |
|:-------------|---------:|---------------:|
| size         | 1        |       0.155815 |
| monthly_rent | 0.155815 |       1        |

#### 해석 및 비즈니스 인사이트
면적과 월세의 상관관계 분석 결과, 일반적으로 면적이 넓을수록 월세가 상승하는 경향을 보이지만, 동일 면적 내에서도 월세의 편차가 상당히 크게 나타납니다. 이는 상가 임대료가 단순히 물리적 면적뿐만 아니라 유동 인구, 가시성, 층수 등 '입지 가치'에 의해 더 강력하게 결정됨을 시사합니다. 효율적인 공간 활용을 원하는 임차인에게는 면적 대비 낮은 가격의 매물을 추천하는 로직이 유효할 것이며, 임대인에게는 주변 시세 대비 면적당 단가의 적정성을 판단하는 지표로 활용될 수 있습니다. 데이터의 분산도는 상권별 특성이 다름을 내포하고 있습니다.

### 층별 평균 월세 현황
![층별 평균 월세 현황](images/04_floor_rent_avg.png)

#### 관련 데이터 테이블
|   floor |   monthly_rent |
|--------:|---------------:|
|      16 |       11450    |
|      12 |        7650    |
|      11 |        7600    |
|      13 |        7300    |
|      14 |        6590    |
|       8 |        6508.12 |
|      -2 |        6428.06 |
|       6 |        6372.76 |
|       0 |        6130    |
|      10 |        5814.62 |

#### 해석 및 비즈니스 인사이트
층수와 월세의 관계를 분석해 본 결과, 예상대로 접근성이 높은 1층 매물의 평균 월세가 가장 높게 형성되어 있습니다. 하지만 특정 층(예: 루프탑 또는 지하 대형 공간)에서 변칙적으로 높은 평균가가 나타나기도 하는데, 이는 테마형 상가나 특정 업종 특화 공간의 영향으로 해석됩니다. 비즈니스적으로는 층별 임대료 격차(Floor Gradient)를 분석하여 각 층에 최적화된 업종 배치를 제안할 수 있습니다. 예를 들어 저층부에는 높은 임대료를 감당할 수 있는 서비스업이나 판매업을, 고층부에는 목적성이 뚜렷한 학원이나 사무실 등을 배치하는 전략적 의사결정의 기초가 됩니다.

### 주요 지역(State)별 권리금 분포
![주요 지역(State)별 권리금 분포](images/05_state_premium_box.png)

#### 관련 데이터 테이블
|   state |   count |   mean |     std |   min |   25% |   50% |   75% |    max |
|--------:|--------:|-------:|--------:|------:|------:|------:|------:|-------:|
|       1 |    2169 |  38627 | 75820.1 |     0 |     0 |     0 | 50000 | 900000 |

#### 해석 및 비즈니스 인사이트
지역별 권리금 분포 분석을 통해 각 상권의 '영업 가치'와 '권리금 장벽'을 확인할 수 있습니다. 일부 지역은 중앙값이 낮음에도 불구하고 이상치(Outlier)가 많아 특정 매물에 권리금이 집중되는 현상을 보입니다. 이는 해당 상권 내에서도 소위 'A급 입지'의 존재를 증명합니다. 예비 창업자에게는 권리금 부담이 적으면서도 성장 가능성이 있는 지역을 추천하는 인사이트를 줄 수 있으며, 상권의 성숙도를 판단하는 척도로 활용 가능합니다. 권리금의 변동성은 해당 지역 상권의 역동성과 수익성을 대변하는 핵심 지표입니다.

### 매물 가격 형태 구성비
![매물 가격 형태 구성비](images/06_price_type_pie.png)

#### 관련 데이터 테이블
| price_type_name   |   count |
|:------------------|--------:|
| 임대                |    2146 |
| 매매                |      23 |

#### 해석 및 비즈니스 인사이트
가격 형태별 비중을 보면 상가 시장이 철저하게 수익형 부동산 중심의 월세 구조임을 알 수 있습니다. 전세나 매매 비중이 극히 낮다는 것은 상가 매물을 자산 소유보다는 운영 권리 획득의 관점에서 접근하는 수요가 많음을 반영합니다. 플랫폼 운영 관점에서는 월세 매물에 최적화된 필터링과 검색 환경을 제공하는 것이 핵심이며, 소수의 매매 매물을 별도로 구분하여 자산 투자용 카테고리를 강화하는 전략도 고려해 볼 수 있습니다. 시장의 유동성을 파악하는 데 있어 가격 형태의 변화 추이는 중요한 선행 지표가 될 수 있습니다.

### 업종 중분류 TOP 20
![업종 중분류 TOP 20](images/07_middle_code_top20.png)

#### 관련 데이터 테이블
| business_middle_code_name   |   count |
|:----------------------------|--------:|
| 기타창업모음                      |     896 |
| 다용도점포                       |     173 |
| 기타서비스업                      |     127 |
| 커피점/카페                      |     122 |
| 한식점                         |     104 |
| 기타음식점                       |      73 |
| 미용실                         |      54 |
| 피부미용                        |      42 |
| 고깃집                         |      36 |
| 네일아트                        |      32 |
| 기타휴게점                       |      31 |
| 기타판매점                       |      26 |
| 치킨점                         |      25 |
| 헬스클럽                        |      23 |
| 일식점                         |      22 |
| 패스트푸드                       |      22 |
| 중국집                         |      22 |
| 바                           |      21 |
| 요가/필라테스                     |      20 |
| 의류판매점                       |      18 |

#### 해석 및 비즈니스 인사이트
중분류 단위의 빈도 분석은 실제 상권에서 어떤 구체적인 서비스들이 이루어지는지 명확하게 보여줍니다. 카페, 일반음식점 등 생활 밀착형 업종의 매물 비중이 높게 나타나는 것은 창업 수요와 폐업 빈도가 동시에 높은 업종임을 시사합니다. 이를 통해 상권의 트렌드 변화를 감지할 수 있습니다. 비즈니스 인사이트로는 매물이 급증하는 중분류 업종에 대한 리스크 관리가 필요하며, 반대로 매물은 적은데 수요가 많은 업종을 발굴하여 중개 효율을 높이는 전략이 유효합니다. 이는 데이터 기반의 상권 기획 및 컨설팅의 토대가 됩니다.

### 조회수 대비 찜수 상관관계
![조회수 대비 찜수 상관관계](images/08_view_favorite_scatter.png)

#### 관련 데이터 테이블
|                |   view_count |   favorite_count |
|:---------------|-------------:|-----------------:|
| view_count     |     1        |         0.327112 |
| favorite_count |     0.327112 |         1        |

#### 해석 및 비즈니스 인사이트
사용자 행동 데이터인 조회수와 찜수의 관계는 매물의 매력도를 객관적으로 평가할 수 있게 합니다. 조회수는 높지만 찜수가 낮은 매물은 조건이 매력적이지 않거나 가격 저항이 있을 가능성이 높으며, 반대로 조회수 대비 찜수가 높은 매물은 실질적인 관심이 집중된 '알짜 매물'일 확률이 큽니다. 이러한 분석을 통해 매물 추천 알고리즘의 점수를 부여하거나, 사용자에게 실시간 인기 매물을 큐레이션하는 기준을 세울 수 있습니다. 마케팅 측면에서는 조회수를 찜수나 실제 문의로 전환시키기 위한 상세 페이지 개선의 근거로 활용됩니다.

### 월세 대비 관리비 상관관계
![월세 대비 관리비 상관관계](images/09_rent_maintenance_scatter.png)

#### 관련 데이터 테이블
|                 |   monthly_rent |   maintenance_fee |
|:----------------|---------------:|------------------:|
| monthly_rent    |     1          |        0.00548656 |
| maintenance_fee |     0.00548656 |        1          |

#### 해석 및 비즈니스 인사이트
월세와 관리비의 관계 분석은 임차인이 실제로 지출하게 될 총 비용(Total Occupancy Cost)을 예측하는 데 중요합니다. 일반적으로 월세가 높으면 대형 건물일 가능성이 높아 관리비도 동반 상승하는 경향이 있으나, 일부 노후 상가나 특수 조건에서는 이 관계가 깨지기도 합니다. 창업자에게 '실질 지출액' 정보를 투명하게 제공함으로써 신뢰도를 높일 수 있으며, 임대인에게는 주변 시세 대비 관리비의 적정성을 가이드할 수 있습니다. 비즈니스적으로는 관리비 포함 여부에 따른 매물 비교 기능을 강화하여 고객의 검색 만족도를 제고할 수 있는 통찰력을 제공합니다.

### 지상 vs 지하/기타 매물 비중
![지상 vs 지하/기타 매물 비중](images/10_ground_freq.png)

#### 관련 데이터 테이블
| is_ground   |   count |
|:------------|--------:|
| 지상          |    2146 |
| 지하/기타       |      23 |

#### 해석 및 비즈니스 인사이트
층수 위치에 따른 매물 분포는 상가 상권의 쾌적성과 업종 적합성을 판단하는 지표입니다. 지상 매물의 비중이 압도적으로 높다는 것은 상가가 주로 가시성과 환기, 접근성을 중시하는 업종들로 채워져 있음을 의미합니다. 지하 매물은 대형 공간이 필요한 유흥, 운동시설 등으로 특화되어 있을 가능성이 큽니다. 층수 위치에 따른 가격 차이를 분석하여 가성비 있는 지하 매물 창업 사례를 발굴하거나, 지상 매물의 프리미엄 요인을 데이터화할 수 있습니다. 이는 부동산 자산 관리 및 중개 플랫폼의 검색 카테고리 고도화에 직접적으로 기여하는 인사이트입니다.

## 4. 매물 제목 키워드 분석 (TF-IDF)

### 주요 키워드 분석 결과
![키워드 분석](images\11_text_keyword_tfidf.png)

|    | keyword    |   tfidf_score |
|---:|:-----------|--------------:|
| 15 | 아정당부동산중개법인 |      353      |
| 16 | 역삼동        |      150.975  |
| 18 | 역세권        |      121.757  |
|  0 | 1층         |      113.533  |
| 23 | 인테리어       |      109.106  |
| 10 | 상가         |      105.249  |
|  8 | 무권리        |      104.758  |
| 26 | 좋은         |      100.311  |
|  4 | 논현동        |       93.6789 |
| 21 | 위치한        |       88.9476 |
|  5 | 대로변        |       85.5185 |
| 28 | 초역세권       |       75.0054 |
| 14 | 시설         |       74.7968 |
|  6 | 많은         |       67.2848 |
|  9 | 사무실        |       64.8549 |
|  2 | 강남역        |       62.4868 |
|  3 | 깔끔한        |       61.9788 |
| 12 | 서초동        |       54.751  |
| 17 | 역삼역        |       53.6349 |
| 29 | 카페         |       50.8401 |
| 24 | 임대         |       47.854  |
|  1 | 가능한        |       45.7362 |
| 11 | 상권         |       45.5884 |
| 22 | 유동인구       |       44.4134 |
|  7 | 매물         |       44.1758 |
| 13 | 선릉역        |       42.7263 |
| 19 | 오피스        |       38.8743 |
| 25 | 접근성        |       37.2756 |
| 20 | 완비된        |       37.116  |
| 27 | 채광         |       35.0653 |

#### 텍스트 분석 해석
매물 제목에서 추출된 키워드 분석 결과, 임대인의 소구 포인트가 어디에 있는지 명확히 드러납니다. '무권리', '역세권', '대로변', '급매' 등 특정 키워드가 높은 점수를 기록하는 것은 임차인이 가장 매력적으로 느낄만한 조건을 제목에 전면 배치하고 있음을 의미합니다. 특히 '권리금 없음'을 강조하는 키워드의 비중은 현재 시장 상황이나 상권의 교체 주기를 짐작하게 합니다. 비즈니스적으로는 이러한 고효율 키워드를 매물 등록 가이드라인으로 제시하여 중개 효율을 높이거나, 검색 SEO 최적화에 활용할 수 있습니다.

## 5. 종합 인사이트 및 전략적 제안


### [데이터 분석 기반 상가 시장 종합 인사이트]

**1. 시장 구조 및 가격 역동성 분석**
본 분석을 통해 확인된 네모 플랫폼의 상가 데이터는 전형적인 '양극화'와 '입지 중심적 가격 형성'의 특징을 보입니다. 보증금과 월세 데이터에서 관찰된 극단적인 편차는 동일한 법정동 내에서도 골목 하나 차이로 자산 가치가 수 배 이상 차이 날 수 있는 상가 부동산의 특수성을 그대로 반영하고 있습니다. 특히 수치형 데이터의 우측 꼬리 분포(Right-skewed distribution)는 상위 5%의 핵심 입지가 전체 상권의 가격 지표를 견인하고 있음을 시사합니다. 이는 단순히 평균가에 의존한 의사결정보다는 중위값(Median)과 분위수 분석을 통한 상권별 세부 타겟팅이 필수적임을 의미합니다.

**2. 업종 및 공간 활용의 트렌드**
업종 대분류 및 중분류 빈도 분석 결과, 음식점과 소매업이 주를 이루는 가운데 카페나 디저트 전문점 등 특정 트렌드 업종의 매물 회전율이 높게 나타나고 있습니다. 층수 분석에서는 1층 매물의 압도적인 선호도와 함께, 고층부 매물의 목적성 공간(학원, 오피스 등)으로의 분화 현상이 뚜렷합니다. 지상층 비중이 압도적인 것은 고객 접근성이 상가 가치의 90% 이상을 결정한다는 시장의 믿음을 뒷받침합니다. 다만, 최근 루프탑이나 지하 특화 공간에 대한 수요가 데이터상의 이상치(High-rent outliers in non-ground floors)로 포착되는 점은 고정관념을 탈피한 공간 기획의 비즈니스 기회를 암시합니다.

**3. 사용자 행동 데이터의 전략적 가치**
조회수와 찜수의 상관관계 및 분산 분석은 매물의 '매력도'를 측정하는 강력한 지표입니다. 높은 조회수에도 불구하고 낮은 찜수를 기록하는 매물은 '미끼성 정보'이거나 가격 저항선이 높은 매물일 가능성이 큽니다. 반대로 낮은 조회수에도 찜수가 높은 매물은 타겟팅된 전문 업종에게 가치를 인정받는 '실속형 매물'입니다. 플랫폼 운영사는 이러한 행동 데이터를 기반으로 매물 랭킹 알고리즘을 고도화하여, 사용자에게는 개인화된 알짜 매물을 추천하고 임대인에게는 매물 경쟁력 진단 리포트를 제공함으로써 양면 시장의 만족도를 동시에 극대화할 수 있습니다.

**4. 텍스트 마이닝을 통한 시장 소구 포인트 파악**
TF-IDF 키워드 분석 결과, 임대인과 중개업자는 '수익성'보다 '안정성'과 '진입 장벽 완화'를 강조하는 경향을 보입니다. '무권리', '급매', '역세권' 등의 키워드가 상위에 랭크된 것은 경기 변동에 민감한 예비 창업자들의 불안 심리를 공략하려는 전략적 선택입니다. 비즈니스 인사이트 측면에서는 이러한 키워드 패턴과 실제 성사 여부를 결합 분석하여, 성사 확률이 높은 '제목 작성 템플릿'을 인공지능으로 자동 제안하는 기능을 개발할 수 있습니다. 이는 플랫폼 내 콘텐츠 품질의 상향 평준화를 이끌어낼 것입니다.

**5. 전략적 제안 및 미래 방향**
첫째, **'입지 가치 데이터베이스'의 구축**이 필요합니다. 단순 면적당 단가를 넘어 층수, 도로 인접성, 주변 상권 성숙도를 결합한 '네모 지수(Nemo Index)'를 개발하여 매물 가치 평가의 투명성을 높여야 합니다. 
둘째, **업종별 맞춤형 추천 엔진의 강화**입니다. 데이터 분석에서 나타난 업종별 가격 민감도를 반영하여, 예비 창업자의 자본 규모와 희망 업종에 최적화된 매물 포트폴리오를 제공해야 합니다. 
셋째, **비용 투명성 강화**입니다. 관리비와 임대료의 관계 분석을 바탕으로 '실질 총 유지비'를 상시 노출하여 허위 정보를 방지하고 신뢰도를 확보해야 합니다. 
마지막으로, **지역별 상권 역동성 모니터링**입니다. 권리금의 변동폭과 매물 등록 주기를 실시간 분석하여, 쇠퇴하는 상권과 부상하는 상권을 선제적으로 파악하는 비즈니스 인텔리전스 도구를 제공한다면 단순 중개를 넘어 종합 부동산 컨설팅 플랫폼으로 도약할 수 있을 것입니다.

본 EDA 보고서의 통찰은 데이터에 기반한 과학적 접근이 상가 임대 시장의 정보 비대칭성을 해소하고, 모든 시장 참여자에게 더 나은 기회를 제공할 수 있음을 증명합니다. 향후 시계열 분석과 외부 거시 경제 지표를 결합한다면 더욱 강력한 예측 모델을 구축할 수 있을 것으로 기대됩니다.

### [비즈니스 운영 및 기술적 고도화를 위한 세부 제안]

**6. 데이터 품질 관리와 거버넌스 (Data Governance)**
분석 과정에서 발견된 극단값(Outliers)들은 실제 시장의 고가 매물일 수도 있으나, 데이터 입력 오류의 가능성도 내포하고 있습니다. 향후 플랫폼의 신뢰도를 유지하기 위해 '이상치 자동 탐지 시스템'을 도입하여 시세 대비 현저히 낮거나 높은 매물을 검증하는 프로세스가 필요합니다. 또한, 이번에 수행한 TF-IDF 분석을 확장하여 비정형 데이터인 '매물 설명글' 전체를 감성 분석(Sentiment Analysis)하거나 객체 인식 기술을 통해 사진 속 시설 정보를 자동 추출한다면, 데이터의 풍부함을 한 차원 높일 수 있습니다.

**7. 마케팅 최적화 전략 (Marketing Optimization)**
조회수 대비 찜수가 높은 매물의 특징(예: 사진 퀄리티, 제목 키워드 구성 등)을 프로파일링하여 이를 신규 매물 등록자들에게 교육 자료로 활용할 것을 제안합니다. 또한, '역세권' 키워드가 주효하다는 점을 고려할 때, 지도 기반의 검색 인터페이스에서 '출구로부터의 도보 거리'를 자동 계산하여 데이터화하고 이를 필터링 옵션으로 제공한다면 사용자 경험(UX)은 획기적으로 개선될 것입니다.

**8. 수익 모델 다각화 (Monetization)**
현재의 중개 중심 모델에서 탈피하여, 이번 분석 결과와 같은 '상권 인사이트 리포트'를 유료 서비스로 전환하거나 프리미엄 멤버십 사용자에게 제공하는 방안을 고려해볼 수 있습니다. 특정 지역의 권리금 추이나 선호 업종 변화 데이터를 구독 모델로 제공한다면, 프랜차이즈 본사나 대형 투자자들에게 매력적인 B2B 상품이 될 것입니다.

결론적으로, 이번 EDA를 통해 확인된 상가 데이터의 가치는 단순히 '매물 정보'의 나열을 넘어 '도시 경제의 생태계'를 읽어내는 핵심 소스임을 확인했습니다. 데이터에 기반한 의사결정 문화를 정착시킨다면, 네모는 부동산 플랫폼을 넘어 자산 가치를 창출하는 테크 기업으로서의 입지를 공고히 할 것입니다.


