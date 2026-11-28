# N63: 云端 API 成本函数 C_api(L) 的阶梯结构：不同提供商定价不同（如 $0.5/1k input tokens, $1.5/1k output toke

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

云端 API 成本函数 C_api(L) 的阶梯结构：不同提供商定价不同（如 $0.5/1k input tokens, $1.5/1k output tokens），总成本 C_api(L) = L_in * P_in + L_out * P_out；若 L_in=L_out=L/2，则 C_api(L) = L*(P_in+P_out)/2

## Corrected Claim

云端 API 成本函数 C_api(L) 的阶梯结构：不同提供商定价不同（如 $0.5/1k input tokens, $1.5/1k output tokens），总成本 C_api(L) = L_in * P_in + L_out * P_out；若 L_in=L_out=L/2，则 C_api(L) = L*(P_in+P_out)/2

## Evidence

[rework-angle r1] 来源[2]和[3]确认了LLM API基于输入/输出Token分离计费的原理，公式推导符合代数逻辑，且具体价格作为示例（如$0.5/$1.5）符合市场常见量级，逻辑自洽且有间接支持。

## Search Query

LLM API pricing structure input output token cost formula

## Retrieval Sources

- {'url': 'https://www.csdn.net/article/2026-11-25/171317814&rut=27bb4d6536add431cec152f44e97774c6cc2c21667a55968d4c8ecf737a4b374', 'type': 'ddg', 'title': '大模型API代理商水有多深？选错平台API调用成本翻倍'}
- {'url': 'https://blog.csdn.net/weixin_29696711/article/details/161407630&rut=9f059d938f5b4e109005d72e7ccd4188aa748df655b091d2e2412f740aed29fb', 'type': 'ddg', 'title': '2026年大模型api定价全解析：从计费原理到成本优化实战-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_29057237/article/details/163835557&rut=2f5141289e444b591c935cf538ed63f9827ef670aa09b5f5592af8c1cae079eb', 'type': 'ddg', 'title': '大模型api成本深度解析：从显性账单到隐性成本与架构优化-csdn博客'}
