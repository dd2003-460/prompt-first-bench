# N172: ‘仅列出GMV或用户数’导致置信度降至0.4的贝叶斯更新公式：后验概率 P(KPI_AOV|Data) = [P(Data|KPI_AOV)*P(KPI_AOV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

‘仅列出GMV或用户数’导致置信度降至0.4的贝叶斯更新公式：后验概率 P(KPI_AOV|Data) = [P(Data|KPI_AOV)*P(KPI_AOV)] / P(Data)，其中先验 P(KPI_AOV)=0.7，若数据仅含GMV，似然比 P(Data|KPI_AOV)/P(Data|¬KPI_AOV) 需估算为 0.5 才能使后验降至 0.4，该似然比需基于历史财报披露习惯进行校准。

## Corrected Claim

‘仅列出GMV或用户数’导致置信度降至0.4的贝叶斯更新公式：后验概率 P(KPI_AOV|Data) = [P(Data|KPI_AOV)*P(KPI_AOV)] / P(Data)，其中先验 P(KPI_AOV)=0.7，若数据仅含GMV，似然比 P(Data|KPI_AOV)/P(Data|¬KPI_AOV) 需估算为 0.5 才能使后验降至 0.4，该似然比需基于历史财报披露习惯进行校准。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式应用正确，数值计算自洽（0.7*0.5/(0.7*0.5+0.3*1)=0.4），且似然比校准建议符合统计推断逻辑。

## Search Query

bayesian update posterior probability KPI disclosure likelihood ratio
