# N173: 当用户地理分布从集中（80%核心/20%长尾）变为分散（50%核心/50%长尾）时，混合策略的带宽成本 C_bandwidth_mix 从 0.8*C_band

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N44

## Claim

当用户地理分布从集中（80%核心/20%长尾）变为分散（50%核心/50%长尾）时，混合策略的带宽成本 C_bandwidth_mix 从 0.8*C_bandwidth_self + 0.2*C_bandwidth_public 变为 0.5*C_bandwidth_self + 0.5*C_bandwidth_public，由于 C_bandwidth_public > C_bandwidth_self，总带宽成本上升约 40%。

## Corrected Claim

当用户地理分布从集中（80%核心/20%长尾）变为分散（50%核心/50%长尾）时，混合策略的带宽成本 C_bandwidth_mix 从 0.8*C_bandwidth_self + 0.2*C_bandwidth_public 变为 0.5*C_bandwidth_self + 0.5*C_bandwidth_public。由于 C_bandwidth_public > C_bandwidth_self，总带宽成本将上升，具体上升幅度取决于 C_bandwidth_public 与 C_bandwidth_self 的比值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义总成本公式，节点2和节点3分别定义两个组成部分的具体计算逻辑（自建与公有云），节点4聚焦于分布变化带来的增量分析。各节点职责明确，无重复或矛盾，且共同覆盖了父节点中关于公式结构、参数计算及变化影响的描述。）

## Search Query

Hybrid CDN cost model geographic traffic split
