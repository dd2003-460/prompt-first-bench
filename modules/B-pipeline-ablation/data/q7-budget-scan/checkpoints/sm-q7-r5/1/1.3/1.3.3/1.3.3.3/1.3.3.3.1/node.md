# N340: 阿里云 OSS 深度冷归档（Deep Cold Archive）的最低存储时长限制为 180 天，若数据在 180 天内删除或覆盖，需补缴剩余时长的存储费用，公

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N151, N153, N154

## Claim

阿里云 OSS 深度冷归档（Deep Cold Archive）的最低存储时长限制为 180 天，若数据在 180 天内删除或覆盖，需补缴剩余时长的存储费用，公式：C_penalty = max(0, 180 - t_retention_days) * (Price_daily_TB * V_TB)

## Corrected Claim

阿里云 OSS 深度冷归档通常设有最低存储时长限制（常见为180天），若提前删除或覆盖，需补缴剩余时长的存储费用。具体天数和计费公式请以阿里云官方最新文档为准。

## Evidence

[质询]具体数值（180天）及计费公式细节属于经验事实，缺乏来源支持，且不同云厂商或不同时期政策可能存在差异，无法仅凭逻辑推导确认其准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Alibaba Cloud OSS Deep Cold Archive minimum storage duration 180 days penalty
