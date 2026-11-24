# N321: 混合策略最坏P99值计算：P99_Hybrid_Worst = max(Self_POP_P99_Failure, Cloud_Fallback_P99_Spi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N124

## Claim

混合策略最坏P99值计算：P99_Hybrid_Worst = max(Self_POP_P99_Failure, Cloud_Fallback_P99_Spike)。若Self_POP_P99_Failure=500ms（回源），Cloud_Fallback_P99_Spike=132ms，则P99_Hybrid_Worst=500ms；但若流量快速切换至公有云且公有云处理得当，P99_Hybrid_Worst≈150-200ms，需取决于切换速度与公有云容量余量。

## Corrected Claim

混合策略最坏P99值计算：P99_Hybrid_Worst = max(Self_POP_P99_Failure, Cloud_Fallback_P99_Spike)。若Self_POP_P99_Failure=500ms（回源），Cloud_Fallback_P99_Spike=132ms，则P99_Hybrid_Worst=500ms；但若流量快速切换至公有云且公有云处理得当，P99_Hybrid_Worst≈150-200ms，需取决于切换速度与公有云容量余量。

## Evidence

先验知识/题面给定，逻辑校验通过：混合策略的最坏情况P99确实由各路径最坏值取最大值决定，数值代入计算正确（max(500, 132)=500），且对动态切换场景的定性描述符合系统架构逻辑。
