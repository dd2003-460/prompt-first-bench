# N118: 年电力成本公式假设 24/7 满载运行，但实际推理负载利用率（Duty Cycle）通常为 10%-50%，需乘以实际利用率系数（如 0.3）得到真实年电力成本

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36, N37, N38

## Claim

年电力成本公式假设 24/7 满载运行，但实际推理负载利用率（Duty Cycle）通常为 10%-50%，需乘以实际利用率系数（如 0.3）得到真实年电力成本，否则高估 2-5 倍

## Corrected Claim

年电力成本公式假设 24/7 满载运行，但实际推理负载利用率（Duty Cycle）通常为 10%-50%，需乘以实际利用率系数（如 0.3）得到真实年电力成本，否则高估 2-5 倍

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个核心要素：1. 实际利用率的场景分解（Duty Cycle定义）；2. 修正后的通用计算公式（公式结构）；3. 具体数值验证与误差分析（实例证明）。三者逻辑层层递进，互不重叠，且完整覆盖了从定义、公式到验证的全过程，无冗余。）

## Search Query

GPU inference duty cycle typical utilization
