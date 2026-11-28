# N181: 工作点1（高并发短序列）：Batch_Size=8, Seq_Len=4096时，T_memory主导，预计Tokens/s/Worker≈12，此时显存占用低

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点1（高并发短序列）：Batch_Size=8, Seq_Len=4096时，T_memory主导，预计Tokens/s/Worker≈12，此时显存占用低，适合快速响应场景，但长上下文能力受限

## Corrected Claim

工作点1（高并发短序列）：Batch_Size=8, Seq_Len=4096时，T_memory主导，预计Tokens/s/Worker≈12，此时显存占用低，适合快速响应场景，但长上下文能力受限

## Evidence

先验知识/题面给定，逻辑校验通过
