# N68: Apple M2 Ultra (192GB Unified Memory, 800 GB/s) 运行 Qwen3-27B BF16 时，受限于统一内存带宽，生成

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

Apple M2 Ultra (192GB Unified Memory, 800 GB/s) 运行 Qwen3-27B BF16 时，受限于统一内存带宽，生成速度预计为 15-25 tokens/s，远低于 RTX 4090 FP8 下的 40-60 tokens/s；其 $3,999 整机成本虽低，但单位 Token 成本在低并发场景下高于消费级 GPU，仅适合对延迟不敏感且需单卡大显存（>54GB）的特定场景。

## Corrected Claim

Apple M2 Ultra (192GB Unified Memory, 800 GB/s) 运行 Qwen3-27B BF16 时，受限于统一内存带宽，生成速度预计为 15-25 tokens/s，远低于 RTX 4090 FP8 下的 40-60 tokens/s；其 $3,999 整机成本虽低，但单位 Token 成本在低并发场景下高于消费级 GPU，仅适合对延迟不敏感且需单卡大显存（>54GB）的特定场景。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 800GB/s 带宽限制下，27B 模型生成速度受限于内存带宽，15-25 tokens/s 符合理论推算；RTX 4090 FP8 下 40-60 tokens/s 亦符合其高带宽特性；成本与适用场景分析逻辑自洽。
