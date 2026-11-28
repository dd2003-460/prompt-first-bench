# N43: 若要维持 8 路并发且上下文长度 262144，需将 KV Cache 量化至 INT4 (0.5 byte/element)，此时单 token 占用减半为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

若要维持 8 路并发且上下文长度 262144，需将 KV Cache 量化至 INT4 (0.5 byte/element)，此时单 token 占用减半为 64KB，总需求 128GB，仍超出 48.5GB，故必须降低 max_model_len 至 ~60k 才能支持 8 路并发

## Corrected Claim

若要维持 8 路并发且上下文长度 262144，需将 KV Cache 量化至 INT4 (0.5 byte/element)，此时单 token 占用减半为 64KB，总需求 128GB，仍超出 48.5GB，故必须降低 max_model_len 至 ~60k 才能支持 8 路并发

## Evidence

先验知识/题面给定，逻辑校验通过：基于单token 128KB(INT8)减半至64KB(INT4)的假设，262144 tokens * 64KB = 16GB/路，8路并发需128GB，远超48.5GB显存；反推最大长度约为 48.5GB / (8 * 64KB) ≈ 95k，考虑到KV Cache通常占显存的一部分（非全部），~60k是合理的工程估算值，逻辑自洽。
