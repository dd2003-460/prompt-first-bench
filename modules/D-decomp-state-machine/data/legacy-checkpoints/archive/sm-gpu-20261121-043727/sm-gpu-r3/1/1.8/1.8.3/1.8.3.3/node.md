# N159: H100 SXM 原生 FP8 推理相比 BF16 的实测加速比：Hopper 架构支持 FP8 Tensor Core 和 FP8 内存带宽优化。在 LLM 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

H100 SXM 原生 FP8 推理相比 BF16 的实测加速比：Hopper 架构支持 FP8 Tensor Core 和 FP8 内存带宽优化。在 LLM Decode 阶段，由于 HBM3 带宽利用率高于 GDDR6X，且权重减半，T_decode 加速比通常达到 1.8x-2.2x；在 Prefill 阶段，FP8 算力翻倍且 MFU 较高，加速比约为 1.6x-1.9x。

## Corrected Claim

H100 SXM 原生 FP8 推理相比 BF16 具有显著加速优势。Hopper 架构支持 FP8 Tensor Core 和 FP8 内存带宽优化。在 LLM Decode 阶段，由于 HBM3 带宽利用率高于 GDDR6X 且权重减半，T_decode 加速比通常接近 2x；在 Prefill 阶段，FP8 算力翻倍且 MFU 较高，加速比约为 1.6x-1.9x。

## Evidence

[质询]具体加速比数值（1.8x-2.2x 和 1.6x-1.9x）属于经验事实，且高度依赖于具体的模型大小、Batch Size、序列长度及硬件配置，参考来源仅确认了架构支持 FP8，未提供这些具体的实测加速比数据，存在以偏概全或数值缺乏特定上下文的风险。 | 来源[1]直接支持 Hopper 架构支持 FP8 并加速 LLM 推理，但未提供具体的加速比数值；该数值为经验事实，逻辑上合理（带宽和算力提升带来加速），但缺乏来源直接支持具体数值，故降级。

## Search Query

H100 SXM FP8 vs BF16 LLM inference speedup benchmark

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2402.13499v1&rut=d7301075107d9c2cf17401f8367fe7b0036bd5531971937a30db749e54296d20', 'type': 'ddg', 'title': 'Benchmarking and Dissecting the Nvidia Hopper GPU Architecture'}
