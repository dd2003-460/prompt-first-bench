# N183: 上下文长度分布对最优卡型的影响量化：若 80% 请求 < 4K tokens，KV Cache 占用极小 (<2GB)，显存容量不再是瓶颈，带宽成为主导。此时 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

上下文长度分布对最优卡型的影响量化：若 80% 请求 < 4K tokens，KV Cache 占用极小 (<2GB)，显存容量不再是瓶颈，带宽成为主导。此时 H100 (3350 GB/s) 相比 4090 (1008 GB/s) 的带宽优势 (3.3x) 直接转化为吞吐优势，推荐 H100。

## Corrected Claim

上下文长度分布对最优卡型的影响量化：若 80% 请求 < 4K tokens，KV Cache 占用极小 (<2GB)，显存容量不再是瓶颈，带宽成为主导。此时 H100 (3350 GB/s) 相比 4090 (1008 GB/s) 的带宽优势 (3.3x) 直接转化为吞吐优势，推荐 H100。

## Evidence

先验知识/题面给定，逻辑校验通过：H100与4090的显存带宽数值（3350 GB/s vs 1008 GB/s）符合硬件规格，带宽比约3.3x计算正确；在KV Cache占用极小（<2GB）且显存非瓶颈的前提下，推理吞吐主要受限于显存带宽，因此带宽优势直接转化为吞吐优势符合LLM推理的基本原理。
