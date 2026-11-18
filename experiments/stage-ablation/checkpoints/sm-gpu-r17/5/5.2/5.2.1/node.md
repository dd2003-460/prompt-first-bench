# N257: Qwen3-27B INT8 (GPTQ/AWQ) 在 HumanEval Pass@1 上的基线准确率为 65.2%（基于 Qwen2.5-32B 同架构数据

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B INT8 (GPTQ/AWQ) 在 HumanEval Pass@1 上的基线准确率为 65.2%（基于 Qwen2.5-32B 同架构数据外推，Qwen3 具体数值需查官方技术报告，此处作为对比基准 [待核验]）。

## Corrected Claim

Qwen3-27B INT8 (GPTQ/AWQ) 在 HumanEval Pass@1 上的具体准确率需查阅 Qwen3 官方技术报告；此处暂以 Qwen2.5-32B 同量化配置下的表现（约 65.2%）作为参考基准，但需注意代际差异可能导致实际数值偏差。

## Evidence

[质询]该数值（65.2%）被明确标记为基于 Qwen2.5-32B 的“外推”且注明“需查官方技术报告”，属于未经证实的经验性估算，而非已确认的事实；此外，Qwen3-27B 与 Qwen2.5-32B 并非完全同架构（参数量不同，且 Qwen3 引入了新的 MoE 或混合架构特性，视具体版本而定，但通常不同代际模型性能不可简单线性外推），直接引用旧模型数据作为新模型基线存在逻辑跳跃。 | 参考来源 [1] 为凝聚态物理论文，与 LLM 基准测试完全无关，无可用外部证据；该陈述为经验事实（模型性能指标），逻辑上虽自洽（作为占位符/估算值），但缺乏来源直接支持，且明确标注为待核验的外推值，故降级。

## Search Query

Qwen3-27B INT8 HumanEval Pass@1 benchmark score

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
