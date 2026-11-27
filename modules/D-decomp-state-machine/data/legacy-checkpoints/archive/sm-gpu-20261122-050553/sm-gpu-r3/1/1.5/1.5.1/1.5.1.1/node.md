# N160: PCIe 4.0 x16 接口的实际有效带宽受协议开销影响，理论单向 32 GB/s，实际有效带宽约为 28-30 GB/s (扣除 TLP 头尾、流控包等开销

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

PCIe 4.0 x16 接口的实际有效带宽受协议开销影响，理论单向 32 GB/s，实际有效带宽约为 28-30 GB/s (扣除 TLP 头尾、流控包等开销，约 8-12% 损耗)，需参考 PCIe 规范或实测基准 (如 fio/dd 测试) 确定具体值。

## Corrected Claim

PCIe 4.0 x16 接口的理论单向带宽为 32 GB/s，实际有效带宽受协议开销（如 TLP 头尾、流控包等）影响，通常低于理论值，具体数值需参考 PCIe 规范或实测基准确定。

## Evidence

[质询]该陈述包含具体的经验性数值（理论带宽 32 GB/s 和实际损耗 8-12%），属于硬件规格与性能指标，无法仅通过第一性原理严格推导得出具体损耗比例，且当前无可用外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PCIe 4.0 x16 actual effective bandwidth overhead TLP header size
