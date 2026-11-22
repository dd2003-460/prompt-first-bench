# N85: BF16 作为基准的 MMLU/HumanEval 准确率：Qwen3-27B 在 BF16 下的 MMLU 准确率约为 85-88% [待核验]，HumanE

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

BF16 作为基准的 MMLU/HumanEval 准确率：Qwen3-27B 在 BF16 下的 MMLU 准确率约为 85-88% [待核验]，HumanEval 通过率约为 60-65% [待核验]；需查阅 Qwen3 官方技术报告或 HuggingFace 模型卡获取确切基准分数，作为后续量化损失计算的基线。

## Corrected Claim

Qwen3-27B 在 BF16 下的 MMLU 准确率和 HumanEval 通过率需查阅官方技术报告确认，参考来源显示 Qwen3.8-27B 在特定量化下的综合评测得分约为 75.70%，MMLU-Pro 得分约为 58.25%，具体数值可能因模型版本和评测基准不同而异。

## Evidence

[质询]参考来源均指向 'Qwen3.8' 系列模型（如 Qwen3.8-Flash-Next, Qwen3.8-27B），而非陈述中的 'Qwen3-27B'；且来源提供的基准分数（MMLU-Pro 58.25%, 综合评测 75.70%）与陈述中的数值范围（MMLU 85-88%, HumanEval 60-65%）存在显著差异或口径不一致，无法直接支持陈述中的具体数值。 | 来源 [1] 和 [2] 讨论的是 Qwen3.8 系列模型，与陈述中的 Qwen3-27B 型号不完全匹配，且提供的基准分数（MMLU-Pro 58.25%, 综合 75.70%）与陈述中的 MMLU 85-88% 不符，缺乏直接支持证据，但逻辑上 BF16 作为基线是合理的。

## Search Query

Qwen3-27B official benchmark MMLU HumanEval BF16 accuracy score

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00165/article/details/171185226&rut=5b9b84606627de6af83e7d47f5d1bc9eb411a7b1a4c88c4cd4503997895d1002', 'type': 'ddg', 'title': '量化模型反超BF16达2.85分？Qwen3.8-Flash-Next-GSQ-RCO-GGUF的MMLU-Pro 58'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=27b228d7af16e490b9adc87fd3e0b74e8a1ee61e6f65c589f50808764d00c34b', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
