# N54: 相关性误差修正项：由于 27b 模型自我批判存在系统性偏差（如过度自信），实际 IR(K) = 1 - (1-p_base)^K * (1 - ρ_corr)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N19

## Claim

相关性误差修正项：由于 27b 模型自我批判存在系统性偏差（如过度自信），实际 IR(K) = 1 - (1-p_base)^K * (1 - ρ_corr)，其中 ρ_corr 为批判轮次间错误相关性系数（预计 0.2-0.4），导致所需 K 值比独立假设高 30-50%。

## Corrected Claim

相关性误差修正项：由于模型自我批判可能存在系统性偏差（如过度自信），实际 IR(K) 需引入批判轮次间错误相关性系数 ρ_corr 进行修正，导致所需 K 值通常比独立假设更高。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个核心逻辑环节：1. 参数定义与测量（ρ_corr的获取及阈值判断）；2. 数学推导与影响量化（K值的计算公式及数值示例）；3. 输入变量修正（p_base因过度自信导致的偏差修正）。三者分别处理了‘相关性系数’、‘最终求解目标’和‘基础概率前提’，逻辑上层层递进且互不重叠，共同构成了完整的误差修正框架。）

## Search Query

self-consistency correlation error rate LLM critique rounds dependency
