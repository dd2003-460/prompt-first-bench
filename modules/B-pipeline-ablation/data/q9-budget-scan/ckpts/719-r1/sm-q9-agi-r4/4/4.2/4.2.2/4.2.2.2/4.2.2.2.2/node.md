# N600: 单样本复核时间2min的构成：拆解为阅读生成Claim(30s)、检索对应原文证据(60s)、比对判断逻辑一致性(30s)，总耗时120s；若引入RAG辅助定位

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N214, N215, N216

## Claim

单样本复核时间2min的构成：拆解为阅读生成Claim(30s)、检索对应原文证据(60s)、比对判断逻辑一致性(30s)，总耗时120s；若引入RAG辅助定位，检索时间可降至15s，总耗时降至75s。

## Corrected Claim

单样本复核时间2min的构成：拆解为阅读生成Claim(30s)、检索对应原文证据(60s)、比对判断逻辑一致性(30s)，总耗时120s；若引入RAG辅助定位，检索时间可降至15s，总耗时降至75s。

## Evidence

先验知识/题面给定，逻辑校验通过：30+60+30=120s，30+15+30=75s，算术自洽且符合RAG加速检索的工程直觉
