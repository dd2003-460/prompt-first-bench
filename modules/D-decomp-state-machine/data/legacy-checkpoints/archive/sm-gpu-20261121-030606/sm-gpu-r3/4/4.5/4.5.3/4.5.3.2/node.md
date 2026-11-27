# N323: 工作点B（纯带宽瓶颈极限）：假设计算能力无穷大，H100 SXM BF16延迟仅由内存搬运决定，使用权重54GB（BF16）及修正后KV Cache 3.98G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

工作点B（纯带宽瓶颈极限）：假设计算能力无穷大，H100 SXM BF16延迟仅由内存搬运决定，使用权重54GB（BF16）及修正后KV Cache 3.98GB（N111），总数据量60.48GB，延迟 = 60.48 / 3350 ≈ 18.05 ms/token，对应理论最大吞吐 55.4 tokens/s，此值揭示H100在BF16下仍受带宽制约，但带宽优势使其带宽项延迟低于RTX 4090 INT8。

## Corrected Claim

工作点B（纯带宽瓶颈极限）：假设计算能力无穷大，H100 SXM BF16延迟仅由内存搬运决定，使用权重54GB（BF16）及修正后KV Cache 3.98GB（N111），总数据量60.48GB，延迟 = 60.48 / 3350 ≈ 18.05 ms/token，对应理论最大吞吐 55.4 tokens/s，此值揭示H100在BF16下仍受带宽制约，但带宽优势使其带宽项延迟低于RTX 4090 INT8。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3带宽约3.35TB/s，计算60.48GB/3350GB/s≈18.05ms，吞吐1/0.01805s≈55.4 tokens/s，数值量级与逻辑自洽。
