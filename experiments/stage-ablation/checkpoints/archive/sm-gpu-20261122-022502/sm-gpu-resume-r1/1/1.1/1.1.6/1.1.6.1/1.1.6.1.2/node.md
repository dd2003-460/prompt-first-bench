# N468: Qwen3-27B BF16 基线在 MMLU-Pro 上的准确率为 75.2% (来源：Qwen3 官方技术报告 Table 3 或 HuggingFace 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N146

## Claim

Qwen3-27B BF16 基线在 MMLU-Pro 上的准确率为 75.2% (来源：Qwen3 官方技术报告 Table 3 或 HuggingFace 模型卡片，需核验具体版本)。

## Corrected Claim

Qwen3-27B BF16 基线在 MMLU-Pro 上的准确率约为 75.2%（需进一步核验具体版本及测试条件，现有来源未直接支持该数值）。

## Evidence

[质询]参考来源中未包含 Qwen3-27B 在 MMLU-Pro 上的具体基线数据，且来源 [3] 提到的 Qwen3.6-27B 精度为 86.3%，与声称的 75.2% 存在显著差异，可能涉及版本混淆或数据错误。 | 经验事实，逻辑自洽但缺来源支持；来源 [1] 仅提及 Qwen3.7 Max 得分，未覆盖 Qwen3-27B 基线；来源 [3] 显示 Qwen3.6-27B 得分远高于 75.2%，暗示该数值可能偏低或对应早期版本，但无直接证据证实 75.2% 的准确性。

## Search Query

Qwen3-27B MMLU-Pro accuracy BF16 official report

## Retrieval Sources

- {'url': 'https://benchlm.ai/benchmarks/mmlu-pro&rut=62238d7f75a0ca07dbaefc0218621ba3c229544d8162f3825c81da37003d29f9', 'type': 'ddg', 'title': 'MMLU-Pro Leaderboard & Scores — November 2026 | BenchLM.ai'}
- {'url': 'https://blog.gitcode.com/2168c60dae62628d71ae7c68a0c402ff.html&rut=9591a030fe17d9bec407823257887c3b3b690470e089990e93cd6a2bf17c1dff', 'type': 'ddg', 'title': '如何开启Qwen3.8-27B-AP-GGUF视觉能力:mmproj-BF16实战教程与踩坑清单'}
- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=83b2f645f8d3eb7bca0588168465104066fc61b7e0fdcd8c134eb2e096deb4e6', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
