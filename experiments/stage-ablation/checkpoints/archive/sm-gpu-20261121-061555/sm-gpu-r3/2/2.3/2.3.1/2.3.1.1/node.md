# N188: vLLM 框架在 CUDA 12.x 环境下初始化 Context 及加载 PyTorch 运行时（含 cuDNN/cuBLAS 句柄）的固定显存开销基准值，通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

vLLM 框架在 CUDA 12.x 环境下初始化 Context 及加载 PyTorch 运行时（含 cuDNN/cuBLAS 句柄）的固定显存开销基准值，通常约为 0.4-0.6 GB，可通过 `nvidia-smi` 在空进程启动后监控确认。

## Corrected Claim

vLLM 框架在 CUDA 12.x 环境下初始化 Context 及加载 PyTorch 运行时（含 cuDNN/cuBLAS 句柄）的固定显存开销基准值，通常约为 0.4-0.6 GB，可通过 `nvidia-smi` 在空进程启动后监控确认。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM CUDA context memory overhead 0.5GB
