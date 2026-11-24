# N183: 在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_base = 2 * 1.0ms + 2.5ms = 4.5ms，相比基准点增加 1.5ms 的纯物理延迟开销。

## Corrected Claim

在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_base = 2 * 1.0ms + 2.5ms = 4.5ms，相比基准点增加 1.5ms 的纯物理延迟开销。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000km/s，200km/200,000km/s=1ms，计算无误；RTT公式逻辑自洽。

## Search Query

long distance fiber optic latency 200km
