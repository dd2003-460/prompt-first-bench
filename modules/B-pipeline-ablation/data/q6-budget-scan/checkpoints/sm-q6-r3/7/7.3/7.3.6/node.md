# N298: NVMe SSD写入寿命与缓存刷新成本：NVMe TBW（Total Bytes Written）通常为200-600TB/盘，日均2TB下载对应缓存写入量需根

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

NVMe SSD写入寿命与缓存刷新成本：NVMe TBW（Total Bytes Written）通常为200-600TB/盘，日均2TB下载对应缓存写入量需根据命中率H计算为W_daily = 2TB * (1-H)，若H=0.9，W_daily=200GB，年写入73TB，寿命≈3-8年，需纳入折旧或更换计划

## Corrected Claim

NVMe SSD写入寿命与缓存刷新成本：NVMe TBW（Total Bytes Written）通常为200-600TB/盘，日均2TB下载对应缓存写入量需根据命中率H计算为W_daily = 2TB * (1-H)，若H=0.9，W_daily=200GB，年写入73TB，寿命≈3-8年，需纳入折旧或更换计划

## Evidence

[质询]TBW范围（200-600TB）可能偏向低端或消费级SSD，企业级SSD通常更高，但作为一般性估算范围在逻辑上可接受；寿命计算基于线性磨损假设，未考虑过度配置（Over-provisioning）和磨损均衡算法的影响，但作为粗略工程估算合理。 | 先验知识/题面给定，逻辑校验通过：数学计算正确（2TB*0.1=200GB/天，200GB*365≈73TB/年，73TB/200TB≈0.365年/200TB寿命 -> 200/73≈2.7年，600/73≈8.2年，范围3-8年合理），符合NVMe SSD寿命估算的基本工程逻辑。

## Search Query

nvme ssd tbw write endurance cache hit rate daily write volume calculation
