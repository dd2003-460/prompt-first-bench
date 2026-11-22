# N184: 断点回归(RDD)中，以‘算法改版时间点’为断点，需验证断点处的左极限与右极限之差（跳跃）是否显著：ΔRDD = lim_{t→t0-} E[T|X=t] - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

断点回归(RDD)中，以‘算法改版时间点’为断点，需验证断点处的左极限与右极限之差（跳跃）是否显著：ΔRDD = lim_{t→t0-} E[T|X=t] - lim_{t→t0+} E[T|X=t]，若 |ΔRDD| / SE(ΔRDD) > 1.96 (95%置信水平)，则确认算法改版对成交周期有因果影响。

## Corrected Claim

断点回归(RDD)中，以‘算法改版时间点’为断点，需验证断点处的左极限与右极限之差（跳跃）是否显著：ΔRDD = lim_{t→t0-} E[T|X=t] - lim_{t→t0+} E[T|X=t]，若 |ΔRDD| / SE(ΔRDD) > 1.96 (95%置信水平)，则确认算法改版对成交周期有因果影响。

## Evidence

先验知识/题面给定，逻辑校验通过
