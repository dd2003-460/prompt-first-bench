# N52: 任务复杂度评分 K 的计算公式为 K = α * L_tokens + β * D_depth + γ * C_context，其中 L_tokens 为预估输

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

任务复杂度评分 K 的计算公式为 K = α * L_tokens + β * D_depth + γ * C_context，其中 L_tokens 为预估输出 token 数，D_depth 为逻辑推理链深度 (1-5 级)，C_context 为所需上下文长度占比；权重系数通过 A/B 测试回归确定，初始建议 α=1, β=10, γ=5；当 K > 1000 时切换云端，意味着长上下文 (C_context>0.5) 或深推理 (D_depth>4) 的任务优先卸载。

## Corrected Claim

任务复杂度评分 K 的计算公式为 K = α * L_tokens + β * D_depth + γ * C_context，其中 L_tokens 为预估输出 token 数，D_depth 为逻辑推理链深度 (1-5 级)，C_context 为所需上下文长度占比；权重系数通过 A/B 测试回归确定，初始建议 α=1, β=10, γ=5；当 K > 1000 时切换云端，意味着长上下文 (C_context>0.5) 或深推理 (D_depth>4) 的任务优先卸载。

## Evidence

先验知识/题面给定，逻辑校验通过
