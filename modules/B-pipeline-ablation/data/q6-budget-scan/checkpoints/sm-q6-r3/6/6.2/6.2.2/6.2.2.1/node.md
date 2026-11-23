# N293: 工作点A（纯长尾兜底）：假设混合策略中仅将10%的长尾流量（月6TB）路由至公有云，且无额外回源惩罚，月带宽成本为 $C_{bw,hybrid,cloud} =

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

工作点A（纯长尾兜底）：假设混合策略中仅将10%的长尾流量（月6TB）路由至公有云，且无额外回源惩罚，月带宽成本为 $C_{bw,hybrid,cloud} = 6 \times 1024 \times 0.24 = 1474.56$ 元/月。

## Corrected Claim

工作点A（纯长尾兜底）：假设混合策略中仅将10%的长尾流量（月6TB）路由至公有云，且无额外回源惩罚，月带宽成本为 $C_{bw,hybrid,cloud} = 6 \times 1024 \times 0.24 = 1474.56$ 元/月。

## Evidence

先验知识/题面给定，逻辑校验通过：6TB * 1024 GB/TB * 0.24 元/GB = 1474.56 元，计算无误且符合成本估算逻辑。
