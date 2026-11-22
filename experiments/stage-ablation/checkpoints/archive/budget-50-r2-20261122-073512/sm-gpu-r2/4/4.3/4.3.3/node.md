# N155: 数据中心方案（如 H100）的 PUE（电能利用效率）在自建本地工作站（非大型云数据中心）环境下通常无法达到 1.2，实际 PUE 约为 1.5-2.0（因缺乏

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

数据中心方案（如 H100）的 PUE（电能利用效率）在自建本地工作站（非大型云数据中心）环境下通常无法达到 1.2，实际 PUE 约为 1.5-2.0（因缺乏集中冷热通道和高效制冷），因此 H100 方案的 OPEX 电力成本系数应修正为 1.5-2.0 而非 1.2-1.4。

## Corrected Claim

数据中心方案（如 H100）的 PUE（电能利用效率）在自建本地工作站（非大型云数据中心）环境下通常无法达到 1.2，实际 PUE 约为 1.5-2.0（因缺乏集中冷热通道和高效制冷），因此 H100 方案的 OPEX 电力成本系数应修正为 1.5-2.0 而非 1.2-1.4。

## Evidence

先验知识/题面给定，逻辑校验通过：小型本地工作站缺乏数据中心级的集中制冷与气流管理，PUE 1.5-2.0 符合工程常识，且高于大型数据中心的 1.2-1.4 符合物理直觉。

## Search Query

PUE local server rack vs data center typical value small office
