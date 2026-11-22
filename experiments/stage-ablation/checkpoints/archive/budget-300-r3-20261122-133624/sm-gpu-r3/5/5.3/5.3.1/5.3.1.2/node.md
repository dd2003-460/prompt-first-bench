# N373: MI300X 的 ROCm 软件栈对 Qwen3-27B 的推理支持成熟度低于 CUDA，vLLM 或 TensorRT-LLM 在 ROCm 上的优化程度可能

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

MI300X 的 ROCm 软件栈对 Qwen3-27B 的推理支持成熟度低于 CUDA，vLLM 或 TensorRT-LLM 在 ROCm 上的优化程度可能导致实际吞吐量比理论值 (166.9 tokens/s) 低 10-20%，需引入软件效率系数 0.8-0.9 进行修正。

## Corrected Claim

MI300X 的 ROCm 软件栈对 Qwen3-27B 的推理支持成熟度通常低于 CUDA，vLLM 或 TensorRT-LLM 在 ROCm 上的优化程度可能导致实际吞吐量低于理论值，建议引入软件效率系数进行修正，具体系数需根据实际基准测试确定。

## Evidence

[质询]该陈述包含具体的经验性数值（10-20% 的性能损耗、0.8-0.9 的效率系数），这些并非第一性原理可推导的数学或物理常数，而是依赖于具体硬件配置、软件版本及工作负载的经验数据。在缺乏具体基准测试数据支持的情况下，直接断言具体的损耗区间存在过度精确化的风险。 | 经验事实，逻辑自洽（ROCm 成熟度低于 CUDA 是业界共识，引入效率系数修正理论峰值符合工程直觉），但缺来源支持具体数值区间。

## Search Query

ROCm vLLM MI300X inference performance benchmark Qwen
