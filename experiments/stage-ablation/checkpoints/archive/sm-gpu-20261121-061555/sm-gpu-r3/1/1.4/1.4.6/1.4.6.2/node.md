# N183: V100 32GB (32GB) 支持 INT8 硬件加速，但不支持 FP8，Qwen3-27B BF16 推理吞吐量约为 RTX 4090 的 20-30%，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

V100 32GB (32GB) 支持 INT8 硬件加速，但不支持 FP8，Qwen3-27B BF16 推理吞吐量约为 RTX 4090 的 20-30%，32GB 显存勉强容纳 32K 上下文 (KV Cache ~16GB + Weights ~54GB BF16 需量化至 INT8 ~27GB)，可行但性能低下

## Corrected Claim

V100 32GB 支持 INT8 硬件加速但不支持 FP8。Qwen3-27B 在 INT8 量化下权重约 27GB，32GB 显存仅能容纳权重及极短上下文（如 4K-8K），无法稳定支持 32K 上下文（KV Cache 将导致显存溢出）。其推理吞吐量显著低于 RTX 4090，但具体比例需视具体负载而定，通常远低于 4090 的 FP16/BF16 性能。

## Evidence

[质询]数值量级与逻辑自洽性存在严重矛盾：Qwen3-27B 的 BF16 权重约为 54GB，INT8 量化后约为 27GB。若显存为 32GB，扣除 27GB 权重后仅剩 5GB 用于 KV Cache 和激活值，无法支持 32K 上下文（通常 32K 上下文的 KV Cache 需数 GB 至十几 GB 不等，具体取决于模型架构，但 5GB 余量极小且未考虑激活值开销）。此外，V100 不支持 FP8 是正确的，但 V100 的 INT8 吞吐量相对于 RTX 4090 的 20-30% 这一具体比例缺乏通用基准支持，且 32GB 显存‘勉强容纳’32K 上下文的描述在数学上过于乐观，通常 27B 模型在 32GB 显存下运行 32K 上下文会因 KV Cache 溢出而失败或需要极激进的量化/分页策略。 | 先验知识/题面给定，逻辑校验未通过：27B 模型 INT8 权重约 27GB，32GB 显存剩余空间不足以稳定支撑 32K 上下文的 KV Cache 及推理激活值，存在显存溢出风险；且 V100 与 4090 的吞吐量比例缺乏统一基准，属于经验事实且逻辑推导存在漏洞。

## Search Query

V100 32GB LLM inference throughput comparison RTX 4090
