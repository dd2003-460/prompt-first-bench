# N79: 单点设备维护成本 C_maintenance 由硬件保修服务费和备件库成本构成，C_maintenance = N_servers * C_warranty +

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

单点设备维护成本 C_maintenance 由硬件保修服务费和备件库成本构成，C_maintenance = N_servers * C_warranty + C_spare_parts，其中 C_warranty 为单台服务器年延保费用（约 ¥1k-3k/台），C_spare_parts 为硬盘/内存等易损件预留预算（约 ¥2k-5k/点/年），取决于设备折旧年限和故障率 MTBF。

## Corrected Claim

单点设备维护成本 C_maintenance 由硬件保修服务费和备件库成本构成，C_maintenance = N_servers * C_warranty + C_spare_parts，其中 C_warranty 为单台服务器年延保费用（约 ¥1k-3k/台），C_spare_parts 为硬盘/内存等易损件预留预算（约 ¥2k-5k/点/年），取决于设备折旧年限和故障率 MTBF。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上互斥且覆盖了高/中/低三种典型场景，具备正交性和完备性。然而，这三个子节点本质上是同一公式 C_maintenance = N_servers * C_warranty + C_spare_parts 在不同参数取值下的实例化，属于典型的参数化冗余。在学术或工程建模中，应将公式作为核心节点，而将具体数值作为该节点的属性或示例，而非拆分为三个并列的子节点，否则会导致知识图谱结构扁平化且难以扩展。）

## Search Query

server hardware warranty cost annual maintenance budget IT infrastructure
