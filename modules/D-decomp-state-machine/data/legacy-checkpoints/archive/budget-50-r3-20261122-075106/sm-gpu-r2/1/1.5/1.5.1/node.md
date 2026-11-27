# N60: Intel Gaudi 3 (128GB) 的 HBM2e 带宽为 3.7 TB/s，理论最大 Token/s 吞吐率约为 3.7e12 / 54e9 ≈ 68

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Intel Gaudi 3 (128GB) 的 HBM2e 带宽为 3.7 TB/s，理论最大 Token/s 吞吐率约为 3.7e12 / 54e9 ≈ 68 Token/s，实际预计为 30-45 Token/s [待核验]，低于 MI300X 和 H100

## Corrected Claim

Intel Gaudi 3 (128GB) 的 HBM2e 带宽为 3.7 TB/s，理论最大 Token/s 吞吐率约为 3.7e12 / 54e9 ≈ 68,500 Token/s，实际预计受限于计算和通信开销，通常远低于理论值，但不会低至 68 Token/s。

## Evidence

[质询]数值量级与物理直觉严重不符：3.7 TB/s 的带宽除以 54 GB 的模型大小，得到的理论上限约为 68,500 Token/s（即 6.8e4），而非陈述中的 68 Token/s（6.8e1）。陈述中的计算结果比理论上限低了三个数量级，且 68 Token/s 的实际吞吐率对于拥有 3.7 TB/s 带宽的顶级 AI 加速器而言极低，违背基本性能直觉。 | 逻辑校验失败：带宽除以模型大小得到的理论吞吐率应为 ~68,500 Token/s，陈述中写为 68 Token/s，存在数量级错误；且 source 为 knowledge，但内部逻辑矛盾无法排除。

## Search Query

Intel Gaudi 3 HBM2e bandwidth LLM inference benchmark
