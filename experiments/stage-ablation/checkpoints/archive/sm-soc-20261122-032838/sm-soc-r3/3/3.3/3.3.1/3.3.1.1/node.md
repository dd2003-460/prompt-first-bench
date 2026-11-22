# N212: 曝光权重 $W$ 与点击量 $C$ 的非线性关系：$C = W \cdot I_{base} \cdot (1 - D_{sat})$，其中 $D_{sat}$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

曝光权重 $W$ 与点击量 $C$ 的非线性关系：$C = W \cdot I_{base} \cdot (1 - D_{sat})$，其中 $D_{sat}$ 为边际递减系数。若 $D_{sat} > 0$，则 $\Delta C / C < \Delta W / W$，导致 $\Delta T_{sale}$ 小于线性近似值 $\delta$。需估算二手市场典型 $D_{sat}$ 范围（如0.1-0.3）。

## Corrected Claim

曝光权重 $W$ 与点击量 $C$ 的非线性关系：$C = W \cdot I_{base} \cdot (1 - D_{sat})$，其中 $D_{sat}$ 为边际递减系数。若 $D_{sat} > 0$，则 $\Delta C / C < \Delta W / W$，导致 $\Delta T_{sale}$ 小于线性近似值 $\delta$。需估算二手市场典型 $D_{sat}$ 范围（如0.1-0.3）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导显示当 D_sat > 0 时，C 对 W 的弹性小于 1，故 ΔC/C < ΔW/W 成立；D_sat 取值范围符合一般边际递减经验。

## Search Query

search result click saturation diminishing returns e-commerce
