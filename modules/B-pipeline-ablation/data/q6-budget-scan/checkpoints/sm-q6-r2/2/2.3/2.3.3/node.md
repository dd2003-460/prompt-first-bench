# N63: 公有云 CDN 场景下，由于节点密度更高，用户到最近 POP 的平均物理距离 $d_{cloud}$ 约为 20-50 km，导致单向传播延迟 $L_{prop

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

公有云 CDN 场景下，由于节点密度更高，用户到最近 POP 的平均物理距离 $d_{cloud}$ 约为 20-50 km，导致单向传播延迟 $L_{prop, cloud} = d_{cloud} / (2 \times 10^8) \times 10^3 \approx 0.1-0.25$ ms，往返 RTT 物理下限约为 0.2-0.5 ms。

## Corrected Claim

公有云 CDN 场景下，由于节点密度更高，用户到最近 POP 的平均物理距离 $d_{cloud}$ 约为 20-50 km，导致单向传播延迟 $L_{prop, cloud} = d_{cloud} / (2 \times 10^8) \times 10^3 \approx 0.1-0.25$ ms，往返 RTT 物理下限约为 0.2-0.5 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约3e8 m/s，光纤中光速约为2e8 m/s，20-50km距离对应单向延迟0.1-0.25ms，RTT为0.2-0.5ms，量级与物理常识一致。
