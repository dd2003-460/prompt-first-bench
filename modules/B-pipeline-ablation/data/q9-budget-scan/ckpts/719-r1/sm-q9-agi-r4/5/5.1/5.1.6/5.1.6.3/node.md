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

父节点级核验通过：正交+完备+无冗余（子节点分别对应实验设计的五个核心环节：数据构造（复杂度定义）、本地模型测量、云端模型测量、数据拟合与阈值提取、误差控制。各部分职责清晰，无重叠或矛盾。FCR测量方法虽相似但针对不同执行环境（本地vs云端）且涉及不同的成本记录方式，属于必要区分而非冗余。所有关键步骤均被覆盖。）
