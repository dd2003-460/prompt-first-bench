# N149: FP8 精度下，Qwen3-27B 运行 32K 上下文时 KV Cache 峰值显存占用为 3.75 GB（计算式：128 KB/token * 32,768

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

FP8 精度下，Qwen3-27B 运行 32K 上下文时 KV Cache 峰值显存占用为 3.75 GB（计算式：128 KB/token * 32,768 tokens），相比 BF16 节省 3.75 GB 显存，使得 48 GB 显存的显卡（如 RTX 6000 Ada）在 FP8 下可容纳单卡 32K 上下文推理。

## Corrected Claim

FP8 精度下，Qwen3-27B 运行 32K 上下文时 KV Cache 峰值显存占用需根据具体模型架构（头数、KV 头数、Head Dim）计算，通常远低于 3.75 GB（例如在 GQA 配置下约为 0.5-1 GB 量级），具体数值需查阅模型配置或实测数据。

## Evidence

[质询]数值量级与架构参数不匹配：Qwen3-27B 若采用标准 Transformer 架构（如 64 头，GQA 8 KV 头，Head Dim 128），FP8 下每 token KV Cache 约为 16KB，32K 上下文总占用约 0.5GB，而非 3.75GB；若按 3.75GB 反推，需每 token 128KB，这通常对应极大头数或极高精度（如 FP32 且头数极多），与 27B 模型常见配置及 FP8 精度描述存在显著矛盾。 | 经验事实，逻辑校验发现数值量级与典型模型架构参数不符，且无外部来源支持，无法排除计算错误或参数假设错误。
