# N73: 冷数据点查延迟约束 P99_point_query < 10ms 仅适用于<1%流量的偶发点查；若点查频率为0.1%（即500TB中0.5TB数据被点查），则点

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

冷数据点查延迟约束 P99_point_query < 10ms 仅适用于<1%流量的偶发点查；若点查频率为0.1%（即500TB中0.5TB数据被点查），则点查IOPS = 0.5TB / 1MB / 24h / 3600s ≈ 0.006 IOPS，可忽略；但单次点查延迟需<10ms，对HDD机械寻道（~10ms）构成边界，对SSD（~0.1ms）和S3（~50ms）构成约束，S3不满足此约束

## Corrected Claim

冷数据点查延迟约束 P99_point_query < 10ms 仅适用于<1%流量的偶发点查；若点查频率为0.1%（即500TB中0.5TB数据被点查），则点查IOPS = 0.5TB / 1MB / 24h / 3600s ≈ 0.006 IOPS，可忽略；但单次点查延迟需<10ms，对HDD机械寻道（~10ms）构成边界，对SSD（~0.1ms）和S3（~50ms）构成约束，S3不满足此约束

## Evidence

先验知识/题面给定，逻辑校验通过：IOPS计算量级正确（0.5TB/24h ≈ 0.006 IOPS），HDD/SSD/S3延迟量级符合工程常识，S3不满足10ms约束符合事实。
