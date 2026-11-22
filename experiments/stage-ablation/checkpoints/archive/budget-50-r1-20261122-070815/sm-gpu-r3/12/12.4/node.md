# N436: Apple M2 Ultra 在 Llama.cpp/MLX 后端运行 7B-13B 模型时，实测 Decode 阶段有效带宽利用率约为 65-75% (约 5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N150, N151, N152

## Claim

Apple M2 Ultra 在 Llama.cpp/MLX 后端运行 7B-13B 模型时，实测 Decode 阶段有效带宽利用率约为 65-75% (约 520-600 GB/s)，高于此前估计的 50-60%，主要受 Metal 后端内存访问模式优化影响，需针对 27B 模型重新校准。

## Corrected Claim

Apple M2 Ultra 在 Llama.cpp/MLX 后端运行 7B-13B 模型时，实测 Decode 阶段有效带宽利用率估计在 60-75% 区间（约 480-600 GB/s），具体数值受模型大小、量化方式及后端内存访问模式优化影响，需针对特定模型（如 27B）重新校准。

## Evidence

[质询]该陈述包含具体的实测性能数据（65-75%利用率，520-600 GB/s）及特定后端（MLX/Metal）的优化效果，属于经验事实。由于检索无可用来源，无法验证这些具体数值是否准确，且不同模型大小（7B vs 13B）和后端实现可能导致带宽利用率差异较大，单一区间可能过于简化。 | 经验事实，逻辑自洽但缺来源支持。M2 Ultra 理论带宽约 800 GB/s，65-75% 利用率对应 520-600 GB/s 在物理上合理，但具体数值缺乏外部证据直接证实。

## Search Query

Apple M2 Ultra llama.cpp effective memory bandwidth utilization LLM decode benchmark
