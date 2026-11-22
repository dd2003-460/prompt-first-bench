# N252: 验证 N26 错误根源：N26 错误地将 k_max 限制为 C/E[S_avg] 且未取 min(N, ...)。若 S_avg=10KB，C/E[S_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N93

## Claim

验证 N26 错误根源：N26 错误地将 k_max 限制为 C/E[S_avg] 且未取 min(N, ...)。若 S_avg=10KB，C/E[S_avg]=1.28e7，但 N=1e5，故 k_max=1e5。若 S_avg=1MB，C/E[S_avg]=128，则 k_max=128。需明确 S_avg 是‘缓存内对象平均大小’而非‘全局平均大小’，否则 k_max 计算失效。

## Corrected Claim

验证 N26 错误根源：N26 错误地将 k_max 限制为 C/E[S_avg] 且未取 min(N, ...)。若 S_avg=10KB，C/E[S_avg]=1.28e7，但 N=1e5，故 k_max=1e5。若 S_avg=1MB，C/E[S_avg]=128，则 k_max=128。需明确 S_avg 是‘缓存内对象平均大小’而非‘全局平均大小’，否则 k_max 计算失效。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（1.28e7 > 1e5 取 1e5；128 < 1e5 取 128），且明确指出了 S_avg 定义对 k_max 计算的关键影响，逻辑自洽。
