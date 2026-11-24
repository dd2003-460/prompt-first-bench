# N524: N171 工作点下，自建节点存储容量成本增量 ΔC_storage_self = (C_self_storage_target - C_self_storage

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N171

## Claim

N171 工作点下，自建节点存储容量成本增量 ΔC_storage_self = (C_self_storage_target - C_self_storage_base) * C_storage_unit，其中 C_self_storage_target = 100TB，C_self_storage_base 需根据 N68 热数据量修正，C_storage_unit = ¥0.8/GB/月，计算得月增成本约 ¥80,000。

## Corrected Claim

N171 工作点下，自建节点存储容量成本增量 ΔC_storage_self = (C_self_storage_target - C_self_storage_base) * C_storage_unit。若 C_self_storage_target = 100TB 且 C_storage_unit = ¥0.8/GB/月，则月增成本约为 ¥80,000 的前提是 C_self_storage_base ≈ 0。若 C_self_storage_base 非零，则月增成本将低于 ¥80,000，具体数值取决于 N68 热数据量确定的 Base 值。

## Evidence

[质询]数值量级与公式逻辑存在严重矛盾：若 C_storage_unit 为 ¥0.8/GB/月，且月增成本为 ¥80,000，则存储增量 ΔC_storage 应为 100,000 GB (100TB)。这意味着 C_self_storage_base 必须为 0。然而陈述中明确指出 C_self_storage_base 需根据 N68 热数据量修正（隐含 base > 0），且 target 为 100TB。若 base > 0，则增量 < 100TB，成本应远低于 ¥80,000。反之，若成本确为 ¥80,000，则 base 必须为 0，与“需修正”的描述矛盾。 | 逻辑校验失败：根据公式 ΔC = (Target - Base) * Unit，若 Target=100TB, Unit=0.8/GB/月, Cost=80,000，则 Base 必须为 0。但陈述称 Base 需根据热数据量修正（通常非零），导致数值结果与前提条件内部矛盾。
