# N717: FP8 量化下模型权重大小 = 27e9 * 1 byte = 27 GB，但需验证 Qwen3-27B 是否原生支持 FP8 推理或需转换为 E4M3/E5M

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N256

## Claim

FP8 量化下模型权重大小 = 27e9 * 1 byte = 27 GB，但需验证 Qwen3-27B 是否原生支持 FP8 推理或需转换为 E4M3/E5M2 格式，不同 FP8 变体可能影响精度损失。

## Corrected Claim

FP8 量化下模型权重大小约为 27 GB（基于 27e9 参数 * 1 byte），但 Qwen3-27B 是否原生支持 FP8 推理、具体格式（E4M3/E5M2）及精度损失需查阅官方文档或实测数据确认。

## Evidence

[质询]该陈述包含具体的经验性技术规格（Qwen3-27B 的 FP8 支持情况、具体格式转换需求及精度影响），这些属于经验事实，无法仅从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 quantization support E4M3 E5M2
