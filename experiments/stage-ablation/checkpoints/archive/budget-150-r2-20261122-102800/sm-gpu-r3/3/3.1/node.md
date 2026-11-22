# N18: 工作点1（高保真/高显存）：BF16精度，质量损失≈0%（参考基准），显存占用54GB权重+4.29GB KV=58.29GB，适合A100-80GB/H100

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

工作点1（高保真/高显存）：BF16精度，质量损失≈0%（参考基准），显存占用54GB权重+4.29GB KV=58.29GB，适合A100-80GB/H100-80GB/M3 Ultra 96GB+，推理速度受限于显存带宽，tokens/s ≈ 显存带宽 / 模型字节数 = 2039 GB/s / 58.29 GB ≈ 35 tokens/s (A100), 3350 GB/s / 58.29 GB ≈ 57 tokens/s (H100)

## Corrected Claim

工作点1（高保真/高显存）：BF16精度，质量损失≈0%（参考基准），显存占用54GB权重+4.29GB KV=58.29GB，适合A100-80GB/H100-80GB/M3 Ultra 96GB+，推理速度受限于显存带宽，tokens/s ≈ 显存带宽 / 模型字节数 = 2039 GB/s / 58.29 GB ≈ 35 tokens/s (A100), 3350 GB/s / 58.29 GB ≈ 57 tokens/s (H100)

## Evidence

先验知识/题面给定，逻辑校验通过：显存占用计算（54+4.29=58.29GB）正确；推理速度估算基于显存带宽瓶颈模型（带宽/模型大小），数值量级符合A100/H100硬件规格与LLM推理常识。

## Search Query

BF16 LLM inference throughput tokens per second A100 H100 memory bandwidth bound
