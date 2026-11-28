# N140: 在 vLLM 中，当后端硬件不支持原生 FP8 时，'FP8 KV Cache' 选项实际上是在 CPU 侧或 GPU 显存中以 FP16/BF16 存储 KV

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34, N35, N38

## Claim

在 vLLM 中，当后端硬件不支持原生 FP8 时，'FP8 KV Cache' 选项实际上是在 CPU 侧或 GPU 显存中以 FP16/BF16 存储 KV，但在读取/写入时进行动态量化/反量化模拟，或者在某些实现中直接回退到 FP16 存储，此时 dtype_bytes 仍为 2 bytes，而非 1 byte。

## Corrected Claim

在 vLLM 中，若后端硬件不支持原生 FP8 加速，启用 'FP8 KV Cache' 选项可能导致性能下降或功能受限。通常，若无法利用硬件 FP8 单元，系统可能回退至 FP16/BF16 存储（此时占用 2 bytes），或者在极少数软件模拟情况下以 FP8 存储（1 byte）但计算开销极大。具体行为取决于 vLLM 版本及驱动支持情况，不能一概而论为“动态量化模拟且仍占 2 bytes”。

## Evidence

[质询]该陈述将“硬件不支持原生FP8”时的行为描述为“动态量化/反量化模拟”或“直接回退”，并断言此时dtype_bytes仍为2。然而，vLLM的`kv_cache_dtype`参数通常控制的是存储格式。如果用户强制指定`fp8`但硬件不支持，vLLM可能会报错、忽略该设置（从而使用默认的fp16/bf16，此时确实是2字节），或者在某些特定软件模拟路径下以fp8存储（1字节）但计算慢。陈述中关于“动态量化/反量化模拟”导致“dtype_bytes仍为2”的逻辑存在混淆：如果是模拟FP8精度，存储通常是FP8（1字节）；如果是回退到FP16，则根本不是在“模拟FP8”，而是完全放弃了FP8模式。此外，来源主要讨论Hopper/Blackwell（支持FP8）的情况，未明确覆盖“不支持硬件”下的具体fallback机制细节，特别是是否真的存在一种“存储为FP16但称为FP8 KV Cache”的中间状态。 | 来源[1]和[2]主要描述在支持FP8的硬件（Hopper/Blackwell）上的行为及配置，未直接提供“硬件不支持FP8时”的具体回退机制或存储字节数变化的详细文档支持；逻辑上，若回退到FP16，则不应再称为FP8 KV Cache的模拟，而是FP16 KV Cache，因此原陈述的机制描述可能存在概念混淆，但核心结论（非原生支持时无法获得1字节存储优势）在工程实践中通常成立，故降级为定性表述。

## Search Query

vLLM FP8 KV cache fallback behavior on unsupported hardware V100 compute capability 7.0

## Retrieval Sources

- {'url': 'https://vllm.ai/blog/2026-04-22-fp8-kvcache&rut=ea02048a617effeb7518c7683a032ae6964cf0b556f3950d8e7e3ed0c2803999', 'type': 'ddg', 'title': 'The State of FP8 KV-Cache and Attention Quantization in vLLM'}
- {'url': 'https://docs.vllm.ai/en/v0.5.4/quantization/fp8.html&rut=b4784931a9f56cb51c7041e8d09fd6af2f768b57dcd01268c40d9155731bce09', 'type': 'ddg', 'title': 'FP8 — vLLM'}
- {'url': 'https://docs.vllm.ai/projects/llm-compressor/en/latest/examples/quantization_kv_cache/&rut=3577c61b1bddd4423db05792de3f7d08fae71a5619d542311a33af5b1166b4ed', 'type': 'ddg', 'title': 'KV Cache Quantization - LLM Compressor Docs'}
