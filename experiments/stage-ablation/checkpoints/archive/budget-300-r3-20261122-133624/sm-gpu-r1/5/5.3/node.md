# N36: 非典型候选集：AMD MI300X (192GB HBM3, $15000, 750W), Intel Gaudi 2 (64GB, $5000 [待核验], 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

非典型候选集：AMD MI300X (192GB HBM3, $15000, 750W), Intel Gaudi 2 (64GB, $5000 [待核验], 500W), Apple M2 Ultra (192GB unified, $3999 Mac Studio, 150W)；关键参数：ROCm 兼容性 (MI300X 支持 vLLM 0.6+), 统一内存带宽 (800 GB/s for M2 Ultra), 软件栈成熟度 (AMD ROCm 落后 CUDA 6-12 个月 [待核验])。

## Corrected Claim

非典型候选集包括AMD MI300X、Intel Gaudi 2和Apple M2 Ultra。AMD MI300X专为生成式AI设计（来源[1]）。具体参数如价格、功耗及软件栈成熟度需进一步核验，当前数据仅供参考。

## Evidence

[质询]陈述包含多个具体经验参数（如价格、功耗、软件栈滞后时间），其中部分标记为[待核验]，且参考来源仅覆盖MI300X的基本定位，未提供价格、功耗或与其他芯片（Gaudi 2, M2 Ultra）的对比数据，无法通过现有来源直接验证所有数值。 | 来源[1]确认了AMD MI300X的存在及其针对生成式AI的定位，间接支持其作为非典型候选集成员的合理性；但缺乏对具体价格、功耗及软件栈成熟度滞后时间的直接支持，且其他芯片参数无来源覆盖，属于经验事实缺来源支持。

## Search Query

AMD MI300X Intel Gaudi 2 Apple M2 Ultra LLM inference vLLM ROCm compatibility 2024

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html&rut=664468f1a80701a3043a2829ae9945f2b3b30a1a5c8a1638aa17c298fcd0c0f6', 'type': 'ddg', 'title': 'AMD Instinct™ MI300X Accelerators'}
