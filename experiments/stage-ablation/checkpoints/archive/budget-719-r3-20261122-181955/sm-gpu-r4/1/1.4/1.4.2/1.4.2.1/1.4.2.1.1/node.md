# N547: Intel Max 1550 的 2.5 PFLOPS (sparse) 规格中，'sparse' 指硬件支持 2:4 结构化稀疏加速，实际 LLM 推理中若模

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

Intel Max 1550 的 2.5 PFLOPS (sparse) 规格中，'sparse' 指硬件支持 2:4 结构化稀疏加速，实际 LLM 推理中若模型未采用稀疏量化，有效算力仅为稠密峰值的 50% 即 1.25 PFLOPS

## Corrected Claim

Intel Max 1550 的 2.5 PFLOPS (sparse) 规格中，'sparse' 指硬件支持 2:4 结构化稀疏加速，实际 LLM 推理中若模型未采用稀疏量化，有效算力仅为稠密峰值的 50% 即 1.25 PFLOPS

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Max 1550 确实支持 2:4 结构化稀疏加速，稀疏峰值算力通常为稠密算力的 2 倍，因此若未利用稀疏性，有效算力为稠密峰值（即稀疏峰值的 50%）。
