# N116: Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 的 Prefill (提示词处理) 阶段速度约为 500-800 tokens/s 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 的 Prefill (提示词处理) 阶段速度约为 500-800 tokens/s (取决于矩阵乘法效率)，远低于 NVIDIA RTX 4090 的 ~2000-3000 tokens/s，导致长上下文 (32K) 的首字延迟 (TTFT) 约为 40-64 秒，显著高于 GPU 方案的 10-16 秒。

## Corrected Claim

Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 的 Prefill 阶段速度显著低于 NVIDIA RTX 4090，导致长上下文 (32K) 的首字延迟 (TTFT) 显著高于 GPU 方案。

## Evidence

[质询]数值量级与硬件规格存在显著偏差：Mac Studio M2 Ultra 拥有 800GB/s 内存带宽，运行 27B 参数模型（BF16 约 54GB）时，理论 Prefill 速度受限于内存带宽，约为 800/54 ≈ 14.8 tokens/s（若完全受带宽限制）或更高（若计算受限，M2 Ultra 算力约 30+ TFLOPS BF16，理论可达数百 tokens/s，但实际受内存墙限制通常远低于 500-800 tokens/s）。500-800 tokens/s 的速度更接近于小模型或极高优化下的峰值，对于 27B 模型在 M2 Ultra 上显得过于乐观，导致 TTFT 估算（40-64秒）可能严重低估（实际可能更长）。 | 先验知识/题面给定，逻辑校验通过，但数值量级存疑，降级为定性表述
