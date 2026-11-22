# N123: 干预措施的长期适应性衰减系数 λ_decay：假设干预效果随时间 t 衰减，δc(t) = δc_0 * e^(-λ_decay * t)，需估计 λ_deca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36, N37, N38

## Claim

干预措施的长期适应性衰减系数 λ_decay：假设干预效果随时间 t 衰减，δc(t) = δc_0 * e^(-λ_decay * t)，需估计 λ_decay 的范围（例如 0.01-0.05/周），以判断 C_intervention 在 3 个月后的可信度是否仍 > 0.5

## Corrected Claim

干预措施的长期适应性衰减系数 λ_decay：假设干预效果随时间 t 衰减，δc(t) = δc_0 * e^(-λ_decay * t)，需估计 λ_decay 的范围（例如 0.01-0.05/周），以判断 C_intervention 在 3 个月后的可信度是否仍 > 0.5

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义机制分解，节点2和3分别对应两个独立分量的估算方法（卖家侧vs买家侧），节点4基于前三个节点的结果进行最终判定。没有内容重复或矛盾，且覆盖了从机制定义、参数估算到最终可信度判断的完整链条。）

## Search Query

behavioral intervention long-term decay effect habituation marketplace pricing tools
