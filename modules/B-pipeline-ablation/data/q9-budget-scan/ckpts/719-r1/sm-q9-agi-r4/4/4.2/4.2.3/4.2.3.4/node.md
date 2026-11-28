# N219: 多样性损失的量化指标：计算Temperature=0.1 vs 0.7下的词汇多样性（Type-Token Ratio, TTR）和语义多样性（平均余弦距离），

- **status**: pending
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

父节点级核验未通过：不完备（子节点在主题上正交（分别针对指标校正、语义计算、采样策略对比），无重复或矛盾。但在完备性上存在缺失：父节点明确提出的核心判定逻辑（'若TTR_0.1 < TTR_0.7 * 0.8，则判定多样性损失过大，需引入...'）未在任何一个子节点中体现。子节点1虽然讨论了TTR的校正（Root-TTR/MTLD），但这改变了父节点定义的指标体系，而非执行父节点的判定流程；且没有任何子节点描述具体的决策触发条件或后续动作（引入top_k/min_p的具体实施步骤）。）
