# N223: 平台佣金率 r 的基准值：主流二手交易平台（如闲鱼、转转）对普通商品的佣金率 r 通常为 0% - 1%（或会员费摊销），需检索具体平台的最新费率结构以计算 U

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

平台佣金率 r 的基准值：主流二手交易平台（如闲鱼、转转）对普通商品的佣金率 r 通常为 0% - 1%（或会员费摊销），需检索具体平台的最新费率结构以计算 U_platform 的收入项。

## Corrected Claim

主流二手交易平台（如闲鱼）对普通个人卖家的佣金率通常为0.6%左右（部分时期或活动可能更低或封顶），而专业卖家（如鱼小铺）或特定高价值品类（如二手手机）的佣金率可达1.6%-2.6%。

## Evidence

[质询]陈述中“0% - 1%”的范围下限（0%）与来源显示的当前实际费率（0.6%）存在偏差，且未涵盖来源中提到的更高费率（如鱼小铺1.6%、二手手机2.6%），导致范围描述不够精确，可能误导对平台收入项的计算。 | 来源[1]和[2]直接支持闲鱼普通卖家佣金率为0.6%，属于0%-1%区间，但同时也指出特定卖家或品类费率更高（1.6%-2.6%），因此原陈述的“0%-1%”虽逻辑自洽但不够全面，且0%下限缺乏当前来源支持（来源显示为0.6%），故降级为定性表述。

## Search Query

Xianyu Zhuanzhuan commission rate percentage 2023 2024

## Retrieval Sources

- {'url': 'https://aiqicha.baidu.com/details/ugknowledge?id=fd725756e021844365699af26cb9860b&rut=a6dfb9965fc43df829aec7504a2a22fe016a5c91df53559383bd0c0d6a69ad6c', 'type': 'ddg', 'title': '闲鱼的交易佣金比例是多少 - 爱企查'}
- {'url': 'https://aiqicha.baidu.com/details/ugknowledge?id=d474bafb3aef2cc6f294d95b4a278018&rut=e3c4e0aa1adda23db72949279286ccf3419458e74031d184eb74437639238e56', 'type': 'ddg', 'title': '闲鱼平台提多少佣金 - 爱企查'}
