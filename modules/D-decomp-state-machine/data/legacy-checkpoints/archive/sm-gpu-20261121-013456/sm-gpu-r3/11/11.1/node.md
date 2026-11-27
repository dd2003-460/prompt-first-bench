# N120: Qwen3-27B 在 FP8 E4M3 精度下，WikiText-103 或 C4 数据集上的 Perplexity (PPL) 增加量（FP8_PPL - 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N46

## Claim

Qwen3-27B 在 FP8 E4M3 精度下，WikiText-103 或 C4 数据集上的 Perplexity (PPL) 增加量（FP8_PPL - BF16_PPL），预期 < 0.05-0.1，用于衡量 FP8 相比 BF16 的通用语言建模能力退化程度。

## Corrected Claim

Qwen3-27B 在 FP8 E4M3 精度下，WikiText-103 或 C4 数据集上的 Perplexity (PPL) 相比 BF16 会有轻微增加，具体数值需参考官方技术报告或基准测试，通常预期在较小范围内（如 < 0.1），但当前来源未提供确切数据。

## Evidence

[质询]参考来源均为部署指南或提示词工程博客，未提供具体的 Perplexity (PPL) 数值对比数据，无法直接验证 < 0.05-0.1 这一具体量化指标；且来源中模型名称标注为 'Qwen3.8-27B'，与事实节点中的 'Qwen3-27B' 存在版本命名上的潜在不一致（虽可能指代同一系列，但缺乏明确对应关系）。 | 逻辑上 FP8 相比 BF16 精度降低，PPL 轻微上升符合直觉，量级 0.05-0.1 在 LLM 量化领域属于合理预期范围；但参考来源 [1][2][3] 仅涉及部署和提示词，未包含 PPL 基准测试数据，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B FP8 perplexity increase WikiText

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01040/article/details/152202097&rut=d2d34c2797c59de523a09697634e52740594d0d8572f600769ed3d81ea70fb96', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 提示词工程指南：10 个让多模态大模型发挥全部实力的技巧-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=90c2b8874e00fe7c65b297d67da0c9b8864d2183e939c714938b3ce2952db9f2', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/lovely_yoshino/article/details/163828474&rut=f6894b90ac7485860ac5f5249184ac86fb627c1a73eb675037becd7558980c4f', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 部署实践：从原理到生产 - CSDN博客'}
