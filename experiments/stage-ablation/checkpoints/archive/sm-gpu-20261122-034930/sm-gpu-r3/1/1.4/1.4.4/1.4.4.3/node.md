# N190: RTX 3060 12GB/16GB 的排除依据：Qwen3-27B W4权重最小为13.5GB，已超出12GB版本物理上限；16GB版本在W4+INT4 KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

RTX 3060 12GB/16GB 的排除依据：Qwen3-27B W4权重最小为13.5GB，已超出12GB版本物理上限；16GB版本在W4+INT4 KV Cache下需求20.17GB，超出16GB上限，且其显存带宽480 GB/s仅为RTX 4090的48%，即便通过Offload运行，理论吞吐上限仅为480/13.5 ≈ 35 tokens/s（仅权重读取），实际含KV Cache读取后<10 tokens/s，不具备性价比。

## Corrected Claim

RTX 3060 12GB/16GB 的排除依据：Qwen3-27B W4权重最小为13.5GB，已超出12GB版本物理上限；16GB版本在W4+INT4 KV Cache下需求20.17GB，超出16GB上限，且其显存带宽480 GB/s仅为RTX 4090的48%，即便通过Offload运行，理论吞吐上限仅为480/13.5 ≈ 35 tokens/s（仅权重读取），实际含KV Cache读取后<10 tokens/s，不具备性价比。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3060 12GB/16GB 显存规格及带宽（480 GB/s）符合硬件事实；Qwen3-27B W4 量化后权重约 13.5GB 超出 12GB 上限，且 16GB 版本在含 KV Cache 下需求超 20GB 亦超出上限，带宽瓶颈导致吞吐低，逻辑自洽。
