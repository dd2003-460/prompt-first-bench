# N118: Qwen3-27B 在 BF16 基准下于 MMLU 数据集上的具体准确率数值 (Baseline_Acc_BF16_MMLU)，作为计算 INT8 下降幅度的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

Qwen3-27B 在 BF16 基准下于 MMLU 数据集上的具体准确率数值 (Baseline_Acc_BF16_MMLU)，作为计算 INT8 下降幅度的分母。

## Corrected Claim

Qwen3-27B 在 BF16 基准下于 MMLU 数据集上的具体准确率数值需查阅官方技术报告或权威基准测试数据，当前参考来源未提供该确切数值。

## Evidence

[质询]参考来源中未包含 Qwen3-27B 在 BF16 精度下 MMLU 数据集的具体准确率数值，且来源主要涉及其他版本（Qwen3.6/3.8）或不同量化格式（NVFP4/GSQ-RCO）的评测，无法直接支持该特定基准值。 | 经验事实，逻辑自洽但缺来源支持；来源[2]和[3]提及了相关模型的评测分数（如74.34, 86.3），但并非 Qwen3-27B BF16 在 MMLU 上的具体数值，无法直接验证。

## Search Query

Qwen3-27B MMLU benchmark accuracy BF16

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=7aae2ac515b2d8496787d3262e190159eac55c7fb3ba5e9d4de1f8edb620e8de', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=8d101b892bffb46b87003cdc8ef3a4d74fd9cad312ea5acd751e7c426bb2b5fe', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=83b2f645f8d3eb7bca0588168465104066fc61b7e0fdcd8c134eb2e096deb4e6', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
