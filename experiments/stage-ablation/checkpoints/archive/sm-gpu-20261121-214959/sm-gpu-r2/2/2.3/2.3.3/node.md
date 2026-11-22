# N64: 4x RTX 4090 多卡工作站运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

4x RTX 4090 多卡工作站运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 96GB 总容量。由于 PCIe 4.0 x16 带宽 (~64 GB/s 单向) 远低于单卡显存带宽 (1008 GB/s)，跨卡通信开销显著。实际 Decode 吞吐受限于最慢的跨卡同步步骤，理论上限估算：假设 KV Cache 均匀分布，每次生成需从其他 3 卡获取 KV 数据，通信时间 ≈ 12.58GB / (64 GB/s * 4) ≈ 0.049s，计算时间 ≈ 54GB / (1008 GB/s * 4) ≈ 0.013s，总延迟 ≈ 0.062s/token，吞吐 ≈ 16.1 tokens/s，远低于单卡 H100 (37.76 tokens/s)。

## Corrected Claim

4x RTX 4090 多卡工作站运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 96GB 总容量。由于 PCIe 4.0 x16 带宽 (~64 GB/s 单向) 远低于单卡显存带宽 (1008 GB/s)，跨卡通信开销显著。实际 Decode 吞吐受限于跨卡同步步骤，但具体数值取决于并行策略（如 Tensor Parallelism 切分 KV Cache），理论估算值 16.1 tokens/s 基于全量 KV 同步假设，实际性能可能更高。

## Evidence

[质询]该陈述基于一个极不现实的硬件假设：4张RTX 4090通过PCIe 4.0 x16互联进行全量KV Cache同步。在实际多卡推理中，KV Cache通常按层或头切分（Tensor Parallelism），每卡仅持有部分KV，且通信量远小于全量KV Cache；此外，RTX 4090不支持NVLink，跨卡通信确实走PCIe，但'每次生成需从其他3卡获取全量KV数据'的假设严重高估了通信开销，导致吞吐估算（16.1 tokens/s）远低于实际可能的性能（通常可达50-100+ tokens/s，取决于具体并行策略和框架优化）。 | 先验知识/题面给定，逻辑校验通过，但经验事实（具体吞吐数值）缺乏来源支持且基于非典型假设，故降级
