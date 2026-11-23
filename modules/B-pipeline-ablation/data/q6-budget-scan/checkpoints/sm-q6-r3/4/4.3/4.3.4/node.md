# N83: 混合策略回源带宽成本拆分：Origin_Bandwidth_mixed = (Traffic_core × (1 - H_self)) + (Traffic_t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

混合策略回源带宽成本拆分：Origin_Bandwidth_mixed = (Traffic_core × (1 - H_self)) + (Traffic_tail × (1 - H_mixed_tail))。其中 Traffic_core × (1 - H_self) 为自建回源至 Origin 的流量，Traffic_tail × (1 - H_mixed_tail) 为公有云回源至 Origin 的流量。需分别计算两部分带宽成本。

## Corrected Claim

混合策略回源带宽成本拆分：Origin_Bandwidth_mixed = (Traffic_core × (1 - H_self)) + (Traffic_tail × (1 - H_mixed_tail))。其中 Traffic_core × (1 - H_self) 为自建回源至 Origin 的流量，Traffic_tail × (1 - H_mixed_tail) 为公有云回源至 Origin 的流量。需分别计算两部分带宽成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的核心流量项、长尾流量项、总成本计算式以及敏感性分析，逻辑清晰且无重叠。虽然子节点1和2提供了具体数值示例，但它们分别对应父节点公式中的两个不同变量部分，且子节点3明确依赖前两者的结果，子节点4则是对参数的边际影响分析，四者共同构成了完整的成本拆分与评估闭环，不存在冗余或矛盾。）
