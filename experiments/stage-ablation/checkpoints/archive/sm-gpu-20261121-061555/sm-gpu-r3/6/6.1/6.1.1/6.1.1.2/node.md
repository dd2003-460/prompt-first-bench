# N306: 工作点 B（价格敏感情景）：假设 GPU 采购价格为 [实时查询] 数据，波动幅度 >15%（例如 RTX 4090 在 $1600-$2200 之间波动），需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

工作点 B（价格敏感情景）：假设 GPU 采购价格为 [实时查询] 数据，波动幅度 >15%（例如 RTX 4090 在 $1600-$2200 之间波动），需构建 TCO = f(Price) 函数，并计算使方案 A 优于方案 B 的价格临界点 P*，若 P* 落在当前市场波动区间内，则推荐必须附带 '价格监控条件'。

## Corrected Claim

工作点 B（价格敏感情景）：假设 GPU 采购价格为 [实时查询] 数据，波动幅度 >15%（例如 RTX 4090 在 $1600-$2200 之间波动），需构建 TCO = f(Price) 函数，并计算使方案 A 优于方案 B 的价格临界点 P*，若 P* 落在当前市场波动区间内，则推荐必须附带 '价格监控条件'。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO模型构建及临界点P*的计算逻辑符合经济学基本原理，波动区间设定合理，无内部矛盾。

## Search Query

RTX 4090 price history volatility 2024 2025
