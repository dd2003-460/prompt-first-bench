# N65: C=0.5高容量下LRU的长尾覆盖能力：LRU在C=0.5时能覆盖的请求流量比例为1-(1-0.5)^{1/1.2} ≈ 0.595，而LFU因固定头部导致长尾

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

C=0.5高容量下LRU的长尾覆盖能力：LRU在C=0.5时能覆盖的请求流量比例为1-(1-0.5)^{1/1.2} ≈ 0.595，而LFU因固定头部导致长尾覆盖率下降，需计算两者在尾部（bottom 50%）的命中率差距ΔH_tail_C50。

## Corrected Claim

C=0.5高容量下LRU的长尾覆盖能力：LRU在C=0.5时能覆盖的请求流量比例为1-(1-0.5)^{1/1.2} ≈ 0.595，而LFU因固定头部导致长尾覆盖率下降，需计算两者在尾部（bottom 50%）的命中率差距ΔH_tail_C50。
