# N57: 带宽利用率修正因子：实际 Throughput = Theoretical_Throughput × η，其中 η (效率因子) 通常在 0.6-0.8 之间，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

带宽利用率修正因子：实际 Throughput = Theoretical_Throughput × η，其中 η (效率因子) 通常在 0.6-0.8 之间，受内存访问模式、PCIe 延迟及 GPU 调度影响；对于 HBM 高带宽卡，η 接近 0.8，对于 GDDR6X 卡，η 约为 0.6-0.7。

## Corrected Claim

带宽利用率修正因子：实际 Throughput = Theoretical_Throughput × η，其中 η (效率因子) 通常在 0.6-0.8 之间，受内存访问模式、PCIe 延迟及 GPU 调度影响；对于 HBM 高带宽卡，η 接近 0.8，对于 GDDR6X 卡，η 约为 0.6-0.7。

## Evidence

先验知识/题面给定，逻辑校验通过
