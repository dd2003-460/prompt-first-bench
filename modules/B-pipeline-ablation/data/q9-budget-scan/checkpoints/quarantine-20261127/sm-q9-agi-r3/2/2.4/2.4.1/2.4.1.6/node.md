# N140: 为避免重复失败，需计算新生成假设与历史失败案例的嵌入余弦相似度 Sim_repeat；若Sim_repeat > 0.85，则判定为高重复风险，强制触发假设变异

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47, N48, N49

## Claim

为避免重复失败，需计算新生成假设与历史失败案例的嵌入余弦相似度 Sim_repeat；若Sim_repeat > 0.85，则判定为高重复风险，强制触发假设变异（Mutation）操作，修改核心变量或方法路径，直至Sim_repeat < 0.7。

## Corrected Claim

为避免重复失败，需计算新生成假设与历史失败案例的嵌入余弦相似度 Sim_repeat；若Sim_repeat > 0.85，则判定为高重复风险，强制触发假设变异（Mutation）操作，修改核心变量或方法路径，直至Sim_repeat < 0.7。

## Evidence

先验知识/题面给定，逻辑校验通过
