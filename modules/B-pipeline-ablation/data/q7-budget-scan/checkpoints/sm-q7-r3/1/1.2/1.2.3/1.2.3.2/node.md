# N149: 分层方案的热数据迁移开销对总TCO的影响：若温数据每日有5%（5TB）从HDD层迁移至SSD层，迁移带宽占用I/O通道，导致冷数据读延迟增加；假设迁移吞吐为1G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

分层方案的热数据迁移开销对总TCO的影响：若温数据每日有5%（5TB）从HDD层迁移至SSD层，迁移带宽占用I/O通道，导致冷数据读延迟增加；假设迁移吞吐为1GB/s，每日迁移耗时 = 5TB / 1GB/s = 5000秒 ≈ 1.4小时；期间冷数据读吞吐下降50%，若冷数据月均访问1次，则年额外等待成本 = 12 * 1.4h * 0.5 * ¥5000/h = ¥42,000/年；需将此成本加入分层方案TCO，并与纯NVMe方案的无迁移成本对比。

## Corrected Claim

分层方案的热数据迁移开销对总TCO的影响：若温数据每日有5%（5TB）从HDD层迁移至SSD层，迁移带宽占用I/O通道，导致冷数据读延迟增加；假设迁移吞吐为1GB/s，每日迁移耗时 = 5TB / 1GB/s = 5000秒 ≈ 1.4小时；期间冷数据读吞吐下降50%，若冷数据月均访问1次，则年额外等待成本 = 12 * 1.4h * 0.5 * ¥5000/h = ¥42,000/年；需将此成本加入分层方案TCO，并与纯NVMe方案的无迁移成本对比。

## Evidence

先验知识/题面给定，逻辑校验通过：时间计算（5000s≈1.39h）正确，成本估算（12*1.4*0.5*5000=42000）算术无误，逻辑自洽。

## Search Query

data tiering migration overhead impact on cold data latency
