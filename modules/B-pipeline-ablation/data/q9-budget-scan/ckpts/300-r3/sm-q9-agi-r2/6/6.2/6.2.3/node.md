# N108: 低接受率负载基准：选用 GSM8K 数学推理任务（平均生成长度 ~200 tokens，含大量逻辑推导步骤），测量 MTP×4 下的实际 Token Accep

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

低接受率负载基准：选用 GSM8K 数学推理任务（平均生成长度 ~200 tokens，含大量逻辑推导步骤），测量 MTP×4 下的实际 Token Acceptance Rate (AR_low) 及对应的 Speedup_low

## Corrected Claim

低接受率负载基准：选用 GSM8K 数学推理任务（平均生成长度 ~200 tokens，含大量逻辑推导步骤），测量 MTP×4 下的实际 Token Acceptance Rate (AR_low) 及对应的 Speedup_low

## Evidence

先验知识/题面给定，逻辑校验通过：GSM8K 是标准的数学推理基准，其生成长度通常在数百 token 级别（~200 tokens 符合量级），用于测试低接受率场景（相比代码生成等高重复率任务）在逻辑和实验设计上自洽。

## Search Query

speculative decoding low acceptance rate math reasoning benchmark
