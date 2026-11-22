# N101: RTX 4090 (1008 GB/s) 在 BF16 下 Decode 理论最大吞吐为 1008 / 55 ≈ 18.3 tokens/s；H100 SXM 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

RTX 4090 (1008 GB/s) 在 BF16 下 Decode 理论最大吞吐为 1008 / 55 ≈ 18.3 tokens/s；H100 SXM (3350 GB/s) 理论最大吞吐为 3350 / 55 ≈ 60.9 tokens/s。实际吞吐受内存控制器效率影响，通常打 6-8 折。

## Corrected Claim

RTX 4090 (1008 GB/s) 在 BF16 下 Decode 理论最大吞吐为 1008 / 55 ≈ 18.3 tokens/s；H100 SXM (3350 GB/s) 理论最大吞吐为 3350 / 55 ≈ 60.9 tokens/s。实际吞吐受内存控制器效率影响，通常打 6-8 折。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，H100 SXM 约 3350 GB/s，BF16 下 55GB 模型权重读取耗时计算符合算术逻辑，且实际吞吐受内存效率影响打 6-8 折符合工程经验。

## Search Query

RTX 4090 H100 decode throughput theoretical limit 55GB
