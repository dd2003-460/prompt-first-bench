# N62: 自建 POP 场景下，核心区域（华东/华南/华北）用户到最近 POP 的平均物理距离 $d_{self}$ 约为 50-150 km，导致单向传播延迟 $L_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

自建 POP 场景下，核心区域（华东/华南/华北）用户到最近 POP 的平均物理距离 $d_{self}$ 约为 50-150 km，导致单向传播延迟 $L_{prop, self} = d_{self} / (2 \times 10^8) \times 10^3 \approx 0.25-0.75$ ms，往返 RTT 物理下限约为 0.5-1.5 ms。

## Corrected Claim

自建 POP 场景下，核心区域（华东/华南/华北）用户到最近 POP 的平均物理距离 $d_{self}$ 约为 50-150 km，导致单向传播延迟 $L_{prop, self} = d_{self} / (2 \times 10^8) \times 10^3 \approx 0.25-0.75$ ms，往返 RTT 物理下限约为 0.5-1.5 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：距离50-150km对应传播延迟0.25-0.75ms（基于光速2e8 m/s），RTT为单向两倍即0.5-1.5ms，量纲与数值均自洽。
