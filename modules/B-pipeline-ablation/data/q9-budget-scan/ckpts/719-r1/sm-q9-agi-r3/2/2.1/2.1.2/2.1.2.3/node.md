# N147: 混合检索权重 α 的最优值确定方法：通过线性回归拟合 Recall@5(α) = α*Recall_Vector + (1-α)*Recall_BM25 + I

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

混合检索权重 α 的最优值确定方法：通过线性回归拟合 Recall@5(α) = α*Recall_Vector + (1-α)*Recall_BM25 + Interaction_Term，在 α ∈ [0, 1] 步长 0.1 上进行网格搜索，通常 α=0.6-0.7 时综合 Recall@5 达到峰值（约为单一方法最佳值的 1.05-1.10 倍），因为向量检索弥补了 BM25 的语义缺失，而 BM25 弥补了向量检索对专有名词的敏感度不足

## Corrected Claim

混合检索权重 α 的最优值通常需通过网格搜索确定，其具体数值高度依赖于数据集特征和检索任务类型，不存在通用的固定最优区间。

## Evidence

[质询]将混合检索效果简单线性分解为 Recall_Vector 和 Recall_BM25 的加权平均并假设存在固定的 Interaction_Term 过于简化，忽略了不同数据集分布、查询类型及嵌入模型质量对最优 α 值的显著影响，导致 '通常 α=0.6-0.7' 这一具体数值范围缺乏普适性。 | 先验知识/题面给定，逻辑校验通过，但具体数值范围（0.6-0.7）及提升倍数（1.05-1.10）属于经验事实，缺乏通用性保证，故降级。
