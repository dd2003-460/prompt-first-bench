# N181: 在 FP8 KV Cache 设置下，基于 6.3 GB 单序列显存限制，理论最大安全序列长度 Max_Safe_Seq 为 102,400 Tokens (计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

在 FP8 KV Cache 设置下，基于 6.3 GB 单序列显存限制，理论最大安全序列长度 Max_Safe_Seq 为 102,400 Tokens (计算方式：6.3 * 1024^2 KB / 64 KB)，远低于配置的 max_model_len=262144，证实存在 OOM 风险。

## Corrected Claim

在 FP8 KV Cache 设置下，基于 6.3 GB 单序列显存限制，理论最大安全序列长度 Max_Safe_Seq 为 102,400 Tokens (计算方式：6.3 * 1024^2 KB / 64 KB)，远低于配置的 max_model_len=262144，证实存在 OOM 风险。

## Evidence

先验知识/题面给定，逻辑校验通过：6.3GB转换为KB后除以64KB每Token的开销，计算结果确为102,400，且小于262,144，逻辑自洽。
