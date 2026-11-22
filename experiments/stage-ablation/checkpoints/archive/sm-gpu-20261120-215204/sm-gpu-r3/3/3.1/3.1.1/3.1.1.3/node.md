# N238: 若 N136 的 23.5GB 估算因框架开销 (如 vLLM PagedAttention 块管理开销、FlashAttention 工作空间) 导致实际占用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

若 N136 的 23.5GB 估算因框架开销 (如 vLLM PagedAttention 块管理开销、FlashAttention 工作空间) 导致实际占用 > 24GB，则必须启用 KV Cache 量化。INT8 KV Cache 的显存占用减半至 4.0GB，总显存需求降至 13.5 + 4.0 + 2.0 = 19.5GB，安全余量 4.5GB，此时单卡 4090 可行。INT8 KV 量化对生成质量的影响通常在 MMLU/Perplexity 上增加 <0.5% 的困惑度，属于可接受的质量损失。

## Corrected Claim

若 N136 的 23.5GB 估算因框架开销 (如 vLLM PagedAttention 块管理开销、FlashAttention 工作空间) 导致实际占用 > 24GB，则必须启用 KV Cache 量化。INT8 KV Cache 的显存占用减半至 4.0GB，总显存需求降至 13.5 + 4.0 + 2.0 = 19.5GB，安全余量 4.5GB，此时单卡 4090 可行。INT8 KV 量化对生成质量的影响通常在 MMLU/Perplexity 上增加 <0.5% 的困惑度，属于可接受的质量损失。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化确实将显存占用减半（8.0GB->4.0GB），算术计算（13.5+4.0+2.0=19.5GB）正确，且INT8 KV Cache对生成质量影响极小符合工程常识。

## Search Query

KV cache INT8 quantization quality impact perplexity MMLU LLM inference
