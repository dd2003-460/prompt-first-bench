# N189: 用户到 CDN 边缘节点/自建 POP 的 RTT 与物理距离 d(km) 的经验公式为 RTT_ms ≈ 0.05 * d + 5，其中 5ms 为固定处理延

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49

## Claim

用户到 CDN 边缘节点/自建 POP 的 RTT 与物理距离 d(km) 的经验公式为 RTT_ms ≈ 0.05 * d + 5，其中 5ms 为固定处理延迟，0.05ms/km 为光纤传播延迟系数（光速在光纤中约 200,000 km/s，往返加倍）

## Corrected Claim

用户到 CDN 边缘节点/自建 POP 的 RTT 与物理距离 d(km) 的经验公式为 RTT_ms ≈ 0.05 * d + 5，其中 5ms 为固定处理延迟，0.05ms/km 为光纤传播延迟系数（光速在光纤中约 200,000 km/s，往返加倍）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别解释了公式中的斜率系数（物理基础）、截距项（固定延迟）以及公式的适用边界（非线性修正），三者维度不同，互不重叠且无矛盾，共同完整覆盖了父节点公式的构成要素及局限性。）
