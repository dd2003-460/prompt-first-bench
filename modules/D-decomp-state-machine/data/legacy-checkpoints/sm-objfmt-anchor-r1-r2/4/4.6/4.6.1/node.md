# N93: 基准价格基准值 P_gpu_base：RTX 4090 (24GB) 当前市场均价为 $1,800 (来源: [search] 需核验最新电商价), RTX 3

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N26

## Claim

基准价格基准值 P_gpu_base：RTX 4090 (24GB) 当前市场均价为 $1,800 (来源: [search] 需核验最新电商价), RTX 3090 为 $1,200, A100 40GB 为 $8,000。敏感度分析的基准点必须锚定在此实时价格上，否则 ±20% 的扰动无意义。

## Corrected Claim

基准价格基准值 P_gpu_base 应锚定分析时的实时市场均价（例如：RTX 4090 约 $1,600-$1,800, RTX 3090 约 $1,000-$1,200, A100 40GB 约 $7,000-$9,000，具体需以当日电商报价为准），以确保 ±20% 扰动分析的有效性。

## Evidence

[质询]具体GPU的市场价格是高度波动的经验事实，且不同渠道（新品/二手/企业采购）价格差异巨大，缺乏实时数据支持时，固定数值极易过时或偏差。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体价格数值）

## Search Query

RTX 4090 current market price 2024 average cost USD
