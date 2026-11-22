# N133: Apple M3 Ultra 512GB 统一内存运行 Qwen3-27B BF16 精度时的实测吞吐量在 10-20 tokens/s 范围内 [待核验]，其

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

Apple M3 Ultra 512GB 统一内存运行 Qwen3-27B BF16 精度时的实测吞吐量在 10-20 tokens/s 范围内 [待核验]，其瓶颈在于内存带宽 (800 GB/s) 而非计算能力；相比 RTX 5090 FP8 (理论 662 tokens/s, 实际 330-460 tokens/s)，M3 Ultra 的吞吐量低 16-66 倍，但在 32K 上下文下的 TTFT 可能更优，因为统一内存避免了 GPU-CPU 数据拷贝开销，需实测 TTFT 以量化差异。

## Corrected Claim

Apple M3 Ultra 512GB 统一内存运行 Qwen3-27B BF16 精度时，其性能瓶颈主要在于内存带宽 (800 GB/s) 而非计算能力；相比高端GPU（如RTX 5090），其吞吐量显著较低，但在长上下文场景下，统一内存架构可能因避免数据拷贝开销而在TTFT方面具有潜在优势，具体数值需实测验证。

## Evidence

[质询]陈述中包含大量具体的经验性数值（如M3 Ultra实测吞吐量10-20 tokens/s、RTX 5090具体吞吐量、TTFT对比结论），这些属于硬件性能实测数据，无法从第一性原理推导，且参考来源[1]仅定性说明M3 Ultra可运行大模型，未提供具体的吞吐量数值或瓶颈分析，缺乏直接证据支持具体数值范围。 | 逻辑上，LLM推理在长上下文或大模型下通常受内存带宽限制，M3 Ultra 800GB/s带宽低于高端GPU，吞吐量较低符合物理直觉；但具体数值（10-20 tokens/s）及与RTX 5090的精确倍数关系属于经验事实，来源[1]未提供相关数据支持，仅能确认其可运行大模型。

## Search Query

Apple M3 Ultra Qwen3 27B inference benchmark tokens per second

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1928856739001927267&rut=fa4f9f415c7129ecb06af59f90715076c249fe09bb0a90bacc1260e3b11d07c9', 'type': 'ddg', 'title': 'Apple M3 Ultra（512GB统一内存）本地LLM推理全面分析'}
