# N185: Qwen3-27B 在 BF16 精度下的 MMLU 基准测试基准分数（Baseline Score），作为量化后退化计算的参照零点，需查阅 Qwen3 官方技

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

Qwen3-27B 在 BF16 精度下的 MMLU 基准测试基准分数（Baseline Score），作为量化后退化计算的参照零点，需查阅 Qwen3 官方技术报告或 HuggingFace 模型卡。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的标准 MMLU 基准分数需查阅 Qwen3 官方技术报告或 HuggingFace 模型卡；现有参考来源主要涉及 Qwen3.6-27B 变体的 MMLU Pro 分数（如 86.3），不能直接作为标准 Qwen3-27B 的 BF16 MMLU 基准参照。

## Evidence

[质询]参考来源均指向 'Qwen3.6-27B' 这一特定变体或未来版本，而非标准的 'Qwen3-27B' 基础模型；且来源 [2] 提供的是 MMLU Pro 分数而非标准 MMLU 基准分数，存在模型版本混淆和指标口径不一致的风险。 | 来源 [2] 间接提及了 Qwen3.6-27B 系列的 MMLU Pro 分数（86.3），但未直接提供标准 Qwen3-27B 在 BF16 下的标准 MMLU 基准分数，属于间接支持且存在版本/指标偏差，故降级。

## Search Query

Qwen3-27B MMLU benchmark score BF16 official

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=7aae2ac515b2d8496787d3262e190159eac55c7fb3ba5e9d4de1f8edb620e8de', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=83b2f645f8d3eb7bca0588168465104066fc61b7e0fdcd8c134eb2e096deb4e6', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
