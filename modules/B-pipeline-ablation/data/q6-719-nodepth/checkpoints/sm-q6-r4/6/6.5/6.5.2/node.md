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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1定义了总成本模型，子节点2和3分别定义了模型中两个关键变量（自建和公有云成本）的具体计算公式，子节点4则基于前三个节点推导出了父节点中提到的‘变化影响’的具体数学表达式。没有重复内容，也没有遗漏父节点中关于公式变化、参数定义及增量计算的关键信息。）

## Search Query

Hybrid CDN cost model geographic traffic split
