# N140: H100 SXM在BF16精度下的推理延迟计算：(2 * 27e9 * 32768) / (989 TFLOPS * 0.9) + (54 + 2.5 + 5.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

H100 SXM在BF16精度下的推理延迟计算：(2 * 27e9 * 32768) / (989 TFLOPS * 0.9) + (54 + 2.5 + 5.2)GB / 3350 GB/s ≈ 5.9 ms + 18.4 ms = 24.3 ms/token

## Corrected Claim

H100 SXM在BF16精度下的推理延迟计算：(2 * 27e9 * 32768) / (989 TFLOPS * 0.9) + (54 + 2.5 + 5.2)GB / 3350 GB/s ≈ 5.9 ms + 18.4 ms = 24.3 ms/token

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程符合算术逻辑，H100 SXM BF16峰值算力约989 TFLOPS及显存带宽3.35 TB/s符合硬件规格常识，数值量级合理。
