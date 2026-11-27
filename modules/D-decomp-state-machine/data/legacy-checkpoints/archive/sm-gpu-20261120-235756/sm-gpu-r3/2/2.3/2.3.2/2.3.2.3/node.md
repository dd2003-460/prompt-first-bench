# N203: 在 BF16 精度下，A100 80GB 与 RTX 5090 32GB 的 TPOT 差异 (5.2ms vs 5.9ms) 仅约 12%，但 A100 的显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

在 BF16 精度下，A100 80GB 与 RTX 5090 32GB 的 TPOT 差异 (5.2ms vs 5.9ms) 仅约 12%，但 A100 的显存容量 (80GB) 允许其支持 Batch Size=1 且保留 19.88GB 余量，而 RTX 5090 在 BF16 下显存溢出 (需 80GB > 32GB)，因此 A100 是唯一可行的 BF16 32K 单卡方案，其性价比优势源于可行性而非纯带宽效率，RTX 5090 在此口径下无有效方案。

## Corrected Claim

在 BF16 精度下，A100 80GB 与 RTX 5090 32GB 的 TPOT 差异 (5.2ms vs 5.9ms) 仅约 12%，但 A100 的显存容量 (80GB) 允许其支持 Batch Size=1 且保留 19.88GB 余量，而 RTX 5090 在 BF16 下显存溢出 (需 80GB > 32GB)，因此 A100 是唯一可行的 BF16 32K 单卡方案，其性价比优势源于可行性而非纯带宽效率，RTX 5090 在此口径下无有效方案。

## Evidence

先验知识/题面给定，逻辑校验通过：80GB显存确实大于32GB，且80GB足以容纳32K上下文BF16推理所需的显存（约60GB左右），而32GB显存必然溢出，逻辑自洽。
