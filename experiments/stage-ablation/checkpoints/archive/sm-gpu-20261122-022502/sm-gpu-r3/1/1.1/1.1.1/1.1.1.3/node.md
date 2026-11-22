# N106: Qwen3-27B 的 Head Dim (head_dim) 为 128，需通过模型 config.json 确认，结合层数和 KV 头数确定单 Token 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Qwen3-27B 的 Head Dim (head_dim) 为 128，需通过模型 config.json 确认，结合层数和 KV 头数确定单 Token KV 大小

## Corrected Claim

Qwen3-27B 的 Head Dim (head_dim) 为 128，需通过模型 config.json 确认，结合层数和 KV 头数确定单 Token KV 大小

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json head_dim
