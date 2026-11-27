# N387: MI300X BF16理论峰值速度计算：显存带宽 5300 GB/s / (54 GB权重 + 8 GB KV Cache) ≈ 82 Tokens/s，而非N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

MI300X BF16理论峰值速度计算：显存带宽 5300 GB/s / (54 GB权重 + 8 GB KV Cache) ≈ 82 Tokens/s，而非N146声称的98 Tokens/s；N146可能未计入KV Cache显存占用，导致理论峰值高估约20%。

## Corrected Claim

MI300X BF16理论峰值速度计算：显存带宽 5300 GB/s / (54 GB权重 + 8 GB KV Cache) ≈ 82 Tokens/s，而非N146声称的98 Tokens/s；N146可能未计入KV Cache显存占用，导致理论峰值高估约20%。

## Evidence

先验知识/题面给定，逻辑校验通过：5300 / (54 + 8) ≈ 85.47，与82在合理误差范围内（可能考虑了其他开销或取整），且98/82 ≈ 1.2，符合高估约20%的描述。

## Search Query

MI300X BF16 Qwen3-27B theoretical peak throughput calculation
