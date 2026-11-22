# N537: RTX 5090 单卡 FP8 理论 Decode 吞吐量上限推导：基于带宽瓶颈模型 T_decode = Weight_Size / Bandwidth，27

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N222

## Claim

RTX 5090 单卡 FP8 理论 Decode 吞吐量上限推导：基于带宽瓶颈模型 T_decode = Weight_Size / Bandwidth，27GB / 1792 GB/s ≈ 15.07ms/token，对应 66.3 tokens/s；考虑 KV Cache 读取开销和实际利用率 (70-80%)，实际预期 46-52 tokens/s，修正 N222 中 61.8 tokens/s 的过高估计（未计入 KV 开销和利用率损耗）。

## Corrected Claim

RTX 5090 单卡 FP8 理论 Decode 吞吐量上限推导：基于带宽瓶颈模型 T_decode = Weight_Size / Bandwidth，27GB / 1792 GB/s ≈ 15.07ms/token，对应 66.3 tokens/s；考虑 KV Cache 读取开销和实际利用率 (70-80%)，实际预期 46-52 tokens/s，修正 N222 中 61.8 tokens/s 的过高估计（未计入 KV 开销和利用率损耗）。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存带宽 1792 GB/s 与 27GB 显存规格符合已知硬件参数，带宽瓶颈模型推导逻辑自洽，利用率修正符合工程直觉。
