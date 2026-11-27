# N39: INT8/W8A8量化下的权重显存占用：27.2B params * 1 byte/param = 27.2GB（假设使用Symmetric Quantizat

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

INT8/W8A8量化下的权重显存占用：27.2B params * 1 byte/param = 27.2GB（假设使用Symmetric Quantization，无额外bias开销）

## Corrected Claim

INT8/W8A8量化下的权重显存占用：27.2B params * 1 byte/param = 27.2GB（假设使用Symmetric Quantization，无额外bias开销）

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化下每参数1字节，27.2B参数对应27.2GB显存，计算无误且符合工程常识。
