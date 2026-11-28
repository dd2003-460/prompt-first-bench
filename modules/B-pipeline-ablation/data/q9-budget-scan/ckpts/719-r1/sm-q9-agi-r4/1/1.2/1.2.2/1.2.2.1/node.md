# N125: Needle-in-a-Haystack 测试中'开头位置'与'中间位置'的标准化定义：开头指上下文的前 5% tokens（即 128K 中的前 6.4K），

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Needle-in-a-Haystack 测试中'开头位置'与'中间位置'的标准化定义：开头指上下文的前 5% tokens（即 128K 中的前 6.4K），中间指上下文的 40%-60% 区间（即 51.2K-76.8K），需在此定义下测量准确率差异

## Corrected Claim

Needle-in-a-Haystack 测试中'开头位置'与'中间位置'的标准化定义：开头指上下文的前 5% tokens（即 128K 中的前 6.4K），中间指上下文的 40%-60% 区间（即 51.2K-76.8K），需在此定义下测量准确率差异

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 非正交且冗余：三个子节点本质上是同一个变量（测试采样策略/粒度）的不同取值（Low/Medium/High），属于同一维度的层级划分，而非正交的不同方面。2. 不完备：父节点核心要求是‘测量准确率差异’，但子节点仅描述了‘如何设置测试点’（输入端），完全缺失了‘如何计算准确率’、‘使用何种指标’或‘数据预处理’等执行层面的关键信息。）

## Search Query

needle in a haystack test position definition beginning middle context length
