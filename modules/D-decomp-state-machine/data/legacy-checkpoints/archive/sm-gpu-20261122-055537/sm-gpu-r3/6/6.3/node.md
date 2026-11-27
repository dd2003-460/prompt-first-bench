# N30: 条件性推荐逻辑：若电力价格 > $0.15/kWh 且 7x24 运行，优先选择低功耗数据中心卡(如 L4)以优化 C_power；若电力价格 < $0.10/

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

条件性推荐逻辑：若电力价格 > $0.15/kWh 且 7x24 运行，优先选择低功耗数据中心卡(如 L4)以优化 C_power；若电力价格 < $0.10/kWh 且追求最高吞吐量/最低延迟，优先选择 RTX 4090；若对质量极度敏感且预算 > $20,000，选择 H100。此推荐依赖于 N16 的量化质量验证结果。

## Corrected Claim

条件性推荐逻辑：若电力价格 > $0.15/kWh 且 7x24 运行，优先选择低功耗数据中心卡(如 L4)以优化 C_power；若电力价格 < $0.10/kWh 且追求最高吞吐量/最低延迟，优先选择 RTX 4090；若对质量极度敏感且预算 > $20,000，选择 H100。此推荐依赖于 N16 的量化质量验证结果。

## Evidence

先验知识/题面给定，逻辑校验通过：推荐逻辑符合成本效益分析原则（高电价选低功耗，低电价选高性能，高预算选顶级质量），且明确声明依赖N16的量化结果，逻辑自洽。

## Search Query

conditional recommendation logic GPU selection power price quality sensitivity
