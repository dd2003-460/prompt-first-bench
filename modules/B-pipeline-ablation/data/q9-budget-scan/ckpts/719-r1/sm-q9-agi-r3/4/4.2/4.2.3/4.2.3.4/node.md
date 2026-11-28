# N219: 多样性损失的量化指标：计算Temperature=0.1 vs 0.7下的词汇多样性（Type-Token Ratio, TTR）和语义多样性（平均余弦距离），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

多样性损失的量化指标：计算Temperature=0.1 vs 0.7下的词汇多样性（Type-Token Ratio, TTR）和语义多样性（平均余弦距离），若TTR_0.1 < TTR_0.7 * 0.8，则判定多样性损失过大，需引入top_k=50或min_p采样策略平衡幻觉率与多样性。

## Corrected Claim

多样性损失的量化指标：计算Temperature=0.1 vs 0.7下的词汇多样性（Type-Token Ratio, TTR）和语义多样性（平均余弦距离），若TTR_0.1 < TTR_0.7 * 0.8，则判定多样性损失过大，需引入top_k=50或min_p采样策略平衡幻觉率与多样性。

## Evidence

先验知识/题面给定，逻辑校验通过
