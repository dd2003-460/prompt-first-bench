# N106: 工作点 A（头部密集区）：假设 Top 1% 对象（K=1000）平均大小为 0.5KB（因负相关），占用容量 0.5MB，剩余容量 128GB-0.5MB 可

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

工作点 A（头部密集区）：假设 Top 1% 对象（K=1000）平均大小为 0.5KB（因负相关），占用容量 0.5MB，剩余容量 128GB-0.5MB 可容纳中尾部对象，此工作点下 K_eff 接近 N=100,000

## Corrected Claim

工作点 A（头部密集区）：假设 Top 1% 对象（K=1000）平均大小为 0.5KB（因负相关），占用容量 0.5MB，剩余容量 128GB-0.5MB 可容纳中尾部对象，此工作点下 K_eff 接近 N=100,000

## Evidence

先验知识/题面给定，逻辑校验通过：1000个对象*0.5KB=0.5MB，远小于128GB，剩余容量充足；K_eff接近N符合头部密集区假设下的逻辑推导。
