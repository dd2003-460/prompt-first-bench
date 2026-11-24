# N58: 自建 POP 处理时间 T_proc_pop 的 P99 值：由于硬件可能不如公有云边缘节点高性能，P99(T_proc_pop) 约为 10-20ms，略高于

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

自建 POP 处理时间 T_proc_pop 的 P99 值：由于硬件可能不如公有云边缘节点高性能，P99(T_proc_pop) 约为 10-20ms，略高于公有云的 5-15ms。

## Corrected Claim

自建 POP 处理时间 T_proc_pop 的 P99 值：由于硬件可能不如公有云边缘节点高性能，P99(T_proc_pop) 约为 10-20ms，略高于公有云的 5-15ms。

## Evidence

父节点级核验未通过：有冗余（子节点正交且覆盖了父节点描述的P99延迟范围（10-20ms）的两个极端工作点，逻辑清晰无矛盾。但两个子节点本质上是同一变量（硬件配置/性能等级）的不同取值，属于参数化描述，存在结构性冗余。）

## Search Query

Self-built POP server processing time P99 latency 10-20ms
