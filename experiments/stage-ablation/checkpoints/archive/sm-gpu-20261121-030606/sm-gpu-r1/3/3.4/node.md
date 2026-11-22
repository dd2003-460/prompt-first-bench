# N18: W4精度下，Qwen3-27B在MMLU基准上得分降至81.5%（-3.7%），GSM8K降至77.8%（-4.3%），HumanEval降至62.3%（-6.

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

W4精度下，Qwen3-27B在MMLU基准上得分降至81.5%（-3.7%），GSM8K降至77.8%（-4.3%），HumanEval降至62.3%（-6.2%），质量损失3.7-6.2%，显著影响代码和数学任务，仅适用于对质量要求极低的场景或作为极端成本优化选项。

## Corrected Claim

W4精度下，Qwen3-27B在MMLU、GSM8K和HumanEval基准上通常会出现性能下降（约3-6%），其中代码和数学任务受影响较大，适用于对质量要求较低或极端成本优化场景。

## Evidence

[质询]具体数值（81.5%, 77.8%, 62.3%）及特定模型（Qwen3-27B）的量化损失缺乏公开权威基准测试的直接支持，可能混淆了不同量化方案（如GPTQ vs AWQ）或不同模型版本（Qwen2 vs Qwen3）的数据，且'显著影响'的定性结论依赖于未提供的基线对比。 | 逻辑自洽：量化精度降低通常导致性能下降，且代码/数学任务对精度更敏感，符合一般规律；但source为knowledge，且无外部来源支持具体数值，根据规则，经验事实（具体基准分数）若无来源直接支持且无法从第一性原理严格推出具体数值，应降级。注：虽然knowledge节点通常逻辑自洽即verified，但此处涉及具体经验数据（benchmark scores），且无来源佐证，存在数值不准确的风险，故保守判为degraded以提示需核实具体数值。

## Search Query

Qwen3 27B W4 quantization benchmark loss
