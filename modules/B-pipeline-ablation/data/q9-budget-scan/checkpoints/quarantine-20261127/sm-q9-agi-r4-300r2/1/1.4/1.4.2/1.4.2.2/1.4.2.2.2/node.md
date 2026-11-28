# N266: 假设生成任务的 Token 消耗基准：单次假设生成平均 Input Tokens L_in_hyp ≈ 1200 (包含文献摘要+问题陈述), Output T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

假设生成任务的 Token 消耗基准：单次假设生成平均 Input Tokens L_in_hyp ≈ 1200 (包含文献摘要+问题陈述), Output Tokens L_out_hyp ≈ 300 (结构化 JSON 假设)；在 Throughput_eff=45 tok/s 下，单次生成耗时 T_hyp ≈ (1200*1 + 300*1.5) / 45 ≈ 33.3s (假设输出耗时系数 1.5x)；每小时可生成 N_hyp/hour ≈ 108 个假设，需与 Critic 验证吞吐匹配。

## Corrected Claim

假设生成任务的 Token 消耗基准：单次假设生成平均 Input Tokens L_in_hyp ≈ 1200 (包含文献摘要+问题陈述), Output Tokens L_out_hyp ≈ 300 (结构化 JSON 假设)；在 Throughput_eff=45 tok/s 下，单次生成耗时 T_hyp ≈ (1200*1 + 300*1.5) / 45 ≈ 33.3s (假设输出耗时系数 1.5x)；每小时可生成 N_hyp/hour ≈ 108 个假设，需与 Critic 验证吞吐匹配。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (1200 + 450) / 45 = 33.33s 正确，3600 / 33.33 ≈ 108 正确，参数设定符合大语言模型推理的典型量级与逻辑自洽性。

## Search Query

LLM hypothesis generation token count benchmark research agent
