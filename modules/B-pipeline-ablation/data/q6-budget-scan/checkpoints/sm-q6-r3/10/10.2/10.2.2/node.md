# N378: 在 $s_{avg}=5\text{MB}$ 场景下，单流传输时间 $T_{transfer}$ 的量化计算：假设用户端下行带宽 $B_{link} = 10 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

在 $s_{avg}=5\text{MB}$ 场景下，单流传输时间 $T_{transfer}$ 的量化计算：假设用户端下行带宽 $B_{link} = 10 \text{ Mbps}$，则 $T_{transfer} = s_{avg} / B_{link} = (5 \times 1024 \text{ KB}) / (10/8 \text{ KB/ms}) = 5120 / 1.25 = 4096 \text{ ms}$，比 $s_{avg}=1\text{MB}$ 场景增加 4 倍（5 倍大小，但带宽不变）。

## Corrected Claim

在 $s_{avg}=5\text{MB}$ 场景下，单流传输时间 $T_{transfer}$ 的量化计算：假设用户端下行带宽 $B_{link} = 10 \text{ Mbps}$，则 $T_{transfer} = s_{avg} / B_{link} = (5 \times 1024 \text{ KB}) / (10/8 \text{ KB/ms}) = 5120 / 1.25 = 4096 \text{ ms}$，比 $s_{avg}=1\text{MB}$ 场景增加 4 倍（5 倍大小，但带宽不变）。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（10 Mbps = 1.25 MB/ms），计算过程 5MB / 1.25MB/ms = 4ms 错误，应为 5 * 1024 KB / (10/8 * 1000/1000 KB/ms) -> 10 Mbps = 1.25 MB/s = 1.25 KB/ms 是错误的，10 Mbps = 1.25 MB/s。1 MB = 1024 KB。10 Mbps = 10,000,000 bits/s = 1,250,000 bytes/s = 1250 KB/s。题目中写的是 10/8 KB/ms = 1.25 KB/ms = 1250 KB/s。单位换算正确。5 MB = 5120 KB。5120 / 1.25 = 4096 ms。逻辑自洽。
