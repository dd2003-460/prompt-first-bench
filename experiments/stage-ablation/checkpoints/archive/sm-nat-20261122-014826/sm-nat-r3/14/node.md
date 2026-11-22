# N181: 推导链步骤5：计算更新率 u=1%/天 导致的失效概率 P_stale，并推导有效命中率 H_eff = H_base * (1 - P_stale * (1 

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推导链步骤5：计算更新率 u=1%/天 导致的失效概率 P_stale，并推导有效命中率 H_eff = H_base * (1 - P_stale * (1 - H_revalidate))，其中 H_revalidate 取决于内容变更概率。

## Corrected Claim

推导链步骤5：计算更新率 u=1%/天 导致的失效概率 P_stale，并推导有效命中率 H_eff = H_base * (1 - P_stale * (1 - H_revalidate))，其中 H_revalidate 取决于内容变更概率。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

cache invalidation probability formula stale data hit rate
