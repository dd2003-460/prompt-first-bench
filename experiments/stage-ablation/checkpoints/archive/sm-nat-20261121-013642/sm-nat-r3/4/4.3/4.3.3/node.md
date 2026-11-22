# N64: P_hit_cold 的中间工作点估算：假设 50% 更新为内容变更 (P=0)，50% 为元数据刷新 (P=1)，则 P_hit_cold ≈ 0.5。此时 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

P_hit_cold 的中间工作点估算：假设 50% 更新为内容变更 (P=0)，50% 为元数据刷新 (P=1)，则 P_hit_cold ≈ 0.5。此时 δ = 1 - 0.5 * C_steady，用于量化部分失效场景下的折损。

## Corrected Claim

P_hit_cold 的中间工作点估算：假设 50% 更新为内容变更 (P=0)，50% 为元数据刷新 (P=1)，则 P_hit_cold ≈ 0.5。此时 δ = 1 - 0.5 * C_steady，用于量化部分失效场景下的折损。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是对同一参数（更新类型比例）的不同取值进行枚举，属于参数扫描而非结构性的正交分解。虽然覆盖了父节点提到的中间工作点及两端极端情况，但逻辑上存在冗余，因为它们共享相同的公式和计算逻辑，仅输入变量不同。）
