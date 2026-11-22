# N314: 采样次数N与标准差收敛率的关系：蒙特卡洛标准差的收敛速度为O(1/sqrt(N))；若N从1000增加到5000（5倍），标准差应减少至1/sqrt(5) ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

采样次数N与标准差收敛率的关系：蒙特卡洛标准差的收敛速度为O(1/sqrt(N))；若N从1000增加到5000（5倍），标准差应减少至1/sqrt(5) ≈ 0.447倍；若实测标准差减少比例偏离此理论值超过10%，则表明存在系统性偏差或变量间相关性未考虑

## Corrected Claim

采样次数N与标准差收敛率的关系：蒙特卡洛标准差的收敛速度为O(1/sqrt(N))；若N从1000增加到5000（5倍），标准差应减少至1/sqrt(5) ≈ 0.447倍；若实测标准差减少比例偏离此理论值超过10%，则表明存在系统性偏差或变量间相关性未考虑

## Evidence

先验知识/题面给定，逻辑校验通过：蒙特卡洛标准误收敛率为O(1/sqrt(N))是统计学基本定理，数值计算1/sqrt(5)≈0.447正确，逻辑自洽。

## Search Query

Monte Carlo convergence rate O(1/sqrt(N)) deviation check
