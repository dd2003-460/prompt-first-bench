# N283: TTFT 的实测分布特征：在 32K 上下文下，RTX 4090 的 TTFT 中位数约为 1.2-1.5 秒，95 分位数约为 2.0-2.5 秒；A100 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

TTFT 的实测分布特征：在 32K 上下文下，RTX 4090 的 TTFT 中位数约为 1.2-1.5 秒，95 分位数约为 2.0-2.5 秒；A100 80GB 的 TTFT 中位数约为 0.3-0.5 秒，95 分位数约为 0.6-0.8 秒，差异主要源于 Prefill 吞吐量的硬件差距。

## Corrected Claim

在 32K 上下文下，RTX 4090 的 TTFT 通常显著高于 A100 80GB，差异主要源于 Prefill 阶段算力与显存带宽的硬件差距；具体数值需视模型规模与负载情况而定。

## Evidence

[质询]具体数值（如1.2-1.5秒、0.3-0.5秒）属于经验事实，受模型大小、批处理大小、并发数及具体硬件驱动版本影响极大，缺乏统一基准测试数据支持，存在口径混淆风险。 | 经验事实，逻辑自洽（A100算力与显存带宽优于RTX 4090，Prefill阶段A100确实更快，量级差异合理），但检索无可用来源，无法验证具体数值区间，故降级。

## Search Query

LLM TTFT benchmark 32K context RTX 4090 A100 median p95 latency
