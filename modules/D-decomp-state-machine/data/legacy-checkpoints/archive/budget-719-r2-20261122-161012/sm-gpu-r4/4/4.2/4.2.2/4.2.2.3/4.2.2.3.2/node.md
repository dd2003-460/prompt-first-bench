# N508: 在 32K 上下文下，INT4 权重的 KV Cache 若保持 BF16 精度，Decode 阶段总读取量 R_decode = 13.5 GB (Weigh

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N209

## Claim

在 32K 上下文下，INT4 权重的 KV Cache 若保持 BF16 精度，Decode 阶段总读取量 R_decode = 13.5 GB (Weight_INT4) + 1.07 GB (KV_BF16) = 14.57 GB；若 KV 同步量化为 INT4，则 R_decode = 13.5 GB + 0.268 GB = 13.768 GB，显著降低带宽压力。

## Corrected Claim

在 32K 上下文下，INT4 权重的 KV Cache 若保持 BF16 精度，Decode 阶段总读取量 R_decode = 13.5 GB (Weight_INT4) + 1.07 GB (KV_BF16) = 14.57 GB；若 KV 同步量化为 INT4，则 R_decode = 13.5 GB + 0.268 GB = 13.768 GB，显著降低带宽压力。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（13.5+1.07=14.57, 13.5+0.268=13.768），且符合INT4量化后KV Cache体积约为BF16的1/4（1.07/4≈0.2675）的物理/工程直觉。
