# N135: 缓存命中率 $H$ 与回源比例 $(1-H)$ 的线性关系：回源流量 $V_{origin} = V_{total} \times (1-H)$，回源延迟贡献 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

缓存命中率 $H$ 与回源比例 $(1-H)$ 的线性关系：回源流量 $V_{origin} = V_{total} \times (1-H)$，回源延迟贡献 $L_{backhaul} \times (1-H)$ 在 P99 计算中需加权。

## Corrected Claim

缓存命中率 $H$ 与回源比例 $(1-H)$ 的线性关系：回源流量 $V_{origin} = V_{total} \times (1-H)$，回源延迟贡献 $L_{backhaul} \times (1-H)$ 在 P99 计算中需加权。

## Evidence

先验知识/题面给定，逻辑校验通过：回源流量定义为总流量减去命中流量，即 V_total * (1-H)，符合定义；延迟贡献按概率加权符合期望值计算逻辑。
