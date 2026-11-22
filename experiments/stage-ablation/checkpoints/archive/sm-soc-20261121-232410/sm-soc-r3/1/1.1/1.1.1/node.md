# N31: 锚定参考点P_reference的构成公式：P_reference = w_1*P_initial + w_2*P_max + w_3*P_median，其中w

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

锚定参考点P_reference的构成公式：P_reference = w_1*P_initial + w_2*P_max + w_3*P_median，其中w_1=0.4, w_2=0.3, w_3=0.3，权重通过平台A/B测试确定，用于计算ΔP_anchor的基准。

## Corrected Claim

锚定参考点P_reference的构成公式：P_reference = w_1*P_initial + w_2*P_max + w_3*P_median，其中w_1=0.4, w_2=0.3, w_3=0.3，权重通过平台A/B测试确定，用于计算ΔP_anchor的基准。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的三个变量（P_initial, P_max, P_median）和权重确定机制（w_1, w_2, w_3），逻辑上互斥且无重叠。每个子节点聚焦于一个特定组成部分的定义、计算逻辑或优化策略，未出现内容交叉或矛盾。）

## Search Query

anchoring effect reference price composition formula e-commerce
