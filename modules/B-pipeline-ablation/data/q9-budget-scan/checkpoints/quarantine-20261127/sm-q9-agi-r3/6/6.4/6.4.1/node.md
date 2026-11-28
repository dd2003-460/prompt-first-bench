# N106: 幻觉率实时监控的计算窗口：滑动窗口大小为最近 100 个生成结论，每新增 1 个结论即触发一次幻觉率更新，计算公式为 Hallucination Rate = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

幻觉率实时监控的计算窗口：滑动窗口大小为最近 100 个生成结论，每新增 1 个结论即触发一次幻觉率更新，计算公式为 Hallucination Rate = (Number of Failed Fact-Check / 100) × 100%，其中 Fact-Check 通过 RAG 检索比对和逻辑一致性检查完成

## Corrected Claim

幻觉率实时监控的计算窗口：滑动窗口大小为最近 100 个生成结论，每新增 1 个结论即触发一次幻觉率更新，计算公式为 Hallucination Rate = (Number of Failed Fact-Check / 100) × 100%，其中 Fact-Check 通过 RAG 检索比对和逻辑一致性检查完成

## Evidence

先验知识/题面给定，逻辑校验通过
