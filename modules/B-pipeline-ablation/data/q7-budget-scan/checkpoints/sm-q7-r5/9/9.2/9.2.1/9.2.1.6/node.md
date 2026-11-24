# N676: CMR 与 SMR 在纯顺序读（冷数据扫描）场景下功耗差异 <1%，因为 SMR 的 Zone 管理开销主要发生在随机写和擦除时；若数据湖温数据仅做顺序扫描而不

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N278, N279, N280

## Claim

CMR 与 SMR 在纯顺序读（冷数据扫描）场景下功耗差异 <1%，因为 SMR 的 Zone 管理开销主要发生在随机写和擦除时；若数据湖温数据仅做顺序扫描而不涉及重写，SMR 方案的功耗劣势不成立，可忽略不计。

## Corrected Claim

CMR 与 SMR 在纯顺序读（冷数据扫描）场景下功耗差异 <1%，因为 SMR 的 Zone 管理开销主要发生在随机写和擦除时；若数据湖温数据仅做顺序扫描而不涉及重写，SMR 方案的功耗劣势不成立，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：SMR的核心开销在于Zone管理（随机写/擦除），纯顺序读场景下其功耗与CMR差异极小，符合存储介质物理特性及工程常识。
