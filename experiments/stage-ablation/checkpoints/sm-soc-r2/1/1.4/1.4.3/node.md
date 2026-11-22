# N41: 注意力成本 C_att 的量化构成：C_att = C_cognitive * (1 + I_overload)，其中 I_overload = N_visib

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

注意力成本 C_att 的量化构成：C_att = C_cognitive * (1 + I_overload)，其中 I_overload = N_visible_items / Attention_Capacity，N_visible_items 为同屏展示商品数（通常 20-50），Attention_Capacity 为个体认知带宽（标准化为 1.0）。

## Corrected Claim

在特定注意力成本模型中，C_att 可量化为 C_cognitive * (1 + I_overload)，其中 I_overload 定义为同屏展示商品数与个体认知带宽标准化值（设为1.0）的比值，该模型假设同屏商品数通常在 20-50 之间。

## Evidence

[质询]该公式为特定理论模型下的假设性定义，并非普适的物理或数学定律；'Attention_Capacity 标准化为 1.0' 及 'N_visible_items 通常 20-50' 属于经验性参数设定，缺乏通用实证支持，且不同认知心理学模型对注意力过载的量化方式差异巨大。 | source=knowledge，逻辑自洽（量纲一致，公式结构合理），但作为经验性量化模型，其具体参数（如标准化值、典型商品数）缺乏普适性来源支持，依据经验事实排除条款及知识节点降级规则，保留但降级为定性/模型特定表述。

## Search Query

cognitive load cost of attention overload e-commerce
