# N695: H_self=0.95 场景下，RTT_user_pop_core_p99=20ms 对应的用户地理分布约束：核心区域用户需距离最近 POP 点 D < 300

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N231

## Claim

H_self=0.95 场景下，RTT_user_pop_core_p99=20ms 对应的用户地理分布约束：核心区域用户需距离最近 POP 点 D < 300km（基于 RTT_ms ≈ 0.05 * d + 5，解得 d < 300km），即 10 个 POP 需覆盖 70% 的 DAU 用户，相比 H_self=0.98 场景覆盖范围扩大 50%。

## Corrected Claim

在假设 RTT 与距离满足线性关系 RTT_ms ≈ 0.05 * d + 5 的经验模型下，RTT_user_pop_core_p99=20ms 对应核心区域用户需距离最近 POP 点 D < 300km；该覆盖范围结论依赖于特定网络延迟经验参数，实际部署中需根据具体网络环境校准。

## Evidence

[质询]RTT 经验公式 `RTT_ms ≈ 0.05 * d + 5` 中的系数 0.05 ms/km 和基础延迟 5ms 属于特定网络环境下的经验估算值，并非普适物理常数；不同网络架构、光纤铺设密度及协议开销会导致该系数显著波动，直接据此推导出的 300km 距离约束缺乏通用性。 | source=knowledge，逻辑推导过程自洽（20 = 0.05d + 5 => d=300），但涉及具体网络延迟经验参数，属于经验事实，缺乏外部来源直接支持该特定系数及覆盖范围结论，故降级。

## Search Query

user distance to POP point RTT 20ms geographic coverage 300km
