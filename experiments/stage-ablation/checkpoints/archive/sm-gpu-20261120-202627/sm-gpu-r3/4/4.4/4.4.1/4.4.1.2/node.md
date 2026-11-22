# N360: 数据中心 NVSwitch 模组的集成成本结构：A100/H100 SXM 服务器中，NVSwitch 通常已集成在基板中，无额外 CapEx；若需独立 NVS

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

数据中心 NVSwitch 模组的集成成本结构：A100/H100 SXM 服务器中，NVSwitch 通常已集成在基板中，无额外 CapEx；若需独立 NVSwitch 卡（如 DGX 系列），则单卡成本约为 $2000-$4000，但此类方案仅适用于 8 卡以上集群，对于 2 卡方案无适用性，故在 2 卡对比中 NVSwitch 成本项为 $0。

## Corrected Claim

在 A100/H100 SXM 服务器中，NVSwitch 通常集成在基板中，其成本已包含在基板或系统整体价格中，无单独列出的 NVSwitch 硬件 CapEx；独立 NVSwitch 卡方案较少见且成本高，不适用于 2 卡方案，故在 2 卡对比中 NVSwitch 的独立硬件成本项可视为 $0，但需注意基板成本可能因集成 NVSwitch 而高于无 NVSwitch 版本。

## Evidence

[质询]NVSwitch 并非完全“无额外 CapEx”，它通常作为基板的一部分存在，但会显著增加基板（Baseboard）的成本，且 DGX 系列中 NVSwitch 往往是独立模块或高集成度组件，其成本分摊逻辑复杂，简单归为 $0 或仅针对独立卡定价可能忽略基板溢价。 | 先验知识/题面给定，逻辑校验通过；但 NVSwitch 成本通常隐含在基板或系统整体溢价中，而非绝对为零，且 DGX 系列 NVSwitch 集成方式多样，具体成本结构需视具体型号而定，故降级为定性表述。
