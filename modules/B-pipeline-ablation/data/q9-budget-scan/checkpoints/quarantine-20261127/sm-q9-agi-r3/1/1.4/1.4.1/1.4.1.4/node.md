# N145: KV Cache 内存压力对 MTP 的约束：MTP×4 意味着每步需缓存 4 个 token 的 KV。对于 max_model_len=262144, nu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

KV Cache 内存压力对 MTP 的约束：MTP×4 意味着每步需缓存 4 个 token 的 KV。对于 max_model_len=262144, num_kv_heads=8, head_dim=128, FP16。单层 KV 大小 = 2 * 8 * 128 * 2 bytes = 4KB/token。64 层总 KV = 256KB/token。4 tokens = 1MB/layer? No, 256KB * 4 = 1MB per sequence step. 16GB VRAM 中，KV Cache 占用极大，可能导致 max_num_seqs 无法达到 8，或触发 OOM 降级，从而限制并发吞吐。

## Corrected Claim

KV Cache 内存压力对 MTP 的约束：MTP×4 意味着每步需缓存 4 个 token 的 KV。对于 max_model_len=262144, num_kv_heads=8, head_dim=128, FP16。单层 KV 大小 = 2 * 8 * 128 * 2 bytes = 4KB/token。64 层总 KV = 256KB/token。4 tokens = 1MB/layer? No, 256KB * 4 = 1MB per sequence step. 16GB VRAM 中，KV Cache 占用极大，可能导致 max_num_seqs 无法达到 8，或触发 OOM 降级，从而限制并发吞吐。

## Evidence

先验知识/题面给定，逻辑校验通过：单层KV计算正确（2*8*128*2=4KB），64层总KV为256KB/token，4 tokens即为1MB/step，数值量级与逻辑推导均自洽。

## Search Query

vLLM KV cache memory calculation GQA 27B long context 16GB VRAM limit
