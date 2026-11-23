# N170: 自建策略的 P99 延迟对回源概率的敏感度：∂P99_self/∂p_miss_self = t_origin_self，其中 t_origin_self 为自

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

自建策略的 P99 延迟对回源概率的敏感度：∂P99_self/∂p_miss_self = t_origin_self，其中 t_origin_self 为自建POP点到源站的回源延迟，通常 30-80ms（取决于POP点与源站距离），每增加 1% 回源概率，P99 增加 0.3-0.8ms

## Corrected Claim

自建策略的 P99 延迟对回源概率的敏感度：∂P99_self/∂p_miss_self = t_origin_self，其中 t_origin_self 为自建POP点到源站的回源延迟，通常 30-80ms（取决于POP点与源站距离），每增加 1% 回源概率，P99 增加 0.3-0.8ms

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟对回源概率的导数在理想情况下等于回源延迟与本地延迟之差，量级30-80ms符合物理直觉，且数值换算（1%概率*30-80ms=0.3-0.8ms）逻辑自洽。

## Search Query

P99 latency sensitivity to cache miss rate edge computing
