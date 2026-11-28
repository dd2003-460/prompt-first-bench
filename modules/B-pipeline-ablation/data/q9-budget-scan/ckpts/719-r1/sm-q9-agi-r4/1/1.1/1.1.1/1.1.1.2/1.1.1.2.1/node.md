# N346: MMLU-Pro 基准中各学科子集准确率的实际标准差 σ_subject 需通过查阅 Qwen3 Technical Report 附录或第三方评测博客获取，若

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

MMLU-Pro 基准中各学科子集准确率的实际标准差 σ_subject 需通过查阅 Qwen3 Technical Report 附录或第三方评测博客获取，若 σ_subject 实际为 8.0%（而非假设的 5.0%），则整体标准误 SE ≈ 8.0/√16 = 2.0%，这将直接影响对模型能力波动的置信区间估计。

## Corrected Claim

MMLU-Pro 基准中各学科子集准确率的实际标准差 σ_subject 需通过查阅具体模型技术报告或第三方评测数据获取；若 σ_subject 为 8.0%，则整体标准误 SE ≈ 2.0%（基于 n=16 的假设），这将影响置信区间估计。

## Evidence

[质询]该陈述包含具体的经验数值（σ_subject = 8.0%）和特定的数据来源指向（Qwen3 Technical Report 附录），但参考来源中均未提供 MMLU-Pro 各学科子集准确率的标准差具体数值，也未提及 Qwen3 报告中的相关数据，属于缺乏直接证据支持的经验事实。 | 逻辑推导部分（SE = σ/√n）正确，但核心经验参数（σ=8.0%）在提供的参考来源 [1]-[3] 中均无直接支持，来源仅介绍 MMLU-Pro 的基本定义和评测方法，未涉及具体统计分布参数。

## Search Query

Qwen3 MMLU-Pro subject standard deviation variance

## Retrieval Sources

- {'url': 'https://github.com/modelscope/evalscope/blob/main/docs/zh/benchmarks/mmlu_pro.md&rut=541fe162344c0e28390f14dbae4442faf42d82ba6839b85721c2d787293561af', 'type': 'ddg', 'title': 'evalscope/docs/zh/benchmarks/mmlu_pro.md at main - GitHub'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=7247257&rut=40d8de73d3f3acdf69ada2c7f616eb689848fcc5e340b76e56001195b78d5ef6', 'type': 'ddg', 'title': '多领域语言模型评估指南：基于mmlu基准的实践与优化-百度开发者中心'}
- {'url': 'https://zhuanlan.zhihu.com/p/702019999&rut=68fd6a511623f6e35c90dcf829b4a015b6cad3ff88813d5d0f2121c1fb98d6e4', 'type': 'ddg', 'title': 'Aigc每周精选--大模型评测之mmlu-pro与mmlu - 知乎'}
