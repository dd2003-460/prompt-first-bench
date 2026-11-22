# N487: 2x RTX 4090 方案的 TCO 修正项：除硬件成本 $3,200 外，需计入 PCIe 4.0 x16 插槽带宽瓶颈导致的性能降级因子 (Perform

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N199, N200, N201

## Claim

2x RTX 4090 方案的 TCO 修正项：除硬件成本 $3,200 外，需计入 PCIe 4.0 x16 插槽带宽瓶颈导致的性能降级因子 (Performance_Penalty_Factor = 0.85)，即有效吞吐量需打 85 折；此外，双卡功耗 900W 导致年电力成本 $131-$394 (N113)，3 年 OPEX 约 $393-$1,182，总 TCO 3 年 = $3,200 + $1,000 (均値) ≈ $4,200，每美元有效吞吐 = 36.6 * 0.85 / 4200 ≈ 0.0074 tokens/$/s。

## Corrected Claim

2x RTX 4090 方案的 TCO 修正项：除硬件成本 $3,200 外，需计入双卡功耗 900W 导致的年电力成本 $131-$394 (N113)，3 年 OPEX 约 $393-$1,182，总 TCO 3 年 ≈ $4,200。关于 PCIe 4.0 x16 插槽带宽瓶颈导致的性能降级因子 (Performance_Penalty_Factor = 0.85) 及由此计算的每美元有效吞吐 (≈ 0.0074 tokens/$/s)，该因子为特定负载下的经验估计值，非通用物理常数，实际性能需根据具体模型和通信开销实测确定。

## Evidence

[质询]PCIe 4.0 x16 插槽带宽瓶颈导致 0.85 的性能降级因子（Performance_Penalty_Factor）缺乏普遍适用的物理或工程依据，属于高度依赖具体工作负载（如模型大小、Batch Size、通信模式）的经验参数，且 0.85 这一具体数值在通用场景下并非标准共识，存在口径混淆或过度简化的风险。 | 先验知识/题面给定，逻辑校验通过（算术运算正确：36.6*0.85/4200≈0.0074），但关键经验参数（0.85 惩罚因子）缺乏来源支持且非第一性原理可推导，依据经验事实排除条款降级。

## Search Query

dual GPU TCO calculation electricity cost performance penalty
