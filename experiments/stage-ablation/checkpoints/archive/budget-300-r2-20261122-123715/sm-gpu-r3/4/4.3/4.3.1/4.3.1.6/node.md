# N313: FP8 精度下 Qwen3-27B 的实测困惑度增加量 ΔPPL_FP8 需引用 HuggingFace 或 GitHub 上具体量化模型 (如 FP8-E4M

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91, N92, N93

## Claim

FP8 精度下 Qwen3-27B 的实测困惑度增加量 ΔPPL_FP8 需引用 HuggingFace 或 GitHub 上具体量化模型 (如 FP8-E4M3) 的 benchmark 报告；若缺乏直接数据，可参考 LLaMA-3-8B FP8 的 ΔPPL ≈ 0.05-0.1 作为同规模模型的近似上限，但需标注 [待核验]。

## Corrected Claim

FP8 精度下 Qwen3-27B 的实测困惑度增加量 ΔPPL_FP8 需引用 HuggingFace 或 GitHub 上具体量化模型 (如 FP8-E4M3) 的 benchmark 报告；若缺乏直接数据，可参考同规模模型（如 LLaMA-3-8B）的 FP8 量化基准作为近似参考，但具体数值需标注 [待核验]。

## Evidence

[质询]该陈述包含具体的经验数值（LLaMA-3-8B FP8 的 ΔPPL ≈ 0.05-0.1），属于经验事实，无法从第一性原理推导，且缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B FP8 perplexity benchmark delta PPL
