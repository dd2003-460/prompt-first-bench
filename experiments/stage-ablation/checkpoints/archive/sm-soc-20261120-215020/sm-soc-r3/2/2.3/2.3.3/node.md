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

父节点级核验通过：正交+完备+无冗余（子节点分别针对均衡稳定性（离散陷阱）、参数敏感性（价格量级影响）和时间动态性（临界点分布）三个不同维度展开，彼此正交且无冗余。它们共同覆盖了父节点中涉及的临界条件、具体数值验证及时间变量，逻辑完备。）

## Search Query

threshold condition for seller price maintenance waiting cost vs psychological loss
