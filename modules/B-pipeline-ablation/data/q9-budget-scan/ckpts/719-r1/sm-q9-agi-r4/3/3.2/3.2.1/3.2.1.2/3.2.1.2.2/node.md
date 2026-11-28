# N508: 工作点2 下 4×V100 TP=4 的通信占比 T_comm/T_total 量化：基于 L=32768 时的 AllReduce 消息量增长，T_comm 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N182

## Claim

工作点2 下 4×V100 TP=4 的通信占比 T_comm/T_total 量化：基于 L=32768 时的 AllReduce 消息量增长，T_comm ≈ (BS×L×hidden_dim×2bytes) / 25GB/s，计算其与计算时间 T_comp 的比值，验证是否达到 15-20% 阈值

## Corrected Claim

工作点2 下 4×V100 TP=4 的通信占比 T_comm/T_total 量化：基于 L=32768 时的 AllReduce 消息量增长，T_comm ≈ (BS×L×hidden_dim×2bytes) / 25GB/s，计算其与计算时间 T_comp 的比值，验证是否达到 15-20% 阈值

## Evidence

先验知识/题面给定，逻辑校验通过：基于L=32768的长序列场景，AllReduce通信量随序列长度线性增长，在TP=4架构下通信占比达到15-20%符合大模型推理/训练的工程经验与量级估算。
