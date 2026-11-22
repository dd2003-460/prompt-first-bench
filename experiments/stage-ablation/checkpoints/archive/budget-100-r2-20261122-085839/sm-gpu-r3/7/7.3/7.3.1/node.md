# N263: A6000 Ada 48GB 在 2024年Q4 的实际渠道现货均价为 $7,200-$7,800（MSRP $6,800 溢价约 5%-15%），其 48GB

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

A6000 Ada 48GB 在 2024年Q4 的实际渠道现货均价为 $7,200-$7,800（MSRP $6,800 溢价约 5%-15%），其 48GB 显存足以容纳 Qwen3-27B INT8 权重（27.1GB）+ FP8 KV Cache（32K ctx, Batch=1 约 10.3GB）+ 激活值（约 2GB），剩余显存约 8.6GB，满足安全余量要求。

## Corrected Claim

A6000 Ada 48GB 的 48GB 显存足以容纳 Qwen3-27B INT8 权重（27.1GB）+ FP8 KV Cache（32K ctx, Batch=1 约 10.3GB）+ 激活值（约 2GB），剩余显存约 8.6GB，满足安全余量要求。其 2024年Q4 的市场价格需参考实时渠道报价。

## Evidence

[质询]2024年Q4 A6000 Ada 48GB 的渠道现货均价及具体溢价比例属于实时市场经验数据，缺乏权威来源支持，且不同地区/渠道价格波动较大，该具体数值区间可能不准确。 | 显存占用计算逻辑自洽（27.1+10.3+2=39.4GB < 48GB，剩余8.6GB），但价格部分为经验事实且无来源支持，故降级。

## Search Query

NVIDIA A6000 Ada 48GB street price 2024
