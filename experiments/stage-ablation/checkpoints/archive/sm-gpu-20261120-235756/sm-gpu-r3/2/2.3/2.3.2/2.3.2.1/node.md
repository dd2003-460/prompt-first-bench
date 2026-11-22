# N201: 在 BF16 精度、32K 上下文单流场景下，RTX 4090 的理论 TPOT 为 10.5 ms/token (95 tokens/s)，A100 80GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

在 BF16 精度、32K 上下文单流场景下，RTX 4090 的理论 TPOT 为 10.5 ms/token (95 tokens/s)，A100 80GB 为 5.2 ms/token (192 tokens/s)，RTX 5090 为 5.9 ms/token (169 tokens/s)；该数值表明在 BF16 下，RTX 5090 因带宽优势 (1792 vs 1008 GB/s) 相比 RTX 4090 有 1.78x 的吞吐提升，但略低于 A100 (1.32x)，确立了 A100 在 BF16 单流场景下的性能标杆地位。

## Corrected Claim

在 BF16 精度、32K 上下文单流场景下，RTX 4090 的理论 TPOT 为 10.5 ms/token (95 tokens/s)，A100 80GB 为 5.2 ms/token (192 tokens/s)，RTX 5090 为 5.9 ms/token (169 tokens/s)；该数值表明在 BF16 下，RTX 5090 因带宽优势 (1792 vs 1008 GB/s) 相比 RTX 4090 有 1.78x 的吞吐提升，但略低于 A100 (1.32x)，确立了 A100 在 BF16 单流场景下的性能标杆地位。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽比 1792/1008≈1.78，TPOT 比 10.5/5.9≈1.78，A100 带宽 2039GB/s 对应 5.2ms 与 4090 的 10.5ms 比例约 2.02，符合带宽主导的线性关系，数值自洽。
