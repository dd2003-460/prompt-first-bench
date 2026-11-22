# N153: CPU 上 INT4 推理的吞吐量提升系数：在 Apple M3 Ultra (192GB) 上，MLX 框架 INT4 量化相比 BF16 的吞吐量提升为 1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

CPU 上 INT4 推理的吞吐量提升系数：在 Apple M3 Ultra (192GB) 上，MLX 框架 INT4 量化相比 BF16 的吞吐量提升为 1.8-2.0x，主要受内存带宽限制（800 GB/s），反量化开销占比 < 5%

## Corrected Claim

在 Apple M3 Ultra 上，MLX 框架 INT4 量化相比 BF16 的吞吐量显著提升（理论上限接近 2x，实际受反量化开销影响略低），主要受内存带宽限制（约 800-820 GB/s）。

## Evidence

[质询]参考来源中未包含具体的 INT4 吞吐量提升系数（1.8-2.0x）及反量化开销占比（<5%）的数据，且来源[3]提到的内存带宽为 819 GB/s 而非 800 GB/s，存在数值细节偏差。 | 逻辑自洽（INT4 相比 BF16 数据量减半，在内存带宽受限场景下理论加速比接近 2x，反量化开销通常较低），但来源[1]仅提及基准测试存在，未提供具体数值；来源[3]确认了 M3 Ultra 的高带宽特性（819 GB/s），间接支持内存带宽受限的结论，但缺乏直接支持 1.8-2.0x 具体系数的证据。

## Search Query

Apple M3 Ultra MLX INT4 vs BF16 inference throughput

## Retrieval Sources

- {'url': 'https://machinelearning.apple.com/research/mlx-distributed-inference&rut=d84ba69941e0fda21eb2b57b3c3fd7670935ddd6997e756d4bc9f0976a40c8f2', 'type': 'ddg', 'title': 'Local and Distributed Large LLM Inference with MLX and RDMA on Mac ...'}
- {'url': 'https://www.apple.com/newsroom/2025/03/apple-reveals-m3-ultra-taking-apple-silicon-to-a-new-extreme/&rut=6144cc6ce2ac7a69882cfe90b29c8750b76b41c35c190a63e94f12e26ecc19be', 'type': 'ddg', 'title': 'Apple reveals M3 Ultra, taking Apple silicon to a new extreme'}
- {'url': 'https://canitrun.dev/gpus/m3-ultra/&rut=5baba6998dd659b823c7b2603a259e264775960a016878c6f525d8a0231f50c2', 'type': 'ddg', 'title': 'Apple M3 Ultra (96-512 GB VRAM): Which LLMs Can It Run?'}
