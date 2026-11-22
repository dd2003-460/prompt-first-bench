# N353: Nielsen Norman Group的100ms阈值原文针对的是‘用户动作到系统反馈’的响应时间（Response Time），在LLM场景中对应从用户提交

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

Nielsen Norman Group的100ms阈值原文针对的是‘用户动作到系统反馈’的响应时间（Response Time），在LLM场景中对应从用户提交Prompt到首个Token输出的时间（TTFT），而非流式生成过程中的Token间延迟（ITL）

## Corrected Claim

Nielsen Norman Group的100ms阈值原文针对的是‘用户动作到系统反馈’的响应时间（Response Time），在LLM场景中对应从用户提交Prompt到首个Token输出的时间（TTFT），而非流式生成过程中的Token间延迟（ITL）

## Evidence

先验知识/题面给定，逻辑校验通过：Nielsen Norman Group 的 100ms 阈值确实定义为系统对用户输入的响应时间（Response Time），在 LLM 流式输出场景中，该概念对应首字延迟（TTFT），而非后续 Token 间的生成间隔（ITL），逻辑自洽且符合行业共识。
