# N122: 每美元吞吐量 (Throughput per Dollar, TpD) 修正系数：TpD = (Measured_Throughput_tokens_per_s

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

每美元吞吐量 (Throughput per Dollar, TpD) 修正系数：TpD = (Measured_Throughput_tokens_per_s) / (Total_Hardware_Cost_USD)。对于多卡方案，需除以 (1 - Interconnect_Overhead_Factor)，其中 PCIe Gen4 x16 互联开销系数约为 0.1-0.15，NVLink 约为 0.02-0.05。

## Corrected Claim

每美元吞吐量 (Throughput per Dollar, TpD) 修正系数：TpD = (Measured_Throughput_tokens_per_s) / (Total_Hardware_Cost_USD)。对于多卡方案，需除以 (1 - Interconnect_Overhead_Factor)，其中 PCIe Gen4 x16 和 NVLink 的互联开销系数需根据具体硬件架构和负载类型实测确定，通常 PCIe 开销高于 NVLink。

## Evidence

[质询]该陈述包含具体的经验数值（PCIe Gen4 和 NVLink 的互联开销系数），属于硬件性能经验事实，无法从第一性原理严格推导，且参考来源中未包含相关数据支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为NVIDIA官网新闻，来源[2]为通用性能指标定义，均未覆盖具体互联开销系数）。

## Retrieval Sources

- {'url': 'https://nvidia.com', 'type': None, 'title': 'direct-browser: nvidia.com'}
- {'url': 'https://zhuanlan.zhihu.com/p/337708438&rut=526b93cdb24b748f434aa02a855c2bf839a67d124f7c6e3312d1c011b9733869', 'type': 'ddg', 'title': '一文搞懂高并发性能指标：QPS、TPS、RT、并发数、吞吐量'}
