# N17: INT8精度下，Qwen3-27B在MMLU基准上得分降至83.9%（-1.3%），GSM8K降至80.2%（-1.9%），HumanEval降至66.1%（-

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

INT8精度下，Qwen3-27B在MMLU基准上得分降至83.9%（-1.3%），GSM8K降至80.2%（-1.9%），HumanEval降至66.1%（-2.4%），质量损失1-2.5%，对于代码生成和数学推理任务可能不可接受，需结合具体应用场景判断。

## Corrected Claim

INT8精度下，Qwen3-27B在MMLU基准上得分降至83.9%（-1.3%），GSM8K降至80.2%（-1.9%），HumanEval降至66.1%（-2.4%），质量损失1-2.5%，对于代码生成和数学推理任务可能不可接受，需结合具体应用场景判断。

## Evidence

父节点级核验未通过：不完备（子节点之间存在明显的逻辑矛盾和覆盖缺失。1. 矛盾：父节点提到MMLU下降1.3%，但子节点完全未提及MMLU，导致信息丢失；更严重的是，子节点1声称INT8需27GB显存（不可行），而子节点2和3却在讨论INT8在GSM8K和HumanEval上的具体得分和可行性判断，这隐含了INT8是可运行的前提，两者在‘可行性’这一核心结论上存在潜在冲突（除非明确区分硬件限制与性能指标，但表述上易混淆）。2. 完备性：父节点包含MMLU数据，子节点未覆盖。3. 冗余：GSM8K和HumanEval的论述结构高度相似（均为‘阈值判断+可行性结论’），虽不构成严格冗余，但可优化。）

## Search Query

Qwen3 27B INT8 quantization benchmark loss
