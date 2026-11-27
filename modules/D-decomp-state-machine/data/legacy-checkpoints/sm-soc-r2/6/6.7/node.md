# N107: 探索概率 ε_explore 的异质性分解：ε_explore = ε_base + ε_curiosity × I(new_category)，其中 ε_ba

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

探索概率 ε_explore 的异质性分解：ε_explore = ε_base + ε_curiosity × I(new_category)，其中 ε_base=0.05 为基线随机噪声，ε_curiosity=0.15 为对新品类/新品牌的探索加成。对于二手平台常见的‘重复购买品类’（如手机），ε_explore ≈ 0.05；对于‘长尾兴趣品类’（如手办），ε_explore ≈ 0.2。这解释了为何高价长尾商品成交周期更短。

## Corrected Claim

在特定的探索-利用（Exploration-Exploitation）模型设定中，若定义探索概率 ε_explore = ε_base + ε_curiosity × I(new_category)，且设定 ε_base=0.05, ε_curiosity=0.15，则对于长尾兴趣品类（如手办），其探索概率约为 0.2，高于重复购买品类（如手机）的 0.05。这种更高的探索概率可能增加用户接触长尾商品的频率，但关于其对成交周期的具体影响需结合需求弹性和决策成本进一步分析。

## Evidence

[质询]该陈述包含具体的经验参数（ε_base=0.05, ε_curiosity=0.15）以及基于这些参数推导出的具体行为结论（高价长尾商品成交周期更短）。这些数值并非第一性原理或数学公理可推导，而是特定模型设定或经验估计。此外，‘高价长尾商品成交周期更短’这一结论在经济学直觉上存在争议，通常高价商品决策周期更长，除非有极强的稀缺性或特定平台机制支持，仅靠探索概率增加不足以直接解释成交周期缩短，可能存在因果倒置或混淆变量（如需求刚性）。 | 经验事实，逻辑自洽但缺来源支持。检索无可用来源，且具体数值参数及行为结论属于经验性模型设定，无法从第一性原理严格推出，故降级。

## Search Query

exploration probability heterogeneity category novelty curiosity bias online shopping behavior
