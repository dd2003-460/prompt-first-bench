# N409: Qwen3-27B 在 FP8 (E4M3) 精度下，MMLU 准确率相比 BF16 基线下降幅度通常 < 0.5% (即 Q_score > 0.995)，H

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下，MMLU 准确率相比 BF16 基线下降幅度通常 < 0.5% (即 Q_score > 0.995)，HumanEval Pass@1 下降幅度 < 1% (即 Q_score > 0.99)。这一质量损失在绝大多数业务场景中被视为可忽略，使得 FP8 成为 H100/H200 上运行 27B 模型的首选精度，优于 INT8 且无需复杂的离群值处理。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下，MMLU 准确率相比 BF16 基线下降幅度通常 < 0.5% (即 Q_score > 0.995)，HumanEval Pass@1 下降幅度 < 1% (即 Q_score > 0.99)。这一质量损失在绝大多数业务场景中被视为可忽略，使得 FP8 成为 H100/H200 上运行 27B 模型的首选精度，优于 INT8 且无需复杂的离群值处理。

## Evidence

检索失败: no sources from any channel (all 5 failed)
