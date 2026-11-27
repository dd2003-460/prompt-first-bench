# N745: INT8 KV Cache 量化对 HumanEval (Pass@1) 代码生成任务的影响量化：代码生成任务对数值精度更敏感。实测显示 INT8 KV Cac

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N262

## Claim

INT8 KV Cache 量化对 HumanEval (Pass@1) 代码生成任务的影响量化：代码生成任务对数值精度更敏感。实测显示 INT8 KV Cache 相比 BF16，HumanEval Pass@1 下降幅度约为 1.0% - 2.0%。若基准线为 60%，则降至 58.8% - 58.0%，通常仍在可接受范围内（<2% 绝对误差），N262 的 '超出可接受阈值' 结论需重新定义阈值。

## Corrected Claim

INT8 KV Cache 量化通常会对代码生成任务（如 HumanEval）产生负面影响，具体下降幅度取决于模型架构和量化策略，需实测确定，但通常认为在合理阈值内。

## Evidence

[质询]该陈述包含具体的经验性数值（INT8 KV Cache 导致 HumanEval Pass@1 下降 1.0%-2.0%），属于特定模型架构和量化实现下的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

LLM KV cache INT8 quantization HumanEval pass@1 degradation study
