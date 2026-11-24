# N717: Broadcom MegaRAID 9560-16i在重建过程中，由于PCIe带宽争用，主机侧PCIe链路利用率峰值达到95%，剩余5%带宽不足以支撑高并发小I

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N250, N251, N252

## Claim

Broadcom MegaRAID 9560-16i在重建过程中，由于PCIe带宽争用，主机侧PCIe链路利用率峰值达到95%，剩余5%带宽不足以支撑高并发小IO请求

## Corrected Claim

Broadcom MegaRAID 9560-16i在重建过程中，由于PCIe带宽争用，可能导致主机侧PCIe链路利用率显著升高，进而影响高并发小IO请求的性能。

## Evidence

[质询]该陈述包含具体的性能监控数据（PCIe链路利用率峰值95%、剩余5%带宽不足），这属于特定负载下的经验观测值或模拟结果，并非Broadcom官方文档中定义的通用硬件规格或必然发生的物理现象。现有公开资料通常只描述PCIe Gen4 x8的理论带宽和控制器架构，不会断言在重建过程中主机侧PCIe利用率必然达到95%这一具体数值。 | 来源[1]确认了MegaRAID 9560-16i采用PCIe Gen4 x8接口，逻辑上重建过程确实会占用大量带宽，但所有参考来源均未提供‘利用率峰值95%’或‘剩余5%带宽不足以支撑高并发小IO’的具体实证数据或官方声明，属于缺乏直接来源支持的经验性细节。

## Search Query

MegaRAID 9560 PCIe bandwidth utilization during RAID rebuild bottleneck

## Retrieval Sources

- {'url': 'https://www.broadcom.com/products/storage/raid-controllers/megaraid-9560-16i&rut=8ccfecff8a4e51aee841e560769746bc980702c636a024981fdb1c70f3d965df', 'type': 'ddg', 'title': 'MegaRAID 9560-16i | PCIe Gen 4.0 RAID Controller - Broadcom Inc.'}
- {'url': 'https://support.huawei.com/enterprise/zh/doc/EDOC1100157934/a466d751&rut=70db2b52282ccb477179ce80c2854b632672cc76136218c1756ece484f71fbda', 'type': 'ddg', 'title': 'BROADCOM MegaRAID 9560-16i - 鲲鹏服务器主板 RAID 控制卡用户指南 36 - 华为'}
- {'url': 'https://docs.broadcom.com/docs/95xx-MR-HBA-Tri-Mode-UG&rut=fe8410be584d1557c976240bce913ad911488b15de5e114f4d0954c52d01087e', 'type': 'ddg', 'title': 'Broadcom 95xx PCIe 4.0 MegaRAID and HBA Tri-Mode Storage Adapters User ...'}
