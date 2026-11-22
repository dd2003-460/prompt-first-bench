# N264: 多卡方案中单卡故障对系统可用性的影响：在2x4090 Tensor Parallel方案中，单卡故障导致整个推理任务中断，系统可用性 = 1 - (1 - (1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

多卡方案中单卡故障对系统可用性的影响：在2x4090 Tensor Parallel方案中，单卡故障导致整个推理任务中断，系统可用性 = 1 - (1 - (1-AFR_gpu)^2)；若单卡AFR为7.5%，系统年故障率约为14.6%，远高于单卡数据中心卡的2%。

## Corrected Claim

多卡方案中单卡故障对系统可用性的影响：在2x4090 Tensor Parallel方案中，单卡故障导致整个推理任务中断，系统可用性 = 1 - (1 - (1-AFR_gpu)^2)；若单卡AFR为7.5%，系统年故障率约为14.6%，远高于单卡数据中心卡的2%。

## Evidence

先验知识/题面给定，逻辑校验通过：Tensor Parallel架构下单卡故障导致整体中断，系统可用性公式推导正确（1-(1-0.925)^2 ≈ 0.854，故障率14.6%），且符合高故障率消费级显卡在关键任务中风险远高于数据中心卡的工程常识。

## Search Query

multi-GPU tensor parallel single point of failure availability calculation
