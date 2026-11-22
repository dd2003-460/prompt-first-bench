# N178: 推导链步骤2：利用 Zipf 分布累积和公式，求解缓存可容纳的 Top-K 对象数量 K_max，使得 Σ_{r=1}^{K_max} r^(-0.9) 对应的

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

推导链步骤2：利用 Zipf 分布累积和公式，求解缓存可容纳的 Top-K 对象数量 K_max，使得 Σ_{r=1}^{K_max} r^(-0.9) 对应的字节权重达到 C/S_total 比例。

## Corrected Claim

推导链步骤2：利用 Zipf 分布累积和公式，求解缓存可容纳的 Top-K 对象数量 K_max，使得 Σ_{r=1}^{K_max} r^(-0.9) 对应的字节权重达到 C/S_total 比例。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Zipf law cumulative sum formula top K objects
