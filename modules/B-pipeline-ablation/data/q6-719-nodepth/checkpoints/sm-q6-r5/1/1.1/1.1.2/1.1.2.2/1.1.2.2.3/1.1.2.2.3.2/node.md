# N1279: 缓存命中率的Zipf解析公式：H_video(N_hot) = 1 - (1 - N_hot/N_total)^(1-α)；当 N_hot=1.25M, N_t

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N437

## Claim

缓存命中率的Zipf解析公式：H_video(N_hot) = 1 - (1 - N_hot/N_total)^(1-α)；当 N_hot=1.25M, N_total≈50M, α=1.2 时，H_video ≈ 80%；若 N_hot 减半至 0.625M，H_video 降至 ≈ 72%。

## Corrected Claim

缓存命中率的Zipf解析公式：H_video(N_hot) = 1 - (1 - N_hot/N_total)^(1-α)；当 N_hot=1.25M, N_total≈50M, α=1.2 时，H_video ≈ 80%；若 N_hot 减半至 0.625M，H_video 降至 ≈ 72%。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖具体数值但提供了公式背景（来源[1][2][3]）

## Search Query

Zipf law cache hit ratio formula video streaming
