# N51: 归因决策规则的共享随机源：结构方程模型 (SEM) 中路径系数的估计误差方差 (σ²_SEM)，量化为各利益相关方驱动指标 (S_buyer, R_strate

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

归因决策规则的共享随机源：结构方程模型 (SEM) 中路径系数的估计误差方差 (σ²_SEM)，量化为各利益相关方驱动指标 (S_buyer, R_strategic, B_algo) 标准化影响系数 (β) 的标准误，需通过 Bootstrap 重抽样 1000 次计算 95% 置信区间 [待核验]。

## Corrected Claim

归因决策规则的共享随机源：结构方程模型 (SEM) 中路径系数的估计误差可通过标准化影响系数 (β) 的标准误（SE）或其方差（SE²）量化，通常建议通过 Bootstrap 重抽样（如 1000 次或更多）计算 95% 置信区间以评估估计稳定性。

## Evidence

[质询]该陈述将SEM路径系数的估计误差方差（σ²_SEM）直接等同于标准化影响系数（β）的标准误，这在统计定义上存在混淆：标准误（SE）是估计量的标准差，而方差（σ²）是标准误的平方；此外，Bootstrap重抽样1000次计算95%置信区间是经验性统计实践，并非SEM理论推导的必然结果，且具体迭代次数（1000）属于经验参数而非第一性原理可推导事实。 | 经验事实，逻辑自洽但缺来源支持；统计定义上存在方差与标准误的混淆，且Bootstrap迭代次数为经验参数，无外部来源直接支持该具体量化方式。

## Search Query

structural equation model path coefficient standard error bootstrap
