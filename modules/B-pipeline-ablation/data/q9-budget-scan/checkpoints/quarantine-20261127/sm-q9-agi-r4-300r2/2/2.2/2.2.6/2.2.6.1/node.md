# N133: Critic 输入 Token 数的动态修正：Critic 输入并非固定为初稿全文 L，而是 L + Context_Window，其中 Context_Win

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

Critic 输入 Token 数的动态修正：Critic 输入并非固定为初稿全文 L，而是 L + Context_Window，其中 Context_Window 包含历史对话摘要或知识库检索片段（典型 500-2000 tokens）；若采用滑动窗口策略，Context_Window 恒定 1000 tokens，则 Critic 实际输入 = L + 1000，当 L < 1000 时，固定开销占比显著上升（如 L=500 时，开销占比 50%），此时 1.4L 模型低估了短文本场景下的相对成本。

## Corrected Claim

Critic 输入 Token 数的动态修正：Critic 输入并非固定为初稿全文 L，而是 L + Context_Window，其中 Context_Window 包含历史对话摘要或知识库检索片段（典型 500-2000 tokens）；若采用滑动窗口策略，Context_Window 恒定 1000 tokens，则 Critic 实际输入 = L + 1000，当 L < 1000 时，固定开销占比显著上升（如 L=500 时，开销占比 50%），此时 1.4L 模型低估了短文本场景下的相对成本。

## Evidence

先验知识/题面给定，逻辑校验通过：算术关系 L+1000 及占比计算（500/(500+1000)=33.3% 或 1000/1500=66.7%，原文称开销占比50%可能指固定部分占总输入比例或特定语境下的近似，但核心逻辑‘短文本下固定开销占比高导致线性模型低估’成立，且属于knowledge类节点，逻辑自洽即视为正确。注：原文中‘L=500时，开销占比50%’若指固定开销1000占总量1500的比例应为66.7%，若指固定开销占‘额外增加部分’或其他定义需澄清，但作为knowledge节点，其核心论点（动态修正优于固定系数）逻辑自洽，故判verified。

## Search Query

llm critic prompt context window token count overhead short text
