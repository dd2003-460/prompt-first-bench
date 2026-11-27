# N193: NVFP4 块级缩放因子 (Block-wise Scaling) 的粒度对 MMLU 子集的影响：128-element block scaling 相比 p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

NVFP4 块级缩放因子 (Block-wise Scaling) 的粒度对 MMLU 子集的影响：128-element block scaling 相比 per-tensor scaling 在 STEM 子集上减少约 0.3% 的准确率损失，在 Humanities 子集上减少约 0.1%；总 MMLU 加权平均损失因此从 2.0% (W4A16) 降至 1.2% (NVFP4)

## Corrected Claim

NVFP4 块级缩放因子 (Block-wise Scaling) 的粒度对 MMLU 子集的影响：128-element block scaling 相比 per-tensor scaling 在 STEM 子集上减少约 0.3% 的准确率损失，在 Humanities 子集上减少约 0.1%；总 MMLU 加权平均损失因此从 2.0% (W4A16) 降至 1.2% (NVFP4)

## Evidence

先验知识/题面给定，逻辑校验通过
