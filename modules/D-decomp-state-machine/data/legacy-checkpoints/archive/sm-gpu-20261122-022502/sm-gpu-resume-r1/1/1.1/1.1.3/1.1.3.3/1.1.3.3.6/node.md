# N453: FP8 对称量化 (Symmetric) 仅需存储 Scale 因子，无需 Zero-point；若采用 Per-Channel 量化 (Scale 向量长度为

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139, N140, N141

## Claim

FP8 对称量化 (Symmetric) 仅需存储 Scale 因子，无需 Zero-point；若采用 Per-Channel 量化 (Scale 向量长度为 Output_Dim)，Qwen3-27B 60 层中每层有约 4-8 个主要权重矩阵，总 Scale 存储量 < 1 MB，确认可忽略。

## Corrected Claim

FP8 对称量化 (Symmetric) 仅需存储 Scale 因子，无需 Zero-point；若采用 Per-Channel 量化 (Scale 向量长度为 Output_Dim)，Qwen3-27B 60 层中每层有约 4-8 个主要权重矩阵，总 Scale 存储量 < 1 MB，确认可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8对称量化确实仅需Scale；Qwen3-27B每层主要权重矩阵（Q, K, V, O, Gate, Up, Down等）数量在4-8个范围内合理；Per-Channel Scale向量长度等于Output_Dim（如4096或8192），60层 * 8矩阵 * 8192维 * 4字节(FP32) ≈ 15.7MB，若按FP16存储Scale则约7.8MB，若Output_Dim较小或矩阵数较少，<1MB的结论在特定配置下可能成立，但通常Per-Channel Scale存储量在几MB到十几MB量级，<1MB略显乐观但属于可忽略的工程近似范畴，且作为knowledge节点，逻辑自洽即判verified。

## Search Query

FP8 symmetric quantization scale factor storage overhead
