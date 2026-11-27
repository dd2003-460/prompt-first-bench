# N143: 海维塞德函数 $H(\cdot)$ 的平滑化修正：实际中 $P_{inquiry}$ 并非在 $P_{threshold}$ 处瞬间跳变，而是存在过渡带。修正公

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45, N46, N47

## Claim

海维塞德函数 $H(\cdot)$ 的平滑化修正：实际中 $P_{inquiry}$ 并非在 $P_{threshold}$ 处瞬间跳变，而是存在过渡带。修正公式为 $P_{inquiry}(P_{low}) = P_{base} \cdot \sigma(\kappa (P_{threshold} - P_{low}))$，其中 $\sigma$ 为 Sigmoid 函数，$\kappa$ 为陡峭度参数。需估算 $\kappa$ 的值，使得在 $P_{low} = P_{threshold} \pm 2\%$ 时，咨询率变化不超过 50%，以量化‘断点效应’的实际平滑程度。

## Corrected Claim

海维塞德函数 $H(\cdot)$ 的平滑化修正：实际中 $P_{inquiry}$ 并非在 $P_{threshold}$ 处瞬间跳变，而是存在过渡带。修正公式为 $P_{inquiry}(P_{low}) = P_{base} \cdot \sigma(\kappa (P_{threshold} - P_{low}))$，其中 $\sigma$ 为 Sigmoid 函数，$\kappa$ 为陡峭度参数。需估算 $\kappa$ 的值，使得在 $P_{low} = P_{threshold} \pm 2\%$ 时，咨询率变化不超过 50%，以量化‘断点效应’的实际平滑程度。

## Evidence

先验知识/题面给定，逻辑校验通过：Sigmoid函数在中心点附近近似线性，通过调整陡峭度参数κ可控制过渡带宽度，使得在阈值±2%范围内变化率符合预期，数学逻辑自洽。
