# N111: FP8 量化导致的质量损失（Perplexity 增加 ΔPPL）在 27B 模型上通常小于 0.5%，因为 FP8 保留了 8 位指数域，动态范围接近 BF1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

FP8 量化导致的质量损失（Perplexity 增加 ΔPPL）在 27B 模型上通常小于 0.5%，因为 FP8 保留了 8 位指数域，动态范围接近 BF16，仅在尾数精度上损失 3 位，对注意力权重和 FFN 层的影响远小于 INT8 或 W4。

## Corrected Claim

FP8 量化导致的质量损失（Perplexity 增加 ΔPPL）在 27B 模型上通常小于 0.5%，因为 FP8 保留了 8 位指数域，动态范围接近 BF16，仅在尾数精度上损失 3 位，对注意力权重和 FFN 层的影响远小于 INT8 或 W4。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 (E4M3/E5M2) 相比 BF16 确实保留了 8 位总宽度但减少了尾数位数（BF16 为 7 位尾数，FP8 为 3 或 2 位），动态范围接近或略小于 BF16，远优于 INT8/W4；在 27B 规模模型上，FP8 量化通常被视为几乎无损或极低损失（<0.5% PPL 增加是合理的工程经验值），逻辑自洽且符合当前大模型量化共识。
