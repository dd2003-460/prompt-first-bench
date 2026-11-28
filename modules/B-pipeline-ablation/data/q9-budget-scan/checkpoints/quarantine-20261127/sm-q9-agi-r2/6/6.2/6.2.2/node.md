# N98: MTP×4 投机解码在 V100 上的实际接受率 Acceptance_Rate 受限于模型置信度分布，实测平均值约为 0.65-0.75，导致有效加速比 Sp

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N29

## Claim

MTP×4 投机解码在 V100 上的实际接受率 Acceptance_Rate 受限于模型置信度分布，实测平均值约为 0.65-0.75，导致有效加速比 Speedup_eff = 1 + (Acceptance_Rate * Draft_Len) / (1 + Verify_Overhead)，其中 Verify_Overhead 约为 0.2（即验证步骤耗时为生成步骤的 1.2 倍），最终 Speedup_eff 约为 1.8-2.1x，远低于理论 4x。

## Corrected Claim

MTP×4 投机解码在 V100 上的实际接受率受限于模型置信度分布，通常低于理论最大值，导致有效加速比显著低于理论 4x，具体数值取决于模型与任务特性。

## Evidence

[质询]该陈述包含具体的经验参数（V100硬件上的接受率0.65-0.75、验证开销0.2、最终加速比1.8-2.1x），这些数值高度依赖于具体的模型架构、数据集分布及实现细节，并非普适的物理或数学常数，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值量级）

## Search Query

speculative decoding acceptance rate V100 Qwen actual speedup ratio measured
