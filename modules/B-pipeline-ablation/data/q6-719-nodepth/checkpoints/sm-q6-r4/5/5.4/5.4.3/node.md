# N115: 5k元/月/POP 的风险溢价估算隐含假设：单POP故障或政策限制导致的月均业务损失为50k元（即 P_pop_shutdown × 50k = 5k，若 P=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30, N31, N32

## Claim

5k元/月/POP 的风险溢价估算隐含假设：单POP故障或政策限制导致的月均业务损失为50k元（即 P_pop_shutdown × 50k = 5k，若 P=10% 则单POP月损失50k；若 P=1% 则单POP月损失500k），需验证该损失值是否与平台实际营收匹配

## Corrected Claim

5k元/月/POP 的风险溢价估算隐含假设：单POP故障或政策限制导致的月均业务损失为50k元（即 P_pop_shutdown × 50k = 5k，若 P=10% 则单POP月损失50k；若 P=1% 则单POP月损失500k），需验证该损失值是否与平台实际营收匹配

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1侧重于基于行业基准（ARPU）推导理论营收基线，从而定性判断假设的保守性；子节点2侧重于定义具体的量化检验公式（Match_Ratio）及阈值，从而定量界定场景类型（降级vs中断）。两者在逻辑上互补（定性基准 vs 定量验证），无重复或矛盾。父节点的核心任务（验证损失值与营收匹配）已被这两个方面完整覆盖。）

## Search Query

edge node failure business loss estimation methodology
