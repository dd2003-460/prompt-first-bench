# N189: 一线城市（北上广深）用户到最近POP的距离 d_tier1 ≈ 50-100 km，对应单程传播延迟 d/c ≈ 0.25-0.5 ms，RTT_prop ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

一线城市（北上广深）用户到最近POP的距离 d_tier1 ≈ 50-100 km，对应单程传播延迟 d/c ≈ 0.25-0.5 ms，RTT_prop ≈ 0.5-1 ms，属于低延迟覆盖区

## Corrected Claim

一线城市（北上广深）用户到最近POP的距离 d_tier1 ≈ 50-100 km，对应单程传播延迟 d/c ≈ 0.25-0.5 ms，RTT_prop ≈ 0.5-1 ms，属于低延迟覆盖区

## Evidence

先验知识/题面给定，逻辑校验通过：光速 c≈3×10^8 m/s，距离 50-100 km 对应单程延迟 0.167-0.333 ms，RTT 0.33-0.67 ms，与陈述中的 0.25-0.5 ms 及 0.5-1 ms 量级基本一致（考虑了光纤折射率 n≈1.5 后延迟约为真空的 1.5 倍，即单程 0.25-0.5 ms，RTT 0.5-1 ms，完全吻合）；一线城市 POP 分布密度高，50-100 km 覆盖范围符合工程常识。

## Search Query

CDN POP location major Chinese cities distance latency
