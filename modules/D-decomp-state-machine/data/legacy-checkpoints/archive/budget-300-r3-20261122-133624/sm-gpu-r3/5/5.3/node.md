# N36: 非典型候选集：AMD MI300X (192GB HBM3, $15000, 750W), Intel Gaudi 2 (64GB, $5000 [待核验], 

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（1. 冗余：所有子节点均采用了完全相同的计算逻辑（显存带宽/模型大小*效率）和功耗成本公式，属于同一计算范式在不同参数下的实例化，应压缩为通用公式或表格。2. 不完备：父节点中明确列出的关键参数‘软件栈成熟度’（ROCm vs CUDA 差距）和‘ROCm 兼容性’（vLLM 支持情况）在子节点中完全缺失，子节点仅覆盖了硬件性能（带宽/吞吐）和运行成本（电费），遗漏了软件生态这一核心维度。）

## Search Query

AMD MI300X Intel Gaudi 2 Apple M2 Ultra LLM inference vLLM ROCm compatibility 2024

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html&rut=664468f1a80701a3043a2829ae9945f2b3b30a1a5c8a1638aa17c298fcd0c0f6', 'type': 'ddg', 'title': 'AMD Instinct™ MI300X Accelerators'}
