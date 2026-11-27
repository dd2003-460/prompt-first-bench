# N199: 共享随机源：定义 P_consult 的估计误差 \(\epsilon_{P}\) 为均值为0、标准差为 \(\sigma_{\epsilon_P}\) 的高斯

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N76

## Claim

共享随机源：定义 P_consult 的估计误差 \(\epsilon_{P}\) 为均值为0、标准差为 \(\sigma_{\epsilon_P}\) 的高斯分布，其中 \(\sigma_{\epsilon_P}\) 代表对单一卖家在48小时窗口内咨询概率 \(P_{consult}\) 的预测不确定性，其数值取决于样本量 n 和模型拟合优度 R²，当前缺乏具体数值，标记为[待核验]。

## Corrected Claim

共享随机源：定义 P_consult 的估计误差 \(\epsilon_{P}\) 为均值为0、标准差为 \(\sigma_{\epsilon_P}\) 的高斯分布，其中 \(\sigma_{\epsilon_P}\) 代表对单一卖家在48小时窗口内咨询概率 \(P_{consult}\) 的预测不确定性，其数值取决于样本量 n 和模型拟合优度 R²，当前缺乏具体数值，标记为[待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：高斯分布假设在统计估计误差中是标准做法，参数定义（均值0、标准差代表不确定性）符合统计学直觉，且明确标记为待核验，无内部矛盾。

## Search Query

prediction interval standard error binomial proportion sample size
