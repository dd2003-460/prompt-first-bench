# N527: N172 工作点下，将自建存储从 100TB 提升至 150TB 的硬件增量成本 ΔC_hw_upgrade = (150TB - 100TB) * C_sto

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N172

## Claim

N172 工作点下，将自建存储从 100TB 提升至 150TB 的硬件增量成本 ΔC_hw_upgrade = (150TB - 100TB) * C_storage_unit * 12 / 3年折旧系数，结合 N69 SSD 成本，月均摊销增量约 ¥40,000，用于抵消命中率劣势。

## Corrected Claim

N172 工作点下，将自建存储从 100TB 提升至 150TB 的硬件增量成本可通过公式 ΔC_hw_upgrade = (150TB - 100TB) * C_storage_unit * 12 / 3年折旧系数 计算，结合 N69 SSD 成本进行月均摊销，用于抵消命中率劣势。

## Evidence

[质询]该陈述包含具体的经验性数值（月均摊销增量约 ¥40,000）和特定的成本参数（C_storage_unit），这些属于经验事实而非第一性原理可推导的数学或逻辑结论。虽然公式结构在逻辑上自洽，但具体数值缺乏来源支持，且不同硬件配置下 SSD 单价差异巨大，无法仅凭逻辑校验确认该特定金额的正确性。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值为经验参数，无法仅凭逻辑推导验证其准确性，故降级）
