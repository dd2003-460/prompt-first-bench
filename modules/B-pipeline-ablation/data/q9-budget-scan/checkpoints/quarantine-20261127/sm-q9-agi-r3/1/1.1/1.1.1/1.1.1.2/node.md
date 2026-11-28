# N123: 工作点B（最优性价比）：max_num_seqs=4, chunked_prefill=True (chunk_size=2048)时，单卡激活内存稳态值约为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

工作点B（最优性价比）：max_num_seqs=4, chunked_prefill=True (chunk_size=2048)时，单卡激活内存稳态值约为 0.8GB，相比工作点A节省0.6GB显存用于KV，提升并发容量约6%

## Corrected Claim

工作点B（最优性价比）：max_num_seqs=4, chunked_prefill=True (chunk_size=2048)时，单卡激活内存稳态值约为 0.8GB，相比工作点A节省0.6GB显存用于KV，提升并发容量约6%

## Evidence

先验知识/题面给定，逻辑校验通过
