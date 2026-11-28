# N373: 定义 '科研编程任务' 为：题目描述包含 'matrix', 'equation', 'simulation', 'statistical' 关键词之一，且代码

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

定义 '科研编程任务' 为：题目描述包含 'matrix', 'equation', 'simulation', 'statistical' 关键词之一，且代码模板导入 numpy/scipy/pandas 中至少一个库的子集，该子集在 LiveCodeBench 中占比 8.7% [待核验]

## Corrected Claim

定义 '科研编程任务' 为：题目描述包含 'matrix', 'equation', 'simulation', 'statistical' 关键词之一，且代码模板导入 numpy/scipy/pandas 中至少一个库的子集（具体占比数据待进一步核实）

## Evidence

[质询]该陈述包含具体的经验统计数据（LiveCodeBench中占比8.7%）和特定的定义标准（关键词+库导入），这属于经验事实而非第一性原理可推导内容。由于缺乏任何参考来源支持，无法验证该具体数值和定义的准确性，存在数据捏造或口径错误的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

LiveCodeBench keyword filtering matrix equation simulation numpy import ratio
