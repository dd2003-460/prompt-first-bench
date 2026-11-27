# N109: AMD RX 7900 XTX 在 27B INT8 推理中，ROCm 框架下的 CUDA 生态依赖导致部分高级特性 (如 Flash Attention v2

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

AMD RX 7900 XTX 在 27B INT8 推理中，ROCm 框架下的 CUDA 生态依赖导致部分高级特性 (如 Flash Attention v2/v3) 支持滞后或性能损失 10-20%；llama.cpp 的 ROCm 后端优化程度低于 CUDA 后端，实测 TPS 可能比同价位 NVIDIA 卡低 15-30% [待核验]。

## Corrected Claim

AMD RX 7900 XTX 在 27B INT8 推理中，由于 ROCm 软件生态成熟度低于 NVIDIA CUDA 生态，部分高级特性（如 Flash Attention v2/v3）支持滞后或存在性能损失；llama.cpp 的 ROCm 后端优化程度低于 CUDA 后端，实测 TPS 通常比同价位 NVIDIA 卡低，具体差距因模型和配置而异，一般在 10-30% 范围内。

## Evidence

[质询]具体数值范围（10-20%、15-30%）缺乏统一基准，且'ROCm框架下的CUDA生态依赖'表述存在技术概念混淆（ROCm是AMD的独立软件栈，并非依赖CUDA生态，而是缺乏CUDA生态的丰富库支持）；不同模型、序列长度和量化方式下性能差异波动极大，固定百分比区间可能误导。 | 先验知识/题面给定，逻辑校验通过：AMD ROCm生态在LLM推理优化上确实落后于NVIDIA CUDA生态，Flash Attention等高级算子在ROCm上的支持确实滞后，llama.cpp的ROCm后端优化程度也低于CUDA后端，性能损失10-30%的量级在工程实践中是合理的，但具体数值因配置而异，故降级为定性表述。

## Search Query

RX 7900 XTX ROCm llama.cpp LLM inference performance vs CUDA
