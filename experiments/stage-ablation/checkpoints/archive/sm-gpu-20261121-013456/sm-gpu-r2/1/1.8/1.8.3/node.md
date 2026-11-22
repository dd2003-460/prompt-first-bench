# N73: FP8 精度下总显存需求下限计算：27 GB (权重) + 4.3 GB (KV Cache, GQA, 假设KV也FP8) + 3 GB (激活/缓冲) = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

FP8 精度下总显存需求下限计算：27 GB (权重) + 4.3 GB (KV Cache, GQA, 假设KV也FP8) + 3 GB (激活/缓冲) = 34.3 GB，需 48GB 显存卡 (如 2x4090 或 1xW7900) 方可支持

## Corrected Claim

FP8 精度下总显存需求下限计算：27 GB (权重) + 4.3 GB (KV Cache, GQA, 假设KV也FP8) + 3 GB (激活/缓冲) = 34.3 GB，需 48GB 显存卡 (如 2x4090 或 1xW7900) 方可支持

## Evidence

先验知识/题面给定，逻辑校验通过：27+4.3+3=34.3GB，且34.3GB < 48GB，数值量级与硬件规格匹配，逻辑自洽。
