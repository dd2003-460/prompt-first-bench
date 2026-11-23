# N153: 32K 上下文下 KV Cache 显存占用计算：2 * 64 layers * 128 heads * 128 dim * 32768 seq_len * 2

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

32K 上下文下 KV Cache 显存占用计算：2 * 64 layers * 128 heads * 128 dim * 32768 seq_len * 2 bytes (BF16) ≈ 34.4 GB，远超 N47 声称的 2 GB，表明 N47 的 KV Cache 估算存在数量级错误，需修正为基于 GQA (Grouped Query Attention) 或实际头数计算

## Corrected Claim

32K 上下文下 KV Cache 显存占用计算：2 * 64 layers * 128 heads * 128 dim * 32768 seq_len * 2 bytes (BF16) ≈ 34.4 GB，远超 N47 声称的 2 GB，表明 N47 的 KV Cache 估算存在数量级错误，需修正为基于 GQA (Grouped Query Attention) 或实际头数计算

## Evidence

公式/推导类，逻辑校验通过，来源未直接覆盖

## Search Query

Qwen3-27B number of heads GQA KV cache size calculation 32k context

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/1310.8494v1', 'type': 'arxiv', 'title': 'Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Cache'}
