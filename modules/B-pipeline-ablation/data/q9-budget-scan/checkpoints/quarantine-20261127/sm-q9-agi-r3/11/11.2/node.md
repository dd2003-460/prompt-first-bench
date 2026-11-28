# N115: 强制集成的SciPy/Statsmodels硬校验流程定义：输入为原始数据矩阵 X(n×d)，执行步骤包括1. Shapiro-Wilk正态性检验（α=0.05

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

强制集成的SciPy/Statsmodels硬校验流程定义：输入为原始数据矩阵 X(n×d)，执行步骤包括1. Shapiro-Wilk正态性检验（α=0.05），2. 根据正态性选择t-test或Mann-Whitney U检验，3. 计算效应量Cohen's d，4. 若p<0.05且d>0.2则标记为‘稳健显著’，否则标记为‘不显著或弱效应’，该流程在Python沙箱中执行耗时<200ms。

## Corrected Claim

强制集成的SciPy/Statsmodels硬校验流程定义：输入为原始数据矩阵 X(n×d)，执行步骤包括1. Shapiro-Wilk正态性检验（α=0.05），2. 根据正态性选择t-test或Mann-Whitney U检验，3. 计算效应量Cohen's d，4. 若p<0.05且d>0.2则标记为‘稳健显著’，否则标记为‘不显著或弱效应’，该流程在Python沙箱中执行耗时<200ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

automated statistical testing pipeline SciPy Statsmodels small sample robustness protocol
