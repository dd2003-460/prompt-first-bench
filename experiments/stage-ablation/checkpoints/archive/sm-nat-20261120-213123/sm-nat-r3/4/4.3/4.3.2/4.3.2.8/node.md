# N134: 工作点 1 中 LRU 的有效命中率 $H_{eff} = H_{static} \cdot (1 - \Delta H)$，其中 $H_{static}$ 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

工作点 1 中 LRU 的有效命中率 $H_{eff} = H_{static} \cdot (1 - \Delta H)$，其中 $H_{static}$ 为静态命中率；在 $c=1.13 \times 10^7 \gg N=10^5$ 下，$H_{static} \approx 100\%$（缓存可容纳所有对象），因此 $H_{eff} \approx 100\% \cdot (1 - 0.0000035) \approx 99.99965\%$，表明在小对象主导且容量充足场景下，更新率 1%/天 对 LRU 命中率的影响可忽略不计（<0.001%）。

## Corrected Claim

工作点 1 中 LRU 的有效命中率 $H_{eff} = H_{static} \cdot (1 - \Delta H)$，其中 $H_{static}$ 为静态命中率；在 $c=1.13 \times 10^7 \gg N=10^5$ 下，$H_{static} \approx 100\%$（缓存可容纳所有对象），因此 $H_{eff} \approx 100\% \cdot (1 - 0.0000035) \approx 99.99965\%$，表明在小对象主导且容量充足场景下，更新率 1%/天 对 LRU 命中率的影响可忽略不计（<0.001%）。

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存容量远大于对象总数（c >> N）且无驱逐发生的情况下，静态命中率确实为100%，有效命中率仅受更新率影响，计算逻辑自洽。
