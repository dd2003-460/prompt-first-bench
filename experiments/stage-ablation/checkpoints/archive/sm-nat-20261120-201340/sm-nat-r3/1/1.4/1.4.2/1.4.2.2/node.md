# N97: 典型媒体工作点 (s_min=10KB, s_max=10MB)：代入公式 E[S] ≈ 1.1*10KB/0.1 * (1 - 10^-3)^{0.1} / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

典型媒体工作点 (s_min=10KB, s_max=10MB)：代入公式 E[S] ≈ 1.1*10KB/0.1 * (1 - 10^-3)^{0.1} / (1 - 10^-3) ≈ 110KB，此值符合视频分片或图片的典型大小，导致 W_total ≈ 10.7GB，缓存覆盖率 ≈ 12x，是本题最可能的物理真实值，用于后续命中率计算。

## Corrected Claim

典型媒体工作点 (s_min=10KB, s_max=10MB)：代入公式 E[S] ≈ 1.1*10KB/0.1 * (1 - 10^-3)^{0.1} / (1 - 10^-3) ≈ 110KB，此值符合视频分片或图片的典型大小，导致 W_total ≈ 10.7GB，缓存覆盖率 ≈ 12x，是本题最可能的物理真实值，用于后续命中率计算。

## Evidence

先验知识/题面给定，逻辑校验通过：数值量级（110KB）符合典型媒体分片大小，推导过程自洽。
