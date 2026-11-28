# N312: 预训练语料高频覆盖区的量化定义：在 Common Crawl 或 The Pile 数据集的 n-gram 频率表中，核心答案短语的 TF-IDF 值需低于数据

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

预训练语料高频覆盖区的量化定义：在 Common Crawl 或 The Pile 数据集的 n-gram 频率表中，核心答案短语的 TF-IDF 值需低于数据集 95th 百分位（即 P95），以确保其不在模型预训练语料的 top 5% 高频模式中

## Corrected Claim

预训练语料高频覆盖区的量化定义：在 Common Crawl 或 The Pile 数据集的 n-gram 频率表中，核心答案短语的 TF-IDF 值需低于数据集 95th 百分位（即 P95），以确保其不在模型预训练语料的 top 5% 高频模式中

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Common Crawl n-gram frequency percentile rare entity detection
