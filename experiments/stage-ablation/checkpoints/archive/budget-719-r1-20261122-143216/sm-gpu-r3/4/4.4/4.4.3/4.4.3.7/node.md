# N321: llama.cpp 在 RTX 4090 (24GB) 上运行 Qwen3-27B (BF16) 时，由于权重 (54GB) 超出显存，必须采用 GPU Off

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113, N114, N115

## Claim

llama.cpp 在 RTX 4090 (24GB) 上运行 Qwen3-27B (BF16) 时，由于权重 (54GB) 超出显存，必须采用 GPU Offload 策略（如 -ngl 60 层卸载至 GPU，剩余层在 CPU），此时 Decode 速度受限于 CPU 内存带宽（DDR5 ~50-80 GB/s）与 GPU 显存带宽 (1008 GB/s) 的混合瓶颈，实测速度约为纯 GPU 推理的 30%-40%。

## Corrected Claim

llama.cpp 在 RTX 4090 (24GB) 上运行 Qwen3-27B (BF16) 时，由于权重 (54GB) 超出显存，必须采用 GPU Offload 策略（部分层卸载至 GPU，剩余层在 CPU），此时 Decode 速度受限于 CPU 内存带宽与 GPU 显存带宽的混合瓶颈，实测速度显著低于纯 GPU 推理。

## Evidence

[质询]具体数值（如 -ngl 60 层、30%-40% 速度比）属于经验事实，缺乏来源支持，且不同量化/配置下结果差异大，无法从第一性原理严格推出。 | 逻辑自洽：Qwen3-27B BF16 权重约 54GB，超出 RTX 4090 24GB 显存，必须部分卸载至 CPU；混合推理速度受限于 CPU 内存带宽瓶颈，显著低于纯 GPU 推理，定性结论合理。但具体层数和速度百分比为经验数据，无来源支持，按经验事实排除条款降级。

## Search Query

llama.cpp Qwen3-27B GPU offload RTX 4090 CPU memory bandwidth bottleneck decode speed
