# N306: 上下文溢出风险量化：5 步累计 20000 tokens + 预留 6000 tokens = 26000 tokens，远低于 max_model_len=2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

上下文溢出风险量化：5 步累计 20000 tokens + 预留 6000 tokens = 26000 tokens，远低于 max_model_len=262144；但需考虑系统提示 (System Prompt) 和历史对话 (History) 的累积效应，若历史窗口保留最近 3 轮完整对话，每轮额外消耗约 5000 tokens，需计算总上下文占用率是否超过 80% 安全阈值

## Corrected Claim

上下文溢出风险量化：5 步累计 20000 tokens + 预留 6000 tokens = 26000 tokens，远低于 max_model_len=262144；但需考虑系统提示 (System Prompt) 和历史对话 (History) 的累积效应，若历史窗口保留最近 3 轮完整对话，每轮额外消耗约 5000 tokens，需计算总上下文占用率是否超过 80% 安全阈值

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（20000+6000=26000 < 262144），且关于系统提示和历史对话累积效应的风险提示符合LLM上下文管理的基本工程逻辑。

## Search Query

LLM context window utilization rate safety threshold long conversation
