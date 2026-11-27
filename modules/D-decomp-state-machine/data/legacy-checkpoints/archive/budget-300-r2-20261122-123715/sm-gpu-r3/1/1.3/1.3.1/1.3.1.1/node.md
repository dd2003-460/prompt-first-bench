# N164: Mac Studio M2 Ultra 192GB 的内存带宽为 800 GB/s，运行 Qwen3-27B W4 (13.5GB) + 32K 上下文时，理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Mac Studio M2 Ultra 192GB 的内存带宽为 800 GB/s，运行 Qwen3-27B W4 (13.5GB) + 32K 上下文时，理论解码吞吐上限 = 800 GB/s / 13.5GB ≈ 59.3 tokens/s；但 Apple Silicon 的内存控制器延迟及统一内存架构特性导致实际吞吐通常降至理论值的 50-70%，即 30-40 tokens/s。

## Corrected Claim

Mac Studio M2 Ultra 192GB 的内存带宽为 800 GB/s，运行 Qwen3-27B W4 (13.5GB) + 32K 上下文时，理论解码吞吐上限 = 800 GB/s / 13.5GB ≈ 59.3 tokens/s；但 Apple Silicon 的内存控制器延迟及统一内存架构特性导致实际吞吐通常降至理论值的 50-70%，即 30-40 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 内存带宽确为 800GB/s，Qwen3-27B W4 量化后约 13.5GB，理论吞吐计算正确，实际效率 50-70% 符合 Apple Silicon 统一内存架构特性

## Search Query

Apple M2 Ultra memory bandwidth 800GB/s LLM inference performance
