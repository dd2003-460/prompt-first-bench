# N117: W4精度下Qwen3-27B的权重存储占用为13.5GB（N19中W4A16=13.5GB为正确值），该数值允许在24GB显存（RTX 4090）下运行，剩余1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

W4精度下Qwen3-27B的权重存储占用为13.5GB（N19中W4A16=13.5GB为正确值），该数值允许在24GB显存（RTX 4090）下运行，剩余10.5GB用于KV Cache和激活值，32K上下文下总占用约18.7GB < 24GB，可行且留有23%余量。

## Corrected Claim

W4精度下Qwen3-27B的权重存储占用为13.5GB（N19中W4A16=13.5GB为正确值），该数值允许在24GB显存（RTX 4090）下运行，剩余10.5GB用于KV Cache和激活值，32K上下文下总占用约18.7GB < 24GB，可行且留有23%余量。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在W4精度下权重约为13.5GB，加上KV Cache和激活值后总占用18.7GB小于24GB显存，计算自洽。
