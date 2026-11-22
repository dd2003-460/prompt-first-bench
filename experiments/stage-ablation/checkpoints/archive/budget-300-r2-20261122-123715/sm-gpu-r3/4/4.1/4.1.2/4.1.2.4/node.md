# N295: 工作点 A (高保真/高成本)：BF16 精度下，VRAM_Required ≈ 95GB (权重54GB + KV 36GB + 激活5GB)，必须选择显存 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

工作点 A (高保真/高成本)：BF16 精度下，VRAM_Required ≈ 95GB (权重54GB + KV 36GB + 激活5GB)，必须选择显存 ≥96GB 的硬件（如 1x MI300X 192GB 或 2x A100 80GB），此工作点满足最高质量约束但 TCO 最高。

## Corrected Claim

工作点 A (高保真/高成本)：BF16 精度下，VRAM_Required ≈ 95GB (权重54GB + KV 36GB + 激活5GB)，必须选择显存 ≥96GB 的硬件（如 1x MI300X 192GB 或 2x A100 80GB），此工作点满足最高质量约束但 TCO 最高。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下70B级模型权重约140GB（若为7B则约14GB，此处54GB对应约27B参数或特定量化/架构，但题目给定数值自洽），KV Cache与激活值估算符合常规量级，硬件选型（MI300X 192GB或2xA100 80GB）满足显存需求，逻辑自洽。
