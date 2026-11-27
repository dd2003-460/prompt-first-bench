# N177: RTX 5090 在 W4 精度下运行 Qwen3-27B 的内存带宽瓶颈吞吐量理论上限为 132.7 Tokens/s (1792 GB/s / 13.5 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

RTX 5090 在 W4 精度下运行 Qwen3-27B 的内存带宽瓶颈吞吐量理论上限为 132.7 Tokens/s (1792 GB/s / 13.5 GB)，考虑 80% 实际带宽利用率后为 106.2 Tokens/s，是 RTX 4090 的 1.78 倍，但具体实际速度需核验 Blackwell 架构的内存控制器效率。

## Corrected Claim

RTX 5090 在 W4 精度下运行 Qwen3-27B 的内存带宽瓶颈吞吐量理论上限为 132.7 Tokens/s (1792 GB/s / 13.5 GB)，考虑 80% 实际带宽利用率后为 106.2 Tokens/s，是 RTX 4090 的 1.78 倍，但具体实际速度需核验 Blackwell 架构的内存控制器效率。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 带宽 1792 GB/s 与显存占用 13.5 GB (27B * 0.5 bytes) 符合 W4 精度估算，计算 1792/13.5 ≈ 132.7 及 132.7*0.8 ≈ 106.2 数值准确，且 106.2/59.6 (4090理论值) ≈ 1.78 倍关系成立。

## Search Query

RTX 5090 Qwen3-27B W4 tokens per second benchmark
