# N11: 显存带宽对 Token 生成速率 (Tokens/s) 的物理限制公式为 Throughput ≈ Memory_Bandwidth_GBps / Bytes_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

显存带宽对 Token 生成速率 (Tokens/s) 的物理限制公式为 Throughput ≈ Memory_Bandwidth_GBps / Bytes_per_token_accessed，其中 Bytes_per_token_accessed 取决于权重大小和 KV Cache 读取量

## Corrected Claim

显存带宽对 Token 生成速率 (Tokens/s) 的物理限制公式为 Throughput ≈ Memory_Bandwidth_GBps / Bytes_per_token_accessed，其中 Bytes_per_token_accessed 取决于权重大小和 KV Cache 读取量

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 814)
