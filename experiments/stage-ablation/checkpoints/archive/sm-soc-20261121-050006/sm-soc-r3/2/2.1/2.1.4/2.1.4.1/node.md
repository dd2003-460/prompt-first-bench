# N179: 信息不对称指标 I_asym 与买家怀疑系数 γ_defect 的线性映射关系：γ_defect = γ_0 + k_I * I_asym，其中 γ_0 ∈ [

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

信息不对称指标 I_asym 与买家怀疑系数 γ_defect 的线性映射关系：γ_defect = γ_0 + k_I * I_asym，其中 γ_0 ∈ [0.1, 0.3] 为基准怀疑系数，k_I ∈ [1.0, 2.0] 为敏感度系数，需通过 A/B 测试中不同透明度标签下的咨询率差异校准。

## Corrected Claim

信息不对称指标 I_asym 与买家怀疑系数 γ_defect 可能存在正相关关系，通常可建模为线性映射 γ_defect = γ_0 + k_I * I_asym，但具体参数 γ_0 和 k_I 的取值范围需通过特定场景下的 A/B 测试或实证数据校准，现有通用文献未提供统一标准值。

## Evidence

[质询]该陈述描述了一个具体的经验性线性映射模型及其参数范围（γ_0, k_I），这属于需要实证数据校准的经验事实，而非可从第一性原理推导的数学或逻辑恒等式。参考来源仅讨论了信息不对称指标的通用测算方法（如KV指数、盈余管理），并未提及买家怀疑系数、线性映射关系或具体的参数区间，因此缺乏直接来源支持。 | 逻辑上线性映射是合理的简化模型，但作为经验事实（具体参数范围和校准方法），参考来源[1]仅涉及信息不对称指标定义，未覆盖该特定映射关系，属于间接相关或无关，无法提供直接支持。

## Search Query

information asymmetry coefficient buyer suspicion lemons market calibration A/B test

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/715321375&rut=66e4d823512e436ac5a87efa47e0f4b9582bfac72ef9dd0a28feb5fc5ba87f5d', 'type': 'ddg', 'title': '上市公司信息不对称指标测算 - 知乎'}
