# N692: H_self=0.98 场景下，RTT_user_pop_core_p99=15ms 对应的用户地理分布约束：核心区域用户需距离最近 POP 点 D < 200

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N230

## Claim

H_self=0.98 场景下，RTT_user_pop_core_p99=15ms 对应的用户地理分布约束：核心区域用户需距离最近 POP 点 D < 200km（基于 RTT_ms ≈ 0.05 * d + 5，解得 d < 200km），即 10 个 POP 需覆盖 80% 的 DAU 用户，且 POP 间距需小于 400km 以确保无覆盖盲区。

## Corrected Claim

H_self=0.98 场景下，RTT_user_pop_core_p99=15ms 对应的用户地理分布约束：核心区域用户需距离最近 POP 点 D < 200km（基于 RTT_ms ≈ 0.05 * d + 5，解得 d < 200km），即 10 个 POP 需覆盖 80% 的 DAU 用户，且 POP 间距需小于 400km 以确保无覆盖盲区。

## Evidence

先验知识/题面给定，逻辑校验通过：基于公式 RTT_ms ≈ 0.05 * d + 5，代入 RTT=15ms 解得 d < 200km，数学推导正确；POP 间距小于 2 倍覆盖半径（400km）以确保无盲区符合几何覆盖逻辑。

## Search Query

user distance to POP point RTT 15ms geographic coverage constraint
