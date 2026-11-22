# N210: RTX 4090 在 BF16 下 Decode 理论最大吞吐为 1008 GB/s / 55.07 GB ≈ 18.3 tokens/s；考虑内存控制器效率 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

RTX 4090 在 BF16 下 Decode 理论最大吞吐为 1008 GB/s / 55.07 GB ≈ 18.3 tokens/s；考虑内存控制器效率 (60%-80%)，实际吞吐约为 11-14.6 tokens/s；H100 SXM 理论最大吞吐为 3350 GB/s / 55.07 GB ≈ 60.8 tokens/s，实际吞吐约为 36-48.6 tokens/s

## Corrected Claim

RTX 4090 在 BF16 下 Decode 理论最大吞吐为 1008 GB/s / 55.07 GB ≈ 18.3 tokens/s；考虑内存控制器效率 (60%-80%)，实际吞吐约为 11-14.6 tokens/s；H100 SXM 理论最大吞吐为 3350 GB/s / 55.07 GB ≈ 60.8 tokens/s，实际吞吐约为 36-48.6 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与 H100 SXM 3350 GB/s 符合硬件规格，55.07 GB 模型大小在 LLM 常见量级，算术推导（1008/55.07≈18.3, 3350/55.07≈60.8）及效率折损逻辑自洽。

## Search Query

RTX 4090 H100 decode throughput actual vs theoretical LLM
