# N7: Qwen3-27B在BF16精度下的基础权重显存占用为54GB（27B参数 * 2 bytes/param），在INT8精度下为27GB，在W4精度下为13.5

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B在BF16精度下的基础权重显存占用为54GB（27B参数 * 2 bytes/param），在INT8精度下为27GB，在W4精度下为13.5GB，这是计算显存需求的基准。

## Corrected Claim

Qwen3-27B在BF16精度下的基础权重显存占用为54GB（27B参数 * 2 bytes/param），在INT8精度下为27GB，在W4精度下为13.5GB，这是计算显存需求的基准。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)下为54GB，INT8(1字节)下为27GB，W4(0.5字节)下为13.5GB，计算准确且符合显存占用基本规律。
