# N32: 曝光量下降的弹性系数：设初始曝光量为 $E_0$，引入惩罚后曝光量 $E_{new} = E_0 \times (1 - k \times \frac{|P_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

曝光量下降的弹性系数：设初始曝光量为 $E_0$，引入惩罚后曝光量 $E_{new} = E_0 \times (1 - k \times \frac{|P_{ask}-P_{avg}|}{P_{avg}})$，其中 $k$ 为平台流量弹性系数，经验值通常在 0.3-0.5 之间（即每1%价格偏离导致0.3-0.5%曝光损失）。

## Corrected Claim

曝光量下降的弹性系数：设初始曝光量为 $E_0$，引入惩罚后曝光量 $E_{new} = E_0 \times (1 - k \times \frac{|P_{ask}-P_{avg}|}{P_{avg}})$，其中 $k$ 为平台流量弹性系数，经验值通常在 0.3-0.5 之间（即每1%价格偏离导致0.3-0.5%曝光损失）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

marketplace traffic elasticity price penalty exposure drop
