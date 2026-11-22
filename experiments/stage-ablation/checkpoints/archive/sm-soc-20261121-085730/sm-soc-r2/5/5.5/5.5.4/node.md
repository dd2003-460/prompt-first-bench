# N120: C_platform_driver 的贝叶斯更新公式：C_posterior = (Likelihood(Data | Platform_Driver) * P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36, N37, N38

## Claim

C_platform_driver 的贝叶斯更新公式：C_posterior = (Likelihood(Data | Platform_Driver) * Prior) / Evidence，其中 Likelihood 需基于 N44-N46 的实证数据计算，若平台流量倾斜效应（N44）显著（p<0.05）且规则无惩罚（N45），则 C_posterior 应 > 0.7，否则维持 0.5 或下调

## Corrected Claim

C_platform_driver 的贝叶斯更新公式：C_posterior = (Likelihood(Data | Platform_Driver) * Prior) / Evidence，其中 Likelihood 需基于 N44-N46 的实证数据计算，若平台流量倾斜效应（N44）显著（p<0.05）且规则无惩罚（N45），则 C_posterior 应 > 0.7，否则维持 0.5 或下调

## Evidence

先验知识/题面给定，逻辑校验通过
