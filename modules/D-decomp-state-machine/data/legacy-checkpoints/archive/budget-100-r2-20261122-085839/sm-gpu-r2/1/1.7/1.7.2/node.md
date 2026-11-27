# N49: Qwen3-27B 在 SmoothQuant (INT8) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 84.1% (Δ=-0.9%)，Hum

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 在 SmoothQuant (INT8) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 84.1% (Δ=-0.9%)，HumanEval (Pass@1) 从 70.0% 降至 68.5% (Δ=-1.5%) [待核验: SmoothQuant 对 Qwen3 的具体实测数据可能缺失，需对比 GPTQ 或检索最新社区测试]

## Corrected Claim

Qwen3-27B 在 SmoothQuant (INT8) 量化下，MMLU 和 HumanEval 分数相较于 BF16 基线出现轻微下降（具体数值需查阅最新官方技术报告或社区实测数据，通常降幅在 1-2% 以内）。

## Evidence

[质询]具体数值（85.0%, 84.1%, 70.0%, 68.5%）属于特定模型版本在特定量化方案下的经验实测数据，无法从第一性原理推导，且当前无可用来源支持这些精确数值，存在数据虚构或混淆不同评测集/版本的风险。 | 逻辑上量化导致精度轻微下降符合直觉（Δ在合理范围内），但作为经验事实，缺乏来源直接支持具体数值，依据经验事实排除条款降级。

## Search Query

Qwen3-27B SmoothQuant INT8 MMLU HumanEval benchmark comparison
