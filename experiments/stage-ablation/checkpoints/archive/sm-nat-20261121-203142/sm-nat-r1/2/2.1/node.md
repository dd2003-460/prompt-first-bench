# N10: LRU 稳态字节命中率下界推导采用工作集模型（Working Set Model），假设缓存容量 C 下 LRU 保留最近访问的 C 字节内容，命中率 H = 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 稳态字节命中率下界推导采用工作集模型（Working Set Model），假设缓存容量 C 下 LRU 保留最近访问的 C 字节内容，命中率 H = P(请求对象在工作集内) × (对象大小/请求大小)

## Corrected Claim

LRU 稳态字节命中率下界推导采用工作集模型（Working Set Model），假设缓存容量 C 下 LRU 保留最近访问的 C 字节内容，命中率 H = P(请求对象在工作集内) × (对象大小/请求大小)

## Evidence

先验知识/题面给定，逻辑校验通过
