# N361: 成本折算中的 '1.805' 若为经验系数，应分解为：k_cost = (P_physical / P_logical_effective)，其中 P_logi

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N160

## Claim

成本折算中的 '1.805' 若为经验系数，应分解为：k_cost = (P_physical / P_logical_effective)，其中 P_logical_effective 需扣除 RAID 冗余、FS 开销、以及因碎片化导致的实际可用空间损失 (Fragmentation Loss, ~5-10%)，修正后 k_cost ≈ 1.017 * 1.05 * 1.07 ≈ 1.15，与 1.805 差距巨大，暗示 N160 的前提假设可能有误。

## Corrected Claim

在假设RAID冗余、FS开销及碎片化损失分别为1.7%、5%、7%的特定简化模型下，计算得出的成本系数约为1.15，这与1.805存在显著差异，提示原系数可能基于不同的存储架构假设或包含未计入的其他成本项。

## Evidence

[质询]该陈述将复杂的存储成本折算简化为三个固定系数的乘积（1.017*1.05*1.07），忽略了RAID级别差异（如RAID 5 vs RAID 10）、文件系统类型及具体硬件配置对有效容量和成本的巨大影响，导致推导出的1.15缺乏普适性，无法确凿证明1.805一定有误，仅能说明在特定假设下两者不一致。 | 先验知识/题面给定，逻辑校验通过：算术运算正确（1.017*1.05*1.07≈1.149），但作为经验事实的通用结论，其前提假设过于简化，缺乏外部来源支持以排除其他合理配置导致高成本系数的可能性。

## Search Query

storage cost per effective TB vs physical TB conversion factor
