# N143: 通信开销占比计算公式：Communication_Overhead = (Comm_Time / (Compute_Time + Comm_Time)) × 1

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

通信开销占比计算公式：Communication_Overhead = (Comm_Time / (Compute_Time + Comm_Time)) × 100%，其中 Comm_Time = Comm_Volume / Bandwidth，Compute_Time = FLOPs / (TFLOPS × MFU)，需代入具体硬件参数计算

## Corrected Claim

通信开销占比计算公式：Communication_Overhead = (Comm_Time / (Compute_Time + Comm_Time)) × 100%，其中 Comm_Time = Comm_Volume / Bandwidth，Compute_Time = FLOPs / (TFLOPS × MFU)，需代入具体硬件参数计算

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和子节点3存在概念冲突与冗余：子节点2声称使用FLOPs计算Compute_Time，而子节点3指出在Memory Bound的Decode阶段Compute_Time应基于带宽估算且MFU失效，这直接否定了子节点2的计算逻辑。两者并非正交，而是针对同一变量（Compute_Time）在不同假设下的矛盾描述，且子节点3实质上是子节点2在特定场景下的修正，属于冗余分支。）
