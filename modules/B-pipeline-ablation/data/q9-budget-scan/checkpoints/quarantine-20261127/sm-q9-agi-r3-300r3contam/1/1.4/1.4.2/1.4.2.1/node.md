# N111: 代码执行成功率的基线分解：Code Pass Rate = P_syntax_valid * P_runtime_success，其中 P_syntax_val

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

代码执行成功率的基线分解：Code Pass Rate = P_syntax_valid * P_runtime_success，其中 P_syntax_valid 为生成代码无语法错误的概率（27B 模型预期 >98%），P_runtime_success 为运行时无异常退出的概率；对于含噪 CSV/JSON 重构任务，主要失败源是未处理的边界情况（如空值、类型不匹配），导致 P_runtime_success 在复杂嵌套结构下降至 85%-90%，低于 95% 阈值。

## Corrected Claim

代码执行成功率可分解为语法有效概率与运行时成功概率的乘积。对于含噪数据结构重构任务，未处理的边界情况（如空值、类型不匹配）是导致运行时失败的主要原因，可能导致复杂场景下的运行时成功率显著低于简单场景，但具体数值需依赖特定模型与数据集的实验测量。

## Evidence

[质询]该陈述包含具体的经验性数值指标（27B模型语法正确率>98%，复杂嵌套结构运行时成功率85%-90%），这些具体参数值无法从第一性原理推导，且参考来源中未提供对应的实证数据支持，属于缺乏来源支撑的经验事实。 | 逻辑上代码通过率分解为语法有效性与运行时成功率的乘积是自洽的，但具体数值（如85%-90%）属于经验事实，参考来源[1][2]仅涉及代码生成评估综述及重放策略，未提供针对27B模型在含噪CSV/JSON重构任务下的具体成功率统计数据，故降级。

## Search Query

LLM code generation pass rate runtime failure causes data cleaning

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2410.12236v1&rut=5df2683305fa5193dd34f774d9d7976a1020c9dc85b56b0b8ce2cdba25803eb0', 'type': 'ddg', 'title': 'Enhancing LLM Agents for Code Generation with Possibility and Pass-rate ...'}
- {'url': 'https://arxiv.org/html/2408.16498v1&rut=3b2916e734ae08c81ca979596e6de07f3072a9e2dda3d4ac979ee9ea2f389a42', 'type': 'ddg', 'title': 'A Survey on Evaluating Large Language Models in Code Generation Tasks'}
