# N269: Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分具体数值需检索确认，当前假设值68.2%（基于N116中66.1%为-2.4%反推）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分具体数值需检索确认，当前假设值68.2%（基于N116中66.1%为-2.4%反推）存在不确定性，需验证是否为官方发布值

## Corrected Claim

Qwen3-27B在BF16精度下的HumanEval Pass@1基准得分具体数值需进一步检索官方发布数据确认，当前假设值68.2%缺乏直接来源支持，且需注意与Qwen3.6-27B版本区分。

## Evidence

[质询]来源均指向 'Qwen3.6-27B' 而非 'Qwen3-27B'，存在版本混淆风险；且来源摘要未直接提供 BF16 下 HumanEval Pass@1 的具体数值，无法直接验证 68.2% 这一假设值。 | 参考来源 [1][2][3] 均涉及 Qwen3.6-27B 的基准测试，但未直接给出 Qwen3-27B BF16 的 HumanEval 具体分数，且版本号存在差异（3 vs 3.6），无法直接支持该具体数值，属于经验事实缺直接来源支持。

## Search Query

Qwen3-27B HumanEval Pass@1 score BF16 official technical report

## Retrieval Sources

- {'url': 'https://www.heyneo.com/blog/evaluating-qwen-3-6-27b-benchmarking-case-study&rut=6ac8f79df6c54461759623add2d7e1fe7c9e0657a40e7be8b00a708ce3c3feda', 'type': 'ddg', 'title': 'Evaluating Qwen 3.6 27B: A Complete Benchmarking Case Study'}
- {'url': 'https://qevos.ai/blog/cn/2026-05-06-qwen36-27b-verilog-lora-finetuning.html&rut=fea8a13556df97dc5fb5b255f3465f7a840eb32587165d8f624516f18806ae79', 'type': 'ddg', 'title': 'Qwen3.6-27B Verilog微调全流程：训练、评估与HumanEval验证'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/141946772&rut=7c62ae5163506309b6b4e745450fb238415164cdf6ba0f290efb724618fd4871', 'type': 'ddg', 'title': 'Qwen3.6-27B-AEON-Ultimate-Uncensored-BF16性能测试：在A100/H100上的吞吐量与延迟基准'}
