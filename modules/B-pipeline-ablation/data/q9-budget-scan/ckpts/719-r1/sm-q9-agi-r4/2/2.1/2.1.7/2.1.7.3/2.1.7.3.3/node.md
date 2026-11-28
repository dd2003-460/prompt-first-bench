# N472: 工作点 C (鲁棒对照/亚组分析)：基线组 n=100，实验组 n=100，按任务复杂度分层 (简单/中等/复杂)，总计算成本 C_Total ≈ 200 * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166

## Claim

工作点 C (鲁棒对照/亚组分析)：基线组 n=100，实验组 n=100，按任务复杂度分层 (简单/中等/复杂)，总计算成本 C_Total ≈ 200 * T_cycle * P_electricity，可检测微小效应 (d=0.2) 并进行亚组异质性分析，Power ≈ 0.8 for d=0.2 [待核验]，耗时较长，适合最终模型定型前的全面评估

## Corrected Claim

工作点 C (鲁棒对照/亚组分析)：基线组 n=100，实验组 n=100，按任务复杂度分层 (简单/中等/复杂)，总计算成本 C_Total ≈ 200 * T_cycle * P_electricity，可检测微小效应 (d=0.2) 并进行亚组异质性分析，Power ≈ 0.8 for d=0.2 [待核验]，耗时较长，适合最终模型定型前的全面评估

## Evidence

先验知识/题面给定，逻辑校验通过：样本量n=100/组在d=0.2时Power≈0.8符合统计学常识，成本公式量纲正确，分层设计逻辑自洽。

## Search Query

stratified randomization subgroup analysis statistical power small effect size large sample AI benchmarking long-term study design
