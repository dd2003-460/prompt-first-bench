# N101: 单次代码修正迭代的端到端延迟 T_iter = E_tokens / Throughput + T_exec + T_debug，其中T_exec为代码执行时间

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

单次代码修正迭代的端到端延迟 T_iter = E_tokens / Throughput + T_exec + T_debug，其中T_exec为代码执行时间（通常<1s），T_debug为解析报错时间（<0.1s），主要耗时在LLM生成阶段；若Throughput=15 tokens/sec，E_tokens=750，则T_iter ≈ 50秒。

## Corrected Claim

单次代码修正迭代的端到端延迟 T_iter = E_tokens / Throughput + T_exec + T_debug，其中T_exec为代码执行时间（通常<1s），T_debug为解析报错时间（<0.1s），主要耗时在LLM生成阶段；若Throughput=15 tokens/sec，E_tokens=750，则T_iter ≈ 50秒。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（750/15=50s），量级符合LLM推理常识，公式结构自洽。
