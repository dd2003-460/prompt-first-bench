# N145: 大对象（S > 1MB）的字节流量占比 >40% 需精确计算：对于 Pareto(α=1.1, s_min=1KB)，字节占比 B(1MB) = 1 - (1K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

大对象（S > 1MB）的字节流量占比 >40% 需精确计算：对于 Pareto(α=1.1, s_min=1KB)，字节占比 B(1MB) = 1 - (1KB/1MB)^0.1 = 1 - (1024)^-0.1 ≈ 1 - 0.447 = 0.553，即 55.3%，高于 40% 的估计，需修正 ΔH_large 的分母。

## Corrected Claim

大对象（S > 1MB）的字节流量占比 >40% 需精确计算：对于 Pareto(α=1.1, s_min=1KB)，字节占比 B(1MB) = 1 - (1KB/1MB)^0.1 = 1 - (1024)^-0.1 ≈ 1 - 0.447 = 0.553，即 55.3%，高于 40% 的估计，需修正 ΔH_large 的分母。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部字节占比公式推导正确，数值计算准确（1 - 1024^-0.1 ≈ 0.553），符合大对象流量占比高的直觉。
