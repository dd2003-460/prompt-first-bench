# N65: Qwen3-27B 在 HumanEval 基准测试上的 BF16 基线 Pass@1 分数约为 50-55% [待核验: 官方技术报告具体数值]，用于评估代码

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

Qwen3-27B 在 HumanEval 基准测试上的 BF16 基线 Pass@1 分数约为 50-55% [待核验: 官方技术报告具体数值]，用于评估代码生成任务的质量保持率

## Corrected Claim

Qwen3-27B 在 HumanEval 基准测试上的 BF16 基线 Pass@1 分数通常远高于 50-55%，参考同类模型数据可能在 80%-95% 区间（需具体查证 Qwen3-27B 官方报告，但绝非 50-55%）。

## Evidence

[质询]数值量级严重错误且来源矛盾：参考来源[3]显示Qwen3.8-27B在HumanEval上得分高达94.5%，而Qwen3系列模型通常具备较强的代码能力，50-55%的Pass@1分数远低于该级别模型的预期水平（通常应在80%-90%以上），且与来源中展示的高分数据存在数量级上的巨大差异。 | 来源[3]显示同类模型（Qwen3.8-27B）在HumanEval上得分为94.5%，与声称的50-55%严重矛盾；且50-55%对于27B规模的现代LLM而言逻辑上不合理（过低）。

## Search Query

Qwen3-27B HumanEval benchmark score pass@1

## Retrieval Sources

- {'url': 'https://www.heyneo.com/blog/evaluating-qwen-3-6-27b-benchmarking-case-study&rut=4e299f6bc14fb19b2cc4fe1ba4bd86c72e0093f622bab73da407c6e139439a3f', 'type': 'ddg', 'title': 'Evaluating Qwen 3.6 27B: A Complete Benchmarking Case Study'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=e39f61fec722c9abc323688d09f8fdce06ba4173462b27b29eaaddb429491031', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
- {'url': 'https://omlx.ai/benchmarks/intelligence/jesz8lt3&rut=ec8965b635bc41ab9d6caaa23ec0fa1f7d8b293cb33bdde52aa6663111ff24c9', 'type': 'ddg', 'title': 'Qwen3.8-27B-bf16-MTP-MLX-oQ8e-mtp — HumanEval 94.5% — oMLX Benchmark'}
