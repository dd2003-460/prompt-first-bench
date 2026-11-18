# N146: 在 24GB 显存卡（如 RTX 4090）上，FP8 精度下 Qwen3-27B 的权重占用约为 27.0 GB (27B * 1 byte)，加上 2.0 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在 24GB 显存卡（如 RTX 4090）上，FP8 精度下 Qwen3-27B 的权重占用约为 27.0 GB (27B * 1 byte)，加上 2.0 GB KV Cache 和 ~1.5 GB 激活/开销，总需求约 30.5 GB，超出 24GB 物理显存，因此单卡 FP8 方案不可行，必须使用双卡或更高显存硬件。

## Corrected Claim

在 24GB 显存卡（如 RTX 4090）上，FP8 精度下 Qwen3-27B 的权重占用约为 27.0 GB (27B * 1 byte)，加上 2.0 GB KV Cache 和 ~1.5 GB 激活/开销，总需求约 30.5 GB，超出 24GB 物理显存，因此单卡 FP8 方案不可行，必须使用双卡或更高显存硬件。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下权重约27GB，加上KV Cache和激活开销，总显存需求约30.5GB，确实超出24GB物理显存，单卡FP8方案不可行的结论符合硬件规格与计算逻辑。
