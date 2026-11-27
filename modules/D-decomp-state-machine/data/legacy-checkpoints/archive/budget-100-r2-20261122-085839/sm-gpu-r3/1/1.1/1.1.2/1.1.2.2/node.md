# N126: W4 量化方案中，每个 Group 所需的额外显存开销 = (Group_Size / Group_Size) * Bytes_per_Scale + (Gro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

W4 量化方案中，每个 Group 所需的额外显存开销 = (Group_Size / Group_Size) * Bytes_per_Scale + (Group_Size / Group_Size) * Bytes_per_Zero，其中 Bytes_per_Scale 通常为 2 (FP16) 或 1 (FP8/INT8)，Bytes_per_Zero 通常为 2 (FP16) 或 1 (FP8/INT8)。若 Group Size=128 且使用 FP16 Scale/Zero，则每组额外 4 Bytes。

## Corrected Claim

W4 量化方案中，每个 Group 所需的额外显存开销 = (Group_Size / Group_Size) * Bytes_per_Scale + (Group_Size / Group_Size) * Bytes_per_Zero，其中 Bytes_per_Scale 通常为 2 (FP16) 或 1 (FP8/INT8)，Bytes_per_Zero 通常为 2 (FP16) 或 1 (FP8/INT8)。若 Group Size=128 且使用 FP16 Scale/Zero，则每组额外 4 Bytes。

## Evidence

先验知识/题面给定，逻辑校验通过：W4量化中每组需存储1个Scale和1个Zero，若均为FP16（2字节），则额外开销为2+2=4字节，公式推导与数值计算自洽。

## Search Query

W4 quantization scale zero point storage overhead bytes
