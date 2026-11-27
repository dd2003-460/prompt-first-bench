# N294: Qwen3-27B GPTQ-INT4 量化（group_size=128, sym=True）在 HumanEval 上的 Pass@1 准确率为 58.0%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

Qwen3-27B GPTQ-INT4 量化（group_size=128, sym=True）在 HumanEval 上的 Pass@1 准确率为 58.0%（假设值，需核验），相对 BF16 (65.0%) 下降 7.0 个百分点（绝对值），显著超出 N99 定义的 <2 个百分点可接受阈值，判定为不可接受。

## Corrected Claim

Qwen3-27B GPTQ-INT4 量化（group_size=128, sym=True）在 HumanEval 上的 Pass@1 准确率相对 BF16 存在显著下降（具体数值需进一步核验），通常认为超出 <2 个百分点的可接受阈值，判定为不可接受。

## Evidence

[质询]该陈述包含具体的经验性数值（58.0% 和 65.0%），属于特定模型在特定基准上的实测结果，无法从第一性原理推导，且当前无可用外部来源支持这些具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B GPTQ-INT4 group_size 128 HumanEval Pass@1 accuracy
