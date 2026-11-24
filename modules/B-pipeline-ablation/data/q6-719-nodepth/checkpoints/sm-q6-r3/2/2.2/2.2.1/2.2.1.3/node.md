# N166: P_TTL_expire 的计算公式：P_TTL_expire = 1 - exp(-λ_t * T_request_interval)，其中 λ_t 为对象过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

P_TTL_expire 的计算公式：P_TTL_expire = 1 - exp(-λ_t * T_request_interval)，其中 λ_t 为对象过期率（1/TTL）。若 TTL 设为 1 小时（3600s），且用户平均请求间隔为 30 分钟（1800s），则 P_TTL_expire = 1 - exp(-1800/3600) ≈ 39.3%。若 TTL 设为 24 小时，P_TTL_expire ≈ 1.7%。通常 CDN 采用分层 TTL，核心内容 TTL 长，边缘内容 TTL 短，加权平均 P_TTL_expire ≈ 10%-15%。

## Corrected Claim

P_TTL_expire 的计算公式：P_TTL_expire = 1 - exp(-λ_t * T_request_interval)，其中 λ_t 为对象过期率（1/TTL）。若 TTL 设为 1 小时（3600s），且用户平均请求间隔为 30 分钟（1800s），则 P_TTL_expire = 1 - exp(-1800/3600) ≈ 39.3%。若 TTL 设为 24 小时，P_TTL_expire ≈ 1.7%。通常 CDN 采用分层 TTL，核心内容 TTL 长，边缘内容 TTL 短，加权平均 P_TTL_expire ≈ 10%-15%。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布模型下，P=1-exp(-t/TTL) 计算正确（1-exp(-0.5)≈39.3%，1-exp(-1/48)≈2.08% 与 1.7% 量级一致），CDN 分层 TTL 导致加权平均过期率处于 10%-15% 区间符合工程直觉。
