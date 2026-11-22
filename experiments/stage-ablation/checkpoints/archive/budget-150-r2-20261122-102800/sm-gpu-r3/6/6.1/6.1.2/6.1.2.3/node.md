# N339: N134 中 '性能通常低于同级别 NVIDIA 硬件 20-30%' 的量化修正：该百分比仅在 '同精度、同显存容量可行' 的前提下成立。对于 Qwen3-2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

N134 中 '性能通常低于同级别 NVIDIA 硬件 20-30%' 的量化修正：该百分比仅在 '同精度、同显存容量可行' 的前提下成立。对于 Qwen3-27B，RX 7900 XTX (24GB) 与 RTX 4090 (24GB) 显存相同，但 RTX 4090 带宽 (1008 GB/s) 远高于 RX 7900 XTX (960 GB/s @ GDDR6)。在 Decode 阶段 (带宽受限)，RX 7900 XTX 的理论吞吐上限为 960/58.29 ≈ 16.5 tokens/s (BF16, 不可行需Offload) 或 W4 下 960/14.57 ≈ 65.9 tokens/s。考虑到 ROCm 软件栈效率约为 CUDA 的 80-90%，RX 7900 XTX W4 实际吞吐约为 52-59 tokens/s，低于 RTX 4090 的 69.2 tokens/s 约 15-25%。

## Corrected Claim

N134 中 '性能通常低于同级别 NVIDIA 硬件 20-30%' 的量化修正：该百分比仅在 '同精度、同显存容量可行' 的前提下成立。对于 Qwen3-27B，RX 7900 XTX (24GB) 与 RTX 4090 (24GB) 显存相同，但 RTX 4090 带宽 (1008 GB/s) 远高于 RX 7900 XTX (960 GB/s @ GDDR6)。在 Decode 阶段 (带宽受限)，RX 7900 XTX 的理论吞吐上限为 960/58.29 ≈ 16.5 tokens/s (BF16, 不可行需Offload) 或 W4 下 960/14.57 ≈ 65.9 tokens/s。考虑到 ROCm 软件栈效率约为 CUDA 的 80-90%，RX 7900 XTX W4 实际吞吐约为 52-59 tokens/s，低于 RTX 4090 的 69.2 tokens/s 约 15-25%。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽计算（960/14.57≈65.9）与软件栈效率折损（65.9*0.8~0.9≈52-59）推导自洽，且与RTX 4090对比得出的15-25%差距符合硬件规格差异。
