# N307: SLA 赔付风险成本量化：更严格的 T 导致 SLA 违约概率 P_violation(T) 指数上升，期望赔付成本 C_sla(T) = P_violatio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

SLA 赔付风险成本量化：更严格的 T 导致 SLA 违约概率 P_violation(T) 指数上升，期望赔付成本 C_sla(T) = P_violation(T) × R_monthly × Penalty_Rate；假设 R_monthly=50 万元，Penalty_Rate=10%，P_violation(300ms)=0.001，P_violation(100ms)=0.01（10 倍增长），则 T=100ms 时的年期望赔付成本为 6 万元，是 T=300ms 时的 10 倍，需计入总运维成本。

## Corrected Claim

SLA 赔付风险成本量化：更严格的 T 导致 SLA 违约概率 P_violation(T) 指数上升，期望赔付成本 C_sla(T) = P_violation(T) × R_monthly × Penalty_Rate；假设 R_monthly=50 万元，Penalty_Rate=10%，P_violation(300ms)=0.001，P_violation(100ms)=0.01（10 倍增长），则 T=100ms 时的年期望赔付成本为 6 万元，是 T=300ms 时的 10 倍，需计入总运维成本。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（0.01 * 50万 * 10% * 12 = 6万），且与300ms时的0.6万相比确为10倍，符合SLA成本量化的一般逻辑。

## Search Query

CDN SLA penalty cost expectation violation probability tail latency
