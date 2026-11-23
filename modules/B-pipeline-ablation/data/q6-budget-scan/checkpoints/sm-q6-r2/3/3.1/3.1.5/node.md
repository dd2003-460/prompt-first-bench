# N54: 回源带宽比例 R_origin = 1 - H_cache_global 中，H_cache_global 为全局缓存命中率，其值取决于对象大小分布、用户请求模

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N15

## Claim

回源带宽比例 R_origin = 1 - H_cache_global 中，H_cache_global 为全局缓存命中率，其值取决于对象大小分布、用户请求模式和缓存策略；若对象大小分布为长尾（如 80% 流量来自 20% 对象），H_cache_global 可达 80%-95%；需基于实际流量分布模型计算 H_cache_global = sum(p_i * h_i) over all objects i，其中 p_i 为对象 i 的请求概率，h_i 为对象 i 的缓存命中率。

## Corrected Claim

回源带宽比例 R_origin = 1 - H_cache_global 中，H_cache_global 为全局缓存命中率，其值取决于对象大小分布、用户请求模式和缓存策略；若对象大小分布为长尾（如 80% 流量来自 20% 对象），H_cache_global 可达 80%-95%；需基于实际流量分布模型计算 H_cache_global = sum(p_i * h_i) over all objects i，其中 p_i 为对象 i 的请求概率，h_i 为对象 i 的缓存命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合概率加权平均原理，长尾分布下高命中率的量级符合CDN缓存工程常识
