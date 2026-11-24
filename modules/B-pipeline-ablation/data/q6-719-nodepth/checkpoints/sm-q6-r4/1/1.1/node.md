# N6: 网络往返时间 (RTT) 基础值 = 2 × (物理距离 / 光速)，其中光速取 2×10^8 m/s（光纤折射率修正），物理距离由用户地理分布与最近 POP 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

网络往返时间 (RTT) 基础值 = 2 × (物理距离 / 光速)，其中光速取 2×10^8 m/s（光纤折射率修正），物理距离由用户地理分布与最近 POP 点的地理坐标计算得出（Haversine 公式）。

## Corrected Claim

网络往返时间 (RTT) 基础值 = 2 × (物理距离 / 光速)，其中光速取 2×10^8 m/s（光纤折射率修正），物理距离由用户地理分布与最近 POP 点的地理坐标计算得出（Haversine 公式）。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为2×10^8 m/s，RTT基础值公式及Haversine距离计算符合物理与地理常识。
