# N219: 当 $P_{list} < P_{anchor}$ 时，损失厌恶项 $(P_{anchor} - P_{list})^+$ 主导决策，此时 $w_{rel}$ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

当 $P_{list} < P_{anchor}$ 时，损失厌恶项 $(P_{anchor} - P_{list})^+$ 主导决策，此时 $w_{rel}$ 的边际贡献接近 0（$\partial U / \partial w_{rel} \approx 0$）；当 $P_{list} > P_{anchor}$ 时，$w_{rel}$ 成为主要驱动项。临界点 $P_{critical} = P_{anchor}$ 处，效用函数导数不连续，导致卖家定价呈现‘跳跃式’分布，而非连续曲线。

## Corrected Claim

当 $P_{list} < P_{anchor}$ 时，损失厌恶项 $(P_{anchor} - P_{list})^+$ 主导决策，此时 $w_{rel}$ 的边际贡献接近 0（$\partial U / \partial w_{rel} \approx 0$）；当 $P_{list} > P_{anchor}$ 时，$w_{rel}$ 成为主要驱动项。临界点 $P_{critical} = P_{anchor}$ 处，效用函数导数不连续，导致卖家定价呈现‘跳跃式’分布，而非连续曲线。

## Evidence

先验知识/题面给定，逻辑校验通过：基于前景理论（Prospect Theory）的损失厌恶特性，当价格低于锚点时，损失项主导且相对权重项边际贡献趋近于零；在临界点处效用函数导数不连续，导致定价分布出现跳跃，符合行为经济学基本逻辑。
