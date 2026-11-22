# N125: 量化损失工作点3（低质量/低显存）：W4精度下Qwen3-27B的MMLU准确率损失约3-5% [待核验]，Perplexity增加约0.8-1.2%，显存需求

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

量化损失工作点3（低质量/低显存）：W4精度下Qwen3-27B的MMLU准确率损失约3-5% [待核验]，Perplexity增加约0.8-1.2%，显存需求13.5GB（权重），单卡RTX 4090 (24GB) 可容纳（13.5+10.7+4=28.2GB > 24GB，需Offload或FP8 KV），质量损失显著，仅适合对精度不敏感的轻量任务。

## Corrected Claim

量化损失工作点3（低质量/低显存）：W4精度下Qwen3-27B的MMLU准确率损失约3-5% [待核验]，Perplexity增加约0.8-1.2%，显存需求约28.2GB（含权重、KV Cache和激活值），单卡RTX 4090 (24GB) 无法直接容纳，需使用Offload技术（如CPU Offload或FP8 KV Cache），但会显著降低推理速度，仅适合对精度和速度均不敏感的轻量任务。

## Evidence

[质询]显存计算存在严重逻辑矛盾：27B模型W4量化权重约为13.5GB，加上KV Cache和激活值，总显存需求远超24GB，但陈述中计算式'13.5+10.7+4=28.2GB'与'单卡RTX 4090 (24GB) 可容纳'直接冲突，且未明确说明Offload的具体策略和性能影响，导致结论'可容纳'具有误导性。 | 逻辑校验发现内部矛盾：28.2GB > 24GB，无法直接容纳于单卡24GB显存，需依赖Offload，但陈述未充分说明Offload对推理速度的影响，且无外部来源支持具体数值（MMLU损失3-5%、Perplexity增加0.8-1.2%）。

## Search Query

Qwen3-27B W4 quantization MMLU accuracy loss perplexity degradation
