# N97: 2x RTX 4090 (PCIe) 方案的一次性硬件成本约为 $3,200-$3,800 (基于 N34 价格)，而 A100 80GB PCIe 约为 $1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

2x RTX 4090 (PCIe) 方案的一次性硬件成本约为 $3,200-$3,800 (基于 N34 价格)，而 A100 80GB PCIe 约为 $15,000-$18,000；2x 4090 的 TCO 优势在 1-2 年使用周期内显著，但需考虑 PCIe 通信开销导致的吞吐量损失对单位 token 成本的抵消效应。

## Corrected Claim

2x RTX 4090 (PCIe) 方案的一次性硬件成本约为 $3,200-$3,800 (基于 N34 价格)，而 A100 80GB PCIe 约为 $15,000-$18,000；2x 4090 的 TCO 优势在 1-2 年使用周期内显著，但需考虑 PCIe 通信开销导致的吞吐量损失对单位 token 成本的抵消效应。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡市场价约 $1600-$1900，双卡加主机成本在 $3200-$3800 区间合理；A100 80GB PCIe 市场价约 $15k-$18k 符合历史行情；PCIe 通信瓶颈导致多卡效率低于 NVLink 是已知物理/工程事实，逻辑自洽。
