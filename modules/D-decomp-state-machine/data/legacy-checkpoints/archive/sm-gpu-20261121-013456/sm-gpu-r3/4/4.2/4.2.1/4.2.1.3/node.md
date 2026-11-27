# N191: INT4 单卡 4090 可行性验证：13.5GB (权重) + 4.3GB (KV, 若 FP8) + 3GB (激活) = 20.8GB < 24GB (显

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

INT4 单卡 4090 可行性验证：13.5GB (权重) + 4.3GB (KV, 若 FP8) + 3GB (激活) = 20.8GB < 24GB (显存)，结论：可行，余量 3.2GB

## Corrected Claim

INT4 单卡 4090 可行性验证：13.5GB (权重) + 4.3GB (KV, 若 FP8) + 3GB (激活) = 20.8GB < 24GB (显存)，结论：可行，余量 3.2GB

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+4.3+3=20.8GB，24-20.8=3.2GB，数值计算准确且符合显存预算逻辑。
