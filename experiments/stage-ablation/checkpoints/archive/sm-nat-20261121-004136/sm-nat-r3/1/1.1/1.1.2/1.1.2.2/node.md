# N85: 代入 S_min=1KB, S_max=100MB, α=1.1，计算得 E[S^2]_trunc ≈ 1.0 * 10^10 KB^2 (量级估算，精确值需数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

代入 S_min=1KB, S_max=100MB, α=1.1，计算得 E[S^2]_trunc ≈ 1.0 * 10^10 KB^2 (量级估算，精确值需数值积分)，进而 Var[S]_trunc = E[S^2]_trunc - (E[S]_trunc)^2 ≈ 1.0 * 10^10 KB^2，表明大小分布具有极重的尾部，方差远大于均值的平方。

## Corrected Claim

代入 S_min=1KB, S_max=100MB, α=1.1，计算得 E[S^2]_trunc ≈ 1.0 * 10^10 KB^2 (量级估算，精确值需数值积分)，进而 Var[S]_trunc = E[S^2]_trunc - (E[S]_trunc)^2 ≈ 1.0 * 10^10 KB^2，表明大小分布具有极重的尾部，方差远大于均值的平方。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布（α=1.1）在截断区间 [1KB, 100MB] 上的积分估算，E[S^2] 量级约为 10^10 KB^2 符合数学推导（S_max^2 ≈ 10^10 KB^2，且 α 接近 1 时二阶矩由上限主导），方差远大于均值平方符合重尾分布特征。
