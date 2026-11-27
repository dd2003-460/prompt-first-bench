# N96: Decode 阶段（带宽密集）TPOT 主导因素：带宽需求 = N_params * Bits，RTX 5090 (1792 GB/s) vs H100 (33

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

Decode 阶段（带宽密集）TPOT 主导因素：带宽需求 = N_params * Bits，RTX 5090 (1792 GB/s) vs H100 (3350 GB/s)，理论 TPOT 比值约为 1.87x，即 H100 生成速度约为 5090 的 53%。

## Corrected Claim

Decode 阶段（带宽密集）TPOT 主导因素：带宽需求 = N_params * Bits，RTX 5090 (1792 GB/s) vs H100 (3350 GB/s)，理论 TPOT 比值约为 1.87x，即 H100 生成速度约为 5090 的 1.87 倍（或 5090 生成速度约为 H100 的 53%）。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 705)

## Search Query

RTX 5090 vs H100 memory bandwidth decode latency
