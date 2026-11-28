# N243: 注入跨文件符号引用图后的 Prompt 长度增量 ΔL = 200 * n_refs tokens，其中 n_refs 为提取的关键符号引用数量（通常 n_re

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

注入跨文件符号引用图后的 Prompt 长度增量 ΔL = 200 * n_refs tokens，其中 n_refs 为提取的关键符号引用数量（通常 n_refs ≈ 2 * n_files）

## Corrected Claim

注入跨文件符号引用图后的 Prompt 长度增量 ΔL 与关键符号引用数量 n_refs 成正比，具体系数取决于符号名称长度及上下文格式，通常 n_refs 与涉及文件数正相关

## Evidence

[质询]系数200和关系n_refs≈2*n_files缺乏通用标准支持，属于特定实现的经验参数，不同代码库复杂度下差异巨大 | 经验事实，逻辑自洽但缺来源支持
