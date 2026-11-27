# N133: 信息边际成本系数 m 的品类依赖性：m 与商品标准化程度负相关，具体表达式为 m = m_base / (1 + λ * Std_score)，其中 m_bas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

信息边际成本系数 m 的品类依赖性：m 与商品标准化程度负相关，具体表达式为 m = m_base / (1 + λ * Std_score)，其中 m_base ≈ 0.10，λ ≈ 0.5，Std_score 为标准化评分（0-1），对于非标品（Std_score < 0.3），m 通常高于 0.10，导致二次方成本增长更快。

## Corrected Claim

信息边际成本系数 m 的品类依赖性：m 与商品标准化程度负相关，具体表达式为 m = m_base / (1 + λ * Std_score)，其中 m_base ≈ 0.10，λ ≈ 0.5，Std_score 为标准化评分（0-1）。由于分母大于等于1，m 的值通常小于或等于 m_base（0.10），标准化程度越高（Std_score越大），m 越小，意味着标准化商品的信息边际成本更低。

## Evidence

[质询]该陈述包含具体的经验参数（m_base ≈ 0.10, λ ≈ 0.5）和特定的数学函数形式，属于经验事实/模型假设，无法从第一性原理严格推导，且参考来源中完全未提及此类信息成本模型或具体数值。 | 逻辑上自洽（分母大于1导致m小于m_base，但题目描述非标品m高于0.10存在内部矛盾：若Std_score<0.3，分母1+0.5*0.3=1.15，m=0.10/1.15≈0.087<0.10，与陈述'非标品m通常高于0.10'矛盾。等等，重新检查逻辑：陈述说'm与商品标准化程度负相关'，即Std_score越高，m越低。公式 m = m_base / (1 + λ * Std_score)。当Std_score增加，分母增加，m减小。这符合负相关。但是陈述后半部分说'对于非标品（Std_score < 0.3），m 通常高于 0.10'。如果 m_base = 0.10，且 Std_score >= 0，则分母 >= 1，所以 m <= 0.10。因此，m 不可能高于 0.10。这是一个硬逻辑错误/内部矛盾。

## Search Query

marginal cost of quality verification standardized vs non-standardized products

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Logistics', 'type': 'wikipedia', 'title': 'Logistics'}
- {'url': 'https://en.wikipedia.org/wiki/5.56%C3%9745mm_NATO', 'type': 'wikipedia', 'title': '5.56×45mm NATO'}
- {'url': 'https://en.wikipedia.org/wiki/Biodiesel', 'type': 'wikipedia', 'title': 'Biodiesel'}
