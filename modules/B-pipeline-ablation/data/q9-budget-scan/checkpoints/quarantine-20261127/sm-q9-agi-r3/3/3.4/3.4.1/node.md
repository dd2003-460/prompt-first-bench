# N57: PP=2 (Pipeline Parallelism) 下的流水线气泡 (Bubble) 占比公式为 Bubble_Ratio = (p-1)/m，其中 p=2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

PP=2 (Pipeline Parallelism) 下的流水线气泡 (Bubble) 占比公式为 Bubble_Ratio = (p-1)/m，其中 p=2 (stages), m=batch_size。当 m=1 时 Bubble_Ratio=50%，导致理论吞吐减半；需推导达到 90% 流水线利用率所需的最小 batch_size m_min >= 10。

## Corrected Claim

PP=2 (Pipeline Parallelism) 下的流水线气泡 (Bubble) 占比公式为 Bubble_Ratio = (p-1)/m，其中 p=2 (stages), m=batch_size。当 m=1 时 Bubble_Ratio=50%，导致理论吞吐减半；需推导达到 90% 流水线利用率所需的最小 batch_size m_min >= 10。

## Evidence

先验知识/题面给定，逻辑校验通过：流水线气泡占比公式 (p-1)/m 符合标准流水线并行理论，代入 p=2, m=1 得 50%，推导 m>=10 达到 90% 利用率（1-1/m >= 0.9 => m>=10）数学逻辑自洽。
