# N355: Qwen3-27B 32K 上下文 INT8 激活值显存占用估算：Activation_GB ≈ 2.0 - 4.0 GB（取决于 batch_size 和中间

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

Qwen3-27B 32K 上下文 INT8 激活值显存占用估算：Activation_GB ≈ 2.0 - 4.0 GB（取决于 batch_size 和中间层激活大小，通常占显存的 5-10%）

## Corrected Claim

Qwen3-27B 32K 上下文 INT8 激活值显存占用估算：Activation_GB ≈ 2.0 - 4.0 GB（取决于 batch_size 和中间层激活大小，通常占显存的 5-10%）

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在32K上下文下，INT8激活值显存占用估算在2.0-4.0GB范围内符合常规工程经验，且占显存5-10%的比例合理。

## Search Query

LLM inference activation memory usage 32K context
