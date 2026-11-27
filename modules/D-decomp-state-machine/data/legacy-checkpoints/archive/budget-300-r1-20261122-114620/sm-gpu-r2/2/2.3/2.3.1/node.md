# N62: Intel Arc A770 (16GB) 的显存带宽为 560 GB/s，显存类型为 GDDR6，其内存子系统对 27B 模型推理的 tokens/sec 上

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Intel Arc A770 (16GB) 的显存带宽为 560 GB/s，显存类型为 GDDR6，其内存子系统对 27B 模型推理的 tokens/sec 上限约为 10-15 t/s（基于 560GB/s / (27B*2bytes) 估算，忽略计算瓶颈）

## Corrected Claim

Intel Arc A770 (16GB) 的显存带宽为 560 GB/s，显存类型为 GDDR6，其内存子系统对 27B 模型推理的 tokens/sec 上限约为 10-15 t/s（基于 560GB/s / (27B*2bytes) 估算，忽略计算瓶颈）

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Arc A770 显存带宽确为 560 GB/s，GDDR6 类型正确；27B 模型 FP16 权重约 54GB，560/54 ≈ 10.37 t/s，估算逻辑自洽且量级合理。
