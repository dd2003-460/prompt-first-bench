# N419: RTX 4090 FP8 推理吞吐量实测修正：由于 FP8 权重体积减半（相比 BF16），显存带宽瓶颈缓解，但在 Ada 架构上 FP8 的内存访问效率略低于

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N164

## Claim

RTX 4090 FP8 推理吞吐量实测修正：由于 FP8 权重体积减半（相比 BF16），显存带宽瓶颈缓解，但在 Ada 架构上 FP8 的内存访问效率略低于 INT8（因对齐和转换开销）。实测 Decode 吞吐量约为 INT8 方案的 90-95%（即约 29-30 tokens/s），而非 N164 声称的相对 3090 INT8 提升 30-50% 后的绝对值；相对 3090 INT8 (29.5 tokens/s) 的提升主要来自带宽而非纯算力，实际提升幅度约为 5-10%。

## Corrected Claim

RTX 4090 FP8 推理吞吐量实测修正：由于 FP8 权重体积减半（相比 BF16），显存带宽瓶颈缓解，但在 Ada 架构上 FP8 的内存访问效率略低于 INT8（因对齐和转换开销）。实测 Decode 吞吐量通常接近但略低于 INT8 方案，相对 3090 INT8 的提升主要源于带宽优势，具体幅度取决于模型配置。

## Evidence

[质询]该陈述包含具体的实测数值（29-30 tokens/s, 90-95%效率, 5-10%提升），属于经验事实。虽然逻辑上FP8相比INT8在Ada架构上因缺乏原生硬件加速（需软件模拟或转换）导致效率略低是合理的，但具体的吞吐量数值和百分比提升幅度缺乏通用基准支持，且高度依赖于具体的模型大小、序列长度和实现细节，无法仅凭逻辑推导得出精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 FP8 vs INT8 inference throughput benchmark LLM
