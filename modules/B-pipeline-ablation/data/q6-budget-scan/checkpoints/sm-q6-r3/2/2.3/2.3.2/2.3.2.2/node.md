# N184: 自建 POP 场景下，P99 延迟对应的物理距离 $d_{self, p99}$ 取 99th 百分位用户的距离，通常比平均值高 2-3 倍，即 $d_{sel

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

自建 POP 场景下，P99 延迟对应的物理距离 $d_{self, p99}$ 取 99th 百分位用户的距离，通常比平均值高 2-3 倍，即 $d_{self, p99} \approx 150-450$ km，导致单向传播延迟 $L_{prop, self, p99} \approx 0.75-2.25$ ms。

## Corrected Claim

自建 POP 场景下，P99 延迟对应的物理距离 $d_{self, p99}$ 取 99th 百分位用户的距离，通常比平均值高 2-3 倍，即 $d_{self, p99} \approx 150-450$ km，导致单向传播延迟 $L_{prop, self, p99} \approx 0.75-2.25$ ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约300,000 km/s，150-450 km对应0.5-1.5 ms纯光纤延迟，考虑介质折射率及网络开销后0.75-2.25 ms量级合理；P99距离为平均2-3倍符合长尾分布特征。
