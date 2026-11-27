# N304: 总激活值峰值合成与N20的2.5GB对比：总激活值峰值 ≈ 注意力峰值 + MLP峰值 + LayerNorm/RMSNorm中间值。注意力峰值 (Flash 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

总激活值峰值合成与N20的2.5GB对比：总激活值峰值 ≈ 注意力峰值 + MLP峰值 + LayerNorm/RMSNorm中间值。注意力峰值 (Flash Attn, BF16) ≈ 1.07-2.15 GB (N173)。MLP峰值 (BF16) ≈ 0.72-0.9 GB (N176/N177)。LayerNorm中间值 ≈ batch * seq_len * hidden_size * dtype_size ≈ 1 * 32768 * 4096 * 2 ≈ 268 MB。总和 ≈ 2.06 - 3.32 GB。N20的2.5GB估算落在该区间内，但主要受注意力部分主导，且假设了BF16计算精度。若使用FP8计算，峰值可降低50%。

## Corrected Claim

总激活值峰值合成与N20的2.5GB对比：总激活值峰值 ≈ 注意力峰值 + MLP峰值 + LayerNorm/RMSNorm中间值。注意力峰值 (Flash Attn, BF16) ≈ 1.07-2.15 GB (N173)。MLP峰值 (BF16) ≈ 0.72-0.9 GB (N176/N177)。LayerNorm中间值 ≈ batch * seq_len * hidden_size * dtype_size ≈ 1 * 32768 * 4096 * 2 ≈ 268 MB。总和 ≈ 2.06 - 3.32 GB。N20的2.5GB估算落在该区间内，但主要受注意力部分主导，且假设了BF16计算精度。若使用FP8计算，峰值可降低50%。

## Evidence

先验知识/题面给定，逻辑校验通过：各组件峰值估算量级合理（注意力~1-2GB, MLP~0.7-0.9GB, Norm~0.27GB），总和区间2.06-3.32GB覆盖2.5GB，且BF16/FP8精度对显存影响的描述符合硬件常识。
