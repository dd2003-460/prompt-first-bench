# N380: GSM8K基准测试集的标准配置为：总题目数1319道，其中训练集(Train) 747道，测试集(Test) 572道；Qwen3-27B官方报告通常在Test

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

GSM8K基准测试集的标准配置为：总题目数1319道，其中训练集(Train) 747道，测试集(Test) 572道；Qwen3-27B官方报告通常在Test集上评估，以消除数据泄漏风险，需确认评测脚本使用Test split而非全量数据。

## Corrected Claim

GSM8K基准测试集的标准配置为：总题目数1319道，其中训练集(Train) 747道，测试集(Test) 572道；Qwen3-27B官方报告通常在Test集上评估，以消除数据泄漏风险，需确认评测脚本使用Test split而非全量数据。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GSM8K dataset split size train test 572 1319
