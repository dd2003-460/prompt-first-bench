# N501: 工作点C（TP=1单卡大模型分片）：Model_Layers=48, TP_Degree=1时，T_comm ≈ 0ms（无跨卡通信），但需激活Offload或

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

工作点C（TP=1单卡大模型分片）：Model_Layers=48, TP_Degree=1时，T_comm ≈ 0ms（无跨卡通信），但需激活Offload或更大显存；在16GB显存限制下不可行，揭示硬件约束下的可行性边界

## Corrected Claim

工作点C（TP=1单卡大模型分片）：Model_Layers=48, TP_Degree=1时，T_comm ≈ 0ms（无跨卡通信），但需激活Offload或更大显存；在16GB显存限制下不可行，揭示硬件约束下的可行性边界

## Evidence

先验知识/题面给定，逻辑校验通过：TP=1意味着无张量并行通信开销，T_comm≈0符合定义；48层大模型在16GB显存下通常因权重+激活值溢出而不可行，需Offload，逻辑自洽。
