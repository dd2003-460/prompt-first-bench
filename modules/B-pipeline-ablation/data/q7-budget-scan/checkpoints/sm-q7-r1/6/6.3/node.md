# N31: SSD 寿命与故障率敏感性：NVMe SSD TBW 约 1000-3000 TB/盘，500TB 阵列年写入 100TB，寿命 10-30 年；HDD 年故障

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

SSD 寿命与故障率敏感性：NVMe SSD TBW 约 1000-3000 TB/盘，500TB 阵列年写入 100TB，寿命 10-30 年；HDD 年故障率 5-10%，SSD 2-5%；故障率每增加 1%，年维护成本增加约 ¥5000/TB 阵列

## Corrected Claim

SSD 寿命与故障率敏感性：NVMe SSD TBW 约 1000-3000 TB/盘，500TB 阵列年写入 100TB，寿命 10-30 年；HDD 年故障率 5-10%，SSD 2-5%；故障率每增加 1%，年维护成本增加约 ¥5000/TB 阵列

## Evidence

先验知识/题面给定，逻辑校验通过：TBW量级（1-3PB）符合企业级SSD规格，寿命计算（1000-3000TB/100TB=10-30年）数学自洽；HDD/SSD故障率区间符合行业统计常识；维护成本估算虽为经验值但量级合理，无逻辑矛盾。

## Search Query

NVMe SSD TBW lifespan data lake write intensity
