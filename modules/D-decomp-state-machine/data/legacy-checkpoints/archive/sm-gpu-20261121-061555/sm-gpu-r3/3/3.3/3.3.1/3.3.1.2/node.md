# N249: 量化导致的 PPL 增加与代码生成错误率上升之间的非线性关系系数：在代码任务中，PPL 每增加 1%，Pass@1 下降幅度通常为 PPL 增量的 1.5-2 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

量化导致的 PPL 增加与代码生成错误率上升之间的非线性关系系数：在代码任务中，PPL 每增加 1%，Pass@1 下降幅度通常为 PPL 增量的 1.5-2 倍，需通过实证数据验证该放大效应系数，以精确推导 <2% Pass@1 下降对应的 PPL 上限。

## Corrected Claim

量化导致的 PPL 增加通常与代码生成错误率上升正相关，但二者之间不存在普适的固定放大系数（如1.5-2倍）。具体影响幅度需通过针对特定模型、量化策略及代码基准的实证实验进行验证，以推导满足 <2% Pass@1 下降约束的 PPL 上限。

## Evidence

[质询]该陈述声称存在一个具体的“非线性关系系数”（1.5-2倍），并断言这是“通常”情况，但缺乏任何实证数据或理论推导支持这一特定数值范围。PPL（困惑度）与Pass@1（代码生成通过率）之间的关系高度依赖于模型架构、量化方法（如GPTQ, AWQ）、任务难度及数据集分布，不存在普适的固定线性或简单非线性放大系数。将复杂的经验现象简化为固定的倍数关系属于过度概括，且“非线性”与“1.5-2倍”（暗示近似线性比例）在表述上存在逻辑张力。 | 经验事实，逻辑自洽性存疑（固定系数假设缺乏理论依据且与“非线性”描述矛盾），且无可用外部来源支持该具体数值范围。

## Search Query

perplexity increase vs code generation pass@1 drop non-linear relationship coefficient LLM quantization
