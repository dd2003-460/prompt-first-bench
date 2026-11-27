# N40: 工作集大小与缓存容量比值 R_ws = W_LRU_bytes / C 是估算 MissRate 的关键参数，其中 W_LRU_bytes 是 LRU 策略下活

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

工作集大小与缓存容量比值 R_ws = W_LRU_bytes / C 是估算 MissRate 的关键参数，其中 W_LRU_bytes 是 LRU 策略下活跃工作集的总字节数，C=128GB，MissRate ≈ max(0, 1 - 1/R_ws) 为近似下界。

## Corrected Claim

工作集大小与缓存容量比值 R_ws = W_LRU_bytes / C 是估算 MissRate 的关键参数，其中 W_LRU_bytes 是 LRU 策略下活跃工作集的总字节数，C=128GB，MissRate ≈ max(0, 1 - 1/R_ws) 为近似下界。

## Evidence

先验知识/题面给定，逻辑校验通过
