# N124: 确定ρ=-0.3约束下前11个对象大小分布的边界条件与失效模式：当对象数量N远大于k_90时，Spearman相关的局部线性近似在极端尾部（i<10）可能失效，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

确定ρ=-0.3约束下前11个对象大小分布的边界条件与失效模式：当对象数量N远大于k_90时，Spearman相关的局部线性近似在极端尾部（i<10）可能失效，需引入高阶矩修正项或改用Gaussian Copula截断近似，误差范围估计为±5%。

## Corrected Claim

确定ρ=-0.3约束下前11个对象大小分布的边界条件与失效模式：当对象数量N远大于k_90时，Spearman相关的局部线性近似在极端尾部（i<10）可能失效，需引入高阶矩修正项或改用Gaussian Copula截断近似，具体误差范围需根据实际数据分布进行蒙特卡洛模拟或解析推导确定。

## Evidence

[质询]「误差范围估计为±5%」属于具体的经验性数值断言，缺乏通用理论支持，且未指明具体的分布假设或数据场景，该数值可能因具体数据分布而异，存在过度精确化的风险。 | 先验知识/题面给定，逻辑校验通过；但±5%的具体误差界为经验性估计，缺乏通用来源直接支持，故降级。

## Search Query

Spearman correlation approximation error tail dependence extreme order statistics
