# N428: H100 SXM 的 700W TDP 是 GPU 芯片本身的功耗，但 SXM 模块还包括 HBM3 内存和互联芯片的功耗，实际 SXM 模块功耗通常为 700

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N177

## Claim

H100 SXM 的 700W TDP 是 GPU 芯片本身的功耗，但 SXM 模块还包括 HBM3 内存和互联芯片的功耗，实际 SXM 模块功耗通常为 700W；然而，节点总功耗还需考虑 NVLink 交换芯片和 PCIe 交换芯片的额外功耗（约 50-100W），因此 1200W 的总功耗估算偏保守，实际可能达到 1250-1300W，需调整电源冗余系数。

## Corrected Claim

H100 SXM 的 700W TDP 通常指 GPU 芯片功耗，但 SXM 模块实际功耗可能更高；节点总功耗需考虑 NVLink 和 PCIe 交换芯片等额外功耗，具体数值需参考官方规格书或实测数据，1200W 估算可能偏保守。

## Evidence

[质询]该陈述包含具体的工程经验数值（如NVLink/PCIe交换芯片额外功耗50-100W，总功耗1250-1300W），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 SXM module power consumption NVLink switch power overhead total node power
