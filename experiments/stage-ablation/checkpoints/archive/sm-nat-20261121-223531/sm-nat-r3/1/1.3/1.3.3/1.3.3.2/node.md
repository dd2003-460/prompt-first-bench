# N110: LRU 稳态模拟的收敛判据与时间窗口：模拟运行时长 T_sim 需满足 T_sim ≥ 10 * max(1/h_i) 以覆盖长尾对象的访问周期；稳态判定标准为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N36

## Claim

LRU 稳态模拟的收敛判据与时间窗口：模拟运行时长 T_sim 需满足 T_sim ≥ 10 * max(1/h_i) 以覆盖长尾对象的访问周期；稳态判定标准为最后 10% 时间窗内的字节命中率波动 < 0.1% 且缓存命中率标准差 < 0.005，若未收敛则延长模拟至 30 天。

## Corrected Claim

LRU 稳态模拟的收敛判据与时间窗口：模拟运行时长 T_sim 需满足 T_sim ≥ 10 * max(1/h_i) 以覆盖长尾对象的访问周期；稳态判定标准为最后 10% 时间窗内的字节命中率波动 < 0.1% 且缓存命中率标准差 < 0.005，若未收敛则延长模拟至 30 天。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU simulation steady state convergence criteria cache hit rate
