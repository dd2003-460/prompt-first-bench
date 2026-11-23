# N79: 单点设备维护成本 C_maintenance 由硬件保修服务费和备件库成本构成，C_maintenance = N_servers * C_warranty +

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

单点设备维护成本 C_maintenance 由硬件保修服务费和备件库成本构成，C_maintenance = N_servers * C_warranty + C_spare_parts，其中 C_warranty 为单台服务器年延保费用（约 ¥1k-3k/台），C_spare_parts 为硬盘/内存等易损件预留预算（约 ¥2k-5k/点/年），取决于设备折旧年限和故障率 MTBF。

## Corrected Claim

单点设备维护成本 C_maintenance 由硬件保修服务费和备件库成本构成，C_maintenance = N_servers * C_warranty + C_spare_parts，其中 C_warranty 为单台服务器年延保费用（约 ¥1k-3k/台），C_spare_parts 为硬盘/内存等易损件预留预算（约 ¥2k-5k/点/年），取决于设备折旧年限和故障率 MTBF。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

server hardware warranty cost annual maintenance budget IT infrastructure
