# N229: 知识库冲突检测的逻辑判定标准：设新证据向量为 $v_{new}$，历史知识向量为 $v_{old}$，若余弦相似度 $\cos(v_{new}, v_{old}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90, N91

## Claim

知识库冲突检测的逻辑判定标准：设新证据向量为 $v_{new}$，历史知识向量为 $v_{old}$，若余弦相似度 $\cos(v_{new}, v_{old}) > 0.95$ 且语义方向相反（由 LLM 判定为矛盾而非补充），则触发冲突；该阈值 0.95 是基于 100 组标注矛盾/相似对的 ROC 曲线最优分割点确定的，误报率 FPR < 5%。

## Corrected Claim

知识库冲突检测的逻辑判定标准：设新证据向量为 $v_{new}$，历史知识向量为 $v_{old}$，若余弦相似度 $\cos(v_{new}, v_{old}) > 0.95$ 且语义方向相反（由 LLM 判定为矛盾而非补充），则触发冲突；该阈值 0.95 是基于 100 组标注矛盾/相似对的 ROC 曲线最优分割点确定的，误报率 FPR < 5%。

## Evidence

先验知识/题面给定，逻辑校验通过
