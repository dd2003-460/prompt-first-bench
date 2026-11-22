# N297: 一次性开发成本 C_dev_fixed 的构成分解：C_dev_fixed = C_backend_api + C_frontend_ui + C_data_m

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N100

## Claim

一次性开发成本 C_dev_fixed 的构成分解：C_dev_fixed = C_backend_api + C_frontend_ui + C_data_migration + C_testing，其中 C_backend_api 通常占 40-50%，C_data_migration 在存量平台中可能高达 30%，需根据具体技术栈（如微服务 vs 单体）进行量化拆分。

## Corrected Claim

一次性开发成本 C_dev_fixed 的构成分解：C_dev_fixed = C_backend_api + C_frontend_ui + C_data_migration + C_testing，其中各部分占比需根据具体技术栈（如微服务 vs 单体）及项目复杂度进行量化拆分，后端 API 和数据迁移通常是主要成本项。

## Evidence

[质询]具体百分比数值（40-50%、30%）属于经验性估算，缺乏普适性标准，不同项目差异巨大，且无来源支持该特定数值范围。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

cost breakdown for e-commerce platform feature development backend frontend data migration
