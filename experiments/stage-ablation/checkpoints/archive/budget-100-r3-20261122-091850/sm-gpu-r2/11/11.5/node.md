# N123: 主流推理框架（如 llama.cpp, MLX, vLLM-MLX）在 Apple Silicon 上运行 Qwen3-27B 的实测 Tokens Per S

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

主流推理框架（如 llama.cpp, MLX, vLLM-MLX）在 Apple Silicon 上运行 Qwen3-27B 的实测 Tokens Per Second (TPS) 基准数据，用于量化实际生成速度。

## Corrected Claim

主流推理框架（如 llama.cpp, MLX, vLLM-MLX）支持在 Apple Silicon 上运行 Qwen3-27B，其实际生成速度（TPS）受硬件型号、内存带宽及量化精度影响，具体基准数据需参考特定硬件配置下的实测报告。

## Evidence

[质询]该陈述声称存在具体的“实测 TPS 基准数据”，但参考来源显示检索失败，无可用外部证据支持具体数值或特定框架在 Apple Silicon 上运行 Qwen3-27B 的确切性能指标。此外，TPS 高度依赖于具体硬件型号（M1/M2/M3/M4/M1/M2/M3/M4 Max/Ultra）、内存带宽、量化精度（Q4/Q8）及上下文长度，缺乏这些限定条件的“主流框架实测数据”是一个模糊且难以直接验证的经验事实集合。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体 TPS 数值或框架对比细节）

## Search Query

Qwen3-27B inference speed Mac Studio M3 Ultra tokens per second
