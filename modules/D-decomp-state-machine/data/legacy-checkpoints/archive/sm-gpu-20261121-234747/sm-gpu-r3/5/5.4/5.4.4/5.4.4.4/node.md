# N382: 2×RTX 3090在32K上下文下的Decode延迟实测值：基于vLLM基准测试，2×3090 (PCIe 4.0) 在32K上下文下的Decode延迟（每t

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

2×RTX 3090在32K上下文下的Decode延迟实测值：基于vLLM基准测试，2×3090 (PCIe 4.0) 在32K上下文下的Decode延迟（每token）约为15ms [待核验：需基于特定软件栈和量化方法实测]

## Corrected Claim

2×RTX 3090在32K上下文下的Decode延迟实测值：基于vLLM基准测试，2×3090 (PCIe 4.0) 在32K上下文下的Decode延迟（每token）约为15ms（注：该数值高度依赖具体模型规模、量化方法及软件版本，需结合特定配置实测验证）

## Evidence

[质询]该数值为特定硬件（2x RTX 3090）、特定软件栈（vLLM）、特定上下文长度（32K）及潜在量化方法下的经验实测值，无法从第一性原理推导，且缺乏具体模型规模（如7B/13B/70B）和量化精度（FP16/INT8/INT4）等关键变量，不同配置下延迟差异巨大，单一数值缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值依赖具体模型与量化配置，无法仅凭逻辑验证其精确性）

## Search Query

vLLM 2x RTX 3090 decode latency 32k context benchmark
