# N581: 双 RTX 4090 在全塔机箱（如 Lian Li O11D EVO）中的空间冲突分析：两张 4090 均为三槽或双槽设计，若主板 PCIe 插槽间距不足，第

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N242

## Claim

双 RTX 4090 在全塔机箱（如 Lian Li O11D EVO）中的空间冲突分析：两张 4090 均为三槽或双槽设计，若主板 PCIe 插槽间距不足，第二张卡可能无法安装或导致气流短路；需验证主板（如 ASUS ProArt X670E-CREATOR）的 PCIe x16 插槽物理间距是否支持双 4090 安装，否则需更换主板或采用垂直支架（额外成本 $50）。

## Corrected Claim

双 RTX 4090 在全塔机箱（如 Lian Li O11D EVO）中安装时，需验证主板 PCIe x16 插槽物理间距是否足够以容纳两张卡（通常为三槽或双槽设计），否则可能导致安装冲突或气流问题；若间距不足，需更换主板或采用垂直支架（具体成本需另行核实）。

## Evidence

[质询]该陈述包含具体的硬件兼容性经验事实（如特定主板 ASUS ProArt X670E-CREATOR 的 PCIe 插槽间距是否支持双 4090，以及垂直支架的具体成本 $50），这些属于经验规格而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

ASUS ProArt X670E-CREATOR dual RTX 4090 clearance
