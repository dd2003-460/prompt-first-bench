# N239: 高挂价商品未在前5位曝光时成交概率 P_deal 骤降至 0.05 以下的边界条件：当 P_listed > P_median * (1 + 2*σ_noise

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

高挂价商品未在前5位曝光时成交概率 P_deal 骤降至 0.05 以下的边界条件：当 P_listed > P_median * (1 + 2*σ_noise) 且 Rank > 5 时，P_deal < 0.05；若 P_listed 在噪声容忍区内（±1*σ_noise），即使 Rank > 5，P_deal 仍可维持在 0.15-0.20 区间。

## Corrected Claim

高挂价商品未在前5位曝光时成交概率显著降低；当价格显著高于中位数（超出噪声容忍区）且排名靠后时，成交概率极低；若价格在噪声容忍区内，即使排名靠后，成交概率仍维持在较高水平。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（如 P_deal < 0.05, 0.15-0.20）和特定的统计关系（2*σ_noise），属于经验事实。参考来源 [1] 为游戏资讯，与电商/交易定价模型完全无关，无法提供外部支持。虽然逻辑上符合经济学直觉（高价+低曝光导致低成交），但具体数值缺乏来源验证。 | 经验事实，逻辑自洽但缺来源支持（来源 [1] 无关）

## Search Query

search result position impact conversion rate second hand goods

## Retrieval Sources

- {'url': 'https://www.gametl.cn/game-debate/2026nyxjbxqlxpdzmkngjzjllkdsybkzn/&rut=39792b3e2d2c105962df762f21a5357a4b73974a55e0a11d6acf101647ac2460', 'type': 'ddg', 'title': '2026年游戏聚宝箱全类型盘点，怎么开拿高价值奖励？零氪党实用避坑指南 - 游戏天龙人'}
