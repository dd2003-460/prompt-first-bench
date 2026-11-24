# N157: 单POP硬件总成本 C_pop_hardware = N_server_per_pop * P_server + N_disk_per_pop * P_disk

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

单POP硬件总成本 C_pop_hardware = N_server_per_pop * P_server + N_disk_per_pop * P_disk + P_network_per_pop，其中 N_server_per_pop 通常配置为 2-4 台冗余服务器，P_server 约为 2-5 万元/台，P_disk (NVMe SSD) 约为 0.3-0.5 元/GB，P_network (10G/40G 网卡及交换机) 约为 1-2 万元/POP

## Corrected Claim

单POP硬件总成本 C_pop_hardware = N_server_per_pop * P_server + N_disk_per_pop * P_disk + P_network_per_pop，其中 N_server_per_pop 通常配置为 2-4 台冗余服务器，P_server 约为 2-5 万元/台，P_disk (NVMe SSD) 约为 0.3-0.5 元/GB，P_network (10G/40G 网卡及交换机) 约为 1-2 万元/POP

## Evidence

先验知识/题面给定，逻辑校验通过
