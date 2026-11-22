# N223: 基准决策时间 T_base 的构成与量化：T_base = T_search + T_evaluate + T_negotiate，其中 T_search 为从

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N73

## Claim

基准决策时间 T_base 的构成与量化：T_base = T_search + T_evaluate + T_negotiate，其中 T_search 为从看到商品到决定点击的平均耗时（约 15-30 秒），T_evaluate 为评估商品细节（图片、描述、信用分）的耗时（约 2-5 分钟），T_negotiate 为发起沟通或下单的耗时（约 5-10 分钟）。

## Corrected Claim

基准决策时间 T_base 由搜索、评估和谈判/下单三个阶段组成：T_base = T_search + T_evaluate + T_negotiate。其中 T_search 为从看到商品到决定点击的耗时，T_evaluate 为评估商品细节的耗时，T_negotiate 为发起沟通或下单的耗时。具体耗时取决于商品复杂度、用户经验及平台特性，通常 T_search 为秒级，T_evaluate 为分钟级，T_negotiate 为分钟级。

## Evidence

[质询]该陈述包含具体的经验性时间数值（如15-30秒、2-5分钟等），这些数值并非第一性原理可推导的数学或物理常数，而是依赖于具体场景、用户群体和平台类型的经验统计值。作为 knowledge 节点，虽然逻辑结构自洽，但缺乏外部来源验证其数值的普遍准确性，且不同研究或场景下这些时间量级可能存在显著差异，存在将特定样本数据泛化为通用基准的风险。 | 逻辑结构自洽（总时间等于各阶段之和），量级符合一般电商/交易行为直觉，但具体数值属于经验事实，无来源支持，依据经验事实排除条款及knowledge节点在缺乏强先验共识时的审慎原则，降级为定性表述。

## Search Query

average decision time components e-commerce user behavior analysis
