# N108: 定义'独立来源'的去重规则：同一厂商的不同文档（如NVIDIA Datasheet与NVIDIA Blog）视为同源；不同厂商或第三方独立评测（如TechPow

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18, N19, N20

## Claim

定义'独立来源'的去重规则：同一厂商的不同文档（如NVIDIA Datasheet与NVIDIA Blog）视为同源；不同厂商或第三方独立评测（如TechPowerUp, ServeTheHome）视为独立源；HuggingFace模型卡与GitHub仓库代码若指向同一Commit，视为同源

## Corrected Claim

定义'独立来源'的去重规则：同一厂商的不同文档（如NVIDIA Datasheet与NVIDIA Blog）视为同源；不同厂商或第三方独立评测（如TechPowerUp, ServeTheHome）视为独立源；HuggingFace模型卡与GitHub仓库代码若指向同一Commit，视为同源

## Evidence

先验知识/题面给定，逻辑校验通过
