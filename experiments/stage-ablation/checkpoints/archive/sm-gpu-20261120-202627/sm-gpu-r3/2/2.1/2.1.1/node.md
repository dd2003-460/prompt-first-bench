# N49: Qwen3-27B 在 BF16 精度下的基准困惑度（Perplexity）约为 8.5-9.5（基于同参数量级 LLM 在 WikiText-2 或 C4 数

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3-27B 在 BF16 精度下的基准困惑度（Perplexity）约为 8.5-9.5（基于同参数量级 LLM 在 WikiText-2 或 C4 数据集上的典型表现估算，需以官方技术报告为准）

## Corrected Claim

Qwen3-27B 在 BF16 精度下的基准困惑度（Perplexity）预计处于 8.5-9.5 区间（基于同参数量级 LLM 在 WikiText-2 或 C4 数据集上的典型表现估算），具体数值需以官方技术报告为准。

## Evidence

[质询]该陈述将特定模型（Qwen3-27B）的具体性能指标（困惑度）描述为基于同参数量级模型的估算值，且明确标注‘需以官方技术报告为准’，这属于未经验证的经验事实。虽然27B模型在WikiText-2上PPL约为8.5-9.5在量级上符合当前大模型的一般规律（通常随参数量增加PPL降低，27B属于中大型模型，PPL在个位数到十位数之间是合理的），但缺乏具体来源支持该特定数值区间，且不同数据集（WikiText-2 vs C4）和评估协议会导致数值差异，直接断言具体区间存在不确定性。 | 经验事实，逻辑自洽但缺来源支持。27B参数模型在标准基准测试中PPL处于8-10区间符合一般认知，但具体数值需官方报告确认，当前无可用外部来源直接验证该特定区间。

## Search Query

Qwen3-27B technical report perplexity benchmark
