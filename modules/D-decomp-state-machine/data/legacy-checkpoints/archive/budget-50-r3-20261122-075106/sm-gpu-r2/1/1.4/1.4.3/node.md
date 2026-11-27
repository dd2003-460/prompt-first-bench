# N58: AMD MI300X 的 HBM3 带宽为 5.3 TB/s，理论最大 Token/s 吞吐率约为 5.3e12 bytes/s / 54e9 bytes/pa

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

AMD MI300X 的 HBM3 带宽为 5.3 TB/s，理论最大 Token/s 吞吐率约为 5.3e12 bytes/s / 54e9 bytes/param ≈ 98 Token/s (计算受限)，实际受限于 Roofline 模型中的算术强度，预计为 40-60 Token/s [待核验]

## Corrected Claim

AMD MI300X 的 HBM3 带宽为 5.3 TB/s。在Decode阶段，Token生成速度受限于内存带宽。对于典型的大语言模型（如70B参数，FP16精度，权重约140GB），理论最大Token/s吞吐率约为 5.3e12 / 140e9 ≈ 37.8 Token/s。考虑实际带宽效率（约60%-70%）和KV Cache开销，实际吞吐率预计为 20-30 Token/s。具体数值取决于模型大小、精度和KV Cache管理策略。

## Evidence

[质询]将HBM带宽直接除以参数量来估算Token/s吞吐率是严重的逻辑错误。Token生成速度（Decode阶段）受限于内存带宽，但每个Token需要读取的字节数并非简单的'参数量'，而是取决于模型架构（如Transformer的层数、隐藏层维度、KV Cache大小等）。对于大语言模型，每生成一个Token通常需要读取整个模型权重（如果是全量加载）或至少是部分权重加上KV Cache。更关键的是，5.3 TB/s是峰值带宽，实际有效带宽通常只有峰值的50%-70%。此外，'54e9 bytes/param'这个假设本身就有问题，通常参数是FP16/BF16（2 bytes/param）或FP8（1 byte/param），54e9 bytes/param意味着每个参数占用54GB，这完全不符合常理。正确的估算应该是：带宽 / (每Token读取的字节数)。如果假设每Token读取整个模型权重（例如70B模型，FP16约140GB），那么理论上限约为 5.3e12 / 140e9 ≈ 37.8 Token/s。如果考虑KV Cache和实际带宽效率，40-60 Token/s的范围对于70B模型来说可能偏高，但对于较小的模型或特定优化下可能合理。然而，原陈述中的计算逻辑（5.3e12 / 54e9）在量纲和物理意义上都是错误的，因为54e9 bytes/param不是一个合理的参数大小单位。 | 逻辑校验失败：原陈述中'54e9 bytes/param'的量纲和数值严重违背基本常识（单个参数不可能占用54GB），且将HBM带宽直接除以参数量来估算Token/s的方法在逻辑上不成立。Token生成速度取决于每Token需要读取的数据量（权重+KV Cache），而非简单的参数量。

## Search Query

AMD MI300X HBM3 bandwidth theoretical throughput LLM inference
