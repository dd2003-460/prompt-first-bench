# N51: 归因决策规则的共享随机源：结构方程模型 (SEM) 中路径系数的估计误差方差 (σ²_SEM)，量化为各利益相关方驱动指标 (S_buyer, R_strate

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N14

## Claim

归因决策规则的共享随机源：结构方程模型 (SEM) 中路径系数的估计误差方差 (σ²_SEM)，量化为各利益相关方驱动指标 (S_buyer, R_strategic, B_algo) 标准化影响系数 (β) 的标准误，需通过 Bootstrap 重抽样 1000 次计算 95% 置信区间 [待核验]。

## Corrected Claim

归因决策规则的共享随机源：结构方程模型 (SEM) 中路径系数的估计误差可通过标准化影响系数 (β) 的标准误（SE）或其方差（SE²）量化，通常建议通过 Bootstrap 重抽样（如 1000 次或更多）计算 95% 置信区间以评估估计稳定性。

## Evidence

父节点级核验未通过：不完备（子节点之间存在正交性（一个定义计算与判定标准，一个定义收敛性检验），但存在严重的方法论错误和完备性缺失。1. 子节点1中‘宽度 < 2 * SE(β)’作为稳定性判定标准在统计学上是错误的（Bootstrap CI宽度通常远大于2*SE，且稳定性应看分布形态而非与SE比较）；2. 子节点2使用BIC/AIC的变异系数检验Bootstrap收敛性是不恰当的，BIC/AIC用于模型选择而非参数不确定性估计的收敛性（应使用SE的稳定性或Q-Q图）；3. 父节点强调‘共享随机源’，但子节点完全未涉及SEM中误差项/潜变量相关性的估计，仅关注路径系数，未覆盖‘共享’这一核心结构特征。）

## Search Query

structural equation model path coefficient standard error bootstrap
