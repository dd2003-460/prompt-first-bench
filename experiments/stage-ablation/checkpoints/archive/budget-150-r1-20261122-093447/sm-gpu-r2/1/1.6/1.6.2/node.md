# N61: vLLM 额外开销 ≈ 500MB-1GB，主要来自 PagedAttention 的 block table 管理结构、调度器状态和 tokenizer 缓存

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

vLLM 额外开销 ≈ 500MB-1GB，主要来自 PagedAttention 的 block table 管理结构、调度器状态和 tokenizer 缓存；TensorRT-LLM 额外开销 ≈ 100-300MB，因其预编译引擎更紧凑

## Corrected Claim

vLLM 的额外内存开销通常高于 TensorRT-LLM，主要源于 PagedAttention 的块表管理、调度器状态及 Python 运行时开销；TensorRT-LLM 因采用预编译引擎，内存占用更为紧凑。具体数值随模型规模和配置变化，典型场景下 vLLM 开销可能在数百 MB 至 GB 级别，而 TensorRT-LLM 相对较低。

## Evidence

[质询]具体数值范围（500MB-1GB vs 100-300MB）属于经验性工程数据，受模型大小、上下文长度、Batch Size 等参数影响极大，缺乏通用性；且参考来源仅介绍 PagedAttention 原理，未提供具体的内存开销量化数据，无法直接支持该具体数值区间。 | 逻辑上 vLLM 因动态分页管理（Block Table）和 Python 调度开销确实通常高于预编译的 TensorRT-LLM，定性结论合理；但参考来源 [1] 仅涉及原理，未提供具体内存数值，属于经验事实且缺乏直接来源支持，故降级。

## Search Query

vLLM vs TensorRT-LLM runtime memory overhead block table scheduler

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/691038809&rut=0b40172c1027d768187aadcf74a5e89fe9a232d129e4a68d96cb84a410ed25bc', 'type': 'ddg', 'title': '图解大模型计算加速系列之：vLLM核心技术PagedAttention原理'}
