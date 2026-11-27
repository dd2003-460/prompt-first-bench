# N115: CTR_high 计算的样本量下限：为保证统计精度，每个价格区间（如15-20%, 20-25%）的样本量 $N_{high}$ 需满足 $N_{high} \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

CTR_high 计算的样本量下限：为保证统计精度，每个价格区间（如15-20%, 20-25%）的样本量 $N_{high}$ 需满足 $N_{high} \ge \frac{Z^2 \times 0.25}{\epsilon^2}$，其中 $\epsilon$ 为允许误差（如5%），$Z=1.96$，即 $N_{high} \ge 384$，否则需合并区间或延长观测期。

## Corrected Claim

CTR_high 计算的样本量下限：为保证统计精度，每个价格区间（如15-20%, 20-25%）的样本量 $N_{high}$ 需满足 $N_{high} \ge \frac{Z^2 \times 0.25}{\epsilon^2}$，其中 $\epsilon$ 为允许误差（如5%），$Z=1.96$，即 $N_{high} \ge 384$，否则需合并区间或延长观测期。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 N >= Z^2 * p(1-p) / e^2 在 p=0.5 (最大方差 0.25), Z=1.96, e=0.05 时计算结果为 384.16，向上取整为 385 或保守取 384 均符合统计学常识，量级与逻辑自洽。
