# N318: 判定'刚查到的'数据源必须包含具体的软件栈版本号，例如 CUDA 12.4.1, cuDNN 9.x, PyTorch 2.3.0, 或推理框架版本 (vLLM

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

判定'刚查到的'数据源必须包含具体的软件栈版本号，例如 CUDA 12.4.1, cuDNN 9.x, PyTorch 2.3.0, 或推理框架版本 (vLLM 0.6.1, llama.cpp b4000+)；仅引用硬件型号或驱动版本号 (如 550.54) 而无框架版本的数据降级为'待核验'。

## Corrected Claim

判定'刚查到的'数据源必须包含具体的软件栈版本号，例如 CUDA 12.4.1, cuDNN 9.x, PyTorch 2.3.0, 或推理框架版本 (vLLM 0.6.1, llama.cpp b4000+)；仅引用硬件型号或驱动版本号 (如 550.54) 而无框架版本的数据降级为'待核验'。

## Evidence

先验知识/题面给定，逻辑校验通过
