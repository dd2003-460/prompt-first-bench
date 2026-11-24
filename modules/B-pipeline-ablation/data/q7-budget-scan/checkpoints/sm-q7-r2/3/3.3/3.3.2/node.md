# N95: 500TB总容量扩展性约束：本地NVMe SSD阵列最大单阵列容量受控制器通道数限制，典型企业级存储控制器支持<1000块盘，500块SSD在限制内；HDD+S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

500TB总容量扩展性约束：本地NVMe SSD阵列最大单阵列容量受控制器通道数限制，典型企业级存储控制器支持<1000块盘，500块SSD在限制内；HDD+SSD分层HDD 30块+SSD 25块共55块盘，在限制内；云存储无扩展性限制，可线性扩展至PB级

## Corrected Claim

500TB总容量扩展性约束：本地NVMe SSD阵列最大单阵列容量受控制器通道数限制，典型企业级存储控制器支持<1000块盘，500块SSD在限制内；HDD+SSD分层HDD 30块+SSD 25块共55块盘，在限制内；云存储无扩展性限制，可线性扩展至PB级

## Evidence

先验知识/题面给定，逻辑校验通过：企业级存储控制器通道数限制通常在数百至千块盘量级，500块SSD及55块混合盘均在合理物理限制范围内；云存储线性扩展至PB级符合分布式存储基本架构原理。

## Search Query

enterprise storage controller maximum disk count limit NVMe HDD
