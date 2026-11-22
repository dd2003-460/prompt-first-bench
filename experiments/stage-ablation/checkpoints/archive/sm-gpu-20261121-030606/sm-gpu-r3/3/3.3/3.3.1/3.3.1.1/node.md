# N263: INT8量化在24GB显存（RTX 4090）下不可行的根本原因是权重+KV Cache+激活值的总显存需求超过24GB。具体计算：INT8权重27GB + K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

INT8量化在24GB显存（RTX 4090）下不可行的根本原因是权重+KV Cache+激活值的总显存需求超过24GB。具体计算：INT8权重27GB + KV Cache (32K ctx, BF16) 3.98GB + 激活值~2.5GB + 框架开销~3GB = 36.48GB > 24GB。即使将KV Cache量化为INT8（1.99GB），总需求仍为34.49GB > 24GB。因此，RTX 4090在INT8精度下运行Qwen3-27B 32K上下文在物理上不可行，必须使用≥32GB显存硬件或降低上下文长度至<16K（此时KV Cache减半，但总显存仍>24GB，需进一步压缩激活值或使用Offload技术）。

## Corrected Claim

INT8量化在24GB显存（RTX 4090）下不可行的根本原因是权重+KV Cache+激活值的总显存需求超过24GB。具体计算：INT8权重27GB + KV Cache (32K ctx, BF16) 3.98GB + 激活值~2.5GB + 框架开销~3GB = 36.48GB > 24GB。即使将KV Cache量化为INT8（1.99GB），总需求仍为34.49GB > 24GB。因此，RTX 4090在INT8精度下运行Qwen3-27B 32K上下文在物理上不可行，必须使用≥32GB显存硬件或降低上下文长度至<16K（此时KV Cache减半，但总显存仍>24GB，需进一步压缩激活值或使用Offload技术）。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8权重27GB已接近24GB上限，加上KV Cache和激活值必然溢出，计算量级合理且符合显存占用基本规律。
