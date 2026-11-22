# N322: 工作点A（纯算力瓶颈极限）：假设内存带宽无穷大，H100 SXM BF16延迟仅由计算项决定，即 (2 * 27e9 * 32768) / (989e12 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

工作点A（纯算力瓶颈极限）：假设内存带宽无穷大，H100 SXM BF16延迟仅由计算项决定，即 (2 * 27e9 * 32768) / (989e12 * 0.9) ≈ 5.9 ms/token，对应理论最大吞吐 169.5 tokens/s，此值代表H100在BF16下的算力天花板，远高于RTX 4090。

## Corrected Claim

工作点A（纯算力瓶颈极限）：假设内存带宽无穷大，H100 SXM BF16延迟仅由计算项决定，即 (2 * 27e9 * 32768) / (989e12 * 0.9) ≈ 5.9 ms/token，对应理论最大吞吐 169.5 tokens/s，此值代表H100在BF16下的算力天花板，远高于RTX 4090。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM BF16峰值算力约989 TFLOPS，计算项公式 (2 * 27e9 * 32768) / (989e12 * 0.9) 量纲与数值推导正确，结果约5.9ms/token及169.5 tokens/s符合理论极限定义。
