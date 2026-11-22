# N190: INT8 单卡 4090 可行性验证：27GB (权重, 若 INT8 则 27GB) + 4.3GB (KV) + 3GB (激活) = 34.3GB > 2

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

INT8 单卡 4090 可行性验证：27GB (权重, 若 INT8 则 27GB) + 4.3GB (KV) + 3GB (激活) = 34.3GB > 24GB (显存)，结论：不可行（注：INT8 权重通常占 27GB，若为 INT4 则不同，此处严格遵循 N78 claim 中 INT8 假设）

## Corrected Claim

INT8 单卡 4090 可行性验证：27GB (权重, 若 INT8 则 27GB) + 4.3GB (KV) + 3GB (激活) = 34.3GB > 24GB (显存)，结论：不可行（注：INT8 权重通常占 27GB，若为 INT4 则不同，此处严格遵循 N78 claim 中 INT8 假设）

## Evidence

先验知识/题面给定，逻辑校验通过：27GB + 4.3GB + 3GB = 34.3GB，显存需求 34.3GB 大于 24GB，结论不可行符合算术逻辑。
