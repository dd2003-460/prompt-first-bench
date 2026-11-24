# N53: T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_to_Origin 受源站出口带宽限制（典型单源站出口 1-10 Gbps）及 TCP 窗口大小限制（MSS × cwnd）[待核验]

## Corrected Claim

T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_to_Origin 受源站出口带宽限制（典型单源站出口 1-10 Gbps）及 TCP 窗口大小限制（MSS × cwnd）[待核验]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于分子（对象大小分布），子节点2聚焦于分母（带宽瓶颈及TCP限制），两者分别对应公式的两个主要变量，正交且互补。虽然子节点2中包含了具体的数值计算示例（如222Mbps），但这属于对‘带宽瓶颈’这一抽象概念的具体量化解释，并未与子节点1的内容重复或矛盾，因此不构成冗余。）

## Search Query

TCP window size limit large file transfer bandwidth efficiency
