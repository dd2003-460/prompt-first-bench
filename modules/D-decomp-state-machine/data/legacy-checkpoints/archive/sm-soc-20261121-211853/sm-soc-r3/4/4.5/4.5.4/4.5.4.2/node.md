# N115: 卖家预期收益 $\pi$ 的动态调整项：$\pi_{adj} = P_{sell} \times (Price - C_{var}) - C_{time} \t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

卖家预期收益 $\pi$ 的动态调整项：$\pi_{adj} = P_{sell} \times (Price - C_{var}) - C_{time} \times T_{cycle} - C_{reputation} \times \Delta T$，其中 $C_{reputation}$ 为每延迟一天成交导致的信誉分衰减损失（估算为 0.5-1.5 元/天），$\Delta T$ 为因流量干预导致的额外延迟天数。

## Corrected Claim

卖家预期收益 $\pi$ 的动态调整项：$\pi_{adj} = P_{sell} \times (Price - C_{var}) - C_{time} \times T_{cycle} - C_{reputation} \times \Delta T$，其中 $C_{reputation}$ 为每延迟一天成交导致的信誉分衰减损失（估算为 0.5-1.5 元/天），$\Delta T$ 为因流量干预导致的额外延迟天数。

## Evidence

先验知识/题面给定，逻辑校验通过
