# N402: MLX框架在Apple Silicon上推理Qwen3-27B (INT8, 32K ctx) 的实测吞吐率约为18-22 tokens/s，相比NVIDIA 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N144

## Claim

MLX框架在Apple Silicon上推理Qwen3-27B (INT8, 32K ctx) 的实测吞吐率约为18-22 tokens/s，相比NVIDIA RTX 4090 (22-26 tokens/s) 持平或略低，主要受限于统一内存带宽(546 GB/s)及缺乏专用Tensor Core加速。

## Corrected Claim

MLX框架在Apple Silicon上推理Qwen3-27B (INT8, 32K ctx) 的吞吐率通常受限于统一内存带宽，实测性能与NVIDIA RTX 4090相当或略低，具体数值因硬件型号和配置而异。

## Evidence

[质询]具体吞吐率数值（18-22 tokens/s）属于高度依赖具体硬件型号（M1/M2/M3/M4）、内存配置及软件版本的经验事实，且不同测试基准（如是否包含KV Cache优化、Batch Size等）会导致结果差异巨大，缺乏统一标准下的直接来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

MLX framework Qwen3-27B inference throughput tokens per second Apple M4 Max
