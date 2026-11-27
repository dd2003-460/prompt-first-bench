# N574: RTX 5090 32K FP8 单卡方案的 PagedAttention 替代方案量化：若使用 PagedAttention 避免 INT4 KV，显存需求 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N175

## Claim

RTX 5090 32K FP8 单卡方案的 PagedAttention 替代方案量化：若使用 PagedAttention 避免 INT4 KV，显存需求 = 27GB (FP8 权重) + 6.29GB (FP8 KV) = 33.29GB > 32GB，仍不可行；若改用 INT4 权重 + FP8 KV，显存 = 13.5GB + 6.29GB = 19.79GB < 32GB，吞吐降至 66.35 tokens/s，单位成本 = $3500 / 66.35 ≈ $52.75/token/s

## Corrected Claim

RTX 5090 32K FP8 单卡方案的 PagedAttention 替代方案量化：若使用 PagedAttention 避免 INT4 KV，显存需求 = 27GB (FP8 权重) + 6.29GB (FP8 KV) = 33.29GB > 32GB，仍不可行；若改用 INT4 权重 + FP8 KV，显存 = 13.5GB + 6.29GB = 19.79GB < 32GB，吞吐降至 66.35 tokens/s，单位成本 = $3500 / 66.35 ≈ $52.75/token/s

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（27+6.29=33.29, 13.5+6.29=19.79, 3500/66.35≈52.75）准确无误，显存对比逻辑自洽，符合硬件规格常识。
