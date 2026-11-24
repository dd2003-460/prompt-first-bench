# N563: 继续使用旧SSD的机会成本修正：原估算¥150,000/年需分解为 (1) 能效损失成本 + (2) 性能瓶颈导致的运维/业务隐性成本；若仅计算能效差，成本 =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N241

## Claim

继续使用旧SSD的机会成本修正：原估算¥150,000/年需分解为 (1) 能效损失成本 + (2) 性能瓶颈导致的运维/业务隐性成本；若仅计算能效差，成本 = (P_old_W - P_new_W) * 500TB * 8760 * E_price，通常远低于¥150k，除非包含高性能I/O需求无法满足的业务损失

## Corrected Claim

继续使用旧SSD的机会成本修正：原估算¥150,000/年需分解为 (1) 能效损失成本 + (2) 性能瓶颈导致的运维/业务隐性成本；若仅计算能效差，成本 = (P_old_W - P_new_W) * 500TB * 8760 * E_price，通常远低于¥150k，除非包含高性能I/O需求无法满足的业务损失

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W * h * 元/W = 元），且明确指出纯能效成本通常远低于总机会成本，符合数据中心经济学常识。

## Search Query

opportunity cost of keeping old storage hardware energy vs performance tradeoff
