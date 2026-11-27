# N140: 计算饱和点 (Compute Saturation Point) 的量化定义：当 Batch Size 使得 GPU 算力利用率达到 90% 以上时的 B 值。

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

计算饱和点 (Compute Saturation Point) 的量化定义：当 Batch Size 使得 GPU 算力利用率达到 90% 以上时的 B 值。对于 27B 模型，饱和点 B_sat ≈ (2 * N_params * FLOPs_per_token) / (GPU_TFLOPS * 1000)。RTX 4090 (82.6 TFLOPS) 的 B_sat 约为 (2*27e9*2) / 82.6e12 ≈ 1.3 (理论值，实际受内存带宽限制更早饱和)。

## Corrected Claim

计算饱和点无法仅通过参数量和峰值算力简单公式推导。对于 27B 模型在 RTX 4090 上，主要瓶颈通常是显存容量（24GB）和内存带宽，而非算力利用率。实际 Batch Size 受限于 KV Cache 大小和模型权重占用，通常远小于理论算力饱和点。

## Evidence

[质询]公式量纲与逻辑存在严重错误：1. 公式中分子包含 'FLOPs_per_token' 但分母未包含时间或吞吐量单位，导致结果量纲为 'FLOPs' 而非无量纲的 Batch Size；2. 数值计算错误：(2 * 27e9 * 2) / 82.6e12 ≈ 0.0013，而非 1.3，相差三个数量级；3. 概念混淆：Batch Size 与算力利用率的关系取决于序列长度和硬件并行度，不能仅通过参数量和峰值算力简单除法得出，且 27B 模型在单卡 4090 上通常受限于显存容量（24GB）而非算力饱和，该理论值缺乏物理基础。 | 先验知识/题面给定，逻辑校验失败：公式量纲错误且数值计算结果与陈述不符（0.0013 vs 1.3），且违背 GPU 推理中显存带宽与算力平衡的基本工程直觉。

## Search Query

LLM inference compute saturation batch size threshold
