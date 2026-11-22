# N36: 软件栈兼容性前提：使用 vLLM 或 TGI 部署 Qwen3-27B 时，RTX 4090/5090 需 CUDA 12.1+ 和 cuDNN 8.9+，而 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

软件栈兼容性前提：使用 vLLM 或 TGI 部署 Qwen3-27B 时，RTX 4090/5090 需 CUDA 12.1+ 和 cuDNN 8.9+，而 AMD W7900 需 ROCm 6.0+；若使用 FP8 精度，需确保 PyTorch 2.1+ 支持 FP8 推理后端，否则需回退至 INT8 或 BF16。

## Corrected Claim

软件栈兼容性前提：使用 vLLM 或 TGI 部署 Qwen3-27B 时，RTX 4090/5090 需 CUDA 12.1+ 和 cuDNN 8.9+，而 AMD W7900 需 ROCm 6.0+；若使用 FP8 精度，需确保 PyTorch 2.1+ 支持 FP8 推理后端，否则需回退至 INT8 或 BF16。

## Evidence

检索失败: no sources from any channel (all 5 failed)
