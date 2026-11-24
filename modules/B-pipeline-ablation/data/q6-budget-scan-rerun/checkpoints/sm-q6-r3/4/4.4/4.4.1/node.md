# N83: 公有云弹性伸缩系数 E_pub 的具体数值：基于峰谷比 R_pg=3，E_pub = (B_peak_pub - B_avg) / B_avg = R_pg -

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

公有云弹性伸缩系数 E_pub 的具体数值：基于峰谷比 R_pg=3，E_pub = (B_peak_pub - B_avg) / B_avg = R_pg - 1 = 2.0。这意味着峰值带宽是平均带宽的 3 倍，弹性空间为 2 倍平均带宽。若平均带宽 26.4 Mbps，则弹性伸缩需额外提供 52.8 Mbps 的瞬时容量。

## Corrected Claim

公有云弹性伸缩系数 E_pub 的具体数值：基于峰谷比 R_pg=3，E_pub = (B_peak_pub - B_avg) / B_avg = R_pg - 1 = 2.0。这意味着峰值带宽是平均带宽的 3 倍，弹性空间为 2 倍平均带宽。若平均带宽 26.4 Mbps，则弹性伸缩需额外提供 52.8 Mbps 的瞬时容量。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（R_pg）下的取值，属于参数枚举而非独立概念，存在高度冗余。此外，父节点明确指定了 R_pg=3 的具体数值和推导，而子节点将其泛化为三个工作点，导致父节点的核心结论（R_pg=3, E_pub=2.0）仅作为子节点之一出现，未体现父节点作为‘具体数值定义’的独立逻辑地位，且缺少对公式本身或前提条件的独立说明，完备性不足。）

## Search Query

CDN elasticity coefficient peak to average ratio
