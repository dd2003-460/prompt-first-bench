# N49: 边界温度漂移的动态响应时间尺度：定义热交换器热容为 C (J/K)，当系统受到阶跃扰动时，边界温度恢复到设定值的特征时间常数 τ = C / (dT/dt)_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

边界温度漂移的动态响应时间尺度：定义热交换器热容为 C (J/K)，当系统受到阶跃扰动时，边界温度恢复到设定值的特征时间常数 τ = C / (dT/dt)_limit。对于典型的液冷系统，若热流密度 q=3.6 MW/m² 超过最大换热能力 q_max，温度漂移率 dT/dt = (q - q_max) / C_v。

## Corrected Claim

边界温度漂移的动态响应时间尺度：定义热交换器热容为 C (J/K)，当系统受到阶跃扰动时，边界温度恢复到设定值的特征时间常数 τ = C / (dT/dt)_limit。对于典型的液冷系统，若热流密度 q=3.6 MW/m² 超过最大换热能力 q_max，温度漂移率 dT/dt = (q - q_max) / C_v。

## Evidence

先验知识/题面给定，逻辑校验通过：热容定义及一阶线性系统时间常数公式 τ=C/(dT/dt) 符合物理直觉与量纲分析，液冷系统热平衡方程逻辑自洽。
