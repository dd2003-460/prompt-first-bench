# N159: 回源概率 p_miss 对 P99 延迟的贡献权重 w_miss = p_miss * (t_origin - t_cache)，其中 t_origin 为回源

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

回源概率 p_miss 对 P99 延迟的贡献权重 w_miss = p_miss * (t_origin - t_cache)，其中 t_origin 为回源延迟，t_cache 为缓存命中延迟；对于 p_miss=0.2，t_origin=50ms，t_cache=5ms，w_miss ≈ 9ms；需根据实际延迟参数确定。

## Corrected Claim

回源概率 p_miss 对 P99 延迟的贡献权重 w_miss = p_miss * (t_origin - t_cache)，其中 t_origin 为回源延迟，t_cache 为缓存命中延迟；对于 p_miss=0.2，t_origin=50ms，t_cache=5ms，w_miss ≈ 9ms；需根据实际延迟参数确定。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 w_miss = p_miss * (t_origin - t_cache) 符合期望延迟贡献的线性叠加原理，数值计算 0.2 * (50 - 5) = 9ms 准确无误。

## Search Query

cache miss probability P99 latency contribution
