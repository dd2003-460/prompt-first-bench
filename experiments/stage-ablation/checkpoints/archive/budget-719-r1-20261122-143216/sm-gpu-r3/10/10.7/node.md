# N145: Batch Size 对通信开销占比的影响：当 Batch Size 从 1 增加到 8 时，Compute_Time 线性增加而 Comm_Time 保持不变

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Batch Size 对通信开销占比的影响：当 Batch Size 从 1 增加到 8 时，Compute_Time 线性增加而 Comm_Time 保持不变（或小幅增加），导致通信开销占比从 >30% 下降到 <15%，这使得 PCIe 互联在较高 Batch Size 下的劣势显著缓解

## Corrected Claim

Batch Size 对通信开销占比的影响：当 Batch Size 从 1 增加到 8 时，Compute_Time 线性增加而 Comm_Time 保持不变（或小幅增加），导致通信开销占比从 >30% 下降到 <15%，这使得 PCIe 互联在较高 Batch Size 下的劣势显著缓解

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从具体实例验证（Node 1）、底层计算机制（Node 2）和显存资源约束（Node 3）三个不同维度解释父节点。三者分别对应‘现象验证’、‘原因机制’和‘边界条件’，逻辑上互不重叠且共同构成了对父节点完整因果链的覆盖。）
