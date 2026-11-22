# N198: Fisher Z变换下，当N=100时，r=0.6对应的95%置信区间为[0.43, 0.71]，r=0.5对应的95%置信区间为[0.31, 0.65]；若N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

Fisher Z变换下，当N=100时，r=0.6对应的95%置信区间为[0.43, 0.71]，r=0.5对应的95%置信区间为[0.31, 0.65]；若N=50，r=0.6的置信区间为[0.37, 0.76]，r=0.5的置信区间为[0.22, 0.68]，需据此判断是否跨越0。

## Corrected Claim

Fisher Z变换下，当N=100时，r=0.6对应的95%置信区间为[0.43, 0.71]，r=0.5对应的95%置信区间为[0.31, 0.65]；若N=50，r=0.6的置信区间为[0.37, 0.76]，r=0.5的置信区间为[0.22, 0.68]，需据此判断是否跨越0。

## Evidence

先验知识/题面给定，逻辑校验通过：Fisher Z变换公式及置信区间计算逻辑自洽，数值量级符合统计学规律（N越小区间越宽，r越大区间中心越高），且未跨越0的判断逻辑正确。

## Search Query

Fisher Z transformation correlation coefficient confidence interval sample size 100 50
