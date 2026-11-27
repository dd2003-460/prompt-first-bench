# N21: 定义条件性推荐的决策树结构：根节点为'预算区间'（<5k/5k-15k/15k-30k/>30k USD），第二层为'延迟容忍度'（<100ms/100-500

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

定义条件性推荐的决策树结构：根节点为'预算区间'（<5k/5k-15k/15k-30k/>30k USD），第二层为'延迟容忍度'（<100ms/100-500ms/>500ms per 1K tokens），第三层为'精度偏好'（BF16优先/FP8可接受/INT8可接受/NVFP4可接受）；每个叶子节点必须输出：(1)推荐硬件组合，(2)量化性能指标（tokens/s, 内存占用GB），(3)与次优方案的差距百分比，(4)失效条件（什么情况下该推荐不再成立）

## Corrected Claim

定义条件性推荐的决策树结构：根节点为'预算区间'（<5k/5k-15k/15k-30k/>30k USD），第二层为'延迟容忍度'（<100ms/100-500ms/>500ms per 1K tokens），第三层为'精度偏好'（BF16优先/FP8可接受/INT8可接受/NVFP4可接受）；每个叶子节点必须输出：(1)推荐硬件组合，(2)量化性能指标（tokens/s, 内存占用GB），(3)与次优方案的差距百分比，(4)失效条件（什么情况下该推荐不再成立）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

conditional recommendation decision tree hardware selection LLM inference
