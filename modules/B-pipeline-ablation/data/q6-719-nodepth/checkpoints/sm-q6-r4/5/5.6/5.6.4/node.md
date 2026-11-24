# N156: 公有云CDN的实际带宽单价 P_actual = P_base * D_scale = ¥0.25/GB * 0.6 = ¥0.15/GB，用于计算最终带宽成本

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

公有云CDN的实际带宽单价 P_actual = P_base * D_scale = ¥0.25/GB * 0.6 = ¥0.15/GB，用于计算最终带宽成本。

## Corrected Claim

公有云CDN的实际带宽单价 P_actual = P_base * D_scale = ¥0.25/GB * 0.6 = ¥0.15/GB，用于计算最终带宽成本。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点存在严重的冗余性，它们本质上是同一个公式（C_bw = (Traffic * P_actual) / Requests）在不同参数（P_actual, D_scale）下的两次实例化，而非独立的逻辑分支。此外，父节点明确定义为 D_scale=0.6 的情况，但子节点2引入了 D_scale=0.8 的假设场景，超出了父节点定义的范畴，导致完备性检查失败（父节点仅关注特定单价，子节点却扩展到了对比场景）。）
