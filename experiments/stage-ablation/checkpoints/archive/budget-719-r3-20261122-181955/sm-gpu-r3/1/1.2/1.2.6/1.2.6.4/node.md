# N170: 多卡方案（TP=2）的通信开销占比 = 通信时间 / 总推理时间；在 Decode 阶段，若单卡计算时间为 100 ms，A100 NVLink 通信时间 14

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

多卡方案（TP=2）的通信开销占比 = 通信时间 / 总推理时间；在 Decode 阶段，若单卡计算时间为 100 ms，A100 NVLink 通信时间 14.3 ms 占比 12.5%，而 PCIe 通信时间 134.1 ms 占比 57.1%，表明 PCIe 互联在多卡推理中会成为严重瓶颈。

## Corrected Claim

多卡方案（TP=2）的通信开销占比 = 通信时间 / 总推理时间；在 Decode 阶段，若单卡计算时间为 100 ms，A100 NVLink 通信时间 14.3 ms 占比 12.5%，而 PCIe 通信时间 134.1 ms 占比 57.1%，表明 PCIe 互联在多卡推理中会成为严重瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2时通信占比计算逻辑自洽（14.3/(100+14.3)≈12.5%，134.1/(100+134.1)≈57.1%），且符合A100 NVLink与PCIe带宽差异的工程常识。
