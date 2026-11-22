# N64: ΔGMV 的计算公式：ΔGMV = (V_new - V_old) * P_avg + V_old * (P_new - P_old)，其中 V_old/V_n

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

ΔGMV 的计算公式：ΔGMV = (V_new - V_old) * P_avg + V_old * (P_new - P_old)，其中 V_old/V_new 为干预前后成交量，P_old/P_new 为干预前后平均成交价，需分别估算成交量弹性和价格弹性。

## Corrected Claim

ΔGMV 的计算公式：ΔGMV = (V_new - V_old) * P_avg + V_old * (P_new - P_old)，其中 V_old/V_new 为干预前后成交量，P_old/P_new 为干预前后平均成交价，需分别估算成交量弹性和价格弹性。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点通过设定不同的弹性参数组合（高/中/低成交量弹性与价格弹性），展示了ΔGMV公式在不同市场响应场景下的计算结果。各场景在参数空间上互斥且覆盖典型区间，逻辑上正交。虽然本质上是同一公式的参数化实例，但在学术分解中，列举关键工作点（Work Points）以展示公式的行为特征（正/负/中性影响）是标准且必要的完备性体现，不构成冗余。）
