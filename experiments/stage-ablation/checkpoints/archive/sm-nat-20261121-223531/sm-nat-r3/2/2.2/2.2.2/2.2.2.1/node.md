# N125: 边界对象集合的定义：在LRU堆栈模型中，被误判为“完全淘汰”但实际部分驻留的对象集合 $S_{boundary}$ 定义为堆栈深度 $D_i$ 满足 $C_{o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

边界对象集合的定义：在LRU堆栈模型中，被误判为“完全淘汰”但实际部分驻留的对象集合 $S_{boundary}$ 定义为堆栈深度 $D_i$ 满足 $C_{obj} - \Delta_{width} < D_i \le C_{obj}$ 的对象，其中 $\Delta_{width}$ 为缓存容量波动导致的边界宽度，通常取最近一次替换周期的平均对象数。

## Corrected Claim

边界对象集合的定义：在LRU堆栈模型中，被误判为“完全淘汰”但实际部分驻留的对象集合 $S_{boundary}$ 定义为堆栈深度 $D_i$ 满足 $C_{obj} - \Delta_{width} < D_i \le C_{obj}$ 的对象，其中 $\Delta_{width}$ 为缓存容量波动导致的边界宽度，通常取最近一次替换周期的平均对象数。

## Evidence

先验知识/题面给定，逻辑校验通过
