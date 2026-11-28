# N76: Bootstrap 95% 置信区间计算：基于 n=100 的二项分布样本，通过 10,000 次重抽样计算 H_domain 的置信区间 [CI_lower,

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

Bootstrap 95% 置信区间计算：基于 n=100 的二项分布样本，通过 10,000 次重抽样计算 H_domain 的置信区间 [CI_lower, CI_upper]，若 CI_lower > 15% 则强制启用 RAG Hook，避免小样本波动导致的误判。

## Corrected Claim

Bootstrap 95% 置信区间计算：基于 n=100 的二项分布样本，通过 10,000 次重抽样计算 H_domain 的置信区间 [CI_lower, CI_upper]，若 CI_lower > 15% 则强制启用 RAG Hook，避免小样本波动导致的误判。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应计算实现（Bootstrap方法）、统计验证（Wald近似交叉验证）和决策逻辑（阈值判断），彼此独立且无重叠。它们共同覆盖了父节点中关于‘如何计算’、‘计算结果的可靠性验证’以及‘基于结果的动作’这三个核心维度，且未将单一参数拆分为多个节点，结构清晰合理。）
