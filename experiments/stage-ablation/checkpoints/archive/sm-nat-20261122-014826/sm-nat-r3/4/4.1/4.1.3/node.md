# N47: Stale Fraction 对有效命中率的非线性影响：H_eff = H_static * (1 - P_stale) + P_stale * H_reval

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Stale Fraction 对有效命中率的非线性影响：H_eff = H_static * (1 - P_stale) + P_stale * H_revalidate，其中 H_revalidate 为重新验证后的命中率；若 H_revalidate=0.9（即 10% 概率内容已变需回源），则 H_eff = H_static * (1 - 0.1 * P_stale)；在 P_stale=0.005 时，H_eff = H_static * 0.9995，即命中率下降 0.05 个百分点，折损倍数约为 0.9995 倍。

## Corrected Claim

Stale Fraction 对有效命中率的非线性影响：H_eff = H_static * (1 - P_stale) + P_stale * H_revalidate，其中 H_revalidate 为重新验证后的命中率；若 H_revalidate=0.9（即 10% 概率内容已变需回源），则 H_eff = H_static * (1 - 0.1 * P_stale)；在 P_stale=0.005 时，H_eff = H_static * 0.9995，即命中率下降 0.05 个百分点，折损倍数约为 0.9995 倍。

## Evidence

父节点级核验未通过：不完备（子节点1修正了H_revalidate的估算值，子节点2引入了LRU驱逐导致的额外Miss机制，两者关注点不同（参数精度 vs 机制缺失），无重复。但父节点公式 H_eff = H_static * (1 - P_stale) + P_stale * H_revalidate 隐含假设所有 Stale 对象都会触发 Revalidate，而子节点2指出部分 Stale 对象会直接变为 Miss。这意味着子节点2揭示的效应无法通过仅修正 H_revalidate 或 H_static 来完全覆盖，需要修改父节点公式的结构（例如增加一项直接 Miss 的概率），因此当前两个子节点未能完备地覆盖父节点公式在真实系统下的所有关键方面（即公式结构本身的缺陷）。）
