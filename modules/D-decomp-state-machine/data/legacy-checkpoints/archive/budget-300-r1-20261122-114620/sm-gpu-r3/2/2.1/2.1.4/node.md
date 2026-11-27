# N57: 消费级 GPU 显存带宽对比：RTX 4090 (1008 GB/s) > RTX 3090 (936 GB/s) > RX 7900 XTX (960 GB/

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

消费级 GPU 显存带宽对比：RTX 4090 (1008 GB/s) > RTX 3090 (936 GB/s) > RX 7900 XTX (960 GB/s) > RX 7900 XT (960 GB/s)；带宽差异直接映射到 tokens/s 上限，4090 理论最大吞吐比 3090 高 7.7% (1008/936)

## Corrected Claim

消费级 GPU 显存带宽对比：RTX 4090 (1008 GB/s) > RX 7900 XTX (960 GB/s) = RX 7900 XT (960 GB/s) > RTX 3090 (936 GB/s)；带宽差异直接映射到 tokens/s 上限，4090 理论最大吞吐比 3090 高约 7.7% (1008/936 ≈ 1.077)

## Evidence

[质询]排序逻辑错误：陈述中声称 RX 7900 XTX (960 GB/s) > RX 7900 XT (960 GB/s)，但两者数值相同，不存在大于关系；且 RTX 3090 (936 GB/s) 小于 RX 7900 XTX (960 GB/s)，但陈述将其排在 RX 7900 XTX 之前，导致整体排序链条（4090 > 3090 > 7900XTX）在数值上不自洽（936 < 960）。 | 陈述内部存在数值比较矛盾：936 (RTX 3090) 被排在 960 (RX 7900 XTX) 之前，违背数值大小逻辑；且 960 > 960 为假。
