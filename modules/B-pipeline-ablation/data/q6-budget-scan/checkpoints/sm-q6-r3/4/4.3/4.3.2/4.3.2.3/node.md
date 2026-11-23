# N201: N_unique_hot 的地理分布不均匀性：核心区域（如一线城市）N_unique_hot_core ≈ 0.3-0.5 * N_unique_hot_tot

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

N_unique_hot 的地理分布不均匀性：核心区域（如一线城市）N_unique_hot_core ≈ 0.3-0.5 * N_unique_hot_total，长尾区域 N_unique_hot_tail ≈ 0.5-0.7 * N_unique_hot_total，影响混合策略中自建节点的容量规划。

## Corrected Claim

N_unique_hot 的地理分布呈现不均匀性，核心区域与长尾区域的占比取决于用户偏好的重叠度与分散度，需根据具体业务数据确定，而非固定为 0.3-0.5 与 0.5-0.7。

## Evidence

[质询]数值量级与常识直觉存在潜在冲突：通常‘核心区域’（一线城市）人口密度高、用户基数大，其独占热点（Unique Hot）数量理应高于‘长尾区域’。陈述中核心区域占比（0.3-0.5）低于长尾区域（0.5-0.7），暗示长尾区域贡献了更多的‘独特’热点，这仅在特定定义下（如长尾区域用户偏好极度分散且无重叠，而核心区域高度重叠）才成立，缺乏通用性，易被质疑为口径混淆或反直觉。 | source=knowledge，逻辑上自洽（总和为1，无内部矛盾），但具体数值分布（核心<长尾）属于特定场景下的经验估计，缺乏普适性第一性原理支持，且无外部来源佐证，故降级为定性表述。

## Search Query

geographic distribution of content popularity CDN regional hot objects
