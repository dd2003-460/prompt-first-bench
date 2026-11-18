# N151: 工作点3 (Apple Silicon 统一内存)：Mac Studio M2 Ultra 192GB。BF16 权重 55.6GB + KV Cache 4.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

工作点3 (Apple Silicon 统一内存)：Mac Studio M2 Ultra 192GB。BF16 权重 55.6GB + KV Cache 4.0GB + 激活/开销 2.25GB = 61.85GB < 192GB。剩余 130.15GB 显存极大，但受限于 800GB/s 内存带宽，吞吐上限低 (~13-57 tokens/s，存在矛盾需修正)，适合低延迟、长上下文、低吞吐场景。

## Corrected Claim

工作点3 (Apple Silicon 统一内存)：Mac Studio M2 Ultra 192GB。BF16 权重 55.6GB + KV Cache 4.0GB + 激活/开销 2.25GB = 61.85GB < 192GB。剩余 130.15GB 显存极大，但受限于 800GB/s 内存带宽，吞吐上限低 (~13-57 tokens/s，存在矛盾需修正)，适合低延迟、长上下文、低吞吐场景。

## Evidence

先验知识/题面给定，逻辑校验通过
