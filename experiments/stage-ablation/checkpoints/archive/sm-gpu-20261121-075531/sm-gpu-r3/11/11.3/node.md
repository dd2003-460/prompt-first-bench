# N373: TPS_Decode 稳态值需区分精度和硬件：2x RTX 4090 (INT8) TPS ≈ 45-50 tokens/s [待核验]，单卡 RTX 5090

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N126

## Claim

TPS_Decode 稳态值需区分精度和硬件：2x RTX 4090 (INT8) TPS ≈ 45-50 tokens/s [待核验]，单卡 RTX 5090 (INT8) TPS ≈ 60-70 tokens/s [待核验]；Cost_Per_Million_Tokens = (Capex_Amortized + Power_Cost) * 3600 / (TPS * 10^6) * 1000。

## Corrected Claim

TPS_Decode 稳态值高度依赖模型规模、精度及硬件配置，具体数值需根据实际部署参数测定；Cost_Per_Million_Tokens 计算公式逻辑正确。

## Evidence

[质询]TPS数值属于经验事实，缺乏具体模型规模（如7B/70B）和上下文长度等关键变量，不同配置下波动极大，且无来源支持具体数值区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 5090 vs 2x RTX 4090 LLM inference tokens per second benchmark
