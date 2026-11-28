# N26: 黑盒变量 1：27b 模型在特定垂直领域（如生物信息学/粒子物理）的知识截止与幻觉率。验证计划：构建 100 道领域特化事实题，测量幻觉率 H_domain。若

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

黑盒变量 1：27b 模型在特定垂直领域（如生物信息学/粒子物理）的知识截止与幻觉率。验证计划：构建 100 道领域特化事实题，测量幻觉率 H_domain。若 H_domain > 15%，则该领域必须强制启用 RAG Hook（N9），否则不可信。置信度评估：使用 Bootstrap 重抽样计算 H_domain 的 95% 置信区间。

## Corrected Claim

黑盒变量 1：27b 模型在特定垂直领域（如生物信息学/粒子物理）的知识截止与幻觉率。验证计划：构建 100 道领域特化事实题，测量幻觉率 H_domain。若 H_domain > 15%，则该领域必须强制启用 RAG Hook（N9），否则不可信。置信度评估：使用 Bootstrap 重抽样计算 H_domain 的 95% 置信区间。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应数据准备（基准构建）、指标定义（幻觉率计算）和统计推断（置信区间），职责清晰且互不重叠；完整覆盖了父节点中提到的‘构建题目’、‘测量幻觉率’及‘Bootstrap评估’三个核心步骤；各节点为独立的方法论组件，不存在参数冗余。）

## Search Query

domain specific hallucination rate LLM benchmark
