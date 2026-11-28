# N18: 可接受质量阈值定义：对于通用推理任务，ΔScore < 2% 视为“无损”，2% ≤ ΔScore < 5% 视为“可接受”，ΔScore > 5% 视为“显著

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

可接受质量阈值定义：对于通用推理任务，ΔScore < 2% 视为“无损”，2% ≤ ΔScore < 5% 视为“可接受”，ΔScore > 5% 视为“显著退化”；对于数学/代码生成等敏感任务，阈值收紧至 ΔScore < 1% 和 < 3%

## Corrected Claim

可接受质量阈值定义：对于通用推理任务，ΔScore < 2% 视为“无损”，2% ≤ ΔScore < 5% 视为“可接受”，ΔScore > 5% 视为“显著退化”；对于数学/代码生成等敏感任务，阈值收紧至 ΔScore < 1% 和 < 3%

## Evidence

先验知识/题面给定，逻辑校验通过
