# N98: 雅可比矩阵 J 的特征值 λ_i 需满足 Re(λ_i) < 0 才能证明均衡稳定；具体需计算 J 的行列式 det(J) > 0 且 trace(J) < 0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

雅可比矩阵 J 的特征值 λ_i 需满足 Re(λ_i) < 0 才能证明均衡稳定；具体需计算 J 的行列式 det(J) > 0 且 trace(J) < 0 作为稳定性判据。

## Corrected Claim

雅可比矩阵 J 的特征值 λ_i 需满足 Re(λ_i) < 0 才能证明均衡稳定；具体需计算 J 的行列式 det(J) > 0 且 trace(J) < 0 作为稳定性判据。

## Evidence

先验知识/题面给定，逻辑校验通过：对于2x2雅可比矩阵，特征值实部小于0的充要条件确实是行列式大于0且迹小于0（Routh-Hurwitz准则在二维的特例）。
