# N139: 2×RTX 4090 方案中，PCIe 带宽瓶颈在长上下文 (32K+) 场景下导致 Attention 计算的重分布 (Recomputation) 开销增加

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

2×RTX 4090 方案中，PCIe 带宽瓶颈在长上下文 (32K+) 场景下导致 Attention 计算的重分布 (Recomputation) 开销增加，使得实际吞吐量比理论峰值低 15-25%，这一效应随上下文长度增加而加剧。

## Corrected Claim

2×RTX 4090 方案中，PCIe 带宽瓶颈在长上下文 (32K+) 场景下可能限制 KV Cache 或中间张量的传输效率，导致实际吞吐量低于理论峰值，具体降幅取决于软件栈优化及具体负载特征，通常可能在 10-30% 范围内，且随上下文长度增加而加剧。

## Evidence

[质询]该陈述包含具体的经验性数值范围（15-25%）和特定的因果机制（PCIe带宽瓶颈导致Recomputation开销增加），这属于硬件性能调优的经验事实，无法从第一性原理严格推导。此外，'Recomputation'通常指为了节省显存而重新计算激活值，其开销主要受限于计算单元（FLOPS）而非PCIe带宽，将PCIe瓶颈直接归因于Recomputation开销增加在机制上存在混淆，更可能是PCIe带宽限制了KV Cache或中间张量的传输，从而限制了整体吞吐，而非直接增加Recomputation的计算开销。 | 经验事实，逻辑自洽但缺来源支持；且机制描述存在潜在混淆（PCIe瓶颈通常限制数据传输而非直接增加计算重分布开销），具体数值缺乏外部证据验证。
