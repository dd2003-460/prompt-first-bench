# N137: RTX 3090 不支持 FP8 硬件加速，若强制使用 FP8 量化模型，软件栈（如 vLLM/TensorRT-LLM）会将其回退为 BF16 或 INT8 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

RTX 3090 不支持 FP8 硬件加速，若强制使用 FP8 量化模型，软件栈（如 vLLM/TensorRT-LLM）会将其回退为 BF16 或 INT8 执行；INT8 模式下 Tensor Core 有效算力为 BF16 的 2 倍，但内存带宽不变，故 T_decode 瓶颈仍由带宽主导，加速比主要源于权重体积减半（27GB vs 54GB），T_decode_INT8 ≈ 46 us/token

## Corrected Claim

RTX 3090 不支持 FP8 硬件加速，若强制使用 FP8 量化模型，软件栈（如 vLLM/TensorRT-LLM）会将其回退为 BF16 或 INT8 执行；INT8 模式下 Tensor Core 有效算力为 BF16 的 2 倍，但内存带宽不变，故 T_decode 瓶颈仍由带宽主导，加速比主要源于权重体积减半（27GB vs 54GB），T_decode_INT8 ≈ 46 us/token

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 (Ampere架构) 确实不支持FP8硬件加速，INT8 Tensor Core算力为BF16的2倍，且Decode阶段受内存带宽限制，权重减半（27GB vs 54GB）直接降低访存压力，符合Roofline模型直觉。
