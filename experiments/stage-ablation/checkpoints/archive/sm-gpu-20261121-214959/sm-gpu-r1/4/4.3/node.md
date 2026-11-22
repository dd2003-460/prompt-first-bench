# N24: 代表工作点 B（数据中心高容量）：以 NVIDIA A100 40GB (1.6 TB/s) 为例，单卡无法容纳 BF16 Qwen3-27B (54GB)，需

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

代表工作点 B（数据中心高容量）：以 NVIDIA A100 40GB (1.6 TB/s) 为例，单卡无法容纳 BF16 Qwen3-27B (54GB)，需 2 卡；若使用 FP8 (27GB) 单卡可容纳，理论 Decode 吞吐上限约为 1600 / 27 ≈ 59.3 tokens/s，展示高带宽数据中心卡的优势。

## Corrected Claim

代表工作点 B（数据中心高容量）：以 NVIDIA A100 40GB (1.6 TB/s) 为例，单卡无法容纳 BF16 Qwen3-27B (54GB)，需 2 卡；若使用 FP8 (27GB) 单卡可容纳，理论 Decode 吞吐上限约为 1600 / 27 ≈ 59.3 tokens/s，展示高带宽数据中心卡的优势。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 40GB 显存无法容纳 54GB 模型需 2 卡，FP8 27GB 可单卡容纳；Decode 吞吐受带宽限制，1.6TB/s / 27GB ≈ 59.3 tokens/s 计算正确且量级合理。

## Search Query

NVIDIA A100 40GB memory bandwidth GB/s FP8 inference throughput
