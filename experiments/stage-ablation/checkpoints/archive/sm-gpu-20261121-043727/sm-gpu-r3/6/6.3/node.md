# N88: Intel Data Center GPU Max 1550 推理支持情况：显存 48GB HBM2e，带宽 921.6 GB/s，价格 ~$3k-$5k；软件

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Intel Data Center GPU Max 1550 推理支持情况：显存 48GB HBM2e，带宽 921.6 GB/s，价格 ~$3k-$5k；软件栈 (oneAPI/SYCL) 对 PyTorch 的支持成熟度低于 CUDA，Qwen3-27B 在 Intel GPU 上的推理需通过 IPEX (Intel Extension for PyTorch) 或 llama.cpp 后端，性能通常比同价位 NVIDIA 卡低 20-40% [待核验]，且不支持原生 FP8，仅支持 BF16/INT8。

## Corrected Claim

Intel Data Center GPU Max 1550 配备 48GB HBM2e 显存，带宽 921.6 GB/s。其软件栈（oneAPI/SYCL）对 PyTorch 的支持通常通过 IPEX 或 llama.cpp 实现，性能及生态成熟度相较于同价位 NVIDIA 产品可能存在差距，且主要支持 BF16/INT8 精度。具体价格及精确性能百分比需参考最新市场数据及基准测试。

## Evidence

[质询]该陈述包含大量经验性事实（具体价格区间、与NVIDIA同价位卡的性能对比百分比、特定模型Qwen3-27B的推理路径及FP8支持情况），这些无法从第一性原理推导，且参考来源[1]仅提供了硬件规格摘要，未涵盖软件栈成熟度、具体价格及性能对比数据，存在来源覆盖不足的风险。 | 来源[1]确认了硬件型号，但缺乏对价格、性能对比及软件支持细节的直接支持；作为经验事实，逻辑自洽但缺充分来源支持，故降级。

## Search Query

Intel Max 1550 48GB inference performance vs NVIDIA Qwen3 support IPEX

## Retrieval Sources

- {'url': 'https://www.intel.com/content/www/us/en/products/sku/232873/intel-data-center-gpu-max-1550/specifications.html&rut=a5fb7f328ba301273f7673117af0f9517ea79fbffcbfa68fb3960a164f9ac494', 'type': 'ddg', 'title': 'Intel® Data Center GPU Max 1550 Specifications'}
