# N97: 认知偏差量化中使用的KL散度计算公式为KL(P_gold || P_model) = Σ p_gold(x) * log(p_gold(x)/p_model(x

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

认知偏差量化中使用的KL散度计算公式为KL(P_gold || P_model) = Σ p_gold(x) * log(p_gold(x)/p_model(x))，其中P_gold来自顶刊论文结论的语义嵌入分布（通过Sentence-BERT提取），P_model来自Qwen3.8-27B生成的假设空间概率分布，计算需在128维向量空间上进行归一化后执行。

## Corrected Claim

认知偏差量化中使用的KL散度计算公式为KL(P_gold || P_model) = Σ p_gold(x) * log(p_gold(x)/p_model(x))，其中P_gold和P_model需分别为顶刊论文结论语义嵌入分布和Qwen3.8-27B生成假设空间概率分布经过归一化（如Softmax）后得到的概率分布，而非直接在原始128维向量空间上计算。

## Evidence

[质询]将KL散度直接应用于高维语义嵌入向量（128维）在数学定义上是不严谨的，因为嵌入向量通常不是概率分布（分量和不为1，且可能包含负值），直接套用KL公式会导致量纲错误或计算无意义，通常需要先将向量转换为概率分布（如Softmax）或计算分布间的距离（如余弦相似度）。 | 先验知识/题面给定，逻辑校验发现数学定义存在瑕疵（嵌入向量非概率分布），故降级。

## Search Query

KL divergence semantic embedding hypothesis space Sentence-BERT
