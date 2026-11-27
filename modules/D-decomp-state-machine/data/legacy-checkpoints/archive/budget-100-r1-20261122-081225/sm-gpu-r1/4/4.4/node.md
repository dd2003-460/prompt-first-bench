# N43: 数据中心单卡工作点（H100 SXM 80GB）：80GB 显存可容纳 BF16 32K 上下文 (81.65GB 略超，需 FP8 或微调 KV 量化)，H1

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

数据中心单卡工作点（H100 SXM 80GB）：80GB 显存可容纳 BF16 32K 上下文 (81.65GB 略超，需 FP8 或微调 KV 量化)，H100 推理吞吐约为 1500 tokens/sec (batch=1)，单卡成本 $30000，tokens/sec per dollar 估算为 0.05。

## Corrected Claim

数据中心单卡工作点（H100 SXM 80GB）：80GB 显存可容纳 BF16 32K 上下文（需考虑 KV 量化或 FP8 以适配显存限制），H100 推理吞吐和单卡成本为经验估算值（约 1500 tokens/sec 和 $30000），具体数值随模型和配置波动。

## Evidence

[质询]陈述包含多个具体的经验性数值（如推理吞吐 1500 tokens/sec、单卡成本 $30000），这些属于市场/性能经验事实，无法从第一性原理推导。参考来源 [1] 仅提供了硬件规格（显存大小、发布时间等），完全未涉及推理吞吐量、具体成本或 KV 量化后的显存占用细节，因此缺乏直接的外部证据支持这些具体数值。 | 来源 [1] 确认了 H100 SXM 80GB 的存在及基本规格，间接支持了显存容量的前提，但无法验证吞吐量和成本等经验参数；逻辑上量纲和估算关系自洽，但具体数值缺乏来源直接支持。

## Search Query

H100 Qwen3 27B inference throughput tokens per second 32K context

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/h100-sxm5-80-gb.c3900&rut=7f09b993aaca417c6d41aa8399b54260e9db367c890d472157a2dd44b4964b15', 'type': 'ddg', 'title': 'NVIDIA H100 SXM5 80 GB Specs | TechPowerUp GPU Database'}
