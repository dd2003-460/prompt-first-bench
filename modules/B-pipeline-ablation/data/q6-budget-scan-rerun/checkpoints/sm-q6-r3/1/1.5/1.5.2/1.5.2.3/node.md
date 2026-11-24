# N167: P99_hybrid(w_core) 的敏感性斜率计算：定义 dP99_hybrid/dw_core = P99_core - P99_tail，若 P99_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

P99_hybrid(w_core) 的敏感性斜率计算：定义 dP99_hybrid/dw_core = P99_core - P99_tail，若 P99_core=250ms, P99_tail=160ms，则斜率=90ms/单位占比，即核心区域占比每增加10%，混合策略P99增加9ms；若 P99_core=200ms, P99_tail=190ms（长尾低命中），则斜率=10ms/单位占比，敏感性大幅降低；此斜率用于评估地理分布不确定性对混合策略P99合规性的影响幅度。

## Corrected Claim

P99_hybrid(w_core) 的敏感性斜率计算：定义 dP99_hybrid/dw_core = P99_core - P99_tail，若 P99_core=250ms, P99_tail=160ms，则斜率=90ms/单位占比，即核心区域占比每增加10%，混合策略P99增加9ms；若 P99_core=200ms, P99_tail=190ms（长尾低命中），则斜率=10ms/单位占比，敏感性大幅降低；此斜率用于评估地理分布不确定性对混合策略P99合规性的影响幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：斜率定义 dP99/dw = P99_core - P99_tail 符合线性混合模型的一阶导数逻辑，数值计算（250-160=90, 200-190=10）及百分比换算（10% * 90 = 9ms）均准确无误。

## Search Query

CDN P99 latency sensitivity geographic distribution slope
