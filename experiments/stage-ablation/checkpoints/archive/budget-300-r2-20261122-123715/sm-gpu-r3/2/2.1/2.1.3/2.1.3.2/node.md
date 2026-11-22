# N202: Qwen3-27B 在 W4A16 量化下长尾任务（如 GSM8K 数学推理或 HumanEval 代码生成）准确率下降幅度 ΔAcc 需通过对比 BF16 基

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Qwen3-27B 在 W4A16 量化下长尾任务（如 GSM8K 数学推理或 HumanEval 代码生成）准确率下降幅度 ΔAcc 需通过对比 BF16 基线与 W4 模型的实测结果确定，若 ΔAcc > 10% 则触发回退机制；具体数值需运行评估脚本获取 [待核验]。

## Corrected Claim

Qwen3-27B 在 W4A16 量化下长尾任务（如 GSM8K 或 HumanEval）的准确率下降幅度 ΔAcc 需通过对比 BF16 基线与 W4 模型的实测结果确定；若实测 ΔAcc 超过预设阈值（如 10%），则触发回退机制。具体数值需运行评估脚本获取。

## Evidence

[质询]该陈述包含具体的经验性阈值（ΔAcc > 10%）和特定模型（Qwen3-27B）在特定量化配置（W4A16）下的性能表现预期，属于经验事实，无法从第一性原理推导，且缺乏实测数据支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值阈值及模型表现）。

## Search Query

Qwen3-27B 4bit quantization GSM8K HumanEval accuracy drop
