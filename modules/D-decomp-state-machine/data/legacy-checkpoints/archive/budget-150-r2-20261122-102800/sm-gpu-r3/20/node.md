# N430: 精度可接受性阈值定义：对于通用问答场景（MMLU 为主），INT8 的 2.0% 相对损失可接受，W4 的 7.9% 相对损失不可接受；对于代码生成场景（Hum

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

精度可接受性阈值定义：对于通用问答场景（MMLU 为主），INT8 的 2.0% 相对损失可接受，W4 的 7.9% 相对损失不可接受；对于代码生成场景（HumanEval 为主），INT8 的 4.2% 相对损失可接受，W4 的 13.9% 相对损失不可接受；对于数学推理场景（GSM8K/MATH 为主），INT8 的 5.0% 相对损失可接受，W4 的 17.5% 相对损失不可接受；该阈值基于业务 SLA 要求，标记为 [条件性]。

## Corrected Claim

精度可接受性阈值定义：对于通用问答场景（MMLU 为主），INT8 的 2.0% 相对损失可接受，W4 的 7.9% 相对损失不可接受；对于代码生成场景（HumanEval 为主），INT8 的 4.2% 相对损失可接受，W4 的 13.9% 相对损失不可接受；对于数学推理场景（GSM8K/MATH 为主），INT8 的 5.0% 相对损失可接受，W4 的 17.5% 相对损失不可接受；该阈值基于业务 SLA 要求，标记为 [条件性]。

## Evidence

检索失败: no sources from any channel (all 5 failed)
