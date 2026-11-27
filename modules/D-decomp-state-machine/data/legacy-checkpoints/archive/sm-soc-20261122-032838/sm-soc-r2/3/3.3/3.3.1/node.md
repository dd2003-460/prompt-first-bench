# N70: 算法降权导致卖家成交周期延长 $\Delta T_{sale}$ 的量化关系。设原曝光权重为 $W_0$，降权后为 $W_1 = W_0 (1 - \delta

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

算法降权导致卖家成交周期延长 $\Delta T_{sale}$ 的量化关系。设原曝光权重为 $W_0$，降权后为 $W_1 = W_0 (1 - \delta)$，其中 $\delta$ 为降权幅度。若曝光量与咨询量成正比，咨询量与成交概率成正比，则 $T_{sale} \propto 1/W$。故 $\Delta T_{sale} = T_{sale}^{old} (\frac{W_0}{W_1} - 1) = T_{sale}^{old} (\frac{1}{1-\delta} - 1) \approx T_{sale}^{old} \delta$（当 $\delta$ 较小时）。若 $\delta = 20\%$，则 $T_{sale}$ 延长约 25%（精确值 $1/0.8 - 1 = 0.25$）。

## Corrected Claim

算法降权导致卖家成交周期延长 $\Delta T_{sale}$ 的量化关系。设原曝光权重为 $W_0$，降权后为 $W_1 = W_0 (1 - \delta)$，其中 $\delta$ 为降权幅度。若曝光量与咨询量成正比，咨询量与成交概率成正比，则 $T_{sale} \propto 1/W$。故 $\Delta T_{sale} = T_{sale}^{old} (\frac{W_0}{W_1} - 1) = T_{sale}^{old} (\frac{1}{1-\delta} - 1) \approx T_{sale}^{old} \delta$（当 $\delta$ 较小时）。若 $\delta = 20\%$，则 $T_{sale}$ 延长约 25%（精确值 $1/0.8 - 1 = 0.25$）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于题设的线性比例关系（曝光∝权重，成交∝曝光），推导出的反比关系 T ∝ 1/W 及数值计算（1/0.8 - 1 = 0.25）在数学上严格自洽。

## Search Query

impact of algorithmic downweighting on sales cycle time exposure rate proportionality
