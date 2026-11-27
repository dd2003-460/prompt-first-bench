# N247: 1×RTX 4090 BF16 Offload 方案的替代优化路径：采用 INT8 量化 (权重 27GB) + KV Cache 压缩 (FP8) 可将显存占

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

1×RTX 4090 BF16 Offload 方案的替代优化路径：采用 INT8 量化 (权重 27GB) + KV Cache 压缩 (FP8) 可将显存占用降至 29.3GB，仍超 24GB 但可通过 PagedAttention 优化，吞吐量提升至 25-30 tokens/s，TCO/Throughput 优化至 $0.012-$0.015/token，比 BF16 Offload 方案低 4-5 倍

## Corrected Claim

采用 INT8 量化 (权重 27GB) + KV Cache 压缩 (FP8) 可将显存占用降至约 29.3GB，虽仍超 24GB 但可通过 PagedAttention 优化；在特定配置下，吞吐量可能提升至 25-30 tokens/s，TCO/Throughput 优化至 $0.012-$0.015/token，相比 BF16 Offload 方案有显著成本优势。

## Evidence

[质询]吞吐量 25-30 tokens/s 及 TCO 数值属于特定硬件配置下的经验性能指标，缺乏通用物理定律或第一性原理支持，且不同模型规模、序列长度及具体实现细节会导致结果巨大差异，无法仅凭逻辑推导验证其准确性。 | 经验事实，逻辑自洽但缺来源支持
