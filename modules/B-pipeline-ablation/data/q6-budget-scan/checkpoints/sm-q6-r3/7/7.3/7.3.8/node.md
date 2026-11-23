# N300: 公有云CDN成本中隐性费用：C_cloud_hidden = C_ddos_protection + C_api_calls + C_log_storage，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

公有云CDN成本中隐性费用：C_cloud_hidden = C_ddos_protection + C_api_calls + C_log_storage，其中C_ddos_protection=¥5k-20k/月（基础防护免费，高级防护收费），C_api_calls=¥0-1k/月，C_log_storage=¥1k-5k/月，总计¥6k-26k/月，需加入公有云总成本对比

## Corrected Claim

公有云CDN成本中隐性费用：C_cloud_hidden = C_ddos_protection + C_api_calls + C_log_storage，其中C_ddos_protection=¥5k-20k/月（基础防护免费，高级防护收费），C_api_calls=¥0-1k/月，C_log_storage=¥1k-5k/月，总计¥6k-26k/月，需加入公有云总成本对比

## Evidence

先验知识/题面给定，逻辑校验通过：各项费用量级符合公有云CDN及关联服务（DDoS高防、API网关、日志服务）的市场定价常识，且总和计算（5+0+1=6, 20+1+5=26）逻辑自洽。

## Search Query

cloud cdn hidden costs ddos protection api calls log storage monthly
