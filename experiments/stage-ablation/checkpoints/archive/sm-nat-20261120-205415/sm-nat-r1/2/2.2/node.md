# N11: 在 Pareto(β=0.9) 下，前 1% 对象贡献约 90% 的流量（Zipf 近似）；LRU 在 128GB 缓存中可缓存约 128 个平均 1MB 的对

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

在 Pareto(β=0.9) 下，前 1% 对象贡献约 90% 的流量（Zipf 近似）；LRU 在 128GB 缓存中可缓存约 128 个平均 1MB 的对象（若大小均匀），但实际因大小分布不均，可缓存对象数 K ≈ C / E[S|S≤S_max]，其中 S_max 为缓存最大对象大小

## Corrected Claim

在 Pareto(β=0.9) 下，前 1% 对象贡献约 90% 的流量（Zipf 近似）；LRU 在 128GB 缓存中可缓存约 128 个平均 1MB 的对象（若大小均匀），但实际因大小分布不均，可缓存对象数 K ≈ C / E[S|S≤S_max]，其中 S_max 为缓存最大对象大小

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto/Zipf分布下头部对象贡献大部分流量符合统计规律；LRU缓存容量与对象数量的关系公式 K ≈ C / E[S|S≤S_max] 在逻辑和量纲上自洽，且符合缓存管理的基本原理。
