# N388: 工作点1（高保真基准）：Q_norm(BF16) = 1.0，作为分母基准；对应硬件显存占用为 54.6 GB (27B * 2 bytes)，在 24GB 显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

工作点1（高保真基准）：Q_norm(BF16) = 1.0，作为分母基准；对应硬件显存占用为 54.6 GB (27B * 2 bytes)，在 24GB 显存卡上不可行，仅在 40GB+ 显存卡（A100/H100/2x4090）上可行。

## Corrected Claim

工作点1（高保真基准）：Q_norm(BF16) = 1.0，作为分母基准；对应硬件显存占用为 54.6 GB (27B * 2 bytes)，在 24GB 显存卡上不可行，仅在 40GB+ 显存卡（A100/H100/2x4090）上可行。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 2字节(BF16) = 54GB，显存占用计算正确；54GB > 24GB故不可行，54GB < 40GB+故可行，逻辑自洽。
