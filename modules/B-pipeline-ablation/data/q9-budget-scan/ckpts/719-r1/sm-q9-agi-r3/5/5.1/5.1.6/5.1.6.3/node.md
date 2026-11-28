# N245: A/B 测试确定 T_threshold 的实验设计：需构建包含 100 个不同复杂度评分（范围 1-10）的基准测试集，分别用本地 Qwen3.8-27B 和

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

A/B 测试确定 T_threshold 的实验设计：需构建包含 100 个不同复杂度评分（范围 1-10）的基准测试集，分别用本地 Qwen3.8-27B 和云端 GPT-4o 处理，记录各自的幻觉率（FCR）和成本，绘制 FCR vs Complexity_Score 曲线，两条曲线的交点即为 T_threshold 的实证值

## Corrected Claim

A/B 测试确定 T_threshold 的实验设计：需构建包含 100 个不同复杂度评分（范围 1-10）的基准测试集，分别用本地 Qwen3.8-27B 和云端 GPT-4o 处理，记录各自的幻觉率（FCR）和成本，绘制 FCR vs Complexity_Score 曲线，两条曲线的交点即为 T_threshold 的实证值

## Evidence

先验知识/题面给定，逻辑校验通过：A/B测试对比两种模型在不同复杂度下的性能（FCR）与成本，寻找平衡点（交点）作为阈值是标准的实验设计方法，逻辑自洽且符合工程实践。
