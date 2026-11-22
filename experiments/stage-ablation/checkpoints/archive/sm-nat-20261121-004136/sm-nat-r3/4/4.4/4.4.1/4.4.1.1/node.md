# N139: 验证更新独立性假设：在 CDN 场景下，对象更新概率通常与对象大小无显著相关性（即 P(Update|Size) ≈ P(Update)），因此 E[Size 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

验证更新独立性假设：在 CDN 场景下，对象更新概率通常与对象大小无显著相关性（即 P(Update|Size) ≈ P(Update)），因此 E[Size | Updated] = E[Size]。若存在微小偏差（如大文件更新更频繁），需引入修正系数 κ_update_size，典型值 κ ∈ [0.9, 1.1] [待核验]。

## Corrected Claim

在 CDN 场景下，对象更新概率通常与对象大小无显著相关性，因此 E[Size | Updated] ≈ E[Size]。若存在偏差，需引入修正系数 κ_update_size，其具体数值需根据实际负载特征进行校准。

## Evidence

[质询]该陈述包含具体的经验性数值范围（κ ∈ [0.9, 1.1]）和统计假设（P(Update|Size) ≈ P(Update)），这些属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏外部来源支持的情况下，无法确认该特定数值范围的准确性或普遍适用性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

CDN object update frequency correlation with file size
