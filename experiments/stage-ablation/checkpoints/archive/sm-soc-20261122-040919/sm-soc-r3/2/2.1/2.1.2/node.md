# N50: 平台收入均值投影：E[r×T] = E[r]×E[T] + Cov(r, T)，其中 E[r]=0.075（5%-10%的中点），E[T] 为平均成交周期；若 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

平台收入均值投影：E[r×T] = E[r]×E[T] + Cov(r, T)，其中 E[r]=0.075（5%-10%的中点），E[T] 为平均成交周期；若 E[T]=7天，Cov(r, T)=0，则 E[r×T]=0.525（单位：佣金率×天数）；平台有动机最大化 E[T] 以提高 E[r×T]

## Corrected Claim

平台收入均值投影：E[r×T] = E[r]×E[T] + Cov(r, T)，其中 E[r]=0.075（5%-10%的中点），E[T] 为平均成交周期；若 E[T]=7天，Cov(r, T)=0，则 E[r×T]=0.525（单位：佣金率×天数）；平台有动机最大化 E[T] 以提高 E[r×T]

## Evidence

先验知识/题面给定，逻辑校验通过：数学恒等式 E[XY]=E[X]E[Y]+Cov(X,Y) 成立，数值计算 0.075*7=0.525 正确，且基于该公式推导出的平台动机逻辑自洽。
