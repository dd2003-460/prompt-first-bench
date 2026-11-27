# N58: 条件相关性差异 ΔCorr = Corr(P_ask, MatchTime | NoCredit) - Corr(P_ask, MatchTime | High

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

条件相关性差异 ΔCorr = Corr(P_ask, MatchTime | NoCredit) - Corr(P_ask, MatchTime | HighCredit)，若 ΔCorr > 0.1 且 p < 0.05，则证明高信用卖家的高挂价对匹配时间的负向影响显著减弱。

## Corrected Claim

条件相关性差异 ΔCorr = Corr(P_ask, MatchTime | NoCredit) - Corr(P_ask, MatchTime | HighCredit)，若 ΔCorr > 0.1 且 p < 0.05，则证明高信用卖家的高挂价对匹配时间的负向影响显著减弱。

## Evidence

先验知识/题面给定，逻辑校验通过
