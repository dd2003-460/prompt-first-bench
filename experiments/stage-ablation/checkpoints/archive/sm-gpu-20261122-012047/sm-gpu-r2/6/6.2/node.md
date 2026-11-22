# N157: Intel Gaudi 2 的显存带宽为 1.6 TB/s，低于 H100 的 3.35 TB/s，导致 KV Cache 生成速度比 H100 慢 50-60

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N42

## Claim

Intel Gaudi 2 的显存带宽为 1.6 TB/s，低于 H100 的 3.35 TB/s，导致 KV Cache 生成速度比 H100 慢 50-60%，在 32K 上下文下首字延迟 (TTFT) 约为 2-3 秒，比 H100 高 1-2 秒。

## Corrected Claim

Intel Gaudi 2 的显存带宽为 1.6 TB/s，低于 H100 的 3.35 TB/s，这通常导致其在 KV Cache 生成阶段的速度低于 H100，在长上下文（如 32K）场景下，其首字延迟 (TTFT) 往往高于 H100，具体数值取决于模型与负载配置。

## Evidence

[质询]TTFT（首字延迟）的具体数值（2-3秒）及与H100的差值（1-2秒）高度依赖于具体的模型规模、批处理大小（batch size）、硬件配置及软件栈优化，并非由显存带宽单一因素决定的固定物理常数。将特定场景下的性能表现泛化为绝对数值存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过。Gaudi 2 显存带宽（1.6 TB/s）低于 H100（3.35 TB/s）是已知硬件规格，带宽瓶颈确实会显著影响 KV Cache 生成速度，逻辑自洽。但具体 TTFT 数值为经验性性能指标，缺乏通用性，故降级。

## Search Query

Intel Gaudi 2 memory bandwidth 1.6 TB/s KV cache generation speed Qwen3-27B
