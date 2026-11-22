# N327: 修正 N112 的功耗假设：AMD Radeon PRO W7900 在 LLM 推理（Decode 阶段显存带宽受限）下的平均功耗并非 TDP 上限 300W

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

修正 N112 的功耗假设：AMD Radeon PRO W7900 在 LLM 推理（Decode 阶段显存带宽受限）下的平均功耗并非 TDP 上限 300W，而是约为 220W-250W（基于 GDDR6 高负载典型功耗曲线），取保守值 240W 用于 TCO 计算。

## Corrected Claim

AMD Radeon PRO W7900 在 LLM 推理（Decode 阶段显存带宽受限）下的平均功耗通常低于 TDP 上限 300W，具体数值需实测确认，此处暂取保守估计值 240W 用于 TCO 计算。

## Evidence

[质询]该陈述包含具体的硬件功耗数值（220W-250W）和特定负载下的功耗曲线假设，属于经验事实。由于缺乏外部来源支持，无法验证该具体数值范围是否准确，且不同批次或驱动版本下实际功耗可能存在波动，仅凭逻辑自洽不足以确认为精确事实。 | 经验事实，逻辑自洽（Decode阶段带宽受限导致GPU计算单元空闲，功耗低于TDP上限符合物理直觉），但缺来源支持。

## Search Query

AMD Radeon PRO W7900 LLM inference power consumption average watts
