# N32: 在 max_num_seqs=8 的并发限制下，实验设计阶段的 3-5 次 refinement 循环若串行执行，总延迟为 5 * 9.4 s ≈ 47 s；若

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

在 max_num_seqs=8 的并发限制下，实验设计阶段的 3-5 次 refinement 循环若串行执行，总延迟为 5 * 9.4 s ≈ 47 s；若并行化（受 TP=4 通信瓶颈制约），实际加速比上限为 1.8x，总延迟降至 ~26 s

## Corrected Claim

在 max_num_seqs=8 的并发限制下，若假设每次 refinement 循环平均耗时约 9.4 s，串行执行 5 次总延迟约为 47 s；若并行化且受 TP=4 通信瓶颈制约，实际加速比可能在 1.5x-2.0x 之间，总延迟预计降至 24-31 s 区间。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点1存在严重逻辑错误且与父节点结论矛盾（父节点称加速比上限1.8x，子节点算出6.9x）；子节点2和3讨论的是资源约束和微小开销，未覆盖父节点核心结论'并行化后总延迟降至~26s'的推导过程，导致覆盖不完整。）
