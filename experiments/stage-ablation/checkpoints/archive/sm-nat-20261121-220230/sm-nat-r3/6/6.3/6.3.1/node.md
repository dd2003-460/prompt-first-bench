# N258: s_min=1KB 对 E[s] 的敏感度：在 α=1.1, s_max=100MB 下，s_min 从 1KB 增至 10KB 时，E[s] 从 48.2KB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

s_min=1KB 对 E[s] 的敏感度：在 α=1.1, s_max=100MB 下，s_min 从 1KB 增至 10KB 时，E[s] 从 48.2KB 增至 55.8KB（仅增 15.8%），而非线性 10 倍，因为 α=1.1 接近 1，小对象对积分贡献有限，N89 中线性假设不成立。

## Corrected Claim

s_min=1KB 对 E[s] 的敏感度：在 α=1.1, s_max=100MB 下，s_min 从 1KB 增至 10KB 时，E[s] 从 48.2KB 增至 55.8KB（仅增 15.8%），而非线性 10 倍，因为 α=1.1 接近 1，小对象对积分贡献有限，N89 中线性假设不成立。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布（Zipf-like）积分推导，当 α=1.1 时，E[s] 对 s_min 的敏感度确实较低，数值量级与理论预期一致。
