# N154: Bootstrap 重抽样必须采用‘分层抽样’策略（Stratified Resampling），按商品品类（Category）分层，每层独立重抽样后合并，以保

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

Bootstrap 重抽样必须采用‘分层抽样’策略（Stratified Resampling），按商品品类（Category）分层，每层独立重抽样后合并，以保留品类结构对 $\eta$ 分布的影响；若采用简单随机重抽样，置信区间宽度可能扩大 15%-20%，降低检验功效。

## Corrected Claim

Bootstrap 重抽样建议采用‘分层抽样’策略（Stratified Resampling），按商品品类（Category）分层，每层独立重抽样后合并，以保留品类结构对 $\eta$ 分布的影响；相较于简单随机重抽样，该策略通常能更准确地估计分布尾部并可能降低置信区间宽度，从而提升检验功效，但具体改善幅度取决于数据分布特征。

## Evidence

[质询]陈述中关于置信区间宽度扩大15%-20%的具体数值缺乏普遍适用的理论依据，该数值高度依赖于具体数据集的品类分布不均程度及样本量，属于经验性估计而非Bootstrap方法的固有属性，存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：分层重抽样确实能保留总体结构并通常降低方差，但具体数值幅度（15%-20%）为经验估计，非绝对真理，故降级为定性表述。
