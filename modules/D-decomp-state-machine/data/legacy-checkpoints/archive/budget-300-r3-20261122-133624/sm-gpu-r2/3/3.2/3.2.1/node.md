# N81: SmoothQuant 算法下 Qwen3-27B INT8 量化后，WikiText-103 PPL 具体增量为 0.15±0.05，MMLU 准确率损失为 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

SmoothQuant 算法下 Qwen3-27B INT8 量化后，WikiText-103 PPL 具体增量为 0.15±0.05，MMLU 准确率损失为 1.5%±0.5%，需区分平滑因子对激活值分布的影响

## Corrected Claim

SmoothQuant 算法下 Qwen3-27B INT8 量化后，WikiText-103 PPL 和 MMLU 准确率会有所下降，具体数值需参考官方技术报告或基准测试数据，需区分平滑因子对激活值分布的影响

## Evidence

[质询]具体数值（PPL增量0.15±0.05，MMLU损失1.5%±0.5%）属于特定模型（Qwen3-27B）在特定算法（SmoothQuant）下的经验测量结果，无法从第一性原理推导，且缺乏来源支持，存在数值虚构或混淆不同模型/量化方案的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B SmoothQuant INT8 PPL MMLU accuracy loss
