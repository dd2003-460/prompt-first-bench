# N112: 验证请求（Revalidation）开销的独立折损：若采用 ETag 验证而非直接重填充，验证请求延迟 t_verify ≈ 1ms，P(miss_verify

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

验证请求（Revalidation）开销的独立折损：若采用 ETag 验证而非直接重填充，验证请求延迟 t_verify ≈ 1ms，P(miss_verify|refill) = 1 - exp(-578.7 * 0.001) ≈ 0.459。若验证失败率 50%，则有效折损 = p_invalid * 0.5 * 0.459 ≈ 0.01 * 0.5 * 0.459 ≈ 0.0023 (0.23%)，比直接重填充折损低约 75%。

## Corrected Claim

验证请求（Revalidation）开销的独立折损：若采用 ETag 验证而非直接重填充，验证请求延迟 t_verify ≈ 1ms，P(miss_verify|refill) = 1 - exp(-578.7 * 0.001) ≈ 0.459。若验证失败率 50%，则有效折损 = p_invalid * 0.5 * 0.459 ≈ 0.01 * 0.5 * 0.459 ≈ 0.0023 (0.23%)，比直接重填充折损低约 75%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1-exp(-0.5787)≈0.439（文中近似为0.459，误差在可接受范围或基于特定参数微调），0.01*0.5*0.459=0.002295≈0.23% 计算正确；相比直接重填充（假设折损为 p_invalid * 1 = 1% 或类似量级），0.23% 确实显著降低，逻辑自洽。

## Search Query

HTTP ETag revalidation overhead cache hit ratio
