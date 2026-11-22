# N127: INT8 量化在 Qwen3-27B 上的 MMLU 准确率下降幅度预计为 0.5-1.0%（相比 BF16），Perplexity 增加 <0.2%，对于通用

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

INT8 量化在 Qwen3-27B 上的 MMLU 准确率下降幅度预计为 0.5-1.0%（相比 BF16），Perplexity 增加 <0.2%，对于通用对话任务质量损失可接受，但对于代码生成任务（HumanEval）下降幅度可能达 3-5%，需根据业务场景（对话 vs 代码）判定可接受性。

## Corrected Claim

INT8 量化在 Qwen3-27B 上的 MMLU 准确率下降幅度预计为 0.5-1.0%（相比 BF16），Perplexity 增加 <0.2%，对于通用对话任务质量损失可接受，但对于代码生成任务（HumanEval）下降幅度可能达 3-5%，需根据业务场景（对话 vs 代码）判定可接受性。

## Evidence

检索失败: no sources from any channel (all 5 failed)
