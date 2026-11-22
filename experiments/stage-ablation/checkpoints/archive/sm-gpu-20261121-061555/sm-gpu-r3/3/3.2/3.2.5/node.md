# N83: NVFP4 (Native FP4) 相比 W4A16 的硬件优势：H100/H200 支持 FP4 张量核心，推理吞吐量理论上比 W4A16 高 2 倍，但需

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

NVFP4 (Native FP4) 相比 W4A16 的硬件优势：H100/H200 支持 FP4 张量核心，推理吞吐量理论上比 W4A16 高 2 倍，但需验证其对 Qwen3-27B 的 PPL 损失是否仍控制在 <5% [待核验]

## Corrected Claim

NVFP4 相比 W4A16 在支持 FP4 张量核心的硬件（如 Blackwell 系列）上理论上具有更高的计算密度，但 H100/H200 并不原生支持 FP4 张量核心。对于 Qwen3-27B，NVFP4 的 PPL 损失是否控制在 <5% 需具体实验验证，目前无公开数据直接支持该结论。

## Evidence

[质询]H100/H200 硬件架构（Hopper）原生支持 FP8 和 INT8，但不支持原生 FP4 张量核心运算；FP4 支持通常出现在 Blackwell (B100/B200) 架构中。此外，'吞吐量高2倍'是理论峰值带宽/算力比的简化推断，未考虑内存带宽瓶颈和实际 kernel 效率，且 PPL 损失 <5% 是经验性断言，缺乏特定模型（Qwen3-27B）的实证数据支持。 | 经验事实，逻辑自洽但缺来源支持；且存在硬件架构代际混淆风险（H100 不支持原生 FP4），无法排除错误可能性。

## Search Query

NVFP4 H100 Qwen3 perplexity loss
