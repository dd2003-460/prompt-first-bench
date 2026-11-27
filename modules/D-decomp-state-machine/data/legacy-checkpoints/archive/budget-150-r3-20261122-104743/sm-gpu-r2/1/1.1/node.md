# N7: 模型权重显存占用 (Weight Memory) = 27,000,000,000 × P_bytes，其中 P_bytes ∈ {2 (BF16), 1 (F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

模型权重显存占用 (Weight Memory) = 27,000,000,000 × P_bytes，其中 P_bytes ∈ {2 (BF16), 1 (FP8/INT8), 0.5 (NVFP4/W4)}，计算结果分别为 54GB, 27GB, 13.5GB

## Corrected Claim

模型权重显存占用 (Weight Memory) = 27,000,000,000 × P_bytes，其中 P_bytes ∈ {2 (BF16), 1 (FP8/INT8), 0.5 (NVFP4/W4)}，计算结果分别为 54GB, 27GB, 13.5GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在BF16(2字节)、FP8/INT8(1字节)、NVFP4/W4(0.5字节)下的显存占用计算分别为54GB、27GB、13.5GB，数值量级与算术逻辑均正确。
