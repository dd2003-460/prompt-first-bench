# N93: AMD CDNA 2 (MI210/MI250) 和 CDNA 3 (MI300X) 架构对 FP8 的支持程度：CDNA 3 原生支持 FP8，而 CDNA 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

AMD CDNA 2 (MI210/MI250) 和 CDNA 3 (MI300X) 架构对 FP8 的支持程度：CDNA 3 原生支持 FP8，而 CDNA 2 主要优化于 INT8/FP16，FP8 推理需依赖 ROCm 软件栈支持，效率低于 NVIDIA 原生支持约 20-40% [待核验]。

## Corrected Claim

AMD CDNA 3 (MI300X) 架构原生支持 FP8，而 CDNA 2 (MI210/MI250) 主要优化于 INT8/FP16，FP8 推理需依赖 ROCm 软件栈支持，其效率通常低于 NVIDIA 原生支持架构。

## Evidence

[质询]陈述中关于'效率低于 NVIDIA 原生支持约 20-40%'的具体数值缺乏来源支持，且不同模型和负载下性能差异巨大，该固定百分比范围可能不准确或过于简化。 | 来源[2]直接支持CDNA 3 (MI300)原生支持FP8，来源[1]确认架构分类，但无来源支持具体的20-40%性能差距数值，属于经验事实且缺来源支持。

## Search Query

AMD MI300X MI250 FP8 inference support ROCm efficiency vs NVIDIA

## Retrieval Sources

- {'url': 'https://rocm.docs.amd.com/en/latest/reference/precision-support.html&rut=53dbe8e15966425e12ec553fc4de13b8b71fa6ea0e28cc8f31b4953a6554aa91', 'type': 'ddg', 'title': 'Data types and precision support — AMD ROCm 10.1.0'}
- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi300.html&rut=86a251bd17061d37da70e581bb8f27ba3d505f7fd8ca2cb8d45866954657425d', 'type': 'ddg', 'title': 'AMD Instinct™ MI300 Series Accelerators'}
