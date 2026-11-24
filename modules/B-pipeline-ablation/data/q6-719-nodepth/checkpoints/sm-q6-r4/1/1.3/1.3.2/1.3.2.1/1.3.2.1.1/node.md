# N491: 核心区域 RTT 分解：用户位于北京/上海/广州等一线，源站位于北京，RTT_core = RTT_physical + RTT_queue，其中 RTT_ph

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N165

## Claim

核心区域 RTT 分解：用户位于北京/上海/广州等一线，源站位于北京，RTT_core = RTT_physical + RTT_queue，其中 RTT_physical ≈ 20ms (同城/邻省光纤时延)，RTT_queue ≈ 10ms (边缘节点排队时延)，合计 30ms，处于 30-50ms 区间下限

## Corrected Claim

核心区域 RTT 分解：用户位于北京/上海/广州等一线，源站位于北京，RTT_core = RTT_physical + RTT_queue，其中 RTT_physical ≈ 20ms (同城/邻省光纤时延)，RTT_queue ≈ 10ms (边缘节点排队时延)，合计 30ms，处于 30-50ms 区间下限

## Evidence

先验知识/题面给定，逻辑校验通过：北京/上海/广州至北京的光纤物理时延在20ms量级符合网络工程常识，排队时延10ms为合理估计，总和30ms处于所述区间下限，数值量级与逻辑自洽。
