# N141: AMD MI300X软件生态兼容性：ROCm对PyTorch/vLLM的支持成熟度低于CUDA，Qwen3-27B在ROCm上的实测吞吐量通常比CUDA版本低1

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N41

## Claim

AMD MI300X软件生态兼容性：ROCm对PyTorch/vLLM的支持成熟度低于CUDA，Qwen3-27B在ROCm上的实测吞吐量通常比CUDA版本低10-20% [待核验]，且缺乏TensorRT-LLM等高级优化库，导致实际性价比需打8折计算。

## Corrected Claim

AMD MI300X软件生态兼容性：ROCm对PyTorch/vLLM的支持成熟度低于CUDA，Qwen3-27B在ROCm上的实测吞吐量通常低于CUDA版本，且缺乏TensorRT-LLM等高级优化库，导致实际性价比通常低于NVIDIA对应方案。

## Evidence

[质询]「实测吞吐量通常比CUDA版本低10-20%」及「性价比需打8折」属于具体的经验性量化数据，缺乏通用基准测试支持，且不同模型、序列长度及优化程度下差异巨大，该具体数值范围可能不准确或过于绝对。 | 先验知识/题面给定，逻辑校验通过：ROCm生态成熟度低于CUDA是公认事实，但具体性能损耗比例（10-20%）和性价比折扣（8折）为经验估计，无来源直接支持，故降级为定性表述。

## Search Query

ROCm vs CUDA LLM inference performance gap Qwen 27B vLLM
