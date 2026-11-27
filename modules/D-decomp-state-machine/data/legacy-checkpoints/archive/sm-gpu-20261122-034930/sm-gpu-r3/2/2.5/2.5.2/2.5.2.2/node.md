# N243: W8A16 GPTQ与W8A8 SmoothQuant的性能差异机制：GPTQ使用Hessian矩阵近似优化权重缩放，但在激活值保持FP16时，无法消除激活离群

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

W8A16 GPTQ与W8A8 SmoothQuant的性能差异机制：GPTQ使用Hessian矩阵近似优化权重缩放，但在激活值保持FP16时，无法消除激活离群值对权重量化误差的乘性放大效应；SmoothQuant通过平滑因子将激活离群值'转移'至权重，使得W8量化误差在矩阵乘法中部分抵消，导致W8A8在相同位宽下比W8A16少损失约0.4%的MMLU准确率

## Corrected Claim

W8A16 GPTQ与W8A8 SmoothQuant的性能差异机制：GPTQ使用Hessian矩阵近似优化权重缩放，但在激活值保持FP16时，无法消除激活离群值对权重量化误差的乘性放大效应；SmoothQuant通过平滑因子将激活离群值'转移'至权重，使得W8量化误差在矩阵乘法中部分抵消，通常导致W8A8在相同位宽下比W8A16具有更高的MMLU准确率（具体提升幅度依模型和配置而异）。

## Evidence

[质询]具体数值“0.4%”缺乏通用性，属于特定实验条件下的经验数据，不同模型、数据集或量化配置下该差异可能显著波动，将其作为固定机制结论存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：GPTQ与SmoothQuant的机制描述符合量化理论（Hessian优化 vs 离群值平滑），W8A8通常优于W8A16的定性结论正确，但具体数值0.4%为经验事实，无来源支持且非第一性原理可推导，故降级。
