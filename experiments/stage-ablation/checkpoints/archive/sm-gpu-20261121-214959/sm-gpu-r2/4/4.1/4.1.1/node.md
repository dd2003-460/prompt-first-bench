# N87: 工作点 A（消费级高带宽低容量）：RTX 4090 (24GB, 1008 GB/s) 运行 Qwen3-27B INT4 (13.5GB) + FP8 KV 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

工作点 A（消费级高带宽低容量）：RTX 4090 (24GB, 1008 GB/s) 运行 Qwen3-27B INT4 (13.5GB) + FP8 KV (6.29GB)，模型在显存中总大小 19.79GB，理论 Decode 吞吐 = 1008 / 19.79 ≈ 50.9 tokens/s。此工作点代表单卡消费级方案的理论上限，但受限于 24GB 容量，无法运行 BF16。

## Corrected Claim

工作点 A（消费级高带宽低容量）：RTX 4090 (24GB, 1008 GB/s) 运行 Qwen3-27B INT4 (13.5GB) + FP8 KV (6.29GB)，模型在显存中总大小 19.79GB，理论 Decode 吞吐 = 1008 / 19.79 ≈ 50.9 tokens/s。此工作点代表单卡消费级方案的理论上限，但受限于 24GB 容量，无法运行 BF16。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与容量 24GB 符合硬件规格；Qwen3-27B INT4 模型大小约 13.5GB 及 FP8 KV 缓存 6.29GB 的估算在合理量级内；总显存占用 19.79GB 小于 24GB，且 Decode 吞吐计算 1008/19.79 ≈ 50.9 tokens/s 符合算术逻辑；BF16 下模型大小将翻倍至约 27GB 以上，确实超出 24GB 容量限制。
