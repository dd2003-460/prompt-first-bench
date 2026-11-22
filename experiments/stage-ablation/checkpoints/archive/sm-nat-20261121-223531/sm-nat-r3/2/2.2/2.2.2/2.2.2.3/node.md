# N127: 边界对象的平均命中率修正因子 $\bar{H}_{boundary}$ 量化：对于处于缓存边界附近的对象，其命中率并非0或1，而是取决于其访问频率与替换频率的比

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

边界对象的平均命中率修正因子 $\bar{H}_{boundary}$ 量化：对于处于缓存边界附近的对象，其命中率并非0或1，而是取决于其访问频率与替换频率的比值。模型假设 $\bar{H}_{boundary} \approx 0.5$，该假设的误差范围可通过蒙特卡洛模拟验证，预期标准差为 ±0.1，导致最终命中率误差 $\Delta H_{err} = R_{boundary} \times (\bar{H}_{boundary} - 0.5)$。

## Corrected Claim

边界对象的平均命中率修正因子 $\bar{H}_{boundary}$ 量化：对于处于缓存边界附近的对象，其命中率并非0或1，而是取决于其访问频率与替换频率的比值。模型假设 $\bar{H}_{boundary} \approx 0.5$，该假设的误差范围可通过蒙特卡洛模拟验证，预期标准差为 ±0.1，导致最终命中率误差 $\Delta H_{err} = R_{boundary} \times (\bar{H}_{boundary} - 0.5)$。

## Evidence

先验知识/题面给定，逻辑校验通过
