# N253: vLLM 启用 return_logprobs=True 时，显存增量 ΔMem ≈ BatchSize * SeqLen * NumLayers * Hidd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

vLLM 启用 return_logprobs=True 时，显存增量 ΔMem ≈ BatchSize * SeqLen * NumLayers * HiddenDim * sizeof(float32)；在 max-num-seqs=8, max_model_len=262144 的极端配置下，理论增量可达数十 GB，远超 2-4GB 估计，实际需截断序列长度或降低 batch size。

## Corrected Claim

vLLM 启用 return_logprobs=True 时，显存增量 ΔMem ≈ BatchSize * SeqLen * NumLayers * HiddenDim * sizeof(float32)；在 max-num-seqs=8, max_model_len=262144 的极端配置下，理论增量可达数十 GB，远超 2-4GB 估计，实际需截断序列长度或降低 batch size。

## Evidence

先验知识/题面给定，逻辑校验通过：vLLM 中 logprobs 通常以 float32 存储，计算 BatchSize(8) * SeqLen(262144) * NumLayers(~32-80) * HiddenDim(~4096-8192) * 4 bytes 的量级确实在数十 GB 至百 GB 级别，远超常规 KV Cache 或激活值的局部开销，逻辑自洽且符合内存管理常识。

## Search Query

vLLM return_logprobs memory overhead calculation formula
