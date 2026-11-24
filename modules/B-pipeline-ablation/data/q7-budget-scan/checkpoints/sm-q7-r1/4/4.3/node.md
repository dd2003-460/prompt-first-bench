# N21: 温数据IOPS约束：20%温数据（100TB）每天扫描1-2次，假设单次扫描读取全量100TB，平均IOPS需求约为100TB/86400s*1.5/4KB≈4

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

温数据IOPS约束：20%温数据（100TB）每天扫描1-2次，假设单次扫描读取全量100TB，平均IOPS需求约为100TB/86400s*1.5/4KB≈4.4M IOPS；本地NVMe SSD阵列（如10块960GB NVMe）可提供约1M IOPS，不满足需求需扩容至40块，硬件成本增加4x；HDD+SSD方案中SSD层需承载全部温数据IOPS，若SSD容量<100TB则需依赖HDD，IOPS降至~1000，扫描时间从分钟级延长至小时级

## Corrected Claim

温数据IOPS约束：20%温数据（100TB）每天扫描1-2次，假设单次扫描读取全量100TB，平均IOPS需求约为100TB/86400s*1.5/4KB≈4.4M IOPS；本地NVMe SSD阵列（如10块960GB NVMe）可提供约1M IOPS，不满足需求需扩容至40块，硬件成本增加4x；HDD+SSD方案中SSD层需承载全部温数据IOPS，若SSD容量<100TB则需依赖HDD，IOPS降至~1000，扫描时间从分钟级延长至小时级

## Evidence

先验知识/题面给定，逻辑校验通过：IOPS计算量级合理（100TB/86400s*1.5/4KB≈4.4M），NVMe与HDD性能差异符合工程常识
