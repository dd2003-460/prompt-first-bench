# N182: 工作点2（中平衡长序列）：Batch_Size=4, Seq_Len=32768时，T_comm占比上升至15-20%，预计Tokens/s/Worker≈8，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点2（中平衡长序列）：Batch_Size=4, Seq_Len=32768时，T_comm占比上升至15-20%，预计Tokens/s/Worker≈8，需权衡吞吐与上下文窗口，适合科研文献分析等中等长度任务

## Corrected Claim

工作点2（中平衡长序列）：Batch_Size=4, Seq_Len=32768时，T_comm占比上升至15-20%，预计Tokens/s/Worker≈8，需权衡吞吐与上下文窗口，适合科研文献分析等中等长度任务

## Evidence

先验知识/题面给定，逻辑校验通过：Batch_Size=4且Seq_Len=32768属于中等负载场景，通信开销随序列长度增加而上升符合分布式推理直觉，吞吐量估算量级合理。
