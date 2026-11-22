# N207: Qwen3-27B 在 BF16 精度下的权重文件大小为 54 GB (27e9 * 2 bytes)，在 FP8 (E4M3) 精度下为 27 GB，在 IN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

Qwen3-27B 在 BF16 精度下的权重文件大小为 54 GB (27e9 * 2 bytes)，在 FP8 (E4M3) 精度下为 27 GB，在 INT8 精度下为 27 GB，在 INT4 (AWQ) 精度下为 13.5 GB；量化精度直接影响 Decode 阶段的显存读取量

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重文件大小为 54 GB (27e9 * 2 bytes)，在 FP8 (E4M3) 精度下为 27 GB，在 INT8 精度下为 27 GB，在 INT4 (AWQ) 精度下为 13.5 GB；量化精度直接影响 Decode 阶段的显存读取量

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)下为54GB，FP8/INT8(1字节)下为27GB，INT4(0.5字节)下为13.5GB，计算准确且符合显存占用原理。

## Search Query

Qwen3-27B model size BF16 FP8 INT4 file size
