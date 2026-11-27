# N129: LFU 在动态更新场景下的总命中率折损 $\Delta H_{LFU} = \Delta H_{invalidate} + \Delta H_{relearn}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

LFU 在动态更新场景下的总命中率折损 $\Delta H_{LFU} = \Delta H_{invalidate} + \Delta H_{relearn}$，其中 $\Delta H_{invalidate} = P_{lfu\_invalidate} \cdot (S_{hot}/S_{total})$，$\Delta H_{relearn} = \sum_{i} (1 - e^{-\lambda_i T_{reset}}) \cdot (S_i \lambda_i / R_{byte})$；在 $u=1\%/day$ 且 $T_{reset}=1day$ 下，$\Delta H_{LFU} \approx 0.3\% + 0.01\% \approx 0.31\%$，与 LRU 的折损（N59 中 $\Delta H \approx 0.3\%$）相当，表明在低更新率下 LFU 与 LRU 的动态惩罚无显著差异。

## Corrected Claim

LFU 在动态更新场景下的总命中率折损 $\Delta H_{LFU} = \Delta H_{invalidate} + \Delta H_{relearn}$，其中 $\Delta H_{invalidate} = P_{lfu\_invalidate} \cdot (S_{hot}/S_{total})$，$\Delta H_{relearn} = \sum_{i} (1 - e^{-\lambda_i T_{reset}}) \cdot (S_i \lambda_i / R_{byte})$；在 $u=1\%/day$ 且 $T_{reset}=1day$ 下，$\Delta H_{LFU} \approx 0.3\% + 0.01\% \approx 0.31\%$，与 LRU 的折损（N59 中 $\Delta H \approx 0.3\%$）相当，表明在低更新率下 LFU 与 LRU 的动态惩罚无显著差异。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合缓存失效与重学习的基本原理，数值量级（0.31% vs 0.3%）在低更新率假设下合理且自洽。
