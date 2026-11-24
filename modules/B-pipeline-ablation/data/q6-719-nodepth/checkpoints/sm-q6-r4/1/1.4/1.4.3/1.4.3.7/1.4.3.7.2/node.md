# N726: 公有云CDN基础请求费 C_request_base 的计算公式为 C_request_base = Q_day * P_request_base / 1000

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N242

## Claim

公有云CDN基础请求费 C_request_base 的计算公式为 C_request_base = Q_day * P_request_base / 1000，其中 Q_day = 2,048,000 req/day，P_request_base 取 ¥0.045/1000 req 时，C_request_base ≈ ¥92.16/天 ≈ ¥2,764.8/月。

## Corrected Claim

公有云CDN基础请求费 C_request_base 的计算公式为 C_request_base = Q_day * P_request_base / 1000，其中 Q_day = 2,048,000 req/day，P_request_base 取 ¥0.045/1000 req 时，C_request_base ≈ ¥92.16/天 ≈ ¥2,764.8/月。

## Evidence

先验知识/题面给定，逻辑校验通过：2,048,000 * 0.045 / 1000 = 92.16，92.16 * 30 = 2764.8，计算无误。
