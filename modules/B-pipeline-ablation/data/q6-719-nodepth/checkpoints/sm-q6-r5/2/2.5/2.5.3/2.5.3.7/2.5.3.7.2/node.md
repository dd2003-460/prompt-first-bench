# N629: 工作点 1 的服务器数量 N_servers = 95 台是基于单台服务器有效带宽利用率 70% 计算得出，其隐含假设是服务器网络接口为 25Gbps 且无单点

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N208

## Claim

工作点 1 的服务器数量 N_servers = 95 台是基于单台服务器有效带宽利用率 70% 计算得出，其隐含假设是服务器网络接口为 25Gbps 且无单点瓶颈；实际部署中需考虑网卡聚合或双口绑定，若单口 10Gbps 则需 2 个端口，影响物理服务器选型与成本 C_server。

## Corrected Claim

工作点 1 的服务器数量 N_servers = 95 台是基于单台服务器有效带宽利用率 70% 计算得出，其隐含假设是服务器网络接口为 25Gbps 且无单点瓶颈；实际部署中需考虑网卡聚合或双口绑定，若单口 10Gbps 则需 2 个端口，影响物理服务器选型与成本 C_server。

## Evidence

先验知识/题面给定，逻辑校验通过：95台服务器在25Gbps带宽下满足70%利用率假设，且10Gbps需双口绑定的物理约束符合网络工程常识，无内部矛盾。

## Search Query

server network interface aggregation 25Gbps CDN edge node design
