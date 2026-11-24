# N53: T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_to_Origin 受源站出口带宽限制（典型单源站出口 1-10 Gbps）及 TCP 窗口大小限制（MSS × cwnd）[待核验]

## Corrected Claim

T_transfer = Object_Size / Effective_Bandwidth_to_Origin，其中 Effective_Bandwidth_to_Origin 受源站出口带宽限制（典型单源站出口 1-10 Gbps）及 TCP 窗口大小限制（MSS × cwnd）[待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：传输时间公式符合物理定义，源站出口带宽量级（1-10 Gbps）及TCP窗口限制机制符合网络工程常识。

## Search Query

TCP window size limit large file transfer bandwidth efficiency
