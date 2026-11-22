# N142: 修正 N59 公式中的 H_LRU_original：根据 N70/N71，在给定参数下容量约束非绑定（K_max >> N），无更新时的命中率 H_LRU_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

修正 N59 公式中的 H_LRU_original：根据 N70/N71，在给定参数下容量约束非绑定（K_max >> N），无更新时的命中率 H_LRU_original ≈ 1.0（而非 N56 中假设的 0.85）。因此 Discount_Factor = 1 - λ_update * (E[Size|Updated]/E[Size]) * (1 - 1.0) = 1.0。这表明在容量充足时，更新率对字节命中率的影响需通过‘失效对象重新填充的时间窗口’而非简单的命中率折损来衡量。

## Corrected Claim

修正 N59 公式中的 H_LRU_original：根据 N70/N71，在给定参数下容量约束非绑定（K_max >> N），无更新时的命中率 H_LRU_original ≈ 1.0（而非 N56 中假设的 0.85）。因此 Discount_Factor = 1 - λ_update * (E[Size|Updated]/E[Size]) * (1 - 1.0) = 1.0。这表明在容量充足时，更新率对字节命中率的影响需通过‘失效对象重新填充的时间窗口’而非简单的命中率折损来衡量。

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU缓存中，若容量K_max远大于对象总数N（非绑定约束），所有对象常驻缓存，无更新时命中率确为1.0；代入公式(1-1.0)项为0，Discount_Factor为1.0，推导自洽。
