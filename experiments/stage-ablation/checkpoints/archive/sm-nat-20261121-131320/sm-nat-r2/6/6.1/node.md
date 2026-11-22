# N48: Pareto(β=0.9)热度分布下，前 k% 对象占据的请求流量比例公式为 R_req(k) = 1 - k^(1-β)，例如前 1% 对象占据 1 - 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Pareto(β=0.9)热度分布下，前 k% 对象占据的请求流量比例公式为 R_req(k) = 1 - k^(1-β)，例如前 1% 对象占据 1 - 0.01^(0.1) ≈ 63.1% 的请求流量。

## Corrected Claim

Pareto(β=0.9)热度分布下，前 k% 对象占据的请求流量比例公式为 R_req(k) = 1 - k^(1-β)，例如前 1% 对象占据 1 - 0.01^(0.1) ≈ 63.1% 的请求流量。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积分布函数推导正确，数值计算 1 - 0.01^0.1 ≈ 0.631 准确无误。
