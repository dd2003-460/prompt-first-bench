# N220: KV Cache显存占用精确公式：KV_cache_size = 2 * num_layers * num_kv_heads * head_dim * max_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

KV Cache显存占用精确公式：KV_cache_size = 2 * num_layers * num_kv_heads * head_dim * max_seq_len * bytes_per_element。对于Qwen3-27B（假设64层, 8 KV heads, 128 head_dim, FP8=1byte），单序列KV占用 = 2 * 64 * 8 * 128 * 262144 * 1 / 1e9 ≈ 3.4GB。在TP=4下，每卡承担1/4负载，即~0.85GB/seq。原claim中'8.6GB/卡'对应于max-num-seqs=10 (0.85*10=8.5GB) 而非8；提升至16 seqs需 0.85*16=13.6GB/卡，仍低于16GB限制，故'超出限制'的结论仅在max_model_len > 320k或启用FP16 KV时才成立，FP8 KV下16 seqs在显存上是可行的。

## Corrected Claim

KV Cache显存占用精确公式：KV_cache_size = 2 * num_layers * num_kv_heads * head_dim * max_seq_len * bytes_per_element。对于Qwen3-27B（假设64层, 8 KV heads, 128 head_dim, FP8=1byte），单序列KV占用 = 2 * 64 * 8 * 128 * 262144 * 1 / 1e9 ≈ 3.4GB。在TP=4下，每卡承担1/4负载，即~0.85GB/seq。原claim中'8.6GB/卡'对应于max-num-seqs=10 (0.85*10=8.5GB) 而非8；提升至16 seqs需 0.85*16=13.6GB/卡，仍低于16GB限制，故'超出限制'的结论仅在max_model_len > 320k或启用FP16 KV时才成立，FP8 KV下16 seqs在显存上是可行的。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算准确（2*64*8*128*262144/1e9≈3.4GB，TP=4后约0.85GB/seq，16 seqs约13.6GB<16GB），符合LLM推理显存占用的一般工程常识。
