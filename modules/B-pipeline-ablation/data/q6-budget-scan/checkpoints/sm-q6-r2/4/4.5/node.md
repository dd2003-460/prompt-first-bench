# N38: 10 个自建 POP 的覆盖效率指标 $\eta_{coverage}$：定义为 $\eta_{coverage} = \frac{\text{命中本地 POP

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

10 个自建 POP 的覆盖效率指标 $\eta_{coverage}$：定义为 $\eta_{coverage} = \frac{\text{命中本地 POP 的请求比例}}{\text{总请求比例}}$；对于 10 个 POP，预期 $\eta_{coverage} \approx 75\%-85\%$（取决于用户分布集中度），剩余 15%-25% 流量需回源或走公有云，该比例直接决定混合策略中公有云的流量基数。

## Corrected Claim

10 个自建 POP 的覆盖效率指标 $\eta_{coverage}$：定义为 $\eta_{coverage} = \frac{\text{命中本地 POP 的请求比例}}{\text{总请求比例}}$；对于 10 个 POP，预期 $\eta_{coverage} \approx 75\%-85\%$（取决于用户分布集中度），剩余 15%-25% 流量需回源或走公有云，该比例直接决定混合策略中公有云的流量基数。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于指标的理论推导与边界估计（基于Zipf分布和选址算法），子节点2聚焦于该指标在实际工程中的具体数值计算及后续模块（带宽成本）的输入映射。两者分别对应‘理论模型’与‘工程应用’，逻辑上正交且互补，共同覆盖了父节点中关于定义、预期范围及后续影响的描述，无重复或矛盾。）
