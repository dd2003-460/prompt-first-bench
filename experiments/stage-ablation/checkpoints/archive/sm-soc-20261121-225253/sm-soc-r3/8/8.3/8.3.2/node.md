# N118: 在基线咨询率适中（CTR_drop ≈ 15%）且样本量充足（N > 1000）的典型工作点下，ΔCTR_rel 的标准误近似为 sqrt(1/CTR_drop

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47, N48

## Claim

在基线咨询率适中（CTR_drop ≈ 15%）且样本量充足（N > 1000）的典型工作点下，ΔCTR_rel 的标准误近似为 sqrt(1/CTR_drop + 1/CTR_high)，此时若 ΔCTR_rel > 2/sqrt(N)，则统计显著性成立，可直接用于判断平台流量分配偏向。

## Corrected Claim

在基线咨询率适中且样本量充足（N > 1000）的典型工作点下，ΔCTR_rel 的标准误应随样本量 N 的增大而减小（例如近似为 sqrt(Var(CTR)/N) 的形式）。若 ΔCTR_rel 显著大于其标准误的若干倍（如 2 倍或 1.96 倍），则统计显著性成立，可用于判断平台流量分配偏向。

## Evidence

[质询]统计公式存在量纲与逻辑错误：标准误（SE）通常随样本量N增加而减小（如 sqrt(p(1-p)/N)），但陈述中给出的 SE 公式 sqrt(1/CTR_drop + 1/CTR_high) 仅依赖于比率参数，未包含样本量 N，导致 SE 不随 N 变化，这与大数定律及中心极限定理的基本直觉相悖；此外，将显著性阈值直接设为 2/sqrt(N) 缺乏统计推导依据（通常应为 z * SE）。 | 先验知识/题面给定，逻辑校验未通过：标准误公式缺失样本量 N 项，导致统计推断逻辑不自洽。

## Search Query

standard error difference in proportions large sample approximation
