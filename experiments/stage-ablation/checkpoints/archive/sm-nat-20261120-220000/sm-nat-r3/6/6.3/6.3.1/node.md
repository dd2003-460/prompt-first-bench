# N131: 在 C/S_total >> 1 条件下，缓存可容纳全部对象，LRU 稳态字节命中率下界趋近于 100%。具体数值取决于未缓存尾部对象的字节占比 $S_{tai

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

在 C/S_total >> 1 条件下，缓存可容纳全部对象，LRU 稳态字节命中率下界趋近于 100%。具体数值取决于未缓存尾部对象的字节占比 $S_{tail}/S_{total}$。若缓存容量足以覆盖前 90% 的字节量，则命中率下界为 $1 - (S_{tail}/S_{total})$。

## Corrected Claim

在 C/S_total >> 1 条件下，缓存可容纳全部对象，LRU 稳态字节命中率下界趋近于 100%。具体数值取决于未缓存尾部对象的字节占比 $S_{tail}/S_{total}$。若缓存容量足以覆盖前 90% 的字节量，则命中率下界为 $1 - (S_{tail}/S_{total})$。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU在稳态下若缓存容量覆盖高频对象，其命中率下界确实由未缓存对象的字节占比决定，推导符合缓存理论基本逻辑。
