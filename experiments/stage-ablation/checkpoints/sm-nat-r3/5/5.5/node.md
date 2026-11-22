# N29: 主要不确定性来源 3：1%/天 更新率是否均匀分布在所有对象上，还是集中在某些对象（如动态内容），影响 Cache Thrashing 的局部化程度，估计误差范

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

主要不确定性来源 3：1%/天 更新率是否均匀分布在所有对象上，还是集中在某些对象（如动态内容），影响 Cache Thrashing 的局部化程度，估计误差范围 ±10-15% [待核验]。

## Corrected Claim

主要不确定性来源 3：1%/天 更新率是否均匀分布在所有对象上，还是集中在某些对象（如动态内容），影响 Cache Thrashing 的局部化程度。具体误差范围需进一步实证数据支持，当前估计为 ±10-15%（待核验）。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是对同一参数（更新率的空间分布模式）的三种不同取值（均匀、极端集中、加权混合），属于同一维度的离散采样而非独立正交维度；此外，子节点3（混合）在逻辑上涵盖了子节点1（β=0）和子节点2（β→∞或极值分布）作为特例，存在包含关系。）

## Search Query

non-uniform object update rate distribution impact on LRU cache invalidation CDN
