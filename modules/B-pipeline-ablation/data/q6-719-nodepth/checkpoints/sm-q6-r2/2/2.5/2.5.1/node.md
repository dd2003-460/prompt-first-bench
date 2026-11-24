# N81: 自建 POP 点的回源流量比例 (Origin Pull Ratio, R_origin) 计算为 1 - H_self，其中 H_self 为自建 POP 的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

自建 POP 点的回源流量比例 (Origin Pull Ratio, R_origin) 计算为 1 - H_self，其中 H_self 为自建 POP 的缓存命中率；在日均 2TB 下载量下，回源流量绝对值 V_origin = 2TB * R_origin (GB/天)。

## Corrected Claim

自建 POP 点的回源流量比例 (Origin Pull Ratio, R_origin) 计算为 1 - H_self，其中 H_self 为自建 POP 的缓存命中率；在日均 2TB 下载量下，回源流量绝对值 V_origin = 2TB * R_origin (GB/天)。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存命中率定义为命中流量占总请求流量的比例，因此回源比例 R_origin = 1 - H_self 符合定义；回源流量绝对值 V_origin 等于总流量乘以回源比例，量纲与逻辑均自洽。
