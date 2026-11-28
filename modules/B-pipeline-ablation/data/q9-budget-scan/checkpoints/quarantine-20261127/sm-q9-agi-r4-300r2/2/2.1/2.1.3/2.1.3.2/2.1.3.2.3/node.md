# N304: 中间区域指令遵循率最低 (50%-60%) 的补偿策略量化成本：通过在 System Prompt 末尾追加“关键约束重申”模块，增加约 200 tokens 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

中间区域指令遵循率最低 (50%-60%) 的补偿策略量化成本：通过在 System Prompt 末尾追加“关键约束重申”模块，增加约 200 tokens 输入开销；预期可将中间区域的关键指令召回率从 55% 提升至 85% (提升 30pp)，代价是每次推理增加 ~0.5s 延迟 (200 tokens @ 45 tok/s)，ROI 为正，适用于高精度科研循环。

## Corrected Claim

在System Prompt末尾追加“关键约束重申”模块（约200 tokens）通常有助于提升中间区域指令遵循率，但具体提升幅度（如从55%至85%）及延迟开销（~0.5s）需根据特定模型和任务场景进行实测校准，不能视为通用固定值。

## Evidence

[质询]数值量级与因果归因缺乏实证支持：声称通过增加200 tokens能将指令遵循率从55%提升至85%（+30pp）是一个具体的经验性能指标，不同模型架构、上下文长度及任务复杂度下，Prompt Engineering的边际收益差异巨大，该线性提升假设过于乐观且缺乏通用性证明；此外，0.5s延迟的计算基于固定吞吐率，未考虑实际推理中的KV Cache影响及硬件波动。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但涉及具体性能提升数值，属经验参数，无法仅凭逻辑推导验证其普适性，故降级）

## Search Query

instruction repetition strategy lost in the middle mitigation cost benefit analysis
