# N125: 用户到最近自建 POP 节点的物理距离 D_user_pop 的 P99 值，基于 10 个 POP 点的覆盖半径（约 500km）及用户地理分布，估算为 10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

用户到最近自建 POP 节点的物理距离 D_user_pop 的 P99 值，基于 10 个 POP 点的覆盖半径（约 500km）及用户地理分布，估算为 100-500km，对应 RTT_user_pop P99 ≈ 10-50ms。

## Corrected Claim

用户到最近自建 POP 节点的物理距离 D_user_pop 的 P99 值，基于 10 个 POP 点的覆盖半径（约 500km）及用户地理分布，估算为 100-500km，对应 RTT_user_pop P99 ≈ 10-50ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义距离分布参数，节点2推导P99距离值，节点3和4分别计算对应核心与长尾区域的RTT。虽然节点3和4结构相似，但它们分别对应不同的距离输入（100km vs 500km）和不同的业务场景（核心 vs 长尾），属于必要的并行计算步骤，而非简单冗余。父节点提到的范围10-50ms与子节点计算的10ms和30ms（30ms略超出父节点估算上限50ms内的合理范围，但父节点是粗略估算，子节点是具体推导，逻辑上子节点更精确，且30ms在50ms以内，无矛盾）一致。）

## Search Query

self-built POP node coverage radius RTT latency
