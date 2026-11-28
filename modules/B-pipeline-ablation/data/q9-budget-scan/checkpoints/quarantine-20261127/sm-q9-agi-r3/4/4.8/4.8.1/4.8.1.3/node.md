# N249: ROC 曲线下面积 (AUC) 用于量化阈值选择的优劣；在科研事实核查场景中，目标 AUC > 0.90；若 AUC < 0.85，表明单一 Logit 阈值不

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

ROC 曲线下面积 (AUC) 用于量化阈值选择的优劣；在科研事实核查场景中，目标 AUC > 0.90；若 AUC < 0.85，表明单一 Logit 阈值不足以区分幻觉，需引入多特征融合（如 Entropy + HR）。

## Corrected Claim

ROC 曲线下面积 (AUC) 用于量化阈值选择的优劣；在科研事实核查场景中，通常追求较高的 AUC（如 > 0.90）；若 AUC 较低（如 < 0.85），往往表明单一 Logit 阈值区分能力有限，可能需要引入多特征融合（如 Entropy + HR）以提升性能。

## Evidence

[质询]将 AUC < 0.85 作为必须引入多特征融合的硬性阈值缺乏普适性标准，不同数据集和任务难度下该临界值可能波动，属于经验性设定而非绝对真理。 | 先验知识/题面给定，逻辑校验通过；但具体阈值（0.90/0.85）及特定特征组合建议属经验性工程实践，缺乏通用理论强制约束，故降级为定性表述。

## Search Query

ROC AUC threshold selection binary classification LLM confidence calibration
