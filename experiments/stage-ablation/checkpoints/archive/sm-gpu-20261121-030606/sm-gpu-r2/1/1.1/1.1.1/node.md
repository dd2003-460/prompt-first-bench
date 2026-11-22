# N80: Qwen3-27B 在 FP8 精度下的权重占用计算：27B 参数 × 1 byte/param = 27GB，修正 N7 中 13.5GB 的错误（13.5G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 在 FP8 精度下的权重占用计算：27B 参数 × 1 byte/param = 27GB，修正 N7 中 13.5GB 的错误（13.5GB 实为 NVFP4/W4 精度下的占用），此为显存下限推导的基准输入

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重占用计算：27B 参数 × 1 byte/param = 27GB，修正 N7 中 13.5GB 的错误（13.5GB 实为 NVFP4/W4 精度下的占用），此为显存下限推导的基准输入

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8（1字节/参数）下占用27GB，在NVFP4/W4（0.5字节/参数）下占用13.5GB，计算逻辑自洽且符合硬件常识。

## Search Query

Qwen3-27B FP8 weight size calculation
