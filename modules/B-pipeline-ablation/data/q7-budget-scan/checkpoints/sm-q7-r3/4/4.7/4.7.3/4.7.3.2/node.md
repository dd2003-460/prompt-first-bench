# N239: 冷启动期间业务查询延迟从SSD缓存命中的5ms上升至HDD读取的100ms，性能降级系数为20倍，若SLA要求P99延迟<50ms，则冷启动期间业务不可用，需计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

冷启动期间业务查询延迟从SSD缓存命中的5ms上升至HDD读取的100ms，性能降级系数为20倍，若SLA要求P99延迟<50ms，则冷启动期间业务不可用，需计入RTO代价

## Corrected Claim

冷启动期间业务查询延迟从SSD缓存命中的5ms上升至HDD读取的100ms，性能降级系数为20倍，若SLA要求P99延迟<50ms，则冷启动期间业务不可用，需计入RTO代价

## Evidence

先验知识/题面给定，逻辑校验通过：100ms/5ms=20倍，且100ms>50ms导致SLA违约，推导自洽
