# N159: NVIDIA L40S (48GB) 运行 Qwen3-27B BF16 TP=2 时，每卡显存占用 29.68GB，剩余 18.32GB；L40S 带宽 86

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

NVIDIA L40S (48GB) 运行 Qwen3-27B BF16 TP=2 时，每卡显存占用 29.68GB，剩余 18.32GB；L40S 带宽 864 GB/s (PCIe) 或 864 GB/s (SXM? 需确认版本)，相比 RTX 5090 (1792 GB/s) 带宽低 51%，但价格更高 ($3000+)，需对比其能效比 (Watts) 和 TCO 以确定是否优于 2x RTX 5090 方案。

## Corrected Claim

NVIDIA L40S (48GB) 运行 Qwen3-27B BF16 TP=2 时，每卡显存占用约 29.68GB，剩余约 18.32GB；L40S 显存带宽为 864 GB/s（GDDR6 理论值），相比 RTX 5090 (1792 GB/s) 带宽低约 51%。由于 L40S 价格较高（$3000+）且能效比数据需具体工况确认，建议结合最新市场价格和 TCO 分析，谨慎评估其相对于 2x RTX 5090 方案的性价比。

## Evidence

[质询]L40S 的显存带宽通常标称为 864 GB/s，但这是基于 GDDR6 的理论峰值带宽，实际有效带宽受 PCIe 版本（Gen4/Gen5）和拓扑影响，且 864 GB/s 并非 PCIe 带宽（PCIe 5.0 x16 仅约 64 GB/s），此处存在概念混淆；此外，Qwen3-27B 在 BF16 下模型权重约 54GB，TP=2 时每卡理论权重占用约 27GB，加上 KV Cache 和激活值，29.68GB 的占用量级合理，但 L40S 与 RTX 5090 的价格和能效对比属于动态市场数据，缺乏实时来源支持。 | 先验知识/题面给定，逻辑校验通过：L40S 48GB 显存、864 GB/s 带宽、Qwen3-27B BF16 权重约 54GB（TP=2 每卡 27GB+开销≈29.68GB）均符合工程常识；但价格、能效比及与 RTX 5090 的具体对比属于经验事实，且无外部来源支持，故降级。

## Search Query

NVIDIA L40S 48GB Qwen3-27B BF16 throughput vs RTX 5090
