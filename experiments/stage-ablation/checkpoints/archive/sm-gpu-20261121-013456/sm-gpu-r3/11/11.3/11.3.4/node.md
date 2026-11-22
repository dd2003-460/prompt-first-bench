# N293: RTX 4090 在 Qwen3-27B FP8 下不支持原生 FP8 加速，需降级为 INT8 或 BF16，实测吞吐量与 BF16 基本持平（提升系数 1.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

RTX 4090 在 Qwen3-27B FP8 下不支持原生 FP8 加速，需降级为 INT8 或 BF16，实测吞吐量与 BF16 基本持平（提升系数 1.0x），FP8 优势无法在消费级 Ada Lovelace 架构上体现。

## Corrected Claim

RTX 4090 基于 Ada Lovelace 架构，硬件支持 FP8，但在 Qwen3-27B 推理中，由于软件栈优化或量化精度损失，FP8 模式下的吞吐量提升有限，与 BF16 基本持平（提升系数约 1.0x），FP8 的性能优势未能在该消费级显卡上显著体现。

## Evidence

[质询]RTX 4090 基于 Ada Lovelace 架构，该架构硬件层面原生支持 FP8 数据格式（通过 Tensor Cores），因此声称“不支持原生 FP8 加速”在硬件能力层面存在事实错误；虽然软件栈（如 CUDA 版本、PyTorch 支持）可能限制其实际性能提升，但将其归因为架构不支持是不准确的。 | 先验知识/题面给定，逻辑校验发现硬件架构描述与事实不符（Ada Lovelace 支持 FP8），且无外部来源支持，故降级。
