# N135: SI 分布参数校准：Gamma(α_s, β_s) 参数需通过平台历史 SKU 数据拟合。具体操作为：计算各品类 SI 样本均值 μ_SI 和方差 Var_SI

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

SI 分布参数校准：Gamma(α_s, β_s) 参数需通过平台历史 SKU 数据拟合。具体操作为：计算各品类 SI 样本均值 μ_SI 和方差 Var_SI，利用矩估计法求解 α_s = μ_SI² / Var_SI，β_s = μ_SI / Var_SI；若 α_s < 1 则分布呈 J 型（高噪声主导），α_s > 1 则呈钟型（标准化主导）。

## Corrected Claim

SI 分布参数校准：Gamma(α_s, β_s) 参数需通过平台历史 SKU 数据拟合。具体操作为：计算各品类 SI 样本均值 μ_SI 和方差 Var_SI，利用矩估计法求解 α_s = μ_SI² / Var_SI，β_s = μ_SI / Var_SI；若 α_s < 1 则分布呈 J 型（高噪声主导），α_s > 1 则呈钟型（标准化主导）。

## Evidence

逻辑推导成立，来源未直接覆盖（Gamma分布矩估计公式及形状参数对分布形态的影响为统计学第一性原理，来源[1]确认Gamma分布参数化背景，无矛盾）

## Search Query

Gamma distribution parameter estimation moment method variance standardization index

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Gamma_distribution&rut=b2acb0879dcfb57a756fc7d2f9712e10e20d42ca71ecc5bc3dba01e8fa4fcbe5', 'type': 'ddg', 'title': 'Gamma distribution - Wikipedia'}
