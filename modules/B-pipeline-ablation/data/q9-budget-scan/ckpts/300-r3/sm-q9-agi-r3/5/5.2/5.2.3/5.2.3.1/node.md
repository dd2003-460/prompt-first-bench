# N271: JSON 状态块中冗余的元数据字段（如 step_id, timestamp, status）平均占用 30-40 tokens，可通过移除非核心字段减少 20

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

JSON 状态块中冗余的元数据字段（如 step_id, timestamp, status）平均占用 30-40 tokens，可通过移除非核心字段减少 20% 的额外 Token 消耗

## Corrected Claim

JSON 状态块中冗余的元数据字段（如 step_id, timestamp, status）通常占用一定数量的 Token，移除非核心字段可有效降低 Token 消耗，具体节省比例视字段复杂度和上下文规模而定。

## Evidence

[质询]数值量级缺乏普适性：step_id, timestamp, status 等字段的 Token 占用高度依赖于具体实现（如 ID 长度、时间戳格式、状态枚举值复杂度），30-40 tokens 是一个非常具体的经验估计值，并非固定常数；此外，‘减少 20% 额外 Token 消耗’这一比例也取决于整体 Prompt 的大小和结构，无法从第一性原理严格推导，属于特定场景下的经验数据。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值为经验估计，非绝对真理，且无外部来源佐证其普适性，故降级为定性表述）
