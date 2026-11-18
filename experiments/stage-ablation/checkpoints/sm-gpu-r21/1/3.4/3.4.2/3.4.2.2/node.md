# N159: 若 AMD 平台仅支持 BF16 推理 (回退)，显存占用将从 FP8 的 27.8 GB 增加到 55.6 GB，导致 32K 上下文下 KV Cache 最

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

若 AMD 平台仅支持 BF16 推理 (回退)，显存占用将从 FP8 的 27.8 GB 增加到 55.6 GB，导致 32K 上下文下 KV Cache 最大并发数从 FP8 的 N 降至 BF16 的 N/2 (假设权重占用主导)，具体并发数需根据总显存和 KV Cache 大小计算

## Corrected Claim

若 AMD 平台仅支持 BF16 推理 (回退)，显存占用将从 FP8 的 27.8 GB 增加到 55.6 GB，导致 32K 上下文下 KV Cache 最大并发数从 FP8 的 N 降至 BF16 的 N/2 (假设权重占用主导)，具体并发数需根据总显存和 KV Cache 大小计算

## Evidence

先验知识/题面给定，逻辑校验通过：BF16 精度为 FP8 的 2 倍，显存占用翻倍（27.8GB * 2 = 55.6GB），在权重占用主导且总显存固定的假设下，剩余用于 KV Cache 的空间减半，故最大并发数降为 N/2，推导自洽。
