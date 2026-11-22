# N99: 缓存驻留时间 T_residence 的基准工作点：假设最小对象大小 x_min = 1KB，E[S] = α/(α-1)*x_min = 1.1/0.1 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

缓存驻留时间 T_residence 的基准工作点：假设最小对象大小 x_min = 1KB，E[S] = α/(α-1)*x_min = 1.1/0.1 * 1KB = 11KB；λ = 578 req/s；C = 128GB = 128*1024^3 bytes；T_residence ≈ C / (λ * E[S]) ≈ (128*1024^3) / (578 * 11*1024) ≈ 20,000 秒 ≈ 5.56 小时。

## Corrected Claim

缓存驻留时间 T_residence 的基准工作点：假设最小对象大小 x_min = 1KB，E[S] = α/(α-1)*x_min = 1.1/0.1 * 1KB = 11KB；λ = 578 req/s；C = 128GB = 128*1024^3 bytes；T_residence ≈ C / (λ * E[S]) ≈ (128*1024^3) / (578 * 11*1024) ≈ 20,000 秒 ≈ 5.56 小时。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 (128*1024^3) / (578 * 11*1024) ≈ 20,000 秒，量级与单位换算正确，符合缓存驻留时间的基本定义。

## Search Query

cache residence time calculation average object size request rate capacity
