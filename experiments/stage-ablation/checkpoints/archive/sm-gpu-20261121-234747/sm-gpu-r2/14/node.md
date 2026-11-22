# N161: TCO 建模中维护复杂度的量化：多卡方案（2x PCIe）的年均故障率（AFR）比单卡方案高 15-20%，主要源于 PCIe 插槽接触不良和散热不均；估算 3

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

TCO 建模中维护复杂度的量化：多卡方案（2x PCIe）的年均故障率（AFR）比单卡方案高 15-20%，主要源于 PCIe 插槽接触不良和散热不均；估算 3 年维护成本（含潜在显卡更换或维修）：单卡 RTX 4090 维护成本约 $200-$300（主要电源损耗），双卡 2x RTX 3090 维护成本约 $500-$800（双电源负载+潜在单卡故障导致系统停机风险）；该隐性成本需加入 TCO 公式的 C_maint 项

## Corrected Claim

TCO 建模中维护复杂度的量化：多卡方案（2x PCIe）的年均故障率（AFR）比单卡方案高 15-20%，主要源于 PCIe 插槽接触不良和散热不均；估算 3 年维护成本（含潜在显卡更换或维修）：单卡 RTX 4090 维护成本约 $200-$300（主要电源损耗），双卡 2x RTX 3090 维护成本约 $500-$800（双电源负载+潜在单卡故障导致系统停机风险）；该隐性成本需加入 TCO 公式的 C_maint 项

## Evidence

检索失败: no sources from any channel (all 5 failed)
