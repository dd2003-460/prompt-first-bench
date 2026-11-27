# N136: AMD RX 7900 XTX 在 ROCm 软件栈下运行 Qwen3-27B 的性能折损系数：相比同等显存带宽的 NVIDIA 卡（如 RTX 4090），由

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

AMD RX 7900 XTX 在 ROCm 软件栈下运行 Qwen3-27B 的性能折损系数：相比同等显存带宽的 NVIDIA 卡（如 RTX 4090），由于 ROCm 优化程度较低及驱动开销，实际吞吐量通常为理论值的 50-70%；理论带宽 960 GB/s，INT4 理论上限 960/14 ≈ 68.5 tokens/s，实际预估 34-48 tokens/s。

## Corrected Claim

AMD RX 7900 XTX 在 ROCm 软件栈下运行 Qwen3-27B 的性能通常低于同等显存带宽的 NVIDIA 卡，具体吞吐量受驱动优化程度影响，需实测数据确认。

## Evidence

[质询]该陈述包含具体的经验性性能数据（50-70%折损系数、34-48 tokens/s预估），属于硬件性能与软件栈效率的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AMD RX 7900 XTX ROCm LLM inference benchmark Qwen 7B 13B 27B tokens per second
