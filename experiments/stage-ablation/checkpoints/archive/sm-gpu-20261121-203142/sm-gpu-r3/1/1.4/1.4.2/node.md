# N47: 基于确认参数的 KV Cache 精确计算：每 token 每层占用 = 8 heads * 128 dim * 2 bytes * 2 (K+V) = 409

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

基于确认参数的 KV Cache 精确计算：每 token 每层占用 = 8 heads * 128 dim * 2 bytes * 2 (K+V) = 4096 bytes; 32K tokens 总 KV Cache = 4096 B/token/layer * 32768 tokens * 48 layers = 6,442,450,944 bytes ≈ 6.0 GB

## Corrected Claim

基于确认参数的 KV Cache 精确计算：每 token 每层占用 = 8 heads * 128 dim * 2 bytes * 2 (K+V) = 4096 bytes; 32K tokens 总 KV Cache = 4096 B/token/layer * 32768 tokens * 48 layers = 6,442,450,944 bytes ≈ 6.0 GB

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 7 column 5 (char 803)
