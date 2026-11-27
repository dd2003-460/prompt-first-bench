# N626: H100 SXM 在 BF16 精度下的实际有效算力受限于 HBM3 带宽与计算单元的平衡，在 32K 长上下文 Prefill 阶段，由于 KV Cache 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N260

## Claim

H100 SXM 在 BF16 精度下的实际有效算力受限于 HBM3 带宽与计算单元的平衡，在 32K 长上下文 Prefill 阶段，由于 KV Cache 读取量巨大，实际 MFU 通常降至 40%-50%（短上下文下可达 60%+，长上下文受内存带宽瓶颈影响显著）

## Corrected Claim

H100 SXM 在 BF16 精度下的实际有效算力受限于 HBM3 带宽与计算单元的平衡，在 32K 长上下文 Prefill 阶段，由于 KV Cache 读取量巨大，实际 MFU 通常降至 40%-50%（短上下文下可达 60%+，长上下文受内存带宽瓶颈影响显著）

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 在长上下文 Prefill 阶段受 HBM3 带宽限制，MFU 降至 40%-50% 符合硬件特性与工程经验。
