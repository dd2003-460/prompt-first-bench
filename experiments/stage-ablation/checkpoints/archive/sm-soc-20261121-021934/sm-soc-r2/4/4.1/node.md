# N15: 基于贝叶斯推理的先验概率 P(假设H|数据D) = P(D|H) * P(H) / P(D)，其中 P(H) 需量化为基于演化心理学文献中‘定向压力’（如损失厌

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

基于贝叶斯推理的先验概率 P(假设H|数据D) = P(D|H) * P(H) / P(D)，其中 P(H) 需量化为基于演化心理学文献中‘定向压力’（如损失厌恶系数λ≈2.25, Kahneman & Tversky 1979）在二手交易场景下的适用性权重，当前置信度区间设定为 [0.6, 0.8]，需通过 A/B 测试数据更新后验

## Corrected Claim

基于贝叶斯推理的后验概率 P(H|D) = P(D|H) * P(H) / P(D)。其中先验 P(H) 应基于演化心理学中‘定向压力’（如损失厌恶现象）在二手交易场景下的定性影响进行设定，初始值可参考专家经验或历史数据（例如设定为 0.7），并通过 A/B 测试数据不断更新后验。

## Evidence

[质询]将损失厌恶系数（λ≈2.25）直接量化为贝叶斯先验概率 P(H) 的适用性权重在方法论上存在混淆：λ 是效用函数中的参数，而 P(H) 是概率值，二者量纲和定义域不同，不能直接等同或简单映射；此外，[0.6, 0.8] 的置信区间缺乏具体的统计依据或文献支持，属于主观设定。 | 先验知识/题面给定，逻辑校验通过（贝叶斯公式本身正确，但参数映射逻辑存在瑕疵，故降级）

## Search Query

Bayesian updating prior probability loss aversion coefficient second-hand market
