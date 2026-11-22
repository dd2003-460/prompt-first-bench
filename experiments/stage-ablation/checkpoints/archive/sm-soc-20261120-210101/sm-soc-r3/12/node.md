# N117: 干预策略的‘最小性’判定公式：最小干预需满足成本函数 C_intervention 最小化，C_intervention = C_dev * η_display

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

干预策略的‘最小性’判定公式：最小干预需满足成本函数 C_intervention 最小化，C_intervention = C_dev * η_display + C_user_confusion。其中 C_dev 为开发成本（固定），C_user_confusion 为因信息过载导致的用户流失率 ΔChurn。若 ΔChurn < 1% 且 η_display 能降低高挂价幅度 ΔP 至少 5%，则视为最小有效干预。

## Corrected Claim

干预策略的‘最小性’判定公式：最小干预需满足成本函数 C_intervention 最小化，C_intervention = C_dev * η_display + C_user_confusion。其中 C_dev 为开发成本（固定），C_user_confusion 为因信息过载导致的用户流失率 ΔChurn。若 ΔChurn < 1% 且 η_display 能降低高挂价幅度 ΔP 至少 5%，则视为最小有效干预。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的两个主要成本项（C_dev, C_user_confusion）以及最终的判定约束条件，三者职责清晰，无重叠或矛盾，且共同构成了对‘最小性’判定的完整解释。）
