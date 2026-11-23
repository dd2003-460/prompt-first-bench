# N162: 月度总请求数 N_requests_monthly 的分解公式：N_requests_monthly = DAU * req_per_user_per_day 

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

月度总请求数 N_requests_monthly 的分解公式：N_requests_monthly = DAU * req_per_user_per_day * 30，其中 DAU=5,000,000，req_per_user_per_day 需拆解为图片请求数与短视频请求数之和，即 req_total = req_img + req_video

## Corrected Claim

月度总请求数 N_requests_monthly 的分解公式：N_requests_monthly = DAU * req_per_user_per_day * 30，其中 DAU=5,000,000，req_per_user_per_day 需拆解为图片请求数与短视频请求数之和，即 req_total = req_img + req_video

## Evidence

先验知识/题面给定，逻辑校验通过
