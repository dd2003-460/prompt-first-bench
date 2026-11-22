# N126: Batch Size 对 RTX 4090 吞吐的非线性影响及饱和点：随着 Batch Size 增加，总吞吐 (Tokens/s) 线性增长直至显存带宽饱和或

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N38

## Claim

Batch Size 对 RTX 4090 吞吐的非线性影响及饱和点：随着 Batch Size 增加，总吞吐 (Tokens/s) 线性增长直至显存带宽饱和或 KV Cache 溢出；在 24GB 显存限制下，W4 模型 (13.5GB) 仅留 ~10GB 给 KV Cache；若使用 FP8 KV (每 token ~0.5KB)，最大并发序列数 ≈ 10GB / (0.5KB * 32K tokens) ≈ 64 序列；但受算力限制，实际有效 Batch Size 饱和点通常在 8-16 之间，超过此值后每增加一个序列，单序列延迟增加 >15%，总吞吐增益 <5%。

## Corrected Claim

Batch Size 对 RTX 4090 吞吐存在非线性影响，受显存带宽和算力限制，存在饱和点。在 24GB 显存限制下，W4 模型 (13.5GB) 约留 10GB 给 KV Cache；若使用 FP8 KV (每 token ~0.5KB)，理论最大并发序列数约为 64 序列。实际有效 Batch Size 饱和点通常低于理论上限，超过该值后单序列延迟显著增加，总吞吐增益递减。

## Evidence

[质询]该陈述包含具体的经验性数值（如饱和点8-16、延迟增加>15%、吞吐增益<5%），这些并非第一性原理可推导的数学或物理定律，而是依赖于具体模型架构、序列长度分布及硬件微架构调优的经验数据。在缺乏来源支持的情况下，无法验证这些具体阈值的准确性，且不同场景下饱和点可能显著不同。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LLM inference batch size saturation point RTX 4090 memory bandwidth bottleneck
