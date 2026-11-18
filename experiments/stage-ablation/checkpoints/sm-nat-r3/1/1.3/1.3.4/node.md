# N33: E[S] 的敏感性分析：若 x_min 取 100 Bytes (更小的最小对象)，则 E[S] = 1.1 KB，K_avg 将增加 10 倍至 ~1.2 万

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

E[S] 的敏感性分析：若 x_min 取 100 Bytes (更小的最小对象)，则 E[S] = 1.1 KB，K_avg 将增加 10 倍至 ~1.2 万，这会显著改变 LRU 的缓存覆盖范围，需确认 x_min 的量级对命中率下界的影响。

## Corrected Claim

E[S] 的敏感性分析：若 x_min 取 100 Bytes (更小的最小对象)，则 E[S] = 1.1 KB，K_avg 将增加 10 倍至 ~1.2 万，这会显著改变 LRU 的缓存覆盖范围，需确认 x_min 的量级对命中率下界的影响。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1聚焦于 x_min=100B 时的参数推导与 K_avg 计算；节点2基于节点1的结果讨论命中率下界的边界条件（全驻留）；节点3引入对照场景 x_min=10KB 以界定敏感性边界。三者分别对应“主场景计算”、“主场景结论”和“对比场景/稳健性分析”，无重复或矛盾，且完整覆盖了父节点中关于 x_min 量级对命中率影响的分析需求。）

## Search Query

Pareto alpha 1.1 mean size sensitivity minimum value
