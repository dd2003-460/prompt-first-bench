# N152: 在主流消费级平台 (Z790/X670) 上，第二张 PCIe 插槽通常由 PCH 提供，物理链路为 PCIe 4.0 x4，双向带宽约为 8 GB/s；对于 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在主流消费级平台 (Z790/X670) 上，第二张 PCIe 插槽通常由 PCH 提供，物理链路为 PCIe 4.0 x4，双向带宽约为 8 GB/s；对于 2x RTX 4090 TP=2 方案，若第二张卡运行在 x4 模式，其有效显存带宽上限被限制在 8 GB/s，导致 Decode 吞吐量上限降至 ~0.14 tokens/s (55GB/8GB/s)，相比双 x16 方案的 ~30 tokens/s 性能损失超过 99%。

## Corrected Claim

在主流消费级平台 (Z790/X670) 上，第二张 PCIe 插槽通常由 PCH 提供，物理链路为 PCIe 4.0 x4，双向带宽约为 8 GB/s；对于 2x RTX 4090 TP=2 方案，若第二张卡运行在 x4 模式，其有效显存带宽上限被限制在 8 GB/s，导致 Decode 吞吐量上限降至 ~0.14 tokens/s (55GB/8GB/s)，相比双 x16 方案的 ~30 tokens/s 性能损失超过 99%。

## Evidence

先验知识/题面给定，逻辑校验通过：Z790/X670平台第二插槽确为PCH提供的PCIe 4.0 x4（双向约8GB/s）；55GB/8GB/s=6.875s，1/6.875≈0.145 tokens/s，与~0.14 tokens/s吻合；相比30 tokens/s损失>99%计算正确。
