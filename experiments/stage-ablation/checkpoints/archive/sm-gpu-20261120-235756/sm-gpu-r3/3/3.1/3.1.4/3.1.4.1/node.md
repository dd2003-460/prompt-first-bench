# N222: 2×RTX 4090 方案的硬件购置成本为 $5,000-$7,550，计算公式为：2 × (单卡市场价 $2,500-$3,775) + NVLink Bri

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67, N68, N69

## Claim

2×RTX 4090 方案的硬件购置成本为 $5,000-$7,550，计算公式为：2 × (单卡市场价 $2,500-$3,775) + NVLink Bridge 成本 $0 (Ada 架构无原生 NVLink，仅支持 PCIe 互联)。

## Corrected Claim

2×RTX 4090 方案的硬件购置成本为 $5,000-$7,550，计算公式为：2 × (单卡市场价 $2,500-$3,775) + NVLink Bridge 成本 $0 (Ada 架构无原生 NVLink，仅支持 PCIe 互联)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡市场价约 $2,500-$3,775 符合市场常识，2 卡总价计算正确；Ada 架构（RTX 40 系列）确实取消了 NVLink 支持，仅通过 PCIe 互联，因此 NVLink Bridge 成本为 $0 符合技术事实。
