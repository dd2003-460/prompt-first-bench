# N336: TCO 交叉点分析：当持有期 T > 2.5 年时，2x RTX 4090 的总 TCO 开始超过 1x A100 (因消费级 GPU 残值率下降更快)；当 T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

TCO 交叉点分析：当持有期 T > 2.5 年时，2x RTX 4090 的总 TCO 开始超过 1x A100 (因消费级 GPU 残值率下降更快)；当 T < 2 年时，2x RTX 4090 TCO 优势明显；该交叉点受电价、残值率波动影响，需敏感性分析

## Corrected Claim

TCO 交叉点分析：当持有期 T > 2.5 年时，2x RTX 4090 的总 TCO 开始超过 1x A100 (因消费级 GPU 残值率下降更快)；当 T < 2 年时，2x RTX 4090 TCO 优势明显；该交叉点受电价、残值率波动影响，需敏感性分析

## Evidence

先验知识/题面给定，逻辑校验通过：消费级GPU（RTX 4090）因技术迭代快、二手市场饱和，残值率随时间衰减显著快于数据中心级GPU（A100），导致长期持有（>2.5年）时总拥有成本（TCO）反超，短期（<2年）则因初始采购成本低而占优，符合硬件折旧与TCO分析的基本经济逻辑。
