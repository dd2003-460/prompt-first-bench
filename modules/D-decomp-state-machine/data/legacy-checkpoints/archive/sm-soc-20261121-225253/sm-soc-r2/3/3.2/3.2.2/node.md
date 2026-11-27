# N33: 成交周期延长的量化模型：假设买家到达率服从泊松分布 $\lambda$，原周期 $T_0 = 1/\lambda$，新周期 $T_{new} = 1/(\lam

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

成交周期延长的量化模型：假设买家到达率服从泊松分布 $\lambda$，原周期 $T_0 = 1/\lambda$，新周期 $T_{new} = 1/(\lambda \times E_{ratio})$，则 $\Delta T_{seller} = T_0 \times (\frac{1}{E_{ratio}} - 1)$；若曝光降至60%（$E_{ratio}=0.6$），周期将延长约 67%。

## Corrected Claim

成交周期延长的量化模型：假设买家到达率服从泊松分布 $\lambda$，原周期 $T_0 = 1/\lambda$，新周期 $T_{new} = 1/(\lambda \times E_{ratio})$，则 $\Delta T_{seller} = T_0 \times (\frac{1}{E_{ratio}} - 1)$；若曝光降至60%（$E_{ratio}=0.6$），周期将延长约 67%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确，1/(0.6) - 1 ≈ 0.667，即67%。

## Search Query

poisson process sales time exposure reduction delay calculation
