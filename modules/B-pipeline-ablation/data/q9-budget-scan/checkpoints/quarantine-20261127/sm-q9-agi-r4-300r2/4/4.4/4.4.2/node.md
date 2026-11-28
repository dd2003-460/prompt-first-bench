# N72: 云端 API 速率限制导致的排队延迟 T_queue = N_requests / (rate_limit * (1 - utilization))，若 rat

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20

## Claim

云端 API 速率限制导致的排队延迟 T_queue = N_requests / (rate_limit * (1 - utilization))，若 rate_limit = 100 req/min, utilization = 0.8, 则 T_queue ≈ 5s/request，需纳入调度模型

## Corrected Claim

云端 API 速率限制下的平均排队延迟 T_queue 近似遵循 M/M/1 排队模型：T_queue ≈ ρ / (μ * (1 - ρ))，其中 μ 为服务速率（req/s），ρ 为利用率。若 μ = 100 req/min ≈ 1.67 req/s, ρ = 0.8，则 T_queue ≈ 0.8 / (1.67 * 0.2) ≈ 2.4s/request。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾且未覆盖父节点核心公式。1. 矛盾：父节点基于利用率推导 T_queue≈5s，而子节点1基于 M/M/1 理论计算 W_q≈2.4s，两者数值差异巨大且未解释（如服务时间分布假设不同），导致结论冲突。2. 缺失：父节点强调将 T_queue '纳入调度模型'，但两个子节点仅分析了延迟成因（排队论 vs TPM限制），完全未涉及如何将这些延迟参数整合进具体的调度算法或策略中。）
