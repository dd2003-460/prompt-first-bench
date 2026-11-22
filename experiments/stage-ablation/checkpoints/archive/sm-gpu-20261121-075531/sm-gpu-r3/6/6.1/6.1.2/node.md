# N323: 理论峰值 TPS 上限公式：TPS_max = Memory_Bandwidth / Bytes_Per_Token；对于 RTX 5090 (1792 GB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

理论峰值 TPS 上限公式：TPS_max = Memory_Bandwidth / Bytes_Per_Token；对于 RTX 5090 (1792 GB/s) 和 RTX 4090 (1008 GB/s)，在 INT8 精度下 Bytes_Per_Token ≈ 28.93GB (含 KV 开销)，理论 TPS_max 分别为 61.9 tokens/s 和 34.8 tokens/s；理论比值为 1.778x，与带宽比值一致。

## Corrected Claim

理论峰值 TPS 上限公式：TPS_max = Memory_Bandwidth / Bytes_Per_Token；对于 RTX 5090 (1792 GB/s) 和 RTX 4090 (1008 GB/s)，在 INT8 精度下 Bytes_Per_Token ≈ 28.93GB (含 KV 开销)，理论 TPS_max 分别为 61.9 tokens/s 和 34.8 tokens/s；理论比值为 1.778x，与带宽比值一致。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 TPS=Bandwidth/Bytes 符合内存带宽瓶颈下的理论上限定义；数值计算 1792/28.93≈61.94 和 1008/28.93≈34.84 准确；比值 1792/1008≈1.778 与带宽比一致，逻辑自洽。
