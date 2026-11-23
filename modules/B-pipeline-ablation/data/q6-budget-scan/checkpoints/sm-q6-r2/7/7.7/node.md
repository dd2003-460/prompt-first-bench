# N129: 95th 带宽计费模式下的等效单价 $P_{95}^{eff} = C_{95} / V_{monthly}$，代入 $B_{95}=0.037 \text{ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

95th 带宽计费模式下的等效单价 $P_{95}^{eff} = C_{95} / V_{monthly}$，代入 $B_{95}=0.037 \text{ Gbps}$ 和 $R_{95}=120 \text{ 元/Gbps/月}$，得 $C_{95} \approx 4.44 \text{ 元/月}$，$P_{95}^{eff} \approx 4.44 / 61440 \text{ GB} \approx 0.00007 \text{ 元/GB}$（注：此估算显示 95th 模式在小带宽下极具优势，但需核实最小起租带宽限制，通常有 10Gbps 起步门槛）。

## Corrected Claim

95th 带宽计费模式下的等效单价 $P_{95}^{eff} = C_{95} / V_{monthly}$，代入 $B_{95}=0.037 \text{ Gbps}$ 和 $R_{95}=120 \text{ 元/Gbps/月}$，得 $C_{95} \approx 4.44 \text{ 元/月}$，$P_{95}^{eff} \approx 4.44 / 61440 \text{ GB} \approx 0.00007 \text{ 元/GB}$（注：此估算显示 95th 模式在小带宽下极具优势，但需核实最小起租带宽限制，通常有 10Gbps 起步门槛）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 $0.037 \times 120 = 4.44$ 及 $4.44 / 61440 \approx 0.000072$ 均正确，量纲与数值量级合理。

## Search Query

CDN 95th percentile billing minimum bandwidth threshold
