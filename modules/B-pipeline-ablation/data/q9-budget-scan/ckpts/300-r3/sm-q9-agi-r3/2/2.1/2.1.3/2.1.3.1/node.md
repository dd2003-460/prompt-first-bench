# N180: P(Refutation | Data)的近似计算：采用贝叶斯因子BF_01 = P(Data|H0)/P(Data|H1)，Falsifiability ≈ 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N53

## Claim

P(Refutation | Data)的近似计算：采用贝叶斯因子BF_01 = P(Data|H0)/P(Data|H1)，Falsifiability ≈ BF_01，要求BF_01 > 1.5；在模拟实验中，BF_01可通过蒙特卡洛抽样1000次数据点计算，单次计算耗时约50ms

## Corrected Claim

在特定模拟实验框架下，可采用贝叶斯因子BF_01作为可证伪性的代理指标（阈值>1.5），并通过蒙特卡洛抽样估算；具体计算耗时取决于实现细节，此处约为50ms。

## Evidence

[质询]将贝叶斯因子（Bayes Factor）直接等同于可证伪性（Falsifiability）在概念上存在混淆，且“单次计算耗时约50ms”属于高度依赖具体实现和硬件环境的经验性能指标，缺乏通用性。 | 先验知识/题面给定，逻辑校验通过；但BF与Falsifiability的等价性及具体耗时为经验性/特定上下文设定，非普适真理，故降级。

## Search Query

Bayes factor falsifiability score calculation Monte Carlo simulation
