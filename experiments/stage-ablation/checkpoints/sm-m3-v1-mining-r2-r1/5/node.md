# N15: 建立输入端验证协议：在最终输出前，必须执行 'contradiction_scan_input' 步骤，对比题面给定常数与领域常识库（如标准材料手册值），若偏差

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

建立输入端验证协议：在最终输出前，必须执行 'contradiction_scan_input' 步骤，对比题面给定常数与领域常识库（如标准材料手册值），若偏差超过 50% 则强制插入 'Warning: Input parameter may be erroneous' 标签，禁止无条件信任输入

## Corrected Claim

建议建立输入端验证机制：在输出前对比题面常数与领域常识，若发现显著偏差（如超过50%），应标记警告并提示用户确认，避免盲目信任输入。

## Evidence

[质询]该陈述描述的是一个具体的工程实践规范或自定义协议（包含特定阈值50%和特定标签文本），属于经验性操作指南而非普适真理或第一性原理推导结果；且参考来源讨论的是形式化程序验证（SAT/SMT/合取范式），与“输入参数合理性检查”这一具体防御性编程策略无直接关联，缺乏权威来源支持其作为通用标准的必要性。 | 逻辑自洽（输入验证是良好实践），但参考来源[1]主题为形式化程序正确性证明，与本节点描述的输入参数合理性校验协议无关，属经验事实且缺直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/636325803&rut=ead7eddc722afb6d93634a423ac0b29f2ba0c3f353b159008a822b6a77f3e55c', 'type': 'ddg', 'title': '第11节：介绍基于约束的程序验证方法 - 知乎'}
