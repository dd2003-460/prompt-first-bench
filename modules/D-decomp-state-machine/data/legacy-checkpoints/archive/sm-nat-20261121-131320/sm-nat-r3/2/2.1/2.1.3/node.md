# N30: 低频大对象带宽占比 B_tail 的计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

低频大对象带宽占比 B_tail 的计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / (Σ_{all} f_i * S_i)；该值代表 LRU 因驱逐这些对象而损失的潜在命中率，是 ΔH_max 的上界来源之一；f_threshold 定义为使得累计请求频率达到 95% 的倒数排名对应的频率值。

## Corrected Claim

低频大对象带宽占比 B_tail 的计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / (Σ_{all} f_i * S_i)；该值代表 LRU 因驱逐这些对象而损失的潜在命中率，是 ΔH_max 的上界来源之一；f_threshold 定义为使得累计请求频率达到 95% 的倒数排名对应的频率值。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中的三个不同维度：1. 核心数值计算（What/How to calculate）；2. 理论意义与验证（Why/Interpretation）；3. 参数鲁棒性分析（Sensitivity/Robustness）。三者关注点明确分离，无逻辑重叠或矛盾，且共同覆盖了定义、应用和稳定性分析，符合学术分解的完备性与正交性要求。）
