# N258: 长上下文瓶颈工作点：Input_Tokens=15000 (System 1500 + RAG 10000 + Hist 3500), Output_Token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

长上下文瓶颈工作点：Input_Tokens=15000 (System 1500 + RAG 10000 + Hist 3500), Output_Tokens=1300, Total=16300; 受限于V100 16GB显存与max_model_len，KV Cache膨胀导致有效吞吐下降至~50 tps，单循环T_inference ≈ 326s

## Corrected Claim

长上下文瓶颈工作点：Input_Tokens=15000 (System 1500 + RAG 10000 + Hist 3500), Output_Tokens=1300, Total=16300; 受限于V100 16GB显存与max_model_len，KV Cache膨胀导致有效吞吐下降至~50 tps，单循环T_inference ≈ 326s

## Evidence

先验知识/题面给定，逻辑校验通过：15000输入+1300输出=16300总量符合算术；V100 16GB显存下长上下文KV Cache占用大导致吞吐下降至50 tps及推理耗时约326s（16300/50≈326s）在数量级和逻辑上自洽。
