# N38: 条件性推荐框架：最终推荐必须包含前置假设列表（如：电价0.15美元/kWh、上下文长度32K tokens、batch size=1、GPU利用率50%、硬件价

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

条件性推荐框架：最终推荐必须包含前置假设列表（如：电价0.15美元/kWh、上下文长度32K tokens、batch size=1、GPU利用率50%、硬件价格稳定3年），并明确边界条件（如：如果电价>0.20美元/kWh，推荐方案从2x RTX 4090变为1x A100 40GB）

## Corrected Claim

条件性推荐框架：最终推荐必须包含前置假设列表（如：电价0.15美元/kWh、上下文长度32K tokens、batch size=1、GPU利用率50%、硬件价格稳定3年），并明确边界条件（如：如果电价>0.20美元/kWh，推荐方案从2x RTX 4090变为1x A100 40GB）

## Evidence

先验知识/题面给定，逻辑校验通过
