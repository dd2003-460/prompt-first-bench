# N117: 在 Zipf 排名近似下，前 K 个最热门对象的请求概率占比 P_topK 的精确解析公式为 P_topK = (∑_{i=1}^K i^{-β}) / (∑_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41, N42, N43

## Claim

在 Zipf 排名近似下，前 K 个最热门对象的请求概率占比 P_topK 的精确解析公式为 P_topK = (∑_{i=1}^K i^{-β}) / (∑_{i=1}^N i^{-β})，其中 N=100,000，β=0.9；该比值是计算字节命中率下界的核心分子项，不可简单用 1-(K/N)^(1-β) 替代，因为 β<1 时调和级数发散需截断处理。

## Corrected Claim

在 Zipf 排名近似下，前 K 个最热门对象的请求概率占比 P_topK 的精确解析公式为 P_topK = (∑_{i=1}^K i^{-β}) / (∑_{i=1}^N i^{-β})，其中 N=100,000，β=0.9；该比值是计算字节命中率下界的核心分子项，不可简单用 1-(K/N)^(1-β) 替代，因为 β<1 时调和级数发散需截断处理。

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf 分布定义下概率占比即为归一化常数之比，公式推导正确；β=0.9<1 时调和级数发散，必须截断至 N，不能用无穷级数近似公式替代，逻辑自洽。

## Search Query

Zipf law cumulative distribution truncated sum formula
