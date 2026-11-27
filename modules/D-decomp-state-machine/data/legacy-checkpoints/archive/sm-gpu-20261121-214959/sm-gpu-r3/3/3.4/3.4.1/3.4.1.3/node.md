# N224: 4x RTX 4090 机箱散热风道与噪声约束：Fractal Design Define 7 XL ($300) 支持 4 个 3.5 英寸硬盘位和多个风扇位

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

4x RTX 4090 机箱散热风道与噪声约束：Fractal Design Define 7 XL ($300) 支持 4 个 3.5 英寸硬盘位和多个风扇位。关键约束：4 张双槽显卡需占用 8 个槽位，若主板为 ATX 标准，需确保机箱支持 4 个全尺寸扩展槽且间距无遮挡。若散热不足导致 GPU 降频 (Thermal Throttling)，实际带宽可能从 1008 GB/s 降至 900 GB/s 以下，影响 N92 的性能估算。

## Corrected Claim

Fractal Design Define 7 XL 支持多硬盘位和风扇位，适合多显卡配置。4 张双槽显卡需占用 8 个扩展槽位，需确认机箱兼容性。若散热不足导致 GPU 降频，实际性能（包括有效带宽）可能显著低于理论峰值，具体数值需实测验证。

## Evidence

[质询]该陈述包含多个具体的经验性硬件参数（如 Fractal Design Define 7 XL 的具体硬盘位数量、价格、以及 4x RTX 4090 在该机箱下的具体散热表现和带宽衰减数值），这些属于经验事实，无法从第一性原理推导。此外，'1008 GB/s' 这一数值对于 4 张 RTX 4090 的总带宽（单卡约 1008 GB/s，4 卡应为 ~4032 GB/s）存在明显的量级或口径混淆嫌疑，可能是指单卡带宽或特定聚合带宽，表述不严谨。 | 经验事实，逻辑自洽但缺来源支持；且带宽数值存在口径混淆风险（单卡 vs 总带宽），无法通过现有逻辑完全排除错误，故降级。

## Search Query

Fractal Design Define 7 XL 4 GPU clearance thermal throttling RTX 4090
