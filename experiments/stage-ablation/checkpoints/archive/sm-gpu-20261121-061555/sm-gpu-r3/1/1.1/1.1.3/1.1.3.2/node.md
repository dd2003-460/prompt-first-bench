# N148: ROCm 软件栈对 AMD RX 8000 系列 GPU 进行 LLM 推理时的驱动版本要求及 FP8/INT4 量化支持状态，需确认是否存在硬件加速指令集或仅

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

ROCm 软件栈对 AMD RX 8000 系列 GPU 进行 LLM 推理时的驱动版本要求及 FP8/INT4 量化支持状态，需确认是否存在硬件加速指令集或仅依赖软件模拟，以评估其相对于 NVIDIA RTX 4090 的性能差距。

## Corrected Claim

ROCm 软件栈对 AMD RX 8000 系列 GPU 的 LLM 推理支持状态（包括驱动版本要求、FP8/INT4 量化支持及硬件加速指令集情况）需依据最新官方文档确认，目前缺乏公开可靠来源以评估其相对于 NVIDIA RTX 4090 的具体性能差距。

## Evidence

[质询]该陈述包含具体的硬件规格（RX 8000系列）、软件栈状态（ROCm驱动版本、量化支持）及性能对比结论，属于经验事实。由于缺乏外部来源支持，无法确认RX 8000系列是否已正式发布、ROCm对其的具体支持状态以及FP8/INT4的硬件加速细节，存在信息滞后或推测性错误的可能。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体驱动版本及量化支持状态）

## Search Query

ROCm support AMD RX 8000 LLM inference FP8 INT4 quantization
