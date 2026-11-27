# N510: RX 7900 XTX 24GB 在 INT4 量化 + INT8 KV Cache（128KB/token）下，剩余 8.5GB 显存可支持最大上下文长度 =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N177

## Claim

RX 7900 XTX 24GB 在 INT4 量化 + INT8 KV Cache（128KB/token）下，剩余 8.5GB 显存可支持最大上下文长度 = 8.5GB / 128KB = 68,000 tokens，或支持 2 个 32K 并发请求（总 KV Cache 8GB），剩余 0.5GB 缓冲。

## Corrected Claim

RX 7900 XTX 24GB 在 INT4 量化 + INT8 KV Cache（128KB/token）下，剩余 8.5GB 显存可支持最大上下文长度 = 8.5GB / 128KB = 68,000 tokens，或支持 2 个 32K 并发请求（总 KV Cache 8GB），剩余 0.5GB 缓冲。

## Evidence

先验知识/题面给定，逻辑校验通过：8.5GB / 128KB = 68,000 tokens 计算正确，2 * 32K * 128KB = 8GB 计算正确，剩余 0.5GB 缓冲逻辑自洽。
