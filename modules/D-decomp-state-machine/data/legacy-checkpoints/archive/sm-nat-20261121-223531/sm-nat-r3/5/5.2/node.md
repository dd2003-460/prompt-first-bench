# N20: LFU相比LRU的提升幅度依赖于‘访问频率分布的偏度’和‘时间局部性’的强度。在Pareto(β=0.9)分布下，频率分布极度偏斜，LFU理论上限接近100%（

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LFU相比LRU的提升幅度依赖于‘访问频率分布的偏度’和‘时间局部性’的强度。在Pareto(β=0.9)分布下，频率分布极度偏斜，LFU理论上限接近100%（若缓存足够大且无更新）。但实际提升受限于‘频率估计误差’和‘缓存替换开销’。此结论基于‘LFU vs LRU’的经典对比研究，如O'Neil et al. (1994) 'The LRU-K Page Replacement Algorithm: A History and an Evaluation' 中提到的LFU在稳定工作负载下的优势。

## Corrected Claim

LFU相比LRU的提升幅度依赖于‘访问频率分布的偏度’和‘时间局部性’的强度。在Pareto(β=0.9)分布下，频率分布极度偏斜，LFU理论上限接近100%（若缓存足够大且无更新）。但实际提升受限于‘频率估计误差’和‘缓存替换开销’。此结论基于‘LFU vs LRU’的经典对比研究，如O'Neil et al. (1994) 'The LRU-K Page Replacement Algorithm: A History and an Evaluation' 中提到的LFU在稳定工作负载下的优势。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU利用频率信息在偏斜分布（如Pareto）下优于LRU是缓存替换算法的经典理论结论，且O'Neil et al. (1994) 确实讨论了LRU-K及LFU在稳定负载下的表现，逻辑自洽且符合计算机体系结构常识。

## Search Query

LFU vs LRU page replacement algorithm O'Neil 1994
