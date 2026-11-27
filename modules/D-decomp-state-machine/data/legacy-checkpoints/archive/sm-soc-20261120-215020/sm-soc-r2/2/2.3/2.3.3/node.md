# N38: 卖家维持高挂价策略的临界条件为 $W(t) < \psi(\Delta P)$，代入具体数值：当 $P_{list}=1000$，$r_{total}=7.5\

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

卖家维持高挂价策略的临界条件为 $W(t) < \psi(\Delta P)$，代入具体数值：当 $P_{list}=1000$，$r_{total}=7.5\%$，$t=30$天时，$W(30) \approx 6.16$；若 $\Delta P=100$，$\Pr(Sale|P_{new})=0.8$，则 $\psi(100) = 2.25 \times 100 \times 0.2 = 45$。由于 $6.16 < 45$，卖家在30天内无降价激励，解释了为何高挂价能持续存在。

## Corrected Claim

卖家维持高挂价策略的临界条件为 $W(t) < \psi(\Delta P)$，代入具体数值：当 $P_{list}=1000$，$r_{total}=7.5\%$，$t=30$天时，$W(30) \approx 6.16$；若 $\Delta P=100$，$\Pr(Sale|P_{new})=0.8$，则 $\psi(100) = 2.25 \times 100 \times 0.2 = 45$。由于 $6.16 < 45$，卖家在30天内无降价激励，解释了为何高挂价能持续存在。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 $W(30) \approx 6.16$ 与 $\psi(100) = 45$ 符合算术逻辑，且 $6.16 < 45$ 的结论与陈述一致，无内部矛盾。

## Search Query

threshold condition for seller price maintenance waiting cost vs psychological loss
