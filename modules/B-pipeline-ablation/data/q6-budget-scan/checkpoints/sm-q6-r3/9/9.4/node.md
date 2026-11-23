# N138: 缓存容量 $C_{cache}$ 与命中率 $H$ 的边际效益递减曲线：$H(C_{cache}) = 1 - (C_{hot} / C_{cache})^\a

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

缓存容量 $C_{cache}$ 与命中率 $H$ 的边际效益递减曲线：$H(C_{cache}) = 1 - (C_{hot} / C_{cache})^\alpha$，其中 $C_{hot}$ 为热点内容大小，$\alpha$ 为衰减因子（通常 0.5-1.0），当 $C_{cache} > 10 \times C_{hot}$ 时，$dH/dC_{cache} < 0.01$，增加容量对 P99 改善不足 1ms。

## Corrected Claim

缓存容量 $C_{cache}$ 与命中率 $H$ 的边际效益递减曲线：$H(C_{cache}) = 1 - (C_{hot} / C_{cache})^\alpha$，其中 $C_{hot}$ 为热点内容大小，$\alpha$ 为衰减因子（通常 0.5-1.0），当 $C_{cache} > 10 \times C_{hot}$ 时，$dH/dC_{cache} < 0.01$，增加容量对 P99 改善不足 1ms。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 56 (char 121)

## Search Query

cache hit ratio vs cache size diminishing returns model
