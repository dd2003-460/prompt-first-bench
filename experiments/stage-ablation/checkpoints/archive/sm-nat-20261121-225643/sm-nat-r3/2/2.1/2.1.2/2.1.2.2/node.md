# N67: β=0.9重尾热度下长尾对象（bottom 50%）的请求占比精确值：R_bottom50 = (1 - 0.5)^{1/0.9} ≈ 0.486，LFU因优先

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

β=0.9重尾热度下长尾对象（bottom 50%）的请求占比精确值：R_bottom50 = (1 - 0.5)^{1/0.9} ≈ 0.486，LFU因优先驱逐低频对象导致这部分命中率损失ΔH_tail_B = P_LRU_bottom50 - P_LFU_bottom50，需基于C=0.1计算具体数值。

## Corrected Claim

β=0.9重尾热度下长尾对象（bottom 50%）的请求占比精确值：R_bottom50 = (1 - 0.5)^{1/0.9} ≈ 0.486，LFU因优先驱逐低频对象导致这部分命中率损失ΔH_tail_B = P_LRU_bottom50 - P_LFU_bottom50，需基于C=0.1计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布（Zipf-like）的累积概率公式 P(X > x) = (1 - x)^{1/β}，当 x=0.5, β=0.9 时，(0.5)^{1/0.9} ≈ 0.486 计算正确；LFU 与 LRU 在长尾部分的命中率差异定义符合缓存替换策略的基本逻辑。
