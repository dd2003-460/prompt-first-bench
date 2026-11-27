# N99: 192GB 统一内存档位 (Apple M3 Ultra) 虽容量充足可运行 BF16 大模型，但内存带宽 (~800GB/s) 低于 RTX 4090 (~1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

192GB 统一内存档位 (Apple M3 Ultra) 虽容量充足可运行 BF16 大模型，但内存带宽 (~800GB/s) 低于 RTX 4090 (~1008GB/s) 和 A100 (~2000GB/s)，导致 LLM 解码速度 (tokens/s) 显著低于同等显存容量的 NVIDIA 卡，仅适合对延迟不敏感且预算受限的场景。

## Corrected Claim

192GB 统一内存档位 (Apple M3 Ultra) 虽容量充足可运行 BF16 大模型，但内存带宽 (~800GB/s) 低于 RTX 4090 (~1008GB/s) 和 A100 (~2000GB/s)，导致 LLM 解码速度 (tokens/s) 显著低于同等显存容量的 NVIDIA 卡，仅适合对延迟不敏感且预算受限的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 192GB 带宽约 800GB/s，RTX 4090 约 1008GB/s，A100 约 2000GB/s，数值量级符合硬件规格常识，且 LLM 解码速度受内存带宽限制的原理正确。

## Search Query

Apple M3 Ultra memory bandwidth vs RTX 4090 A100 LLM inference speed
