# N443: 修正 A100 80GB BF16 理论 Decode 吞吐量：基于 N370 确认的 KV Cache 占用 8 GB（而非 N150 中错误的 32.77 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N150

## Claim

修正 A100 80GB BF16 理论 Decode 吞吐量：基于 N370 确认的 KV Cache 占用 8 GB（而非 N150 中错误的 32.77 GB，后者源于 n_kv_heads 参数错误），计算为 2039 / (54 + 8) ≈ 32.9 tokens/s。

## Corrected Claim

修正 A100 80GB BF16 理论 Decode 吞吐量：基于 N370 确认的 KV Cache 占用 8 GB（而非 N150 中错误的 32.77 GB，后者源于 n_kv_heads 参数错误），计算为 2039 / (54 + 8) ≈ 32.9 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：2039 / (54 + 8) = 2039 / 62 ≈ 32.887，四舍五入为 32.9，计算无误且量级合理。
