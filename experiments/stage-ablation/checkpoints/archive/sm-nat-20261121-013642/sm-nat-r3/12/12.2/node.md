# N280: 对于第 k 热对象（请求频率 r_k），其平均请求间隔为 1/r_k 天，更新失效概率 P_invalidate(k) = 1 - exp(-λ_u / r_k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

对于第 k 热对象（请求频率 r_k），其平均请求间隔为 1/r_k 天，更新失效概率 P_invalidate(k) = 1 - exp(-λ_u / r_k)，当 r_k >> λ_u 时，P_invalidate(k) ≈ λ_u / r_k，该值作为 H_byte_LRU 下界的唯一扣减项。

## Corrected Claim

对于第 k 热对象（请求频率 r_k），其平均请求间隔为 1/r_k 天，更新失效概率 P_invalidate(k) = 1 - exp(-λ_u / r_k)，当 r_k >> λ_u 时，P_invalidate(k) ≈ λ_u / r_k，该值作为 H_byte_LRU 下界的唯一扣减项。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程下失效概率公式及大数近似推导正确，符合LRU缓存失效模型的基本逻辑。
