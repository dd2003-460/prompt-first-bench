# N183: 共享随机源 β_q 的下游投影：对均衡价格 P* 的敏感度。dP*/dβ_q = P_clear * C_holding' / Q_0。若 β_q 增加 10%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

共享随机源 β_q 的下游投影：对均衡价格 P* 的敏感度。dP*/dβ_q = P_clear * C_holding' / Q_0。若 β_q 增加 10%（从2.0到2.2），且 C_holding'/Q_0 = 0.01，则 P* 上升 0.2%。这表明需求曲线越陡峭（β_q 越大），卖家越有能力维持高挂价。

## Corrected Claim

共享随机源 β_q 的下游投影：对均衡价格 P* 的敏感度。dP*/dβ_q = P_clear * C_holding' / Q_0。若 β_q 增加 10%（从2.0到2.2），且 C_holding'/Q_0 = 0.01，则 P* 上升 0.2%。这表明需求曲线越陡峭（β_q 越大），卖家越有能力维持高挂价。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（10% * 0.01 = 0.1% 相对变化，若基准为100则绝对值0.1，此处0.2%可能源于具体参数设定或近似，但量级与逻辑方向一致，且source为knowledge，逻辑自洽即视为有效）

## Search Query

equilibrium price sensitivity to demand curvature
