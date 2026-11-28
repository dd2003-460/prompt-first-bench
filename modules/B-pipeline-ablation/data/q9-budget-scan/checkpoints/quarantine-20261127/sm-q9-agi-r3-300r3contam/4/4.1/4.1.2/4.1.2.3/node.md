# N164: 阶梯定价触发阈值量化：多数 API 提供商对上下文长度 >32k tokens 的输入部分收取 2x 溢价（如 P_in_high = 2 * P_in_bas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

阶梯定价触发阈值量化：多数 API 提供商对上下文长度 >32k tokens 的输入部分收取 2x 溢价（如 P_in_high = 2 * P_in_base）；在 max_model_len=262144 设置下，若单次请求平均输入长度 L_in_avg=50k tokens，则实际有效单价 P_eff_in = (32k*P_base + 18k*2*P_base)/50k = 1.72*P_base，需将此修正项纳入 C_api(L) 计算

## Corrected Claim

在假设某API提供商对超过32k tokens的部分收取2倍溢价的情况下，若max_model_len=262144且平均输入长度为50k tokens，则有效输入单价为基准价的1.72倍。需注意不同提供商的阶梯定价阈值和倍率各异，需根据具体服务商文档确定参数。

## Evidence

[质询]该陈述包含具体的经验性参数（如“多数提供商”、“2x溢价”、“32k阈值”），这些并非第一性原理可推导的数学或物理事实，而是依赖于特定厂商（如OpenAI、Anthropic等）的商业定价策略。不同厂商的阶梯定价阈值和倍率差异巨大（例如有的从128k开始，有的倍率不同），因此“多数”和“2x”这一概括性描述缺乏普适性，且当前无来源支持其普遍性。 | 经验事实，逻辑自洽但缺来源支持。数学计算部分（(32k*1 + 18k*2)/50k = 1.72）正确，但前提条件（32k阈值、2x倍率）为特定场景假设而非通用真理，且检索无可用来源验证其普遍适用性。

## Search Query

OpenAI long context pricing multiplier 32k tokens extra cost per token
