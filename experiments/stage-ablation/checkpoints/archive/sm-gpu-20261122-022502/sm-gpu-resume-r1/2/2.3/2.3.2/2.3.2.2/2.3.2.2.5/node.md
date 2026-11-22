# N624: 4x RTX 4090 在 TP=4 下，若采用 Ring All-Reduce 算法，实际通信量为 2*(N-1)/N * 0.54 GB ≈ 0.405 G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191, N192, N193

## Claim

4x RTX 4090 在 TP=4 下，若采用 Ring All-Reduce 算法，实际通信量为 2*(N-1)/N * 0.54 GB ≈ 0.405 GB（N=4），而非 0.54 GB，因此修正后单次 All-Reduce 延迟为 0.405 GB / 50 GB/s = 8.1 ms，占单 token 生成时间比例降至 30-45%，但仍显著高于 NVLink 方案的 <1 ms 延迟。

## Corrected Claim

4x RTX 4090 在 TP=4 下，若采用 Ring All-Reduce 算法，实际通信量为 2*(N-1)/N * 0.54 GB = 0.81 GB（N=4），而非 0.54 GB，因此修正后单次 All-Reduce 延迟为 0.81 GB / 50 GB/s = 16.2 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：Ring All-Reduce 通信量公式 2*(N-1)/N 正确，数值计算 0.54 * 1.5 = 0.81 GB 与陈述中 0.405 GB 存在矛盾？等等，重新计算：2*(4-1)/4 = 1.5。1.5 * 0.54 GB = 0.81 GB。陈述中写的是 0.405 GB。0.405 / 0.54 = 0.75。而 2*(N-1)/N 当 N=4 时是 1.5。这里数值计算错误。0.54 * 1.5 = 0.81。陈述说实际通信量为 0.405 GB，这是 0.54 * 0.75。0.75 是 (N-1)/N。Ring All-Reduce 的通信量通常是 2*(N-1)/N * S。如果是 0.54 GB 是 S，那么通信量应该是 1.5 * 0.54 = 0.81 GB。陈述中的 0.405 GB 是错误的。因此逻辑校验失败。
