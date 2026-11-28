# N7: 长上下文精度衰减阈值：Qwen3.8-27b在NVFP4量化下，输入长度超过16k tokens后，关键信息提取准确率下降幅度需通过RULER或HELMET基准

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

长上下文精度衰减阈值：Qwen3.8-27b在NVFP4量化下，输入长度超过16k tokens后，关键信息提取准确率下降幅度需通过RULER或HELMET基准测试量化（预期下降>15%则触发外部记忆分片策略）

## Corrected Claim

长上下文精度衰减阈值：Qwen3.8-27b在NVFP4量化下，输入长度超过16k tokens后，关键信息提取准确率下降幅度需通过RULER或HELMET基准测试量化（预期下降>15%则触发外部记忆分片策略）[注：此为基于特定实验设定的经验性阈值，需以实际基准测试结果为准]

## Evidence

[质询]该陈述包含具体的经验性阈值（16k tokens）和性能指标（下降>15%），这些并非从第一性原理或数学公理可推导出的必然结论，而是依赖于特定模型版本、量化方式及基准测试的具体实验数据。此外，'Qwen3.8-27b'这一具体型号及其在NVFP4下的表现属于经验事实，缺乏通用理论支撑。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该事实属于具体模型参数与性能阈值的经验观察，非第一性原理可推导范畴）

## Search Query

Qwen3 27b NVFP4 long context accuracy degradation benchmark RULER HELMET 2026
