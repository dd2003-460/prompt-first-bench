# N221: NVIDIA H100 SXM (80GB) 原生 FP8 精度下运行 Qwen3-27B 的实测吞吐量约为 80-120 tokens/s (单卡, 32K上

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

NVIDIA H100 SXM (80GB) 原生 FP8 精度下运行 Qwen3-27B 的实测吞吐量约为 80-120 tokens/s (单卡, 32K上下文)，其 FP8 Tensor Core 峰值算力 1979 TOPS 在 LLM 解码阶段受限于内存带宽 (3.35TB/s HBM3)，实际瓶颈从计算转为带宽，理论带宽上限 3350GB/s / 45GB (FP8权重+KV) ≈ 74 tokens/s，实测通常低于此值。

## Corrected Claim

NVIDIA H100 SXM (80GB) 原生 FP8 精度下运行 Qwen3-27B 的实测吞吐量通常低于理论带宽上限。若假设总数据量为45GB，理论带宽上限约为 3350GB/s / 45GB ≈ 74 tokens/s，实测吞吐量应低于此值（例如 50-70 tokens/s），具体数值取决于 KV 缓存大小和内存访问效率。

## Evidence

[质询]数值量级与理论上限矛盾：陈述中声称理论带宽上限约为 74 tokens/s，但实测吞吐量却声称约为 80-120 tokens/s。实测值高于理论带宽上限在物理上是不可能的（除非权重或KV缓存大小远小于45GB，但Qwen3-27B FP8权重约27GB，32K上下文KV缓存通常需数GB至十几GB，总占用接近或超过45GB的假设需更精确验证，但即便假设45GB是上限，实测超过理论上限也是逻辑硬伤）。此外，H100 SXM 80GB 的 HBM3 带宽通常为 3.35 TB/s，但 FP8 权重加载和 KV 缓存读取的总数据量计算可能存在口径混淆。 | 逻辑校验失败：实测吞吐量（80-120 tokens/s）高于计算出的理论带宽上限（74 tokens/s），存在内部矛盾。来源未覆盖，但逻辑错误导致无法验证。

## Search Query

H100 SXM Qwen 27B FP8 inference benchmark tokens per second
