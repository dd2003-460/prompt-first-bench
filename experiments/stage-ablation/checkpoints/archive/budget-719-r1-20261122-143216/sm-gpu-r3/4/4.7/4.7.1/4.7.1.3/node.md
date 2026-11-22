# N335: vLLM 框架在单卡推理时的固定显存开销 (VRAM_overhead) 包括 CUDA Context、Kernel 缓存及 PagedAttention 元

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

vLLM 框架在单卡推理时的固定显存开销 (VRAM_overhead) 包括 CUDA Context、Kernel 缓存及 PagedAttention 元数据，通常占用 1.5-2.0 GB 显存，不随 Batch Size 线性增长

## Corrected Claim

vLLM 框架在单卡推理时的固定显存开销 (VRAM_overhead) 包括 CUDA Context、Kernel 缓存及 PagedAttention 元数据，通常占用 1.5-2.0 GB 显存，不随 Batch Size 线性增长

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM fixed GPU memory overhead CUDA context PagedAttention metadata size GB
