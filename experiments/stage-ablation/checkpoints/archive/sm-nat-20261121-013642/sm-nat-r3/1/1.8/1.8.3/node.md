# N55: T_residence 的数值估算：基于 C=128GB 和总请求字节率 R_bytes=50,000,000 * E[size]，假设 E[size]=10K

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

T_residence 的数值估算：基于 C=128GB 和总请求字节率 R_bytes=50,000,000 * E[size]，假设 E[size]=10KB，则 R_bytes≈500GB/day，T_residence ≈ 128GB / (500GB/day * (1-H_LRU))，若 H_LRU=0.7，则 T_residence≈0.85天

## Corrected Claim

T_residence 的数值估算：基于 C=128GB 和总请求字节率 R_bytes=50,000,000 * E[size]，假设 E[size]=10KB，则 R_bytes≈500GB/day，T_residence ≈ 128GB / (500GB/day * (1-H_LRU))，若 H_LRU=0.7，则 T_residence≈0.85天

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点本质上是同一公式 T_residence = C / (R_bytes * (1-H)) 在不同 H 值下的实例化，存在高度冗余；且逻辑矛盾：通常低命中率（高Miss）意味着对象更频繁地被替换，驻留时间应更短，但节点3称 H=0.5 时 T=0.51天比 H=0.7 时的 0.85天短，这与‘低命中率/高驻留’的标题描述（高驻留）直接矛盾，实际上低命中率对应短驻留。此外，父节点仅给出一个估算，子节点却扩展为三个工作点，未覆盖‘参数敏感性’或‘误差范围’等关键方面，且将参数扫描伪装成正交分支。）
