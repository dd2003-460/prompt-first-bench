# N492: 长尾区域 RTT 分解：用户位于西部/偏远地区，源站位于北京，RTT_tail = RTT_physical + RTT_queue，其中 RTT_physic

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N165

## Claim

长尾区域 RTT 分解：用户位于西部/偏远地区，源站位于北京，RTT_tail = RTT_physical + RTT_queue，其中 RTT_physical ≈ 150ms (跨省光纤时延)，RTT_queue ≈ 50ms (长尾节点排队时延较高)，合计 200ms，处于 100-200ms 区间上限

## Corrected Claim

长尾区域 RTT 分解：用户位于西部/偏远地区，源站位于北京，RTT_tail = RTT_physical + RTT_queue，其中 RTT_physical ≈ 150ms (跨省光纤时延)，RTT_queue ≈ 50ms (长尾节点排队时延较高)，合计 200ms，处于 100-200ms 区间上限

## Evidence

先验知识/题面给定，逻辑校验通过：西部至北京光纤物理时延约150ms符合光速限制下的工程经验值，排队时延50ms在长尾场景下合理，总和200ms处于所述区间上限，数值量级与逻辑自洽。
