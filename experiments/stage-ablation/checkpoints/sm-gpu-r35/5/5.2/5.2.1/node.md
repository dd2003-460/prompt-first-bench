# N257: Qwen3-27B INT8 (GPTQ/AWQ) 在 HumanEval Pass@1 上的基线准确率为 65.2%（基于 Qwen2.5-32B 同架构数据

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B INT8 (GPTQ/AWQ) 在 HumanEval Pass@1 上的基线准确率为 65.2%（基于 Qwen2.5-32B 同架构数据外推，Qwen3 具体数值需查官方技术报告，此处作为对比基准 [待核验]）。

## Corrected Claim

Qwen3-27B INT8 (GPTQ/AWQ) 在 HumanEval Pass@1 上的具体准确率需查阅官方技术报告或独立评测，此处 65.2% 仅为基于 Qwen2.5-32B 的粗略外推估计，不应作为确切基线。

## Evidence

[质询]该数值（65.2%）被明确标记为基于 Qwen2.5-32B 的“外推”且注明“需查官方技术报告”，属于未经证实的经验性估算，而非 Qwen3-27B INT8 的实际测量数据；此外，Qwen2.5-32B 与 Qwen3-27B 架构及训练数据不同，直接外推缺乏严谨性。 | 参考来源 [1] 和 [2] 均与该事实主题（LLM 基准测试）无关，无可用外部证据；该陈述为经验事实且自认是外推值，逻辑上虽无硬伤但缺乏直接来源支持，故降级。

## Search Query

Qwen3-27B INT8 HumanEval Pass@1 benchmark score

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
