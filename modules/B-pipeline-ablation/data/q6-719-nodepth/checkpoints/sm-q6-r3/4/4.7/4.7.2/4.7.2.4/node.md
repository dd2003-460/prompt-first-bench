# N407: 自建POP节点总处理时间 T_proc_pop 的P99值为各分项之和：T_proc_pop_P99 = T_cpu_P99 + T_mem_P99 + T_n

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N126

## Claim

自建POP节点总处理时间 T_proc_pop 的P99值为各分项之和：T_proc_pop_P99 = T_cpu_P99 + T_mem_P99 + T_net_P99 ≈ 5 + 2 + 2 = 9ms。

## Corrected Claim

自建POP节点总处理时间 T_proc_pop 的P99值近似为各分项P99之和：T_proc_pop_P99 ≈ T_cpu_P99 + T_mem_P99 + T_net_P99。

## Evidence

[质询]P99延迟通常不等于各分项P99之和（除非各分项完全正相关），且具体数值（5ms, 2ms, 2ms）属于经验参数，缺乏通用理论支持。 | source=knowledge，逻辑上加法自洽，但具体数值为经验事实，无来源支持，依据经验事实排除条款降级。
