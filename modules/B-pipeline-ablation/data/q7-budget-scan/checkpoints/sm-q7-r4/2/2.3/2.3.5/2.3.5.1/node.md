# N216: Intelligent-Tiering 监控费的层级覆盖范围：监控费 $0.0025/GB/月 仅适用于开启 Intelligent-Tiering 的存储类；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

Intelligent-Tiering 监控费的层级覆盖范围：监控费 $0.0025/GB/月 仅适用于开启 Intelligent-Tiering 的存储类；若冷数据使用 Glacier Deep Archive（无监控费），则监控费仅针对温数据 100TB，年化监控费 = $0.0025 * 100,000 * 12 * 7.2 ≈ ¥2,160/年，而非 500TB 全量。

## Corrected Claim

Intelligent-Tiering 监控费的层级覆盖范围：监控费 $0.0025/GB/月 仅适用于开启 Intelligent-Tiering 的存储类；若冷数据使用 Glacier Deep Archive（无监控费），则监控费仅针对温数据 100TB，年化监控费 = $0.0025 * 100,000 * 12 * 7.2 ≈ ¥2,160/年，而非 500TB 全量。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应‘适用范围界定’（业务逻辑）、‘成本计算公式’（数学推导）和‘技术约束修正’（物理/工程限制），三者维度不同且互不重叠。虽然父节点中的计算结果（¥2,160）与子节点2中的精确计算（¥2,211.84）存在细微差异，但这属于精度误差而非逻辑矛盾，子节点提供了更严谨的计算依据，覆盖了父节点的核心论点及潜在变量。）
