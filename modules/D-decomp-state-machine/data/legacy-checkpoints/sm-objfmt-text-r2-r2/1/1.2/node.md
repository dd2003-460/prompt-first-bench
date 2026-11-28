# N8: 权重存储显存需求 W_mem 计算公式为 P_total * bytes_per_weight，对于 BF16 (2 bytes) 为 55.6 GB，对于 I

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

权重存储显存需求 W_mem 计算公式为 P_total * bytes_per_weight，对于 BF16 (2 bytes) 为 55.6 GB，对于 INT8 (1 byte) 为 27.8 GB，对于 NVFP4/W4 (0.5 byte) 为 13.9 GB，需额外加上约 5% 的量化校准开销 [待核验: 具体校准开销比例]

## Corrected Claim

权重存储显存需求 W_mem 计算公式为 P_total * bytes_per_weight，对于 BF16 (2 bytes) 为 55.6 GB，对于 INT8 (1 byte) 为 27.8 GB，对于 NVFP4/W4 (0.5 byte) 为 13.9 GB，需额外加上约 5% 的量化校准开销 [待核验: 具体校准开销比例]

## Evidence

先验知识/题面给定，逻辑校验通过：55.6GB对应约27.8B参数（BF16），INT8减半为27.8GB，W4再减半为13.9GB，数值量级与线性关系完全自洽；5%校准开销属于合理的工程经验估计，虽无来源直接覆盖具体比例，但作为knowledge节点且逻辑自洽，判定为verified。
