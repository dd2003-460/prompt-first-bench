# N51: FP8 (E4M3) 量化下的额外开销：Scale 因子通常每 128 或 4096 个元素存储一个 FP32/FP16 标量，对于 27B 模型，Scale 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

FP8 (E4M3) 量化下的额外开销：Scale 因子通常每 128 或 4096 个元素存储一个 FP32/FP16 标量，对于 27B 模型，Scale 开销约为 (27 * 10^9 / 128) * 4 bytes ≈ 850 MB，加上 Bias 等，总占用约为 27.5-28.0 GB

## Corrected Claim

FP8 (E4M3) 量化下的额外开销：Scale 因子通常每 128 或 4096 个元素存储一个 FP32/FP16 标量，对于 27B 模型，Scale 开销约为 (27 * 10^9 / 128) * 4 bytes ≈ 850 MB，加上 Bias 等，总占用约为 27.5-28.0 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数下，每128元素存1个FP32 Scale，开销计算为 (27e9 / 128) * 4 ≈ 843.75 MB，与陈述中的850 MB量级一致；总占用27.5-28.0 GB符合FP8权重(27GB)加上Scale及少量Bias/其他开销的合理范围。

## Search Query

FP8 E4M3 quantization scale factor overhead size 27B model
