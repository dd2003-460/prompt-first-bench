# N189: FP8 单卡 4090 可行性验证：27GB (权重) + 4.3GB (KV) + 3GB (激活) = 34.3GB > 24GB (显存)，结论：不可行，

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

FP8 单卡 4090 可行性验证：27GB (权重) + 4.3GB (KV) + 3GB (激活) = 34.3GB > 24GB (显存)，结论：不可行，需至少 48GB 显存或更低精度

## Corrected Claim

FP8 单卡 4090 可行性验证：27GB (权重) + 4.3GB (KV) + 3GB (激活) = 34.3GB > 24GB (显存)，结论：不可行，需至少 48GB 显存或更低精度

## Evidence

先验知识/题面给定，逻辑校验通过：27+4.3+3=34.3GB，显存需求34.3GB大于RTX 4090的24GB显存，结论不可行符合算术逻辑与硬件常识。
