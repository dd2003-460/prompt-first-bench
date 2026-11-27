# N175: RX 7900 XTX 在 ROCm 6.0+ 环境下对 BF16 的支持状态：ROCm 原生支持 FP16 和 FP32，BF16 支持依赖于 PyTorch

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

RX 7900 XTX 在 ROCm 6.0+ 环境下对 BF16 的支持状态：ROCm 原生支持 FP16 和 FP32，BF16 支持依赖于 PyTorch 版本和驱动更新；在 LLM 推理中，BF16 精度通常通过软件模拟或特定内核优化实现，实际性能可能低于 FP16，需验证 Qwen3-27B 在 ROCm 下的 BF16 推理是否启用硬件加速。

## Corrected Claim

RX 7900 XTX 在 ROCm 环境下对 BF16 的支持情况需根据具体 ROCm 版本和 PyTorch 配置验证；在 LLM 推理中，BF16 的性能表现取决于是否启用了硬件加速内核，建议在实际部署前进行基准测试以确认 Qwen3-27B 的推理效率。

## Evidence

[质询]该陈述包含具体的软件版本依赖（ROCm 6.0+）和特定模型（Qwen3-27B）的性能推断，属于经验事实。由于缺乏外部来源支持，无法确认 ROCm 6.0 对 BF16 的具体支持状态（是原生硬件加速还是软件模拟）以及 Qwen3-27B 在该环境下的实际表现，存在将一般性推测当作既定事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

ROCm 6.0 BF16 support AMD RX 7900 XTX PyTorch
