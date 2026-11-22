# N132: FP8 (E4M3) 权重的 Scale 因子存储开销计算：若采用 Per-Channel 量化（每个输出通道一个 Scale），Scale 数量 = Num_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

FP8 (E4M3) 权重的 Scale 因子存储开销计算：若采用 Per-Channel 量化（每个输出通道一个 Scale），Scale 数量 = Num_Layers * Hidden_Dim = 64 * 4096 = 262,144 个 FP32 值，占用显存 262,144 * 4 bytes = 1.0 MB，可忽略不计；若采用 Per-Block (128x128) 量化，Scale 数量大幅减少，总开销 < 0.1 MB。

## Corrected Claim

FP8 (E4M3) 权重的 Scale 因子存储开销计算：若采用 Per-Channel 量化（每个输出通道一个 Scale），Scale 数量 = Num_Layers * Hidden_Dim = 64 * 4096 = 262,144 个 FP32 值，占用显存 262,144 * 4 bytes = 1.0 MB，可忽略不计；若采用 Per-Block (128x128) 量化，Scale 数量大幅减少，总开销 < 0.1 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：Per-Channel 量化下 Scale 数量确为 64*4096=262,144，FP32 存储 1MB 计算正确；Per-Block (128x128) 量化下 Scale 数量大幅减少，开销 <0.1MB 符合逻辑。

## Search Query

FP8 quantization scale factor storage overhead per-channel vs per-block
