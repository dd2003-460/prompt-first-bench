# N114: L1 到 L2 的回源延迟 RTT_L1_L2 通常为 5-20ms（取决于 L1 与 L2 节点间的地理距离和网络质量），L2 到源站的回源延迟 RTT_L2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

L1 到 L2 的回源延迟 RTT_L1_L2 通常为 5-20ms（取决于 L1 与 L2 节点间的地理距离和网络质量），L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，总回源延迟 RTT_origin_total = RTT_L1_L2 + RTT_L2_origin + T_transfer_origin，其中 T_transfer_origin 取决于对象大小 s 和源站带宽。

## Corrected Claim

L1 到 L2 的回源延迟 RTT_L1_L2 通常为 5-20ms（取决于 L1 与 L2 节点间的地理距离和网络质量），L2 到源站的回源延迟 RTT_L2_origin 通常为 20-50ms，总回源延迟 RTT_origin_total = RTT_L1_L2 + RTT_L2_origin + T_transfer_origin，其中 T_transfer_origin 取决于对象大小 s 和源站带宽。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别详细阐述了公式中的三个核心变量（RTT_L1_L2, RTT_L2_origin, T_transfer_origin）及其计算逻辑，最后汇总了总延迟的估算逻辑。各节点内容互不重叠，且完整覆盖了父节点定义的所有组成部分和约束条件。虽然子节点1和2对RTT的具体数值范围进行了更细致的场景化拆解（如区分自建/公有云、同城/跨省），但这属于对父节点中“取决于...”这一模糊描述的合理展开，而非冗余重复。）

## Search Query

CDN L1 L2 origin server latency breakdown
