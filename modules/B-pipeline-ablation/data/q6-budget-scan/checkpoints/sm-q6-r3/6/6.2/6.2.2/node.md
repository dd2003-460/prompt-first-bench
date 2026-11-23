# N110: 混合策略公有云部分月带宽成本 $C_{bw,hybrid,cloud}$：长尾 10% 流量（0.2 TB/日）走公有云，月流量 6 TB，流量计费成本 $C_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

混合策略公有云部分月带宽成本 $C_{bw,hybrid,cloud}$：长尾 10% 流量（0.2 TB/日）走公有云，月流量 6 TB，流量计费成本 $C_{bw,hybrid,cloud} = 6 \times 1024 \times 0.24 \approx 1475$ 元/月。

## Corrected Claim

混合策略公有云部分月带宽成本 $C_{bw,hybrid,cloud}$：长尾 10% 流量（0.2 TB/日）走公有云，月流量 6 TB，流量计费成本 $C_{bw,hybrid,cloud} = 6 \times 1024 \times 0.24 \approx 1475$ 元/月。

## Evidence

父节点级核验未通过：非正交（子节点A和B在基础流量计费成本上存在包含关系（B=A+额外项），导致逻辑重叠而非正交；工作点C的计费模式（带宽峰值）与A/B（流量计费）是互斥的计费策略，虽正交但C中计算出的12元/月远低于A的1475元/月，暗示C可能忽略了最低消费或固定接入费，导致结论矛盾。）
