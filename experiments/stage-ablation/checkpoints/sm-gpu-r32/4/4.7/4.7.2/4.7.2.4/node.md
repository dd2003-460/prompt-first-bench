# N243: Qwen3-27B W4 量化在 32K 上下文下的质量损失评估：需对比 W4 与 BF16 在 MMLU/HumanEval 上的准确率差值，通常 W4 量化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

Qwen3-27B W4 量化在 32K 上下文下的质量损失评估：需对比 W4 与 BF16 在 MMLU/HumanEval 上的准确率差值，通常 W4 量化会导致 1-3% 的准确率下降，具体数值需参考 Qwen 官方技术报告或第三方评测。

## Corrected Claim

Qwen3-27B W4 量化在 32K 上下文下的质量损失评估：需对比 W4 与 BF16 在 MMLU/HumanEval 上的准确率差值，具体数值需参考 Qwen 官方技术报告或第三方评测，通常 W4 量化会导致一定程度的准确率下降（具体幅度视模型和任务而定）。

## Evidence

[质询]该陈述包含具体的经验数值断言（W4量化导致1-3%准确率下降），属于经验事实，无法从第一性原理推导，且参考来源中未包含任何关于Qwen3模型量化评测的数据，来源[3]中的W4 theory是量子化学术语，与LLM量化无关，存在主题混淆风险。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为通用平台，[2]无关，[3]为量子化学W4理论，均不支持LLM量化结论）

## Search Query

Qwen3-27B W4 quantization MMLU HumanEval accuracy loss

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://www.investopedia.com/sustainable-investing-4427774', 'type': 'bing', 'title': 'Sustainable Investing - Investopedia'}
- {'url': 'http://arxiv.org/abs/physics/0608123v1', 'type': 'arxiv', 'title': 'W4 theory for computational thermochemistry: in pursuit of confident sub-kJ/mol '}
