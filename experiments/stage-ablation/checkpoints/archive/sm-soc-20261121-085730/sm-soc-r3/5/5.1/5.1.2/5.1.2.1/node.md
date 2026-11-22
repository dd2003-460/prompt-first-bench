# N313: 基准模型 AIC_benchmark 的选择标准：对于二手商品定价预测，基准模型应设定为包含商品类别、成色等级、卖家信用分和控制变量的线性回归模型（OLS），其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

基准模型 AIC_benchmark 的选择标准：对于二手商品定价预测，基准模型应设定为包含商品类别、成色等级、卖家信用分和控制变量的线性回归模型（OLS），其 AIC 值可通过公式 AIC = 2k - 2ln(L) 计算，其中 k 为参数数量，L 为似然函数值，该基准值作为复杂度归一化的分母。

## Corrected Claim

基准模型 AIC_benchmark 的选择标准：对于二手商品定价预测，基准模型应设定为包含商品类别、成色等级、卖家信用分和控制变量的线性回归模型（OLS），其 AIC 值可通过公式 AIC = 2k - 2ln(L) 计算，其中 k 为参数数量，L 为似然函数值，该基准值作为复杂度归一化的分母。

## Evidence

先验知识/题面给定，逻辑校验通过：AIC公式定义正确，OLS作为基准模型符合统计建模常规，逻辑自洽。

## Search Query

AIC benchmark model selection linear regression price prediction second hand
