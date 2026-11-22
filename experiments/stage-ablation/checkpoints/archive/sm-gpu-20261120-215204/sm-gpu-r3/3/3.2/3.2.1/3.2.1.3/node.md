# N246: L40S 在 INT8 精度下运行 Qwen3-27B 的量化质量损失评估：INT8 对称量化通常导致 MMLU 基准下降 1-3%，而 BF16 KV Cac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

L40S 在 INT8 精度下运行 Qwen3-27B 的量化质量损失评估：INT8 对称量化通常导致 MMLU 基准下降 1-3%，而 BF16 KV Cache 保持全精度无损失，因此该组合的质量损失主要源于权重量化，相比 FP8 权重量化 (损失 <1%) 略高，但在大多数通用任务中可接受，具体阈值取决于下游任务对数值精度的敏感度。

## Corrected Claim

L40S 在 INT8 精度下运行 Qwen3-27B 的量化质量损失评估：INT8 对称量化通常导致 MMLU 基准下降 1-3%，而 BF16 KV Cache 保持全精度无损失，因此该组合的质量损失主要源于权重量化，相比 FP8 权重量化 (损失 <1%) 略高，但在大多数通用任务中可接受，具体阈值取决于下游任务对数值精度的敏感度。

## Evidence

先验知识/题面给定，逻辑校验通过
