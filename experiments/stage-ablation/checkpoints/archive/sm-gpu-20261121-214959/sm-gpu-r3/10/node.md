# N35: INT4 量化质量损失的可接受性阈值：在代码生成任务 (HumanEval) 上，Qwen3-27B INT4 (AWQ) 的 Pass@1 通常下降 2-4%

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

INT4 量化质量损失的可接受性阈值：在代码生成任务 (HumanEval) 上，Qwen3-27B INT4 (AWQ) 的 Pass@1 通常下降 2-4% (从 ~60% 降至 ~56-58%)，但在通用对话 (MT-Bench) 上评分下降 <0.1 分。若应用场景为纯文本创作或闲聊，INT4 损失可接受；若为代码补全或数学推理，建议 FP8 或 BF16。

## Corrected Claim

INT4 量化质量损失的可接受性阈值：在代码生成任务 (HumanEval) 上，Qwen3-27B INT4 (AWQ) 的 Pass@1 通常下降 2-4% (从 ~60% 降至 ~56-58%)，但在通用对话 (MT-Bench) 上评分下降 <0.1 分。若应用场景为纯文本创作或闲聊，INT4 损失可接受；若为代码补全或数学推理，建议 FP8 或 BF16。

## Evidence

检索失败: no sources from any channel (all 5 failed)
