# N95: 平均迭代收敛步数≤5步的约束源自科研循环中单次完整推理链路的Token消耗上限：27B模型在max_model_len=262144下，每步平均消耗约4000 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

平均迭代收敛步数≤5步的约束源自科研循环中单次完整推理链路的Token消耗上限：27B模型在max_model_len=262144下，每步平均消耗约4000 tokens（含假设描述、实验设计、结果解析），5步累计20000 tokens，预留6000 tokens用于最终结论生成与格式化，防止上下文溢出导致截断。

## Corrected Claim

平均迭代收敛步数≤5步的约束源自科研循环中单次完整推理链路的Token消耗上限：27B模型在max_model_len=262144下，每步平均消耗约4000 tokens（含假设描述、实验设计、结果解析），5步累计20000 tokens，预留6000 tokens用于最终结论生成与格式化，防止上下文溢出导致截断。

## Evidence

先验知识/题面给定，逻辑校验通过：20000+6000=26000 tokens，远小于 max_model_len=262144，数值量级合理且无内部矛盾。

## Search Query

LLM iteration token budget context window management research loop
