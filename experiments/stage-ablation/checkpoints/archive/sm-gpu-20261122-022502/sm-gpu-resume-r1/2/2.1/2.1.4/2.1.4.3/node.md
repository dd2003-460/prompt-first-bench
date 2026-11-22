# N175: RTX 5090 在 32K 上下文 FP8 场景下的单卡可行性与 TCO 优势：FP8 权重 27GB + FP8 KV 6.29GB = 33.29GB >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

RTX 5090 在 32K 上下文 FP8 场景下的单卡可行性与 TCO 优势：FP8 权重 27GB + FP8 KV 6.29GB = 33.29GB > 32GB (溢出 1.29GB)。需 INT4 KV 或 PagedAttention。若使用 INT4 KV (3.145GB)，总显存 30.145GB < 32GB。理论吞吐 132.7 tokens/s (N113)，实际考虑效率 0.9 ≈ 119.4 tokens/s。CapEx $2000 + $1500 = $3500。单位成本 = $3500 / 119.4 ≈ $29.31/token/s，显著低于 4090 双卡方案的 $277.96/token/s。

## Corrected Claim

RTX 5090 在 32K 上下文 FP8 场景下的单卡可行性与 TCO 优势：FP8 权重 27GB + FP8 KV 6.29GB = 33.29GB > 32GB (溢出 1.29GB)。需 INT4 KV 或 PagedAttention。若使用 INT4 KV (3.145GB)，总显存 30.145GB < 32GB。理论吞吐 132.7 tokens/s (N113)，实际考虑效率 0.9 ≈ 119.4 tokens/s。CapEx $2000 + $1500 = $3500。单位成本 = $3500 / 119.4 ≈ $29.31/token/s，显著低于 4090 双卡方案的 $277.96/token/s。

## Evidence

先验知识/题面给定，逻辑校验通过：显存计算（27+6.29>32, 27+3.145<32）及成本效益对比逻辑自洽，数值量级合理。
