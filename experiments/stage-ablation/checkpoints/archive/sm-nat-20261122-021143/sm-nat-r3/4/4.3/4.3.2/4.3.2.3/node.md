# N130: 边界条件分析：当 T_res(k) << 1 天（极热门对象）时，P(age > 1) ≈ 0，这些对象对 Stale_bytes 贡献极小；当 T_res(k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

边界条件分析：当 T_res(k) << 1 天（极热门对象）时，P(age > 1) ≈ 0，这些对象对 Stale_bytes 贡献极小；当 T_res(k) >> 1 天（冷门对象）时，P(age > 1) ≈ 1，但 S(k) 较小，需量化这两类对象对总 Stale_bytes 的贡献占比。

## Corrected Claim

边界条件分析：当 T_res(k) << 1 天（极热门对象）时，P(age > 1) ≈ 0，这些对象对 Stale_bytes 贡献极小；当 T_res(k) >> 1 天（冷门对象）时，P(age > 1) ≈ 1，但 S(k) 较小，需量化这两类对象对总 Stale_bytes 的贡献占比。

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数衰减或类似分布的缓存年龄模型，T_res远小于1天时存活概率趋近0，远大于1天时趋近1，且冷门对象通常体积较小，符合缓存系统基本直觉。
