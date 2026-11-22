# N52: LRU稳态字节命中率下界的正确公式应为 H_LRU ≥ 1 - (1 - q*) * (S_uncovered / S_total)，其中q*为被缓存对象的热度

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LRU稳态字节命中率下界的正确公式应为 H_LRU ≥ 1 - (1 - q*) * (S_uncovered / S_total)，其中q*为被缓存对象的热度占比，S_uncovered为未缓存对象的字节占比。

## Corrected Claim

LRU稳态字节命中率下界的正确公式应为 H_LRU ≥ 1 - (1 - q*) * (S_uncovered / S_total)，其中q*为被缓存对象的热度占比，S_uncovered为未缓存对象的字节占比。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点1内部存在逻辑矛盾（先引用父节点公式，后声称该公式不适用并给出另一公式），且子节点1与子节点2在'缓存覆盖全部对象时命中率为1'这一结论上存在语义重叠。此外，子节点1中给出的'正确公式'实际上是命中率定义式而非下界推导，未能有效支撑父节点关于'下界'的核心论点。）
