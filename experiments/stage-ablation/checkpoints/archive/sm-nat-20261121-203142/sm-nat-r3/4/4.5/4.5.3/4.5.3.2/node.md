# N160: P_revalidate 在 TTL 场景下的量化：当对象过期时，重新验证命中的概率取决于源站响应时间 T_origin 与客户端超时 T_timeout 的关

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N62

## Claim

P_revalidate 在 TTL 场景下的量化：当对象过期时，重新验证命中的概率取决于源站响应时间 T_origin 与客户端超时 T_timeout 的关系，若 T_origin < T_timeout，则 P_revalidate ≈ 1，否则需引入失败重试因子，典型 CDN 中 T_origin < 200ms，T_timeout > 5s，故 P_revalidate ≈ 0.95-1.0

## Corrected Claim

P_revalidate 在 TTL 场景下，当 T_origin < T_timeout 时，重新验证命中概率接近 1（通常 > 0.95），具体数值取决于网络抖动与源站稳定性。

## Evidence

[质询]P_revalidate ≈ 0.95-1.0 的具体数值缺乏严谨的数学推导支持，仅凭 T_origin < T_timeout 只能定性得出概率接近 1，具体下限 0.95 属于经验估计而非逻辑必然。 | 先验知识/题面给定，逻辑校验通过：T_origin (200ms) 远小于 T_timeout (5s) 符合 CDN 典型工程参数，逻辑上支持高成功率，但具体数值 0.95 为经验值，无来源直接支持，故降级。
