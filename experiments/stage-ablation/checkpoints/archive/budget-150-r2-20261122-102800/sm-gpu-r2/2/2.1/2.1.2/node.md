# N76: 量化对 Embedding 层的影响：通常 Embedding 层保持 BF16 或 FP16 以避免查表精度损失，若全模型 INT8 量化，Embedding

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

量化对 Embedding 层的影响：通常 Embedding 层保持 BF16 或 FP16 以避免查表精度损失，若全模型 INT8 量化，Embedding 层显存占用 = Vocab_size * Hidden_size * 2 bytes，而非 1 byte。

## Corrected Claim

量化对 Embedding 层的影响：通常 Embedding 层保持 BF16 或 FP16 以避免查表精度损失，若全模型 INT8 量化，Embedding 层显存占用 = Vocab_size * Hidden_size * 2 bytes，而非 1 byte。

## Evidence

先验知识/题面给定，逻辑校验通过：Embedding层通常保持高精度（BF16/FP16）以避免查表误差，其显存占用计算符合 Vocab_size * Hidden_size * 2 bytes 的量纲与数值逻辑。
