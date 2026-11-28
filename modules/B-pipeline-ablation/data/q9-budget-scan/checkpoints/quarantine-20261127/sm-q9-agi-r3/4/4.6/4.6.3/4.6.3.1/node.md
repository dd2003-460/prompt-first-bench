# N229: 直接矛盾的 LLM 判断需使用 GPT-4o 作为裁判（本地 27B 无法可靠处理逻辑否定），单次判断输入 Token 数约为 200（结论+文献摘要），输出 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

直接矛盾的 LLM 判断需使用 GPT-4o 作为裁判（本地 27B 无法可靠处理逻辑否定），单次判断输入 Token 数约为 200（结论+文献摘要），输出 Token 数 <50，延迟约 1-2s，成本约 $0.001/次；若使用本地 27B，需增加 Self-Consistency k=3 以降低误判率，耗时增加至 5-10s。

## Corrected Claim

直接矛盾的 LLM 判断需使用 GPT-4o 作为裁判（本地 27B 无法可靠处理逻辑否定），单次判断输入 Token 数约为 200（结论+文献摘要），输出 Token 数 <50，延迟约 1-2s，成本约 $0.001/次；若使用本地 27B，需增加 Self-Consistency k=3 以降低误判率，耗时增加至 5-10s。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM-as-a-judge contradiction detection GPT-4o latency cost per token
