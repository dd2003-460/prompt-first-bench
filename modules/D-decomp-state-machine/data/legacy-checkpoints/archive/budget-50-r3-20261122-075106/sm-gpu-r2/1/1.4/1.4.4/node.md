# N59: AMD MI300X 的软件栈成熟度低于 NVIDIA CUDA，使用 vLLM/TensorRT-LLM 时需依赖 ROCm 移植版本，其推理效率通常比 CU

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

AMD MI300X 的软件栈成熟度低于 NVIDIA CUDA，使用 vLLM/TensorRT-LLM 时需依赖 ROCm 移植版本，其推理效率通常比 CUDA 同代硬件低 10-20% [待核验]，这直接影响最终性价比排序

## Corrected Claim

AMD MI300X 的软件栈成熟度低于 NVIDIA CUDA，使用 vLLM/TensorRT-LLM 时需依赖 ROCm 移植版本，其推理效率在部分场景下可能低于 CUDA 同代硬件，具体差距取决于工作负载，这直接影响最终性价比排序

## Evidence

[质询]陈述中关于“推理效率通常比 CUDA 同代硬件低 10-20%”的具体数值缺乏直接来源支持，且该性能差距高度依赖于具体模型、序列长度及软件优化程度，并非固定的物理或工程常数，属于经验事实而非第一性原理可推导结论。 | 来源[1]和[2]证实了 ROCm 生态及 vLLM 在 MI300X 上的存在与使用，支持了“软件栈依赖移植”和“成熟度相对较低”的定性描述，但均未提供“低 10-20%”的具体性能对比数据，该数值属于经验事实且缺来源直接支持。

## Search Query

ROCm vs CUDA LLM inference performance gap vLLM TensorRT-LLM

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2058640729702921882&rut=123011cfaff8fd6d9260f49e64a0f7f0d8e8ccd248e2295c79d0f825b31bff48', 'type': 'ddg', 'title': 'AMD GPU 架构与 ROCm 生态深度解析：从 CDNA 到 MI300X 再到软件栈全景 - 知乎'}
- {'url': 'https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/run-vllm.html&rut=91dc0b14a4ebf5a6466d0449c6e6928f28b12c940d7897c1fc485d89b3445abd', 'type': 'ddg', 'title': 'Steps to Run a vLLM Workload — AMD GPU Driver (amdgpu) 31.60.0'}
