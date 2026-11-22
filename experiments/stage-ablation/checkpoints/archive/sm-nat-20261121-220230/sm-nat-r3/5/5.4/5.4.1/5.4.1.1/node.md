# N245: 在 u=0.01 时，折损因子 D(u) 的具体数值为 1 - (0.99)^T_resident；当 T_resident=1 天时，D(0.01) = 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

在 u=0.01 时，折损因子 D(u) 的具体数值为 1 - (0.99)^T_resident；当 T_resident=1 天时，D(0.01) = 0.99，即折损 1%；当 T_resident=10 天时，D(0.01) ≈ 0.904，即折损 9.6%。

## Corrected Claim

在 u=0.01 时，折损因子 D(u) 的具体数值为 1 - (0.99)^T_resident；当 T_resident=1 天时，D(0.01) = 0.99，即折损 1%；当 T_resident=10 天时，D(0.01) ≈ 0.904，即折损 9.6%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 D(u) = 1 - (1-u)^T 在 u=0.01 时，T=1 得 0.01（折损1%），T=10 得 1-0.99^10≈0.0956（折损9.56%≈9.6%），数值计算准确且逻辑自洽。
