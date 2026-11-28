# N257: 短上下文工作点：Input_Tokens=2500 (System 1500 + RAG 500 + Hist 500), Output_Tokens=1300

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

短上下文工作点：Input_Tokens=2500 (System 1500 + RAG 500 + Hist 500), Output_Tokens=1300, Total=3800; 此时KV Cache占用低，Throughput_tps接近峰值(预计>100 tps)，单循环T_inference ≈ 38s

## Corrected Claim

短上下文工作点：Input_Tokens=2500 (System 1500 + RAG 500 + Hist 500), Output_Tokens=1300, Total=3800; 此时KV Cache占用低，Throughput_tps接近峰值(预计>100 tps)，单循环T_inference ≈ 38s

## Evidence

先验知识/题面给定，逻辑校验通过：总Token数计算正确(2500+1300=3800)，短上下文下高吞吐(>100tps)与低延迟(38s)符合LLM推理基本规律
