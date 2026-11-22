# N279: Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分具体数值（作为W4精度-6.2%损失的基准参考），需确认是68%还是其他值以校准损失

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分具体数值（作为W4精度-6.2%损失的基准参考），需确认是68%还是其他值以校准损失幅度。

## Corrected Claim

Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分具体数值需进一步查证，当前来源未提供确切数据，无法确认是否为68%。

## Evidence

[质询]参考来源均指向 Qwen3.6 或 Qwen3.8 版本，而非 Qwen3-27B 基础版，且未提供 HumanEval Pass@1 的具体数值，无法确认 68% 这一基准值是否准确。 | 来源 [1][2][3] 均涉及 Qwen3.6/3.8 版本或量化对比，未直接提供 Qwen3-27B BF16 的 HumanEval 具体分数，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B HumanEval Pass@1 score BF16

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=7c62ae5163506309b6b4e745450fb238415164cdf6ba0f290efb724618fd4871', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
- {'url': 'https://blog.csdn.net/gitblog_00251/article/details/155293565&rut=32e4dc142f9def3bcaa50f5802c86a75f7ec62d48a3de9225587fa0c764b7c21', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4 vs 原版BF16：量化后速度、显存与效果全面对比-CSDN博客'}
- {'url': 'https://blog.csdn.net/liangjinhu/article/details/164183862&rut=a6a509f8e74bff9b487998cd33b34a6a6d8d0784c2d7f4310f4e98041b75497e', 'type': 'ddg', 'title': 'Qwen3.8-27B GSQ-RCO 量化部署实测：9.3GB 跑出超 BF16 精度，消费级显卡落地 27B 多模态'}
