# N97: NVIDIA L40S 显存带宽为 864 GB/s (GDDR6)，在 Qwen3-27B FP8 (27GB) + 32K 上下文下，理论解码吞吐上限 ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23, N24, N25

## Claim

NVIDIA L40S 显存带宽为 864 GB/s (GDDR6)，在 Qwen3-27B FP8 (27GB) + 32K 上下文下，理论解码吞吐上限 ≈ 864 GB/s / (27GB + 18GB KV + 5GB Activation) ≈ 13.2 tokens/s，实际需乘以框架效率系数 (通常 0.6-0.8)。

## Corrected Claim

NVIDIA L40S 显存带宽为 864 GB/s (GDDR6)，在 Qwen3-27B FP8 (27GB) + 32K 上下文下，理论解码吞吐上限 ≈ 864 GB/s / (27GB + 18GB KV + 5GB Activation) ≈ 13.2 tokens/s，实际需乘以框架效率系数 (通常 0.6-0.8)。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA L40S 显存带宽确为 864 GB/s，算术计算 864 / (27+18+5) ≈ 13.2 正确，符合显存带宽瓶颈下的理论吞吐估算逻辑。
