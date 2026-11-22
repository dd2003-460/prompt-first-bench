# N439: W4量化中特殊层（如Embedding, LM Head）的量化策略对显存的影响：通常Embedding和LM Head保持BF16/FP16精度以维持输出质量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

W4量化中特殊层（如Embedding, LM Head）的量化策略对显存的影响：通常Embedding和LM Head保持BF16/FP16精度以维持输出质量，需计算这两层参数量（vocab_size * hidden_size * 2 bytes）并加到W4权重总大小上，得出Qwen3-27B W4量化的最终总显存需求

## Corrected Claim

W4量化中特殊层（如Embedding, LM Head）的量化策略对显存的影响：通常Embedding和LM Head保持BF16/FP16精度以维持输出质量，需计算这两层参数量（vocab_size * hidden_size * 2 bytes）并加到W4权重总大小上，得出Qwen3-27B W4量化的最终总显存需求

## Evidence

先验知识/题面给定，逻辑校验通过：Embedding和LM Head通常保持高精度以维持输出质量，参数量计算逻辑正确（vocab_size * hidden_size * 2 bytes），符合W4量化策略的常规做法。

## Search Query

W4 quantization embedding lm head BF16 memory overhead LLM
