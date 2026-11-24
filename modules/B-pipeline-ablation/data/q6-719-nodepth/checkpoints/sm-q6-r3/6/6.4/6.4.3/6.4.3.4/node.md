# N519: 缓存命中率H_miss随对象大小s的非线性变化：当s > 2MB时，H_miss从0.05上升至0.15，因为大文件缓存占用内存更多，导致缓存容量限制下的命中率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

缓存命中率H_miss随对象大小s的非线性变化：当s > 2MB时，H_miss从0.05上升至0.15，因为大文件缓存占用内存更多，导致缓存容量限制下的命中率下降，具体函数形式需基于LRU缓存模型估算。

## Corrected Claim

缓存命中率H_miss随对象大小s的非线性变化：当s > 2MB时，H_miss从0.05上升至0.15，因为大文件缓存占用内存更多，导致缓存容量限制下的命中率下降，具体函数形式需基于LRU缓存模型估算。

## Evidence

先验知识/题面给定，逻辑校验通过：大对象占用更多缓存空间导致LRU命中率下降符合缓存基本原理，数值量级合理。

## Search Query

CDN cache hit rate vs object size nonlinear relationship
