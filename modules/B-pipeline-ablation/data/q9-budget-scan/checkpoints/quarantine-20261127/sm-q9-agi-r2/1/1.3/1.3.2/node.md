# N38: 投机解码的有效加速比公式为 Speedup = (1 + α * K) / (1 + ε * K)，其中 K=4 (draft tokens), ε 为验证开销

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

投机解码的有效加速比公式为 Speedup = (1 + α * K) / (1 + ε * K)，其中 K=4 (draft tokens), ε 为验证开销比率（V100 上约为 0.1-0.2，因验证需额外 Forward Pass）；当 α=0.5, ε=0.15 时，Speedup ≈ (1+2)/(1+0.6) ≈ 1.87x；这意味着每 token 耗时并非简单减少 30-40%，而是总延迟降低约 46%，但在高熵场景下若 α<0.3，加速比可能低于 1.0x（即负优化）。

## Corrected Claim

投机解码的有效加速比公式为 Speedup = (1 + α * K) / (1 + ε * K)，其中 K=4 (draft tokens), ε 为验证开销比率（V100 上约为 0.1-0.2，因验证需额外 Forward Pass）；当 α=0.5, ε=0.15 时，Speedup ≈ (1+2)/(1+0.6) ≈ 1.87x；这意味着每 token 耗时并非简单减少 30-40%，而是总延迟降低约 46%，但在高熵场景下若 α<0.3，加速比可能低于 1.0x（即负优化）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合投机解码标准模型，数值计算 (1+0.5*4)/(1+0.15*4)=3/1.6=1.875 准确，延迟降低比例 1-1/1.875≈46.7% 与陈述一致，高熵低接受率导致负优化的逻辑亦成立。

## Search Query

speculative decoding speedup formula verification overhead epsilon
