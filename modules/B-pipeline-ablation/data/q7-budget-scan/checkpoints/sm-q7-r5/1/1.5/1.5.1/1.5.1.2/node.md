# N164: HDD工作点2（大容量18TB）：选用Seagate Exos X20 18TB，单价约¥550/盘，400TB有效数据需约24块盘（RAID6 N=26, M

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

HDD工作点2（大容量18TB）：选用Seagate Exos X20 18TB，单价约¥550/盘，400TB有效数据需约24块盘（RAID6 N=26, M=2），物理总容量468TB，冗余开销14.5%，虽单价高但盘数减少降低了控制器端口占用和运维复杂度。

## Corrected Claim

HDD工作点2（大容量18TB）：选用Seagate Exos X20 18TB，单价约¥550/盘（需根据实际采购价核实），400TB有效数据需配置26块盘（RAID6，可用24块），物理总容量468TB，冗余开销约14.5%，盘数减少有助于降低控制器端口占用和运维复杂度。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应硬件摊销、电力成本和RTO风险成本，维度清晰且互斥，无重叠；父节点中的容量、冗余及运维复杂度定性描述已隐含在具体的数量参数（26块盘）和成本模型中，未遗漏关键量化维度。）

## Search Query

enterprise 18TB CMR HDD price per unit 2024
