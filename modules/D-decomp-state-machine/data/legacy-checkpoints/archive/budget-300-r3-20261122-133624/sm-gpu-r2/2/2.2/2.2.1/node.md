# N70: 多卡 INT8 方案中，C_overhead 的具体构成包括：支持 2 路 PCIe 4.0 x16 的 E-ATX 主板（如 ASUS Pro WS WRX8

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17, N18, N19

## Claim

多卡 INT8 方案中，C_overhead 的具体构成包括：支持 2 路 PCIe 4.0 x16 的 E-ATX 主板（如 ASUS Pro WS WRX80E-SAGE SE，价格约 $800-$1000）、双路冗余电源（2000W+，价格约 $200-$300）、以及因空间/散热需求增加的机箱与风扇成本（约 $100-$200），合计 C_overhead ≈ $1100-$1500，验证了比单卡方案高 20-30% 的定性结论（单卡基础平台约 $500-$700）。

## Corrected Claim

多卡 INT8 方案中，C_overhead 的具体构成包括支持多路 PCIe 的高性能主板、双路冗余电源（2000W+）以及增加的机箱与散热成本。根据典型配置估算，C_overhead 约为 $1100-$1500，这通常比单卡基础平台（约 $500-$700）高出 50%-100%，而非 20-30%。

## Evidence

[质询]具体硬件型号（ASUS Pro WS WRX80E-SAGE SE）及其价格区间属于经验事实，且该主板通常用于AMD Threadripper平台，是否适用于通用多卡INT8方案（如NVIDIA GPU集群）存在适用性疑问；此外，$1100-$1500的总开销相对于$500-$700的单卡基础平台，增幅约为57%-100%，与陈述中声称的'高20-30%'存在显著数值矛盾。 | 来源不可用。逻辑校验发现内部数值矛盾：计算得出的成本增幅（~60-100%）与陈述结论（20-30%）不符，且具体硬件参数为经验事实，缺乏来源支持。

## Search Query

ASUS Pro WS WRX80E-SAGE SE price dual PCIe 4.0 x16 2000W PSU cost 2024
