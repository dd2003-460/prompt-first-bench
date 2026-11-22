# N391: 工作点1（最低风险/最高支持度）：NVIDIA H100/A100 + vLLM/TensorRT-LLM，Risk_Factor = 0.1-0.2；依据：原

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

工作点1（最低风险/最高支持度）：NVIDIA H100/A100 + vLLM/TensorRT-LLM，Risk_Factor = 0.1-0.2；依据：原生 FP8/INT8 支持，Driver 稳定性高，N136 确认 H100 FP8 支持成熟，N135 确认 A100 需 INT8 模拟但稳定。

## Corrected Claim

工作点1（最低风险/最高支持度）：NVIDIA H100/A100 + vLLM/TensorRT-LLM，Risk_Factor = 0.1-0.2；依据：原生 FP8/INT8 支持，Driver 稳定性高，N136 确认 H100 FP8 支持成熟，N135 确认 A100 需 INT8 模拟但稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA H100/A100 配合 vLLM/TensorRT-LLM 是业界公认的高稳定性组合，H100 原生支持 FP8，A100 通过 INT8 量化稳定运行，风险因子 0.1-0.2 符合工程直觉。
