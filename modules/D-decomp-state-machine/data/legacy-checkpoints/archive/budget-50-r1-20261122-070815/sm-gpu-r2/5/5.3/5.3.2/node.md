# N126: 批处理大小 (Batch Size) 从 1 增加到 8/16/32 时，Qwen3-27B 在 BF16 和 INT4 精度下的单 token 生成延迟 (T

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

批处理大小 (Batch Size) 从 1 增加到 8/16/32 时，Qwen3-27B 在 BF16 和 INT4 精度下的单 token 生成延迟 (TTFT, Time To First Token) 和吞吐量 (tokens/s) 的非线性变化曲线数据，需通过本地复现或搜索详细 profiling 报告获取，以评估多用户并发场景下的性能衰减。

## Corrected Claim

批处理大小 (Batch Size) 从 1 增加到 8/16/32 时，Qwen3-27B 在 BF16 和 INT4 精度下的单 token 生成延迟 (TTFT) 和吞吐量 (tokens/s) 通常呈现非线性变化，具体数值需通过本地复现或搜索详细 profiling 报告获取，以评估多用户并发场景下的性能衰减。

## Evidence

[质询]该陈述声称存在具体的“非线性变化曲线数据”，但参考来源仅涉及模型部署配置、显存需求和量化选择，未提供 Batch Size 对 TTFT 和吞吐量影响的详细 profiling 数据或曲线图，属于经验事实且缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2][3]仅覆盖部署与显存，未覆盖 Batch Size 性能曲线）

## Search Query

Qwen3-27B batch size 1 8 16 32 TTFT throughput scaling curve BF16 INT4 profiling data

## Retrieval Sources

- {'url': 'https://llmconfigurator.com/en/blog/qwen3-8-27b-which-quant-12-16-24-32gb&rut=e981606dfd077d0b9b36469989b7a7aca7afc8e5799846a699acbf246ce23750', 'type': 'ddg', 'title': 'Qwen3.8-27B: Best Quant for 12, 16, 24 and 32 GB'}
- {'url': 'https://docs.kanaries.net/articles/qwen3-8-27b&rut=5ba25a40ebb27f877cce8079e08a764135ca71e65ae263a3be6a4194d3e79b86', 'type': 'ddg', 'title': 'Qwen3.8 27B: Specs, Memory Requirements, and How to Run It'}
- {'url': 'https://magnitude.dev/models/qwen3.8-27b&rut=11d76cc7c2eb2a53025532d7589a72fff9c5ab8e516c82d20d13fb347f12d0d9', 'type': 'ddg', 'title': 'Run Qwen3.8 27B locally: sizes, requirements, downloads | Magnitude'}
