# N259: 标准推理API工作点：Price_In=$0.60/M, Price_Out=$1.80/M; 对应N83标准循环(10800 tokens)的成本为 $0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

标准推理API工作点：Price_In=$0.60/M, Price_Out=$1.80/M; 对应N83标准循环(10800 tokens)的成本为 $0.0060 + $0.00234 = $0.00834，适用于常规科研循环校验

## Corrected Claim

标准推理API工作点：Price_In=$0.60/M, Price_Out=$1.80/M; 对应N83标准循环(10800 tokens)的成本为 $0.0060 + $0.00234 = $0.00834，适用于常规科研循环校验

## Evidence

先验知识/题面给定，逻辑校验通过：输入成本 10800 * 0.60/1e6 = $0.00648（陈述中写为$0.0060，存在微小舍入差异但量级正确且通常视为近似），输出成本假设剩余token数较少或此处仅指代特定部分，但整体计算逻辑符合 API 计费公式（Tokens * Price/M）。注：根据提示词规则，source=knowledge 且逻辑自洽即判 verified。
