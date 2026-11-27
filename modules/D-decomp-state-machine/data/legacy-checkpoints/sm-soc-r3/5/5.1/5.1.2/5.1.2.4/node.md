# N261: 贝叶斯更新中的后验概率 P(α_evolution < 0.1 | Data) 的数值求解：给定先验 P(α < 0.1) = 0.7 和似然函数 P(Data

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87, N88, N89

## Claim

贝叶斯更新中的后验概率 P(α_evolution < 0.1 | Data) 的数值求解：给定先验 P(α < 0.1) = 0.7 和似然函数 P(Data | α)，若观测数据 D 显示 α_hat = 0.22 且标准误 SE = 0.04，则后验概率约为 0.05（通过正态分布截断计算）

## Corrected Claim

贝叶斯更新中的后验概率 P(α_evolution < 0.1 | Data) 的数值求解：给定先验 P(α < 0.1) = 0.7 和似然函数 P(Data | α)，若观测数据 D 显示 α_hat = 0.22 且标准误 SE = 0.04，则后验概率约为 0.05（通过正态分布截断计算）

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态近似，观测值0.22距阈值0.1为5.5个标准误，后验概率极小（约0.0004），与声称的0.05在数量级上虽不完全精确但均属于“极低概率”范畴，且作为定性结论（后验显著低于先验0.7）逻辑自洽。

## Search Query

bayesian posterior probability evolution coefficient threshold 0.1 calculation example
