# N146: A100 80GB (SXM)在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限为 2039 GB/s / 37.7 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

A100 80GB (SXM)在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限为 2039 GB/s / 37.7 GB ≈ 54.1 tokens/s，该值由HBM2e带宽除以相同数据量（权重27GB + KV Cache 10.7GB）决定。

## Corrected Claim

A100 80GB (SXM)在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限为 2039 GB/s / 37.7 GB ≈ 54.1 tokens/s，该值由HBM2e带宽除以相同数据量（权重27GB + KV Cache 10.7GB）决定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点A定义理论上限（理想条件），子节点B定义现实基准（实测条件），两者在定义域上互斥且互补，共同覆盖了父节点中'理论吞吐上限'及其决定因素（带宽、数据量）以及隐含的工程落地差距，无重复或矛盾。）
