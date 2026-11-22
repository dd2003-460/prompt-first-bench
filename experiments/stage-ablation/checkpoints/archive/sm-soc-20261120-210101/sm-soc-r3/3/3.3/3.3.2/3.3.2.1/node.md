# N244: 共享随机源：曝光分配噪声 σ_exposure，源于平台推荐算法中探索-利用平衡（Epsilon-Greedy）的随机探索项及冷启动流量分配的随机扰动，导致同一

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N67

## Claim

共享随机源：曝光分配噪声 σ_exposure，源于平台推荐算法中探索-利用平衡（Epsilon-Greedy）的随机探索项及冷启动流量分配的随机扰动，导致同一商品在不同时间窗口的Impression存在不可预测的方差 Var(Impression) = σ_exposure²。

## Corrected Claim

共享随机源：曝光分配噪声 σ_exposure，源于平台推荐算法中探索-利用平衡（Epsilon-Greedy）的随机探索项及冷启动流量分配的随机扰动，导致同一商品在不同时间窗口的Impression存在不可预测的方差 Var(Impression) = σ_exposure²。

## Evidence

先验知识/题面给定，逻辑校验通过：Epsilon-Greedy算法的随机探索项及冷启动机制确实会引入曝光分配的随机性，导致同一商品在不同时间窗口的曝光量存在方差，该描述符合推荐系统基本原理。
