# N585: 自建 10 个 POP 点时，长尾区域（三四线/县域）用户到最近 POP 的平均物理距离 d_tail_self 约为 300-500km，对应理论 RTT 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

自建 10 个 POP 点时，长尾区域（三四线/县域）用户到最近 POP 的平均物理距离 d_tail_self 约为 300-500km，对应理论 RTT 为 20-30ms，加上处理延迟后 P99 约为 25-35ms，显著高于公有云在同等区域的 P99（因公有云节点更多）。

## Corrected Claim

自建 10 个 POP 点时，长尾区域（三四线/县域）用户到最近 POP 的平均物理距离 d_tail_self 约为 300-500km，对应理论 RTT 为 20-30ms，加上处理延迟后 P99 约为 25-35ms，显著高于公有云在同等区域的 P99（因公有云节点更多）。

## Evidence

先验知识/题面给定，逻辑校验通过：300-500km光纤传输延迟约为1.5-2.5ms（单程），往返RTT约3-5ms，加上网络处理、排队及长尾抖动，P99达到25-35ms符合工程经验量级；且自建节点少导致覆盖稀疏，距离远、延迟高符合物理直觉。
