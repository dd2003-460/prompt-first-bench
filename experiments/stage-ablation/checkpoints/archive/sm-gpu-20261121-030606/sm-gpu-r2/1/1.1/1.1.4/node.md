# N83: INT8 精度下 Qwen3-27B 总显存下限 = 27GB (权重) + 4.7GB (KV) + 2.5GB (激活) = 34.2GB，24GB 显存同

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

INT8 精度下 Qwen3-27B 总显存下限 = 27GB (权重) + 4.7GB (KV) + 2.5GB (激活) = 34.2GB，24GB 显存同样不可行，INT8 与 FP8 在 27B 模型上的显存占用相同（均为 1 byte/param）

## Corrected Claim

INT8 精度下 Qwen3-27B 总显存下限 = 27GB (权重) + 4.7GB (KV) + 2.5GB (激活) = 34.2GB，24GB 显存同样不可行，INT8 与 FP8 在 27B 模型上的显存占用相同（均为 1 byte/param）

## Evidence

先验知识/题面给定，逻辑校验通过：INT8与FP8均为1字节/参数，27B模型权重约27GB，加上KV Cache和激活值，总显存需求远超24GB，计算逻辑自洽。

## Search Query

INT8 quantization weight size LLM inference
