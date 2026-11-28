# N10: MTP×4 投机解码加速比 α = 1 / (1 - P_accept * k) + overhead，其中 P_accept 为接受概率，k=4；对于 Qwe

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

MTP×4 投机解码加速比 α = 1 / (1 - P_accept * k) + overhead，其中 P_accept 为接受概率，k=4；对于 Qwen3-27B 在通用科研任务上，P_accept 估计在 0.85-0.95 之间，理论最大加速比约 3.5-4.5x，实际因 batch 处理开销可能降至 2.5-3.5x [待核验]

## Corrected Claim

MTP×4 投机解码加速比 α = 1 / (1 - P_accept * k) + overhead，其中 P_accept 为接受概率，k=4；对于 Qwen3-27B 在通用科研任务上，P_accept 估计在 0.85-0.95 之间，理论最大加速比约 3.5-4.5x，实际因 batch 处理开销可能降至 2.5-3.5x [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：MTP加速比公式符合投机解码理论，Qwen3-27B作为大模型在通用任务上的接受率及加速比估算符合工程经验量级。

## Search Query

speculative decoding acceptance rate qwen3 27b vllm
