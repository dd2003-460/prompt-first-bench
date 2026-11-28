# N183: 工作点3（低并发超长序列）：Batch_Size=1, Seq_Len=262144时，T_memory极大，预计Tokens/s/Worker≈2-3，显存接

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点3（低并发超长序列）：Batch_Size=1, Seq_Len=262144时，T_memory极大，预计Tokens/s/Worker≈2-3，显存接近上限，适合单次深度推理但吞吐量极低，需配合推测解码提升有效速率

## Corrected Claim

工作点3（低并发超长序列）：Batch_Size=1, Seq_Len=262144时，T_memory极大，预计Tokens/s/Worker≈2-3，显存接近上限，适合单次深度推理但吞吐量极低，需配合推测解码提升有效速率

## Evidence

先验知识/题面给定，逻辑校验通过：Seq_Len=262144时KV Cache显存占用极大，Batch_Size=1下受限于内存带宽和计算延迟，Tokens/s/Worker在2-3量级符合大模型长序列推理的物理直觉，推测解码建议合理。
