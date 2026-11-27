# N770: A100 80GB 在 LLM Decode 阶段（Batch=1, 27B 模型）的有效内存带宽利用率 η_mem 实测值约为 0.75，对应有效带宽 ≈ 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

A100 80GB 在 LLM Decode 阶段（Batch=1, 27B 模型）的有效内存带宽利用率 η_mem 实测值约为 0.75，对应有效带宽 ≈ 1529 GB/s，该系数受 HBM 访问模式（连续 vs 随机）和 ECC 开销影响。

## Corrected Claim

A100 80GB 在 LLM Decode 阶段（Batch=1, 27B 模型）的有效内存带宽利用率 η_mem 实测值约为 0.75，对应有效带宽 ≈ 1529 GB/s，该系数受 HBM 访问模式（连续 vs 随机）和 ECC 开销影响。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 理论带宽约 2039 GB/s，0.75 的利用率对应 1529 GB/s 符合工程实测典型范围（通常 70%-85%），且受访问模式和 ECC 影响符合硬件特性。

## Search Query

A100 LLM inference memory bandwidth efficiency factor
