# N91: N30中Weibull尺度参数η = η_0*(P_ask/P_market)^m的基准值η_0校准方法：η_0定义为P_ask=P_market时的特征寿命，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29, N30, N31

## Claim

N30中Weibull尺度参数η = η_0*(P_ask/P_market)^m的基准值η_0校准方法：η_0定义为P_ask=P_market时的特征寿命，需通过平台历史成交数据回归F(T|P_market)的CDF拟合获得，假设η_0≈7天（基于典型二手商品平均成交周期），m=1.5的置信区间需通过bootstrap重采样计算（n≥300样本）。

## Corrected Claim

N30中Weibull尺度参数η = η_0*(P_ask/P_market)^m的基准值η_0校准方法：η_0定义为P_ask=P_market时的特征寿命，需通过平台历史成交数据回归F(T|P_market)的CDF拟合获得；具体数值（如η_0≈7天，m=1.5）及置信区间计算方法（bootstrap, n≥300）需依据实际数据验证，当前为假设值。

## Evidence

[质询]该陈述包含具体的经验参数（η_0≈7天, m=1.5）和特定的统计方法（bootstrap, n≥300），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Weibull distribution scale parameter estimation second-hand market transaction time calibration
