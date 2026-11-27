# N170: 买家时间机会成本 w_buyer 的量化：w_buyer = M_hourly / 60，其中 M_hourly 为买家时薪（典型值 30-80 元/小时），需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

买家时间机会成本 w_buyer 的量化：w_buyer = M_hourly / 60，其中 M_hourly 为买家时薪（典型值 30-80 元/小时），需基于用户画像分层估算，高收入群体 w_buyer 更高，影响咨询阈值。

## Corrected Claim

买家时间机会成本 w_buyer 的量化：w_buyer = M_hourly / 60，其中 M_hourly 为买家时薪（典型值 30-80 元/小时），需基于用户画像分层估算，高收入群体 w_buyer 更高，影响咨询阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 w_buyer = M_hourly / 60 量纲正确（元/小时 / 60分钟/小时 = 元/分钟），数值量级（0.5-1.33元/分钟）符合经济直觉，分层估算逻辑自洽。
