# N366: 工作点 B（中性价比/PCIe 瓶颈）：使用 2× RTX 4090 PCIe 连接，Throughput_PCIe = 35 tokens/s。OpEx_pe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115

## Claim

工作点 B（中性价比/PCIe 瓶颈）：使用 2× RTX 4090 PCIe 连接，Throughput_PCIe = 35 tokens/s。OpEx_per_hour = 2×450W×0.7×$0.12/kWh ≈ $0.0756/h。CapEx_annualized = $3350/3yr ≈ $1117/yr。计算该工作点因带宽瓶颈导致的年化隐性成本增加，并与工作点 A 的总 TCO 对比，判断 PCIe 是否导致性价比反转。

## Corrected Claim

工作点 B（中性价比/PCIe 瓶颈）：使用 2× RTX 4090 PCIe 连接，Throughput_PCIe = 35 tokens/s。OpEx_per_hour = 2×450W×0.7×$0.12/kWh ≈ $0.0756/h。CapEx_annualized = $3350/3yr ≈ $1117/yr。计算该工作点因带宽瓶颈导致的年化隐性成本增加，并与工作点 A 的总 TCO 对比，判断 PCIe 是否导致性价比反转。

## Evidence

先验知识/题面给定，逻辑校验通过：OpEx计算 (2*450*0.7*0.12=75.6, 75.6/1000=0.0756) 正确；CapEx年化 (3350/3≈1117) 正确；PCIe带宽瓶颈导致吞吐下降进而增加单位Token隐性成本的逻辑自洽。
