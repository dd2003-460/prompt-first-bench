# N117: Pareto 分布尾部指数 α 的极大似然估计值（MLE）为 1.8，置信区间为 [1.6, 2.0]（基于 95% 置信水平）。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N33

## Claim

Pareto 分布尾部指数 α 的极大似然估计值（MLE）为 1.8，置信区间为 [1.6, 2.0]（基于 95% 置信水平）。

## Corrected Claim

Pareto 分布尾部指数 α 的极大似然估计值（MLE）通常由公式 α_hat = n / Σln(x_i/x_min) 计算得出；在特定数据集下，其估计值可能为 1.8，置信区间为 [1.6, 2.0]（基于 95% 置信水平）。

## Evidence

[质询]该陈述包含具体的经验数值（MLE=1.8, CI=[1.6, 2.0]），这依赖于特定的数据集。参考来源仅提供了Pareto分布MLE的通用公式推导，未包含任何具体数据集的计算结果，因此无法验证这些具体数值是否来自某个标准或特定的数据集，存在将特定数据集结果误述为通用事实或来源缺失的风险。 | 来源[1]和[3]提供了Pareto分布MLE的通用公式（α_hat = n / Σln(x_i/x_min)），逻辑上支持该估计方法的存在性，但均未提供具体的数值结果（1.8或[1.6, 2.0]）。由于这是经验事实（具体统计量），且缺乏直接来源支持具体数值，依据经验事实排除条款，判定为degraded。

## Search Query

Pareto tail exponent MLE second hand platform transaction data

## Retrieval Sources

- {'url': 'https://math.stackexchange.com/questions/3174150/find-the-maximum-likelihood-estimator-for-pareto-distribution-and-a-unbiased-est&rut=504a933bd320135ee644e39eb14810ccd83e67c8d519bae4b8fe21132adac5db', 'type': 'ddg', 'title': 'statistics - Find the maximum likelihood estimator for Pareto ...'}
- {'url': 'https://blog.csdn.net/luoganttcc/article/details/154403496&rut=feadc4bf451b9ff376681387e9341b7387def803b82a37989e827acb84a07358', 'type': 'ddg', 'title': '介绍一下帕累托分布 包括概率密度函数，概率分布 和 期望计算与证明_恒盛登陆xk7富3.4.6.5.6杏-CSDN博客'}
- {'url': 'https://math.stackexchange.com/questions/2025137/expected-value-of-mle-parameter-of-pareto-distribution&rut=96e43ea92d991bfc303466dec0a3fda8d7031471ceb1456142c96e7b1d9654e2', 'type': 'ddg', 'title': 'Expected Value of MLE parameter of Pareto distribution'}
