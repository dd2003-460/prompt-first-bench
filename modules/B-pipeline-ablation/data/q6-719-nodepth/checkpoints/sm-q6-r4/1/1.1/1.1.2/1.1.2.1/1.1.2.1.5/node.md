# N444: 跨洋链路中路由跳数延迟的典型值：每跳 (undersea cable landing + peering) 增加 5-20ms 处理与排队延迟，典型跨洋路径含 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148, N149, N150

## Claim

跨洋链路中路由跳数延迟的典型值：每跳 (undersea cable landing + peering) 增加 5-20ms 处理与排队延迟，典型跨洋路径含 3-5 跳，总跳数延迟 15-100ms，与传播延迟 (100ms) 同量级，因此光速修正误差 (±17ms) 相对总延迟 (115-200ms) 占比 8-15%，需纳入精度考量。

## Corrected Claim

跨洋链路中路由跳数延迟的典型值：每跳 (undersea cable landing + peering) 增加 5-20ms 处理与排队延迟，典型跨洋路径含 3-5 跳，总跳数延迟 15-100ms，与传播延迟 (100ms) 同量级，因此光速修正误差 (±17ms) 相对总延迟 (115-200ms) 占比 8-15%，需纳入精度考量。

## Evidence

先验知识/题面给定，逻辑校验通过：跨洋链路每跳处理/排队延迟5-20ms及3-5跳的总延迟15-100ms符合网络工程常识，与传播延迟同量级，占比计算逻辑自洽。
