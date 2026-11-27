# N173: 均衡稳定性临界噪声方差 σ²_critical 的计算：当 P(U_buyer > 0) = 0.5 时，E[U_buyer] = 0，故 σ²_critica

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

均衡稳定性临界噪声方差 σ²_critical 的计算：当 P(U_buyer > 0) = 0.5 时，E[U_buyer] = 0，故 σ²_critical 无解析解，需通过蒙特卡洛模拟确定；若 E[U_buyer]=0.05, Var[U_buyer]=0.0025，则 P(U_buyer > 0) ≈ Φ(0.05/√0.0025) = Φ(1.0) ≈ 0.841 > 0.5，均衡稳定

## Corrected Claim

均衡稳定性临界噪声方差 σ²_critical 的计算：当 P(U_buyer > 0) = 0.5 时，E[U_buyer] = 0，故 σ²_critical 无解析解，需通过蒙特卡洛模拟确定；若 E[U_buyer]=0.05, Var[U_buyer]=0.0025，则 P(U_buyer > 0) ≈ Φ(0.05/√0.0025) = Φ(1.0) ≈ 0.841 > 0.5，均衡稳定

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布下 P(X>0)=Φ(μ/σ) 的推导及数值计算（Φ(1)≈0.841）均符合统计学第一性原理，且 source 为 knowledge，无需外部来源支持。
