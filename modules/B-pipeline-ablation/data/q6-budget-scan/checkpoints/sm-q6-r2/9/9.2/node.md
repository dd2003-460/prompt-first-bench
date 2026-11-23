# N136: Zipf 分布下的理论命中率 $H_{zipf}$ 计算：对于 $N$ 个对象，Zipf 参数 $s=1$ 时，前 $K$ 个热点对象占总请求的比例 $H \a

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Zipf 分布下的理论命中率 $H_{zipf}$ 计算：对于 $N$ 个对象，Zipf 参数 $s=1$ 时，前 $K$ 个热点对象占总请求的比例 $H \approx \sum_{i=1}^{K} (1/i) / \sum_{i=1}^{N} (1/i)$，需根据对象总数和缓存容量确定 $K$。

## Corrected Claim

Zipf 分布下的理论命中率 $H_{zipf}$ 计算：对于 $N$ 个对象，Zipf 参数 $s=1$ 时，前 $K$ 个热点对象占总请求的比例 $H \approx \sum_{i=1}^{K} (1/i) / \sum_{i=1}^{N} (1/i)$，需根据对象总数和缓存容量确定 $K$。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf 分布定义及归一化公式推导正确，量纲与逻辑自洽。

## Search Query

Zipf distribution cache hit ratio formula
