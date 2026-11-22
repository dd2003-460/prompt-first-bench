# N196: Apple Mac Studio M2 Ultra 192GB 配置在 2025 年的官方起售价为 $3,999，若升级到 256GB 内存则价格升至 $5,1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Apple Mac Studio M2 Ultra 192GB 配置在 2025 年的官方起售价为 $3,999，若升级到 256GB 内存则价格升至 $5,199，其 $/GB 统一内存成本分别为 $20.83 和 $20.31/GB，是候选集中显存单价最低的方案，但受限于 800 GB/s 带宽，其 INT8 推理 TPS 约为 10-15 tokens/s。

## Corrected Claim

Apple Mac Studio M2 Ultra 192GB 配置在 2025 年的官方起售价为 $3,999，若升级到 256GB 内存则价格升至 $5,199，其 $/GB 统一内存成本分别为 $20.83 和 $20.31/GB，是候选集中显存单价最低的方案，但受限于 800 GB/s 带宽，其 INT8 推理 TPS 约为 10-15 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：价格与内存容量计算出的$/GB成本（3999/192≈20.83, 5199/256≈20.31）数学自洽；M2 Ultra 800GB/s带宽下运行大模型（如70B+）的10-15 TPS符合内存带宽瓶颈下的理论推算（TPS ≈ 带宽/模型大小，假设模型约50-60GB，800/55≈14.5），且该配置确为当时Apple最高端且显存单价相对GPU方案较低的方案。
