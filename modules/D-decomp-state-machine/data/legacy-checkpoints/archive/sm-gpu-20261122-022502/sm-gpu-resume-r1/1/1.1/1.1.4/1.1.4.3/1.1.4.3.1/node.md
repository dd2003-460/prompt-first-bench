# N455: FP8 权重在 HuggingFace 加载后的实际字节数：27B 参数 × 1 byte/param = 27,000,000,000 bytes，加上 CU

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N142

## Claim

FP8 权重在 HuggingFace 加载后的实际字节数：27B 参数 × 1 byte/param = 27,000,000,000 bytes，加上 CUDA context 初始化开销 1.2GB [待核验]，总占用 28.2GB，超出 RTX 4090 24GB 显存上限，确认为不可行

## Corrected Claim

FP8 权重在 HuggingFace 加载后的实际字节数约为 27GB（27B 参数 × 1 byte/param），加上 CUDA context 及运行时开销，总显存占用必然超过 RTX 4090 的 24GB 显存上限，确认为不可行。

## Evidence

[质询]CUDA context 初始化开销 1.2GB 为经验事实，且不同驱动/框架版本下波动较大，缺乏特定环境下的精确来源支持；此外，HuggingFace 加载 FP8 模型时通常涉及反量化或特定 kernel 调用，实际显存占用可能因实现细节（如是否保留 FP16 副本、KV cache 预分配等）而显著高于纯权重字节数，仅计算权重+固定 context 可能低估实际占用，但核心结论（超出 24GB）在逻辑上大概率成立，主要风险在于具体数值 28.2GB 的精确性。 | 逻辑推导成立：27B 参数 FP8 权重确为 ~27GB，加上任何非零的 CUDA context 开销必然超过 RTX 4090 的 24GB 显存上限，结论‘不可行’在逻辑上自洽且稳健；但具体数值 1.2GB 和 28.2GB 属于经验事实，参考来源 [1] 和 [2] 仅确认模型存在及 FP8 支持，未提供具体显存占用数据，故降级为定性表述。

## Search Query

Qwen3-27B FP8 actual VRAM usage huggingface transformers load

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B-FP8&rut=4408fbcaa0ecf572370c0e5cd3db753c9aed75101561b2d04fe707b20b2db9c6', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B-FP8 · Hugging Face'}
- {'url': 'https://huggingface.co/docs/accelerate/en/package_reference/fp8&rut=4c578b740540eadb839bb6c8455657e48b0f160924c0b683a62317d0e37c4361', 'type': 'ddg', 'title': 'FP8 · Hugging Face'}
