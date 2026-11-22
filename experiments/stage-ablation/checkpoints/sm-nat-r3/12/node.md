# N107: LRU 稳态字节命中率下界 H_LRU_lower 可近似为 1 - (1 - f_byte_cached) / (1 + ε_update)，其中 f_byt

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率下界 H_LRU_lower 可近似为 1 - (1 - f_byte_cached) / (1 + ε_update)，其中 f_byte_cached 为缓存内对象占总体请求字节量的比例。在 128GB 容量下，若缓存能覆盖前 20% 最热门对象（按请求量），且这些对象占总体字节量的 35%，则 f_byte_cached ≈ 0.35，H_LRU_lower ≈ 0.35（未计更新）。

## Corrected Claim

LRU 稳态字节命中率下界 H_LRU_lower 可近似为 1 - (1 - f_byte_cached) / (1 + ε_update)，其中 f_byte_cached 为缓存内对象占总体请求字节量的比例。在 128GB 容量下，若缓存能覆盖前 20% 最热门对象（按请求量），且这些对象占总体字节量的 35%，则 f_byte_cached ≈ 0.35，H_LRU_lower ≈ 0.35（未计更新）。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个核心变量（集合边界/分母基准、分子计算、更新惩罚项），逻辑上互斥且共同构成了公式的完整定义，无重叠或遗漏。）
