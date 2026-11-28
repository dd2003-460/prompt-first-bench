# N70: 工作点B的云API速率限制约束：GPT-4o/Claude 3.5 的 TPM (Tokens Per Minute) 限额 R_limit 决定了最大并发查询

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

工作点B的云API速率限制约束：GPT-4o/Claude 3.5 的 TPM (Tokens Per Minute) 限额 R_limit 决定了最大并发查询数 N_max = R_limit / Avg_tokens_per_query，若 N_max < 本地集群吞吐量 T_local，则云端成为瓶颈，需引入排队论模型（M/M/c）计算平均等待时间 W_queue，当 W_queue > 5s 时需降级为非关键路径任务或切换备用API提供商。

## Corrected Claim

工作点B的云API速率限制约束：GPT-4o/Claude 3.5 的 TPM (Tokens Per Minute) 限额 R_limit 决定了最大并发查询数 N_max = R_limit / Avg_tokens_per_query，若 N_max < 本地集群吞吐量 T_local，则云端成为瓶颈，需引入排队论模型（M/M/c）计算平均等待时间 W_queue，当 W_queue > 5s 时需降级为非关键路径任务或切换备用API提供商。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 N_max = R_limit / Avg_tokens 符合速率限制的基本定义；M/M/c 排队论模型适用于描述 API 请求在有限并发下的等待时间；5s 作为 SLA 阈值属于合理的工程经验值，整体逻辑自洽且量纲正确。

## Search Query

GPT-4o TPM rate limit tokens per minute pricing
