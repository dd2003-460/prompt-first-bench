# N72: BF16 精度下总显存需求下限计算：54 GB (权重) + 4.3 GB (KV Cache, GQA) + 3 GB (激活/缓冲) = 61.3 GB，因

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

BF16 精度下总显存需求下限计算：54 GB (权重) + 4.3 GB (KV Cache, GQA) + 3 GB (激活/缓冲) = 61.3 GB，因此单卡 24GB 或 48GB 无法运行 BF16 全精度 32K 上下文

## Corrected Claim

BF16 精度下总显存需求下限计算：54 GB (权重) + 4.3 GB (KV Cache, GQA) + 3 GB (激活/缓冲) = 61.3 GB，因此单卡 24GB 或 48GB 无法运行 BF16 全精度 32K 上下文

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下32K上下文大模型显存需求通常远超单卡24/48GB，数值量级与工程常识一致
