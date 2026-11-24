# N128: 帕累托前沿最优解判定条件：若存在策略A使得 P99_A ≤ P99_B 且 Cost_A ≤ Cost_B（至少一个严格小于），则A优于B；需比较三者的(P99

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

帕累托前沿最优解判定条件：若存在策略A使得 P99_A ≤ P99_B 且 Cost_A ≤ Cost_B（至少一个严格小于），则A优于B；需比较三者的(P99, Cost)坐标，通常混合策略在P99≤150ms区间成本最低，全公有云在P99≤100ms区间成本最低，自建在P99>200ms区间成本最低但延迟不可接受

## Corrected Claim

帕累托前沿最优解判定条件：若存在策略A使得 P99_A ≤ P99_B 且 Cost_A ≤ Cost_B（至少一个严格小于），则A优于B；需比较三者的(P99, Cost)坐标，通常混合策略在P99≤150ms区间成本最低，全公有云在P99≤100ms区间成本最低，自建在P99>200ms区间成本最低但延迟不可接受

## Evidence

先验知识/题面给定，逻辑校验通过
