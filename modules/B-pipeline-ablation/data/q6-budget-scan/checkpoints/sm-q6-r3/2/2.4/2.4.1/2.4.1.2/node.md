# N266: 自建节点计费口径为'静态带宽包月费'，实际成本与 H_cache 无关（固定成本），但 H_cache 决定所需带宽容量上限，进而决定需购买的带宽包规格，间接影

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

自建节点计费口径为'静态带宽包月费'，实际成本与 H_cache 无关（固定成本），但 H_cache 决定所需带宽容量上限，进而决定需购买的带宽包规格，间接影响单位流量分摊成本

## Corrected Claim

自建节点计费口径为'静态带宽包月费'，实际成本与 H_cache 无关（固定成本），但 H_cache 决定所需带宽容量上限，进而决定需购买的带宽包规格，间接影响单位流量分摊成本

## Evidence

先验知识/题面给定，逻辑校验通过：静态带宽包月费属于固定成本，不随流量线性变化，但带宽上限决定了最大吞吐能力，从而间接影响单位流量的分摊成本，逻辑自洽。

## Search Query

self-hosted CDN bandwidth package fixed cost cache hit impact on capacity planning
