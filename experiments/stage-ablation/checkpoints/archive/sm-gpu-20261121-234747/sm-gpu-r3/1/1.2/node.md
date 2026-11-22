# N7: 数据中心级GPU候选集筛选：基于单卡显存≥48GB或支持多卡互联的型号（A100 40GB/80GB, H100 80GB, L40S 48GB, MI300X

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

数据中心级GPU候选集筛选：基于单卡显存≥48GB或支持多卡互联的型号（A100 40GB/80GB, H100 80GB, L40S 48GB, MI300X 192GB），需标注NVLink/PCIe带宽对多卡推理的影响系数

## Corrected Claim

数据中心级GPU候选集筛选：基于单卡显存≥48GB或支持多卡互联的型号（A100 40GB/80GB, H100 80GB, L40S 48GB, MI300X 192GB），需标注NVLink/PCIe带宽对多卡推理的影响系数

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

A100 H100 L40S MI300X NVLink bandwidth multi-GPU inference overhead
