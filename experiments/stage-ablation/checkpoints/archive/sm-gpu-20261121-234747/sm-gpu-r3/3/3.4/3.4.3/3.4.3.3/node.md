# N278: 4×A100方案的适用域边界量化：在并发用户数N_user ∈ [10, ∞) 且 延迟要求L_req ∈ [0, 100ms] 的条件下，4×A100的TCO

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N99

## Claim

4×A100方案的适用域边界量化：在并发用户数N_user ∈ [10, ∞) 且 延迟要求L_req ∈ [0, 100ms] 的条件下，4×A100的TCO/性能比最优；当N_user < 5 或 L_req > 500ms时，其被2×RTX 3090或1×L40S支配，该边界可通过网格搜索（N_user: 1-50, L_req: 10-1000ms）模拟得出

## Corrected Claim

在特定模型负载和软件栈配置下，通过网格搜索（N_user: 1-50, L_req: 10-1000ms）模拟可得出4×A100方案的适用域边界；一般而言，高并发低延迟场景倾向于多卡高性能方案，而低并发或高延迟容忍场景可能由单卡或双卡消费级/专业级显卡在TCO上占优，具体边界需根据实际基准测试确定。

## Evidence

[质询]该陈述包含具体的硬件性能对比结论（如4×A100在特定并发和延迟下的TCO/性能比最优，以及被2×RTX 3090或1×L40S支配的边界条件），属于经验事实。虽然逻辑框架（网格搜索模拟）合理，但具体的数值边界（N_user < 5, L_req > 500ms）和硬件支配关系缺乏通用物理定律或第一性原理的直接推导支持，且不同模型负载、软件栈优化程度会显著改变这些边界，因此存在将特定场景结论泛化为通用边界的风险。 | 经验事实，逻辑自洽但缺来源支持；source为knowledge，但具体硬件TCO/性能边界属于经验数据，非纯逻辑推导，且无外部来源验证具体数值边界，故降级。

## Search Query

GPU selection decision matrix concurrent users latency TCO dominance
