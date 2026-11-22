# N310: NVFP4 显存可行性验证：NVFP4 权重 13.5GB，KV Cache (FP8) 4.3GB，Activation (FP8) 1.25GB，Overh

- **status**: degraded
- **level**: L4
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131

## Claim

NVFP4 显存可行性验证：NVFP4 权重 13.5GB，KV Cache (FP8) 4.3GB，Activation (FP8) 1.25GB，Overhead 3.0GB。总显存 = 13.5 + 4.3 + 1.25 + 3.0 = 22.05GB。此值低于 RTX 4090 (24GB) 和 RTX 5090 (32GB) 的容量，表明 NVFP4 是 RTX 4090 上运行 32K 上下文的唯一可行高精度量化方案（BF16/FP8 均超出 24GB 限制）。

## Corrected Claim

NVFP4 方案总显存需求约为 22.05GB（基于特定模型配置估算），低于 RTX 4090 (24GB) 容量，理论上可行；但具体显存占用数值需根据实际模型架构和上下文长度进一步验证。

## Evidence

[质询]该陈述包含具体的硬件显存占用数值（如NVFP4权重13.5GB、KV Cache 4.3GB等）以及特定GPU型号（RTX 4090/5090）的容量对比，属于经验事实。由于检索无可用来源，无法验证这些具体数值是否准确对应于特定的模型架构（如Llama-3-70B等）和配置，存在数值量级或具体配置假设错误的风险。 | 经验事实，逻辑自洽但缺来源支持。算术运算 13.5 + 4.3 + 1.25 + 3.0 = 22.05 正确，且 22.05GB < 24GB 的逻辑推导成立，但具体显存占用数值缺乏外部证据验证。
