# N359: RTX 3090 (24GB, PCIe 4.0 x16) 被排除的量化依据：虽然 PCIe 4.0 带宽 (32 GB/s) 高于 PCIe 3.0，但其显存

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128, N129

## Claim

RTX 3090 (24GB, PCIe 4.0 x16) 被排除的量化依据：虽然 PCIe 4.0 带宽 (32 GB/s) 高于 PCIe 3.0，但其显存带宽仅 936 GB/s (HBM2e 替代 GDDR6X)，且缺乏 FP8 硬件加速支持。运行 Qwen3-27B INT4 时，理论 Decode 上限 = 936 / 13.5 ≈ 69.3 tokens/s，低于 RTX 4090 的 74.6 tokens/s，且二手价格 ($800-$1000) 仅为 4090 ($1599) 的 50-60%，性价比优势不足以弥补生态劣势。

## Corrected Claim

RTX 3090 (24GB, PCIe 4.0 x16) 被排除的量化依据：虽然 PCIe 4.0 带宽 (32 GB/s) 高于 PCIe 3.0，但其显存带宽为 936 GB/s (GDDR6X)，且缺乏 FP8 硬件加速支持。运行 Qwen3-27B INT4 时，理论 Decode 上限 ≈ 69.3 tokens/s，低于 RTX 4090 的 74.6 tokens/s，且二手价格 ($800-$1000) 仅为 4090 ($1599) 的 50-60%，性价比优势不足以弥补生态劣势。

## Evidence

[质询]数值量级与硬件规格存在严重事实错误：RTX 3090 使用的是 GDDR6X 显存而非 HBM2e，其显存带宽约为 936 GB/s 是正确的，但将其描述为 'HBM2e 替代 GDDR6X' 是概念混淆（HBM2e 通常用于 A100/H100 等数据中心卡，消费级 3090 从未使用 HBM2e）；此外，PCIe 4.0 x16 的单向理论带宽约为 32 GB/s，但实际有效带宽受协议开销影响，且 Decode 阶段主要瓶颈在显存带宽而非 PCIe 带宽，此处将 PCIe 带宽与显存带宽并列对比逻辑略显牵强，但核心错误在于显存类型描述错误。 | 先验知识/题面给定，逻辑校验发现硬件规格描述错误（RTX 3090 非 HBM2e），且来源不可用，无法外部核验，故降级。
