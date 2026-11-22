# N151: ROCm 生态依赖项具体化为：必须使用 AMD GPU (MI300X/MI325X/Instinct 系列) 且软件栈需支持 ROCm 6.0+ 及 Qwen

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

ROCm 生态依赖项具体化为：必须使用 AMD GPU (MI300X/MI325X/Instinct 系列) 且软件栈需支持 ROCm 6.0+ 及 Qwen3-27B 的 BF16/FP8 算子；该条件排除所有 NVIDIA GPU，但允许 AMD 消费级卡 (RX 7900 XTX 24GB) 若其 ROCm 社区支持足够成熟 [待核验]。

## Corrected Claim

ROCm 生态依赖项具体化为：必须使用 AMD GPU（如 Instinct 系列）且软件栈需支持相应版本的 ROCm 及 Qwen3-27B 的 BF16/FP8 算子；该条件排除所有 NVIDIA GPU。关于 AMD 消费级卡（如 RX 7900 XTX）的支持情况，需根据具体 ROCm 版本和社区驱动成熟度单独评估，不能一概而论。

## Evidence

[质询]该陈述包含具体的硬件型号（MI300X/MI325X）、软件版本（ROCm 6.0+）及特定模型（Qwen3-27B）的算子支持情况，属于经验事实。由于检索失败，无法验证 ROCm 6.0+ 是否确实支持 Qwen3-27B 的 BF16/FP8 算子，也无法确认 RX 7900 XTX 在 ROCm 社区中是否已具备运行该规模模型的‘足够成熟’的支持（通常消费级卡驱动支持滞后且不稳定）。 | 经验事实，逻辑自洽但缺来源支持。ROCm 确实主要支持 AMD GPU 并排除 NVIDIA，但具体版本兼容性和消费级卡支持程度需外部证据确认。

## Search Query

AMD ROCm 6.0 support for Qwen3-27B inference on RX 7900 XTX
