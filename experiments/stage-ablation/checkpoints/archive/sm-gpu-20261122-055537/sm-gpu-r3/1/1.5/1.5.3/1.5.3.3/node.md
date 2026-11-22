# N179: INT4 量化对 KV Cache 的影响：KV Cache 通常保持 BF16 或 FP16 精度（除非使用 PagedAttention 的 KV 量化特性

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

INT4 量化对 KV Cache 的影响：KV Cache 通常保持 BF16 或 FP16 精度（除非使用 PagedAttention 的 KV 量化特性），因此 KV Cache 大小与权重精度无关，仅取决于 Seq_Length, Batch_Size, Num_Layers, Num_KV_Heads, Head_Dim。此点澄清了 N52 中可能存在的混淆，即量化权重不直接减小 KV Cache 占用。

## Corrected Claim

INT4 量化对 KV Cache 的影响：KV Cache 通常保持 BF16 或 FP16 精度（除非使用 PagedAttention 的 KV 量化特性），因此 KV Cache 大小与权重精度无关，仅取决于 Seq_Length, Batch_Size, Num_Layers, Num_KV_Heads, Head_Dim。此点澄清了 N52 中可能存在的混淆，即量化权重不直接减小 KV Cache 占用。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM kv cache quantization int4 weight independent kv cache size
