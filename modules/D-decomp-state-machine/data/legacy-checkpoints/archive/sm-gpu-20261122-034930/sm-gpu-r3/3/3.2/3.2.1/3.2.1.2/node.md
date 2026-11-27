# N263: 功耗-吞吐非线性关系：在 Memory-bound 阶段（KV Cache 读取为主），GPU 功耗与吞吐量近似线性相关（效率恒定）；但在 Compute-bo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

功耗-吞吐非线性关系：在 Memory-bound 阶段（KV Cache 读取为主），GPU 功耗与吞吐量近似线性相关（效率恒定）；但在 Compute-bound 阶段（Prefill 或长序列 Attention），功耗增加但吞吐量增幅递减，导致单位 token 能耗（J/token）上升，因此在计算 TCO 时应使用加权平均功耗而非峰值 TDP。

## Corrected Claim

功耗-吞吐非线性关系：在 Memory-bound 阶段（KV Cache 读取为主），GPU 功耗与吞吐量近似线性相关（效率恒定）；但在 Compute-bound 阶段（Prefill 或长序列 Attention），功耗增加但吞吐量增幅递减，导致单位 token 能耗（J/token）上升，因此在计算 TCO 时应使用加权平均功耗而非峰值 TDP。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU energy efficiency tokens per joule LLM inference
