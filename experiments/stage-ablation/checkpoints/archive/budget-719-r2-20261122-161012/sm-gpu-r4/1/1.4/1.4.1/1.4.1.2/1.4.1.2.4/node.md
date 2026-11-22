# N387: 4x RTX 4090 配置在物理层面需要至少 4 个 PCIe x16 插槽且间距至少 2 槽位，主流消费级主板 (Z790/X670) 通常仅提供 1-2 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160, N161, N162

## Claim

4x RTX 4090 配置在物理层面需要至少 4 个 PCIe x16 插槽且间距至少 2 槽位，主流消费级主板 (Z790/X670) 通常仅提供 1-2 个全速 x16 槽，其余为 x4/x8 或通过 M.2 复用，导致带宽瓶颈或物理空间冲突，需专用 HPC 背板 (如 NVIDIA HGX 架构或定制背板) 才能实现全速互联。

## Corrected Claim

4x RTX 4090 配置在物理层面需要至少 4 个 PCIe x16 插槽且间距至少 2 槽位，主流消费级主板 (Z790/X670) 通常仅提供 1-2 个全速 x16 槽，其余为 x4/x8 或通过 M.2 复用，导致带宽瓶颈或物理空间冲突，需专用 HPC 背板 (如 NVIDIA HGX 架构或定制背板) 才能实现全速互联。

## Evidence

先验知识/题面给定，逻辑校验通过：消费级主板物理布局与PCIe通道分配确实无法支持4张全速x16显卡，需HPC背板或专用服务器主板。

## Search Query

4x RTX 4090 motherboard PCIe slot spacing physical limitation
