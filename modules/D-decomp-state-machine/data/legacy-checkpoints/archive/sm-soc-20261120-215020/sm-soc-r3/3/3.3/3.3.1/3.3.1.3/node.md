# N138: 总基础设施成本增量 $\Delta C_{infra} = \Delta F_{update} \times N_{items} \times C_{unit}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

总基础设施成本增量 $\Delta C_{infra} = \Delta F_{update} \times N_{items} \times C_{unit}$，其中 $N_{items}$ 为受监控商品总数。若 $N_{items}=10^6$，$C_{unit}=0.001$ 元/次，则 $\Delta C_{infra} = 1.5 \times F_{base} \times 10^6 \times 0.001$。

## Corrected Claim

总基础设施成本增量 $\Delta C_{infra} = \Delta F_{update} \times N_{items} \times C_{unit}$，其中 $N_{items}$ 为受监控商品总数。若 $N_{items}=10^6$，$C_{unit}=0.001$ 元/次，则 $\Delta C_{infra} = 1.5 \times F_{base} \times 10^6 \times 0.001$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本累加逻辑，数值代入计算正确（1.5 * 10^6 * 0.001 = 1500，即 1.5 * F_base * 1500 或保留符号形式均自洽）。
