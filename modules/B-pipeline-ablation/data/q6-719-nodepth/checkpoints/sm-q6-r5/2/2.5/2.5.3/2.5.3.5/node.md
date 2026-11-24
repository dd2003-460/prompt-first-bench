# N206: 缓存命中率提升的边际收益曲线：ΔH/ΔC_hit 随 H_current 接近 95% 而急剧下降，当 H_current > 90% 时，每 ¥1 投入带来的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N64, N65, N66

## Claim

缓存命中率提升的边际收益曲线：ΔH/ΔC_hit 随 H_current 接近 95% 而急剧下降，当 H_current > 90% 时，每 ¥1 投入带来的 ΔH < 0.01%，此时 ΔC_hit > ΔC_pop 成为主导

## Corrected Claim

缓存命中率提升的边际收益随当前命中率（H_current）的升高而递减；当 H_current 处于高位（如接近 95%）时，单位成本投入带来的命中率增量显著降低，且缓存成本可能超过其他优化手段的成本。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义了成本侧的非线性函数（C_hit），节点2量化了收益侧（节省带宽 vs 投入成本），节点3综合两者计算决策交叉点（H_cross）。三者分别对应父节点描述中的‘成本急剧上升’、‘边际收益下降/净收益为负’以及‘ΔC_hit > ΔC_pop成为主导’三个核心维度，无重叠且无遗漏。）
