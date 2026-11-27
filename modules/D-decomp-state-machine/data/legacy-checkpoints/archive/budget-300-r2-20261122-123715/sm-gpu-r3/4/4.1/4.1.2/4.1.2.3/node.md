# N294: 基于实测数据的精度-质量映射表构建：将 FP8、INT8 (AWQ)、W4 三种精度的实测 ΔPPL 和任务基准下降率整理为查表结构，明确每种精度对应的质量等级

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

基于实测数据的精度-质量映射表构建：将 FP8、INT8 (AWQ)、W4 三种精度的实测 ΔPPL 和任务基准下降率整理为查表结构，明确每种精度对应的质量等级标签（如 'High-Fidelity', 'Standard', 'Degraded'），用于在最终推荐中根据用户设定的 Quality_Sensitivity 阈值进行筛选。

## Corrected Claim

基于实测数据的精度-质量映射表构建：将 FP8、INT8 (AWQ)、W4 三种精度的实测 ΔPPL 和任务基准下降率整理为查表结构，明确每种精度对应的质量等级标签（如 'High-Fidelity', 'Standard', 'Degraded'），用于在最终推荐中根据用户设定的 Quality_Sensitivity 阈值进行筛选。

## Evidence

先验知识/题面给定，逻辑校验通过
