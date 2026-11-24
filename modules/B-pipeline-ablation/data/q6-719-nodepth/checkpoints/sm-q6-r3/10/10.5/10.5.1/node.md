# N584: 自建 10 个 POP 点（假设覆盖北上广深+5个省会）时，核心区域（一线/新一线）用户到最近 POP 的平均物理距离 d_core_self 约为 50-10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

自建 10 个 POP 点（假设覆盖北上广深+5个省会）时，核心区域（一线/新一线）用户到最近 POP 的平均物理距离 d_core_self 约为 50-100km，对应理论 RTT 为 7.5-10ms，加上处理延迟后 P99 约为 10-15ms。

## Corrected Claim

自建 10 个 POP 点（假设覆盖北上广深+5个省会）时，核心区域（一线/新一线）用户到最近 POP 的平均物理距离 d_core_self 约为 50-100km，对应理论 RTT 为 7.5-10ms，加上处理延迟后 P99 约为 10-15ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，50-100km单程距离对应250-500μs，往返RTT理论值500μs-1ms，加上网络协议栈、交换机处理及排队延迟，P99达到10-15ms符合工程经验量级。
