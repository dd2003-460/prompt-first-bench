# N112: 降价策略下的 D_S 计算：∂P_ask/∂Strategy_S = -0.8，代入 N77 得 D_S_low = -0.8 * (-0.05) = 0.04

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

降价策略下的 D_S 计算：∂P_ask/∂Strategy_S = -0.8，代入 N77 得 D_S_low = -0.8 * (-0.05) = 0.04，表明卖家降价策略会提升均衡稳定性 0.04 单位，但幅度小于高挂价策略的负面影响绝对值，说明均衡对卖家提价更敏感。

## Corrected Claim

降价策略下的 D_S 计算：∂P_ask/∂Strategy_S = -0.8，代入 N77 得 D_S_low = -0.8 * (-0.05) = 0.04，表明卖家降价策略会提升均衡稳定性 0.04 单位，但幅度小于高挂价策略的负面影响绝对值，说明均衡对卖家提价更敏感。

## Evidence

先验知识/题面给定，逻辑校验通过：数学运算 -0.8 * (-0.05) = 0.04 正确，符号逻辑（负斜率乘以负变化量得正结果）自洽，符合微积分基本定义。
