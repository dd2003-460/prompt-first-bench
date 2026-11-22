# N57: 买家伤害投影：买家效用变化 ΔU_buyer = |U_new - U_old| / U_old，由于买家搜索阈值 T_search 未变且偏好分布不变，理论值

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

买家伤害投影：买家效用变化 ΔU_buyer = |U_new - U_old| / U_old，由于买家搜索阈值 T_search 未变且偏好分布不变，理论值 ΔU_buyer = 0，但受 ε_traffic 影响，实际观测值需满足 |ΔU_buyer| < 0.01 (1%) 方可判定为无显著伤害。

## Corrected Claim

买家伤害投影：买家效用变化 ΔU_buyer = |U_new - U_old| / U_old，由于买家搜索阈值 T_search 未变且偏好分布不变，理论值 ΔU_buyer = 0，但受 ε_traffic 影响，实际观测值需满足 |ΔU_buyer| < 0.01 (1%) 方可判定为无显著伤害。

## Evidence

父节点级核验未通过：不完备（子节点分别关注‘效用变化的来源机制（搜索成本）’和‘统计检验标准（阈值与功效）’，两者维度不同，具备正交性。但存在完备性问题：父节点明确提到‘理论值 ΔU_buyer = 0’是基于‘搜索阈值 T_search 未变且偏好分布不变’，而子节点1仅讨论了搜索成本波动，完全遗漏了‘偏好分布不变’这一关键假设的验证或影响分析，也未涵盖除搜索成本外其他可能影响买家效用的因素（如价格、质量感知等）。）
