# N113: 无检索条件下的作答协议：Prompt 严格限制模型仅使用内部参数化知识，明确指令 'Do not use external search tools or re

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

无检索条件下的作答协议：Prompt 严格限制模型仅使用内部参数化知识，明确指令 'Do not use external search tools or retrieve from memory bank. Answer based solely on your internal weights.'，并关闭 RAG Hook

## Corrected Claim

无检索条件下的作答协议：Prompt 严格限制模型仅使用内部参数化知识，明确指令 'Do not use external search tools or retrieve from memory bank. Answer based solely on your internal weights.'，并关闭 RAG Hook

## Evidence

父节点级核验未通过：不完备（子节点分别关注安全性（对抗测试）、基础设施执行验证（RAG监控）和数据生成/评估（边界探测），三者维度不同，互不重叠且无逻辑矛盾，因此正交性好。但存在覆盖缺失：父节点核心是“作答协议”（Prompt设计+执行环境），子节点均侧重于“测试”、“验证”或“后续处理”，缺少关于Prompt本身的结构设计、负面约束的具体措辞策略或指令层级（System/User）配置等基础定义层面的子节点。）

## Search Query

prompt engineering to disable RAG and force parametric knowledge usage
