# N19: LRU 稳态缓存驻留对象的大小阈值 S_threshold：由缓存容量 C=128GB 和对象访问频率决定，S_threshold = C / (Σ_{i in

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LRU 稳态缓存驻留对象的大小阈值 S_threshold：由缓存容量 C=128GB 和对象访问频率决定，S_threshold = C / (Σ_{i in cache} f_i)，需通过求解 ∫_{x_min}^{S_threshold} f(x) * S(x) dx = C 得到具体数值。

## Corrected Claim

LRU 稳态缓存驻留对象的大小阈值 S_threshold：由缓存容量 C=128GB 和对象访问频率决定，S_threshold = C / (Σ_{i in cache} f_i)，需通过求解 ∫_{x_min}^{S_threshold} f(x) * S(x) dx = C 得到具体数值。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（对应不同的假设边界）且覆盖了从保守到极端的关键场景（完备性良好）。然而，三个子节点本质上是同一计算模型（S_threshold 积分方程）在 S_max 参数取不同值时的具体实例。它们共享相同的公式结构和求解逻辑，仅输入参数（S_max）和输出结果（S_threshold, H_LRU）不同，因此存在结构性冗余，应抽象为参数化描述而非三个独立节点。）
