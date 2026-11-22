# N81: 工作点B（BF16量化/48GB显存）：2×RTX 4090运行Qwen3-27B BF16，权重54GB>48GB，显存不足，不可行；需使用GQA+BF16+

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

工作点B（BF16量化/48GB显存）：2×RTX 4090运行Qwen3-27B BF16，权重54GB>48GB，显存不足，不可行；需使用GQA+BF16+KV Cache压缩或切换至INT8/FP8。

## Corrected Claim

工作点B（BF16量化/48GB显存）：2×RTX 4090运行Qwen3-27B BF16，权重54GB>48GB，显存不足，不可行；需使用GQA+BF16+KV Cache压缩或切换至INT8/FP8。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约270亿，BF16精度下权重占用约54GB，超过单卡48GB显存，且2×4090若未启用张量并行或显存池化无法直接加载单模型，结论符合硬件与模型规格常识。
