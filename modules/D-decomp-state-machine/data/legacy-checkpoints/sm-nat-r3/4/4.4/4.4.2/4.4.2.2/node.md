# N214: 尾部对象在 LRU 队列中的抖动风险量化：定义抖动幅度 J_tail = (W_LRU_max - W_LRU_min) / W_LRU_avg，其中 W_LR

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

尾部对象在 LRU 队列中的抖动风险量化：定义抖动幅度 J_tail = (W_LRU_max - W_LRU_min) / W_LRU_avg，其中 W_LRU_max = 1/λ_min，W_LRU_min = 1/λ_max；若 λ_max = 100 次/天，λ_min = 0.1 次/天，则 J_tail = (240h - 0.24h) / 12h ≈ 20，表明尾部对象驻留时间波动极大。

## Corrected Claim

尾部对象在 LRU 队列中的抖动风险量化：定义抖动幅度 J_tail = (W_LRU_max - W_LRU_min) / W_LRU_avg，其中 W_LRU_max = 1/λ_min，W_LRU_min = 1/λ_max；若 λ_max = 100 次/天，λ_min = 0.1 次/天，则 J_tail = (240h - 0.24h) / 12h ≈ 20，表明尾部对象驻留时间波动极大。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（240-0.24=239.76，239.76/12≈19.98≈20），量纲一致（小时），定义与计算过程自洽。
