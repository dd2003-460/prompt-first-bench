# N23: 缓存失效策略：TTL (Time-To-Live) 设置影响命中率与新鲜度；典型 TTL 为 1-24 小时，需平衡存储成本与回源率

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

缓存失效策略：TTL (Time-To-Live) 设置影响命中率与新鲜度；典型 TTL 为 1-24 小时，需平衡存储成本与回源率

## Corrected Claim

缓存失效策略：TTL (Time-To-Live) 设置影响命中率与新鲜度；典型 TTL 为 1-24 小时，需平衡存储成本与回源率

## Evidence

父节点级核验未通过：不完备（子节点分别描述了命中率、存储成本和回源率三个维度，彼此正交且无冗余。但父节点明确提到需平衡'新鲜度'，而子节点仅通过命中率（通常与新鲜度负相关）间接体现，未直接对'新鲜度'或'数据陈旧度'进行独立建模或定义，导致覆盖不全。此外，给出的公式为虚构的通用形式，缺乏具体场景约束，但在结构分解上主要问题是维度缺失。）

## Search Query

CDN cache TTL best practices image video platform
