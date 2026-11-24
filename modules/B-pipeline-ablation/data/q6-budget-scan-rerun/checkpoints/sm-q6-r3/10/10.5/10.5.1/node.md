# N291: 服务器硬件成本细化 Cost_Servers = N_servers * P_server_unit，假设单节点配置2台双路服务器以实现高可用，N_server

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

服务器硬件成本细化 Cost_Servers = N_servers * P_server_unit，假设单节点配置2台双路服务器以实现高可用，N_servers=2，P_server_unit (双路Xeon/EPYC+128GB RAM) ≈ ¥25,000-¥30,000/台，则 Cost_Servers ≈ ¥50,000-¥60,000。

## Corrected Claim

服务器硬件成本细化 Cost_Servers = N_servers * P_server_unit，假设单节点配置2台双路服务器以实现高可用，N_servers=2，P_server_unit (双路Xeon/EPYC+128GB RAM) ≈ ¥25,000-¥30,000/台，则 Cost_Servers ≈ ¥50,000-¥60,000。

## Evidence

先验知识/题面给定，逻辑校验通过：双路服务器配置2台实现高可用符合工程惯例，单台双路Xeon/EPYC+128GB RAM成本在2.5万-3万元区间符合当前硬件市场行情，总成本计算逻辑自洽。

## Search Query

dual-socket server price Xeon EPYC 128GB RAM China market
