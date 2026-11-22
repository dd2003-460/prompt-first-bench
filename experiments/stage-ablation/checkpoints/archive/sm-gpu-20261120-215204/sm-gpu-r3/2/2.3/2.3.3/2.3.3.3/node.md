# N215: INT8 量化下 KV Cache 的位宽配置对 32K 上下文累积误差的影响：若 KV Cache 保持 BF16 vs 量化为 INT8，LongBench

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N75

## Claim

INT8 量化下 KV Cache 的位宽配置对 32K 上下文累积误差的影响：若 KV Cache 保持 BF16 vs 量化为 INT8，LongBench 得分差异的具体量化值

## Corrected Claim

INT8量化KV Cache相比BF16会在32K上下文中引入累积误差，通常导致LongBench等长文本基准测试得分下降，但具体下降幅度取决于模型架构与量化策略，无统一固定值。

## Evidence

[质询]该陈述询问具体的量化数值（LongBench得分差异），但KV Cache量化对长上下文性能的影响高度依赖于模型架构、量化算法（如SmoothQuant, KIVI等）及具体任务分布，不存在一个通用的、固定的“具体量化值”。此外，检索无可用来源，无法验证任何特定数值。 | 经验事实，逻辑自洽但缺来源支持。KV Cache量化确实会引入累积误差并影响长上下文性能，但具体得分差异因模型和实现而异，且无外部来源提供具体数值。

## Search Query

KV cache INT8 vs BF16 impact on long context accuracy Qwen
