# N61: 幻觉率（False Claim Rate, FCR）的计算公式为 FCR = (Number of False Claims) / Total Claims，其

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

幻觉率（False Claim Rate, FCR）的计算公式为 FCR = (Number of False Claims) / Total Claims，其中 False Claim 判定标准需通过语义相似度阈值（如 cosine similarity > 0.85 且事实不符）或人工标注双重验证，以排除因表述差异导致的误判。

## Corrected Claim

幻觉率（False Claim Rate, FCR）的计算公式为 FCR = (Number of False Claims) / Total Claims，其中 False Claim 判定标准需通过语义相似度阈值（如 cosine similarity > 0.85 且事实不符）或人工标注双重验证，以排除因表述差异导致的误判。

## Evidence

父节点级核验未通过：非正交（子节点1（阈值校准）和子节点3（判定逻辑）存在强耦合而非正交关系。子节点3中的布尔表达式直接依赖于子节点1中定义的动态阈值变量（Threshold_CAL），且子节点1中提到的“事实不符”验证隐含了子节点3中Fact_Checker的逻辑。两者分别描述了同一判定流程的“参数确定”和“逻辑执行”，属于同一机制的两个方面，而非独立模块。此外，子节点3的布尔逻辑存在歧义：(A and B) or C 的优先级可能导致在Cosine高但Fact_Checker为Contradiction时触发，这与通常“高相似度视为正确”的直觉可能冲突，需要明确逻辑运算符优先级或括号。）
