# N125: 用于评估数据可信度的三级标注标准定义：'Verified'（来自NVIDIA官方白皮书/学术论文，误差<5%）、'Estimated'（基于社区基准测试平均，误

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

用于评估数据可信度的三级标注标准定义：'Verified'（来自NVIDIA官方白皮书/学术论文，误差<5%）、'Estimated'（基于社区基准测试平均，误差10-20%）、'Speculative'（基于理论推导或传闻，误差>20%）；所有TCO关键参数必须显式标记此级别。

## Corrected Claim

用于评估数据可信度的三级标注标准定义：'Verified'（来自NVIDIA官方白皮书/学术论文，误差<5%）、'Estimated'（基于社区基准测试平均，误差10-20%）、'Speculative'（基于理论推导或传闻，误差>20%）；所有TCO关键参数必须显式标记此级别。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点定义的三个级别（Verified, Estimated, Speculative），彼此在数据源、误差范围和判定条件上互斥且无重叠，覆盖了父节点所有关键方面，且每个子节点包含具体的量化标准和判定逻辑，不属于简单的参数取值枚举，而是具有不同验证方法的独立定义。）
