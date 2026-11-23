# N62: 自建 POP 场景下，核心区域（华东/华南/华北）用户到最近 POP 的平均物理距离 $d_{self}$ 约为 50-150 km，导致单向传播延迟 $L_{

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

自建 POP 场景下，核心区域（华东/华南/华北）用户到最近 POP 的平均物理距离 $d_{self}$ 约为 50-150 km，导致单向传播延迟 $L_{prop, self} = d_{self} / (2 \times 10^8) \times 10^3 \approx 0.25-0.75$ ms，往返 RTT 物理下限约为 0.5-1.5 ms。

## Corrected Claim

自建 POP 场景下，核心区域（华东/华南/华北）用户到最近 POP 的平均物理距离 $d_{self}$ 约为 50-150 km，导致单向传播延迟 $L_{prop, self} = d_{self} / (2 \times 10^8) \times 10^3 \approx 0.25-0.75$ ms，往返 RTT 物理下限约为 0.5-1.5 ms。

## Evidence

父节点级核验未通过：不完备（子节点1和子节点2分别关注平均距离分布和P99尾部延迟，角度正且不重复。但父节点明确给出了'往返RTT物理下限约为0.5-1.5 ms'这一关键结论，而两个子节点仅分别推导了单向传播延迟（0.25-0.75 ms 和 0.75-2.25 ms），均未显式覆盖或推导父节点中的RTT（Round-Trip Time）部分，导致关键指标缺失。）
