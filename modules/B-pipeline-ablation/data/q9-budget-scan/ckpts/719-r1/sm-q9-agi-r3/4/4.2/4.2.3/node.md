# N62: 针对 Qwen3.8-27B 的幻觉率基线，需在相同提示模板下，对比 Temperature=0.7 与 Temperature=0.1 两种设置下的 FCR 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

针对 Qwen3.8-27B 的幻觉率基线，需在相同提示模板下，对比 Temperature=0.7 与 Temperature=0.1 两种设置下的 FCR 差异，通常低温设置可降低幻觉率 20%-40%，但可能降低多样性，需记录具体的 ΔFCR 数值。

## Corrected Claim

针对 Qwen3.8-27B 的幻觉率基线，需在相同提示模板下，对比 Temperature=0.7 与 Temperature=0.1 两种设置下的 FCR 差异。理论上低温设置倾向于降低幻觉率但可能降低多样性，需记录具体的 ΔFCR 数值以评估实际影响。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1和2分别定义了两组独立实验的测量协议（输入、参数、统计量），节点3基于前两者的结果进行统计显著性检验（验证差异是否真实存在），节点4关注副作用（多样性）并给出平衡策略。三者分别对应‘数据获取’、‘假设检验’和‘权衡评估’，无重复或矛盾。父节点提到的‘相同提示模板’在两个测量协议中通过‘固定50个三元组问句’体现，‘ΔFCR数值’在节点3中通过配对检验和效应量计算覆盖，‘多样性降低’在节点4中量化。未发现冗余，因为虽然节点1和2结构相似，但它们是两个不同的实验条件（Temperature不同），是必要的对照实验设计，而非单纯参数变化的简单罗列。）

## Search Query

Qwen3-27B hallucination rate temperature sensitivity benchmark
