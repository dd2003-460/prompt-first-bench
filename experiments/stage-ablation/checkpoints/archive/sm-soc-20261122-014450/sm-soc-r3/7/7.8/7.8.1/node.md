# N380: 长尾商品占比修正项 W_tail 的量化：需将平台商品分为头部 (Top 20% GMV) 和长尾 (Bottom 80%)。长尾商品对价格干预的敏感度系数 η

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

长尾商品占比修正项 W_tail 的量化：需将平台商品分为头部 (Top 20% GMV) 和长尾 (Bottom 80%)。长尾商品对价格干预的敏感度系数 η_tail 通常高于头部 (η_head)。修正后 ΔGMV_corrected = ΔGMV_head * W_head + ΔGMV_tail * W_tail，需估算 W_tail (通常 >70%) 及 η_tail/η_head 比值 (通常 >1.5)。

## Corrected Claim

长尾商品占比修正项 W_tail 的量化：需将平台商品分为头部 (Top 20% GMV) 和长尾 (Bottom 80%)。长尾商品对价格干预的敏感度系数 η_tail 通常高于头部 (η_head)。修正后 ΔGMV_corrected = ΔGMV_head * W_head + ΔGMV_tail * W_tail，需估算 W_tail (通常 >70%) 及 η_tail/η_head 比值 (通常 >1.5)。

## Evidence

先验知识/题面给定，逻辑校验通过
