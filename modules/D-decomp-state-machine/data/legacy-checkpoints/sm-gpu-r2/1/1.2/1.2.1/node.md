# N33: 消费级 GPU 显存容量硬约束筛选：列出 2024-2025 年主流消费级 GPU 的 GDDR6/GDDR6X 容量与有效可用显存 (Reserved for

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

消费级 GPU 显存容量硬约束筛选：列出 2024-2025 年主流消费级 GPU 的 GDDR6/GDDR6X 容量与有效可用显存 (Reserved for Driver/OS ~200MB-500MB)：RTX 4090 (24GB, 有效~23.5GB), RTX 5090 (32GB, 有效~31.5GB), RTX 3090 (24GB, 有效~23.5GB)。

## Corrected Claim

消费级 GPU 显存容量筛选：RTX 4090 (24GB GDDR6X), RTX 3090 (24GB GDDR6X), RTX 5090 (32GB GDDR7)。有效可用显存通常略低于标称容量（约 200MB-500MB 被系统保留），具体数值随驱动和 OS 变化。

## Evidence

[质询]RTX 5090 的显存规格（32GB GDDR7）属于 2025 年发布的新硬件，且其显存类型已升级为 GDDR7 而非 GDDR6/GDDR6X，陈述中将其归类为 GDDR6/GDDR6X 存在技术规格混淆；此外，'有效可用显存'的具体数值（如 23.5GB）因驱动版本和操作系统而异，并非固定硬约束值。 | 经验事实，逻辑自洽但缺来源支持；RTX 5090 实际使用 GDDR7 显存，与陈述中的 GDDR6/GDDR6X 分类不符，且无外部来源验证具体有效显存数值。

## Search Query

RTX 5090 32GB usable VRAM driver overhead RTX 4090 24GB
