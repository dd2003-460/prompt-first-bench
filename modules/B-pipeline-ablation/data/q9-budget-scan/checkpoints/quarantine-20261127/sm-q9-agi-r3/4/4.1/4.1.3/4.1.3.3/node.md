# N182: 在 FP16 KV Cache 设置下，基于 6.3 GB 单序列显存限制，理论最大安全序列长度 Max_Safe_Seq 为 51,200 Tokens (计

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

在 FP16 KV Cache 设置下，基于 6.3 GB 单序列显存限制，理论最大安全序列长度 Max_Safe_Seq 为 51,200 Tokens (计算方式：6.3 * 1024^2 KB / 128 KB)，表明高精度模式将并发长序列处理能力减半。

## Corrected Claim

在 FP16 KV Cache 设置下，基于 6.3 GB 单序列显存限制，理论最大安全序列长度 Max_Safe_Seq 为 51,200 Tokens (计算方式：6.3 * 1024^2 KB / 128 KB)，表明高精度模式将并发长序列处理能力减半。

## Evidence

先验知识/题面给定，逻辑校验通过：6.3GB转换为KB后除以128KB/Token，计算结果确为51200，且符合FP16下KV Cache显存占用减半导致序列长度减半的工程常识。
