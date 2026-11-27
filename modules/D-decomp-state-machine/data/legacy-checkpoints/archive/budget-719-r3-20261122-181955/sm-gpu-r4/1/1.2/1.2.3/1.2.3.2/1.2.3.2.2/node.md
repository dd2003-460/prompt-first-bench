# N463: H100 SXM5 在 BF16 精度下的单位并发 TCO：H100 80GB 显存扣除 54 GB 权重后剩余 26 GB，可支持 3 个并发请求（26 GB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

H100 SXM5 在 BF16 精度下的单位并发 TCO：H100 80GB 显存扣除 54 GB 权重后剩余 26 GB，可支持 3 个并发请求（26 GB / 8 GB/request），单位并发 TCO = $26,791 / 3 ≈ $8,930 USD，需与 A100 80GB 的 $5,258 USD（N377）对比，H100 单位并发成本高出 70%。

## Corrected Claim

H100 SXM5 在 BF16 精度下的单位并发 TCO：H100 80GB 显存扣除 54 GB 权重后剩余 26 GB，可支持 3 个并发请求（26 GB / 8 GB/request），单位并发 TCO = $26,791 / 3 ≈ $8,930 USD，需与 A100 80GB 的 $5,258 USD（N377）对比，H100 单位并发成本高出 70%。

## Evidence

先验知识/题面给定，逻辑校验通过：80GB-54GB=26GB，26/8≈3.25取整为3，26791/3≈8930.33，(8930-5258)/5258≈69.8%≈70%，计算与逻辑均自洽。
