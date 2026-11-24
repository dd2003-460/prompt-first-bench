# N146: 在跨省用户（如北京用户访问广州POP，假设无更近POP）场景下，物理距离 d ≈ 1900 km，RTT 理论下限 = 2×1900km / (2×10^8 m

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在跨省用户（如北京用户访问广州POP，假设无更近POP）场景下，物理距离 d ≈ 1900 km，RTT 理论下限 = 2×1900km / (2×10^8 m/s) ≈ 19ms，代表高延迟/高带宽成本工作点。

## Corrected Claim

在跨省用户（如北京用户访问广州POP，假设无更近POP）场景下，物理距离 d ≈ 1900 km，RTT 理论下限 = 2×1900km / (2×10^8 m/s) ≈ 19ms，代表高延迟/高带宽成本工作点。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在明显的逻辑重叠和冗余。子节点2详细推导了物理RTT下限及实际RTT构成，而子节点1中的 T_rtt_physical 和子节点3中的 T_jitter 实际上是子节点2和3所定义变量的组成部分。子节点1作为总公式，其变量定义与子节点2、3的内容高度重合，导致信息重复而非正交分解。此外，子节点2中关于实际RTT的公式引入了 T_fiber_delay，这与物理光速下限的计算逻辑存在混淆（光速即光纤传播速度，通常不需要额外叠加介质延迟，除非指代设备转发延迟，但命名不准确）。）

## Search Query

Beijing to Guangzhou distance km RTT calculation
