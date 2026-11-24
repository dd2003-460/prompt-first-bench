# N672: RAID-5 重建期间的 I/O 性能降级成本量化：重建期间有效读带宽降至 50%-70%（因校验计算开销），导致温数据扫描时间延长 ΔT_scan = T_s

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N232

## Claim

RAID-5 重建期间的 I/O 性能降级成本量化：重建期间有效读带宽降至 50%-70%（因校验计算开销），导致温数据扫描时间延长 ΔT_scan = T_scan_normal * (1/Ratio_bw - 1)，进而增加集群机会成本 C_opportunity = ΔT_scan * ¥5000/h。

## Corrected Claim

RAID-5 重建期间因校验计算开销会导致有效读带宽显著下降（具体幅度取决于硬件与负载，通常可能在50%-70%区间波动），从而延长温数据扫描时间 ΔT_scan = T_scan_normal * (1/Ratio_bw - 1)。若单位时间机会成本为 C_rate，则额外机会成本 C_opportunity = ΔT_scan * C_rate。

## Evidence

[质询]数值量级与具体参数缺乏普适性依据：RAID-5重建期间的读带宽降级比例（50%-70%）高度依赖于硬件配置（CPU算力、磁盘IOPS、条带大小）及负载特征，并非固定物理常数；此外，¥5000/h的机会成本是特定商业场景下的假设值，非通用工程标准。 | 先验知识/题面给定，逻辑校验通过：公式推导在数学上自洽，但具体数值（带宽比、成本率）属于经验参数，在无外部来源支持且存在显著变量依赖的情况下，不能视为绝对真理，故降级为定性/条件性表述。
