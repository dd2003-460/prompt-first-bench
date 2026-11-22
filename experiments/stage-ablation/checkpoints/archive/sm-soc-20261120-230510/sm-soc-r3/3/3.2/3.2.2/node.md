# N60: 曝光量 Exposure 的量化构成：Exposure = W × Traffic_Pool，其中 W 为推荐权重，Traffic_Pool 为总流量池大小；W

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

曝光量 Exposure 的量化构成：Exposure = W × Traffic_Pool，其中 W 为推荐权重，Traffic_Pool 为总流量池大小；W = α·P_ask + β。

## Corrected Claim

曝光量 Exposure 的量化构成：Exposure = W × Traffic_Pool，其中 W 为推荐权重，Traffic_Pool 为总流量池大小；W = α·P_ask + β。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式 Exposure = W × Traffic_Pool 中的两个主要因子 W 和 Traffic_Pool。其中 W 被进一步分解为线性系数 α 和截距 β，这三个子节点分别独立地定义了公式中的不同组成部分（α, β, Traffic_Pool），彼此之间没有逻辑重叠或矛盾，且共同覆盖了父节点公式的所有变量构成。）
