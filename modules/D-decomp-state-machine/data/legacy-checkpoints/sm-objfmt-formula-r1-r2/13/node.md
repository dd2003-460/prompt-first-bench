# N120: 候选硬件完整性验证：排除低端消费级显卡（如 RTX 3060 12GB/16GB, RTX 4060 Ti 16GB）的理由是其最大显存容量 < 24GB，无法

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件完整性验证：排除低端消费级显卡（如 RTX 3060 12GB/16GB, RTX 4060 Ti 16GB）的理由是其最大显存容量 < 24GB，无法在 BF16/FP8 精度下同时容纳 Qwen3-27B 权重（~27-54GB）和 32K 上下文的 KV Cache（~4-8GB），即使使用 INT4 量化（权重~15GB + KV~2GB = 17GB），也几乎耗尽显存且缺乏余量处理激活值，导致 OOM 风险极高，故不进入性价比核心比较集。

## Corrected Claim

候选硬件完整性验证：排除低端消费级显卡（如 RTX 3060 12GB/16GB, RTX 4060 Ti 16GB）的理由是其最大显存容量 < 24GB，无法在 BF16/FP8 精度下同时容纳 Qwen3-27B 权重（~27-54GB）和 32K 上下文的 KV Cache（~4-8GB），即使使用 INT4 量化（权重~15GB + KV~2GB = 17GB），也几乎耗尽显存且缺乏余量处理激活值，导致 OOM 风险极高，故不进入性价比核心比较集。

## Evidence

检索失败: no sources from any channel (all 5 failed)
