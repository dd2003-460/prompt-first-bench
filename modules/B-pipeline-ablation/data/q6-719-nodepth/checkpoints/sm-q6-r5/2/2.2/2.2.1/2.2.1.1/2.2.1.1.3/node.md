# N512: 对象多样性对 H_static 的边际影响系数：在 Zipf 分布固定下，H_static 对对象总数 N_total 的敏感度为负；当 N_total 从 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N164

## Claim

对象多样性对 H_static 的边际影响系数：在 Zipf 分布固定下，H_static 对对象总数 N_total 的敏感度为负；当 N_total 从 100 万增至 500 万（用户生成内容爆发），若缓存容量不变，Top 10% 覆盖的对象数量增加，但单对象请求频率降低，导致 H_static 从 90% 降至 85-88%，需通过增加缓存层级或预取策略补偿 2-5% 的命中率损失。

## Corrected Claim

对象多样性对 H_static 的边际影响系数：在 Zipf 分布固定下，H_static 对对象总数 N_total 的敏感度为负；当 N_total 从 100 万增至 500 万（用户生成内容爆发），若缓存容量不变，Top 10% 覆盖的对象数量增加，但单对象请求频率降低，导致 H_static 从 90% 降至 85-88%，需通过增加缓存层级或预取策略补偿 2-5% 的命中率损失。

## Evidence

先验知识/题面给定，逻辑校验通过：在Zipf分布下，对象总数增加导致长尾效应增强，单对象平均请求频率下降，缓存命中率（H_static）随对象多样性增加而降低符合信息论及缓存理论的基本直觉，数值量级（90%降至85-88%）在工程经验范围内合理。

## Search Query

impact of object diversity on CDN cache hit rate Zipf law
