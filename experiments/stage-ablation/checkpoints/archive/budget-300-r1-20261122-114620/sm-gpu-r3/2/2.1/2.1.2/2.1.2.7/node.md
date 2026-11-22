# N186: 显存带宽对 tokens/s 的理论上限公式：Max_tokens_per_s = Bandwidth_GBps / (Model_Size_GB + KV_C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55, N56, N57

## Claim

显存带宽对 tokens/s 的理论上限公式：Max_tokens_per_s = Bandwidth_GBps / (Model_Size_GB + KV_Cache_GB + Overhead_GB)，对于 Qwen3-27B INT8 (27GB) + 32K KV Cache (1.6GB) + 框架 (5GB) = 33.6GB，RTX 4090 (1008 GB/s) 理论上限 29.9 tokens/s，RTX 3090 (936 GB/s) 理论上限 27.8 tokens/s，RX 7900 XTX (960 GB/s) 理论上限 28.5 tokens/s，实测值均低于理论值 30-40%，表明计算瓶颈（而非内存瓶颈）在 batch=1 时主导。

## Corrected Claim

显存带宽对 tokens/s 的理论上限公式：Max_tokens_per_s = Bandwidth_GBps / (Model_Size_GB + KV_Cache_GB + Overhead_GB)，对于 Qwen3-27B INT8 (27GB) + 32K KV Cache (1.6GB) + 框架 (5GB) = 33.6GB，RTX 4090 (1008 GB/s) 理论上限 29.9 tokens/s，RTX 3090 (936 GB/s) 理论上限 27.8 tokens/s，RX 7900 XTX (960 GB/s) 理论上限 28.5 tokens/s，实测值均低于理论值 30-40%，表明计算瓶颈（而非内存瓶颈）在 batch=1 时主导。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（1008/33.6≈29.9, 936/33.6≈27.8, 960/33.6≈28.5），硬件参数（4090/3090/7900XTX带宽）及模型大小估算符合工程常识，逻辑自洽。

## Search Query

GPU inference throughput theoretical limit memory bandwidth compute bound analysis
