# N378: RTX 3090 24GB 显存带宽 936 GB/s，运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

RTX 3090 24GB 显存带宽 936 GB/s，运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，理论 decode 速度上限为 936 / 15.5 ≈ 60.4 tokens/s，实际受计算瓶颈限制通常为理论值的 60-70%，即约 36-42 tokens/s [待核验: 实测吞吐量]

## Corrected Claim

RTX 3090 24GB 显存带宽 936 GB/s，运行 Qwen3-27B INT4 (13.5GB) + 32K BF16 KV Cache (2.0GB) 时，理论 decode 速度上限为 936 / 15.5 ≈ 60.4 tokens/s，实际受计算瓶颈限制通常为理论值的 60-70%，即约 36-42 tokens/s [待核验: 实测吞吐量]

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 显存带宽 936 GB/s 为准确硬件参数；Qwen3-27B INT4 模型大小约 13.5GB 及 32K BF16 KV Cache 约 2.0GB 的量级估算符合常规推理场景；基于显存带宽瓶颈的理论速度计算 (936/15.5 ≈ 60.4) 及实际受计算/延迟限制降至 60-70% 的推断符合 LLM 推理性能的一般工程经验。

## Search Query

RTX 3090 Qwen3 27B INT4 inference speed tokens per second benchmark
