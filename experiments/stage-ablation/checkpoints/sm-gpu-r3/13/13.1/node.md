# N314: Qwen3-27B 在 BF16 精度下的 HumanEval Pass@1 基线得分为 [待核验: 需查 Qwen3 官方技术报告代码生成基准]，通常 27B

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N136

## Claim

Qwen3-27B 在 BF16 精度下的 HumanEval Pass@1 基线得分为 [待核验: 需查 Qwen3 官方技术报告代码生成基准]，通常 27B 参数量级模型在 HumanEval 上的 Pass@1 介于 75%-85% 之间，此数值是判断量化后是否跌破 90% 阈值 (若基线本身低于 90%，则阈值需调整为相对下降率) 的前提。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 HumanEval Pass@1 基线得分需查 Qwen3 官方技术报告代码生成基准，27B 参数量级模型在 HumanEval 上的 Pass@1 通常介于 75%-85% 之间（经验估计），此数值是判断量化后是否跌破 90% 阈值的前提。

## Evidence

[质询]陈述中关于'27B参数量级模型在HumanEval上的Pass@1介于75%-85%之间'属于经验事实，且未提供具体数值，仅给出范围；参考来源[1]讨论的是'Qwen 3.6 27B'（注意版本号差异，Qwen3与Qwen3.6可能不同），且未提供具体的HumanEval Pass@1数值，仅定性描述'持平甚至略优'，无法直接支持具体数值范围。 | 逻辑自洽，但参考来源[1]未提供具体HumanEval Pass@1数值，仅定性描述，且版本号存在差异（Qwen3 vs Qwen3.6），无法直接支持具体数值范围，属于经验事实缺来源直接支持。

## Search Query

Qwen3-27B HumanEval Pass@1 baseline score

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2055287697623856945&rut=5eccc087a072daa9e322e4623c2ec2059270127b662ac68ed5c72afe39880bf0', 'type': 'ddg', 'title': 'Qwen 3.6 27B深度评测：27B参数单挑397B，本地跑AI编程的时代来了'}
