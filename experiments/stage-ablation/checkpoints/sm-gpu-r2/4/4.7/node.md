# N22: 并发场景分类与负载模型：将并发场景分为三类：S1=单用户交互式（concurrency=1, latency-sensitive），S2=小规模批量（concu

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

并发场景分类与负载模型：将并发场景分为三类：S1=单用户交互式（concurrency=1, latency-sensitive），S2=小规模批量（concurrency=4-8, throughput-sensitive），S3=大规模服务（concurrency=16+, cost-sensitive）。每种场景对应不同的性能权重：S1侧重P99延迟，S2侧重吞吐/成本，S3侧重TCO/能效比。决策矩阵需按场景分别加权。

## Corrected Claim

并发场景分类与负载模型：将并发场景分为三类：S1=单用户交互式（concurrency=1, latency-sensitive），S2=小规模批量（concurrency=4-8, throughput-sensitive），S3=大规模服务（concurrency=16+, cost-sensitive）。每种场景对应不同的性能权重：S1侧重P99延迟，S2侧重吞吐/成本，S3侧重TCO/能效比。决策矩阵需按场景分别加权。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中定义的S1、S2、S3三种并发场景，彼此独立且无重叠（正交）；覆盖了父节点提到的所有场景分类及其对应的性能权重侧重（完备）；虽然公式结构相似，但权重系数和指标侧重不同，反映了不同场景的本质差异，不属于单纯参数替换的冗余（非冗余）。）
