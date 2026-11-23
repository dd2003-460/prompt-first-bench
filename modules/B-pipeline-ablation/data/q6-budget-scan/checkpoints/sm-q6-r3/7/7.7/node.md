# N129: 95th 带宽计费模式下的等效单价 $P_{95}^{eff} = C_{95} / V_{monthly}$，代入 $B_{95}=0.037 \text{ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

95th 带宽计费模式下的等效单价 $P_{95}^{eff} = C_{95} / V_{monthly}$，代入 $B_{95}=0.037 \text{ Gbps}$ 和 $R_{95}=120 \text{ 元/Gbps/月}$，得 $C_{95} \approx 4.44 \text{ 元/月}$，$P_{95}^{eff} \approx 4.44 / 61440 \text{ GB} \approx 0.00007 \text{ 元/GB}$（注：此估算显示 95th 模式在小带宽下极具优势，但需核实最小起租带宽限制，通常有 10Gbps 起步门槛）。

## Corrected Claim

95th 带宽计费模式下的等效单价 $P_{95}^{eff} = C_{95} / V_{monthly}$，代入 $B_{95}=0.037 \text{ Gbps}$ 和 $R_{95}=120 \text{ 元/Gbps/月}$，得 $C_{95} \approx 4.44 \text{ 元/月}$，$P_{95}^{eff} \approx 4.44 / 61440 \text{ GB} \approx 0.00007 \text{ 元/GB}$（注：此估算显示 95th 模式在小带宽下极具优势，但需核实最小起租带宽限制，通常有 10Gbps 起步门槛）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1处理最小起租门槛下的固定成本（修正父节点中未考虑门槛的错误估算）；子节点2处理超过门槛后的线性增长及与流量计费的临界点；子节点3引入带宽利用率η这一新维度，讨论动态选择策略。三者分别对应“固定成本约束”、“边际成本/临界点分析”和“利用率/动态决策”，无重复且无矛盾。父节点中的初步估算在子节点1中被合理修正，整体覆盖了95th计费模式的关键影响因素。）

## Search Query

CDN 95th percentile billing minimum bandwidth threshold
