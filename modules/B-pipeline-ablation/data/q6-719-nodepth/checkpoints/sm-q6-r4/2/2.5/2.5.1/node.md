# N81: 自建 POP 点的回源流量比例 (Origin Pull Ratio, R_origin) 计算为 1 - H_self，其中 H_self 为自建 POP 的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

自建 POP 点的回源流量比例 (Origin Pull Ratio, R_origin) 计算为 1 - H_self，其中 H_self 为自建 POP 的缓存命中率；在日均 2TB 下载量下，回源流量绝对值 V_origin = 2TB * R_origin (GB/天)。

## Corrected Claim

自建 POP 点的回源流量比例 (Origin Pull Ratio, R_origin) 计算为 1 - H_self，其中 H_self 为自建 POP 的缓存命中率；在日均 2TB 下载量下，回源流量绝对值 V_origin = 2TB * R_origin (GB/天)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了核心变量H_self及其构成（静态/动态未命中率），子节点2深入解释了其中静态未命中率受对象大小影响的特定参数化规则，子节点3提供了基于典型参数的具体数值计算示例。三者分别对应定义、参数敏感性分析和实例验证，逻辑层次清晰，互不重复且无矛盾。）
