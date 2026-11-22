# N243: ΔGMV 的量化计算：ΔGMV = Q_new * P_deal_new - Q_old * P_deal_old，其中 Q 为成交量，P_deal 为平均成交

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

ΔGMV 的量化计算：ΔGMV = Q_new * P_deal_new - Q_old * P_deal_old，其中 Q 为成交量，P_deal 为平均成交价；需代入 N86 中的新成交概率及价格变化量进行差分计算。

## Corrected Claim

ΔGMV 的量化计算：ΔGMV = Q_new * P_deal_new - Q_old * P_deal_old，其中 Q 为成交量，P_deal 为平均成交价；需代入 N86 中的新成交概率及价格变化量进行差分计算。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV（成交总额）定义为成交量乘以平均成交价，其变化量（ΔGMV）自然等于新状态GMV减去旧状态GMV，公式推导符合基本代数逻辑。
