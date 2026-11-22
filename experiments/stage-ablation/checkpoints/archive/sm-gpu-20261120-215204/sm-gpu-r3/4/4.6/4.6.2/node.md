# N111: NVIDIA 消费级/数据中心级 GPU 的矩阵运算实际利用率 (MFU) 在 LLM 预填充阶段通常受限于内存带宽和内核启动开销，经验值范围在 30%-60%

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

NVIDIA 消费级/数据中心级 GPU 的矩阵运算实际利用率 (MFU) 在 LLM 预填充阶段通常受限于内存带宽和内核启动开销，经验值范围在 30%-60% 之间，需根据具体框架 (如 vLLM/TensorRT-LLM) 确定。

## Corrected Claim

NVIDIA 消费级/数据中心级 GPU 的矩阵运算实际利用率 (MFU) 在 LLM 预填充阶段通常受限于内存带宽和内核启动开销，经验值范围在 30%-60% 之间，需根据具体框架 (如 vLLM/TensorRT-LLM) 确定。

## Evidence

先验知识/题面给定，逻辑校验通过
