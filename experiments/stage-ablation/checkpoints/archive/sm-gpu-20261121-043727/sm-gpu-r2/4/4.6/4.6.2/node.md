# N78: H200 vs H100 在 Qwen3-27B 32K 上下文下的 T_decode 加速比：H200 带宽 4.8 TB/s，H100 带宽 3.35 TB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N27

## Claim

H200 vs H100 在 Qwen3-27B 32K 上下文下的 T_decode 加速比：H200 带宽 4.8 TB/s，H100 带宽 3.35 TB/s。加速比 = 4.8 / 3.35 ≈ 1.43x。但 H200 价格通常比 H100 高 30-50% [待核验]，若 H100 为 $30,000，H200 为 $40,000。单位 token 成本比 = (1/1.43) * (40/30) ≈ 0.93，即 H200 单位 token 成本略低或持平，取决于具体市场价格。

## Corrected Claim

H200 vs H100 在 Qwen3-27B 32K 上下文下的 T_decode 理论加速比约为 1.43x（基于带宽比 4.8/3.35）。根据来源[2]，H200 起始价格仅比 H100 高约 $2,000（$31,000 vs $29,000），若按此价格计算，单位 token 成本比约为 (1/1.43) * (31/29) ≈ 0.75，即 H200 单位成本显著更低。具体成本优势取决于实际采购价格。

## Evidence

[质询]价格假设（H100 $30k vs H200 $40k，即33%溢价）与参考来源[2]提供的起始价格（H100 $29k vs H200 $31k，约7%溢价）存在显著偏差，导致单位成本计算结果（0.93x）可能严重失真；此外，将带宽比直接等同于解码加速比忽略了计算延迟和内存访问效率的差异。 | 逻辑推导自洽，但价格数据为经验事实且与来源[2]的起始价格区间不完全一致（来源显示H200仅比H100贵约$2000，而非$10000），缺乏直接支持该特定价格假设的来源，故降级。

## Search Query

NVIDIA H200 vs H100 price difference 2024 inference cost

## Retrieval Sources

- {'url': 'https://www.databasemart.com/blog/nvidia-h20-vs-nvidia-h100&rut=aa2287c0dc4df732f97d40d5b25b402ff91b2111049035356a02be8f53db78b4', 'type': 'ddg', 'title': 'H20 vs H100: AI Performance, Pricing, and Deployment Cost Comparison'}
- {'url': 'https://www.trgdatacenters.com/resource/nvidia-h200-vs-h100/&rut=7f07f779c49c5a77984cf64dbf3fbda83619c7a53dc12966f5d6595b94e93f41', 'type': 'ddg', 'title': 'NVIDIA GPUs H200 vs. H100 - A detailed comparison guide'}
- {'url': 'https://www.spheron.network/blog/nvidia-h100-vs-h200/&rut=093f80be9fac4c56c7e4d6a3563dae3a25ef607c176fd2d0e64d9feafeba15eb', 'type': 'ddg', 'title': 'H100 vs H200: Specs, FP8 Throughput & Cloud Pricing Compared (2026 ...'}
