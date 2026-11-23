# N136: Zipf 分布下的理论命中率 $H_{zipf}$ 计算：对于 $N$ 个对象，Zipf 参数 $s=1$ 时，前 $K$ 个热点对象占总请求的比例 $H \a

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Zipf 分布下的理论命中率 $H_{zipf}$ 计算：对于 $N$ 个对象，Zipf 参数 $s=1$ 时，前 $K$ 个热点对象占总请求的比例 $H \approx \sum_{i=1}^{K} (1/i) / \sum_{i=1}^{N} (1/i)$，需根据对象总数和缓存容量确定 $K$。

## Corrected Claim

Zipf 分布下的理论命中率 $H_{zipf}$ 计算：对于 $N$ 个对象，Zipf 参数 $s=1$ 时，前 $K$ 个热点对象占总请求的比例 $H \approx \sum_{i=1}^{K} (1/i) / \sum_{i=1}^{N} (1/i)$，需根据对象总数和缓存容量确定 $K$。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的关键变量（N, K, s）及最终计算结果，逻辑链条清晰且无重叠。N和K的估算基于不同的物理约束（数据总量 vs 缓存容量），s是分布参数，最后一步是综合计算，符合正交性要求。）

## Search Query

Zipf distribution cache hit ratio formula
