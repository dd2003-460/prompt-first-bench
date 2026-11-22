# N453: A100 40GB在INT4权重+INT8 KV Cache下的质量损失评估：INT4权重导致MMLU基准测试下降约0.5-1.5%，INT8 KV Cache

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

A100 40GB在INT4权重+INT8 KV Cache下的质量损失评估：INT4权重导致MMLU基准测试下降约0.5-1.5%，INT8 KV Cache导致长文本生成一致性下降约2-5%（需实测验证）。综合质量损失约2.5-6.5%，需与BF16精度下的A100 80GB方案对比，判断是否可接受。

## Corrected Claim

A100 40GB在INT4权重+INT8 KV Cache下的质量损失评估：INT4权重通常导致MMLU等基准测试出现轻微下降（具体幅度依模型和量化方法而定，常见范围约0.5-2%），INT8 KV Cache可能导致长文本生成一致性轻微下降（需实测验证）。综合质量损失需与BF16精度下的A100 80GB方案对比，判断是否可接受。

## Evidence

[质询]数值量级缺乏普适性：INT4权重的质量损失高度依赖于模型架构（如LLaMA vs GPT）和量化算法（GPTQ vs AWQ），0.5-1.5%并非固定常数；INT8 KV Cache在长文本下的一致性下降2-5%也缺乏统一的基准测试支持，属于经验性估计而非确定事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理严格推出，符合经验事实排除条款）

## Search Query

INT4 weight INT8 KV cache quantization quality degradation MMLU benchmark
