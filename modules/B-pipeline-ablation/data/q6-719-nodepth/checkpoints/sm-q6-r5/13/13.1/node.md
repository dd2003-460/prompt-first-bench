# N403: 光纤中实际信号传播速度 v_fiber ≈ 200,000 km/s（真空中光速的 2/3），因此单跳传播延迟 L_prop = D / v_fiber；对于 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N134

## Claim

光纤中实际信号传播速度 v_fiber ≈ 200,000 km/s（真空中光速的 2/3），因此单跳传播延迟 L_prop = D / v_fiber；对于 300 km 覆盖半径，L_prop ≈ 1.5 ms；对于 500 km，L_prop ≈ 2.5 ms。此值不含交换机转发延迟和排队延迟。

## Corrected Claim

光纤中实际信号传播速度 v_fiber ≈ 200,000 km/s（真空中光速的 2/3），因此单跳传播延迟 L_prop = D / v_fiber；对于 300 km 覆盖半径，L_prop ≈ 1.5 ms；对于 500 km，L_prop ≈ 2.5 ms。此值不含交换机转发延迟和排队延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：光纤折射率约1.5，光速c≈300,000 km/s，故v≈200,000 km/s；300/200,000=0.0015s=1.5ms，500/200,000=0.0025s=2.5ms，计算无误。

## Search Query

fiber optic signal propagation speed km/s latency calculation
