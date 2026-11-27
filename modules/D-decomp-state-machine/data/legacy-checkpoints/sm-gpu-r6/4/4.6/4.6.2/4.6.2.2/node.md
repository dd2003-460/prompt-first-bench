# N232: vLLM 在单卡 RTX 4090 上运行 27B INT8 模型时，若启用 PagedAttention 且 KV Cache 使用 FP16，32K 上下文

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

vLLM 在单卡 RTX 4090 上运行 27B INT8 模型时，若启用 PagedAttention 且 KV Cache 使用 FP16，32K 上下文下的 KV Cache 显存占用约为 2 * 32768 * n_layers * n_heads * head_dim * 2 bytes，需结合 Qwen3-27B 具体层数(如64层)计算是否触发 OOM 或强制降低 Max Batch Size 至 1。

## Corrected Claim

vLLM 在单卡 RTX 4090 上运行 27B INT8 模型时，若启用 PagedAttention 且 KV Cache 使用 FP16，32K 上下文下的 KV Cache 显存占用需根据具体模型架构参数（层数、注意力头数、head_dim）计算；由于 RTX 4090 显存有限（24GB），高上下文长度下 KV Cache 占用可能显著，需结合具体参数评估是否触发 OOM 或限制 Batch Size。

## Evidence

[质询]参考来源仅涉及 RTX 4060 的功耗/规格，与 RTX 4090 显存容量及 Qwen3-27B 具体架构参数（层数、头数、head_dim）完全无关，无法提供外部证据支持该显存占用计算或 OOM 结论。 | 经验事实，逻辑自洽但缺来源支持（来源[1]不相关）

## Search Query

Qwen3-27B architecture n_layers n_heads head_dim vLLM KV cache size calculation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
