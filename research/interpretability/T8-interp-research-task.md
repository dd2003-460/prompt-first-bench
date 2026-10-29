# origin: ai
# T8-可解释性研究 · 前沿文献调研任务卡（r51）

## 背景
我们在做一个 prompt-first 六阶段流程的优化研究（prompt-first-bench）。核心问题：**如何科学地度量单个 prompt 组件（如 candidate-freeze / owner-tag / evidence-url / negative-example）对最终输出质量的因果贡献**。

我们初步自研了一套方法：用 LLM 最后一层 hidden state（通过 llama.cpp `/embedding` + `--pooling last`）当探针，量"删掉某组件后表征偏离度"，偏离大的优先做正式消融实验。但这套是**拍脑袋定的，没查过领域里有没有成熟做法**。本任务就是去查。

## 要调研的三个方向（每个都要找 ≥2 个独立来源 + 标注置信度 conf）

### 方向 1 · Prompt ablation / sensitivity 的成熟方法
- 测"单个 prompt 组件对输出的因果贡献"，学界/业界有没有标准范式？
- 关键词线索：prompt ablation, prompt sensitivity analysis, component-wise prompt contribution, instruction ablation, "which part of the system prompt matters"
- 要找：代表性论文/框架、它们怎么设计对照、怎么判显著、有没有现成工具

### 方向 2 · LLM interpretability 归因 prompt 段
- 用模型内部状态（hidden states / activations）来归因"哪段 prompt 起作用"，有哪些成熟技术？
- 关键词线索：representation engineering, activation patching / activation addition, causal tracing, probing classifiers, attribution methods, "mechanistic interpretability for prompt components", logit lens
- 特别要查：**activation patching / causal tracing 是不是比"hidden state 余弦偏离度"更标准的因果归因手段？** 我们的"表征偏离度排序"在方法论上站不站得住？
- 要找：这些方法的原理、适用条件、和简单 cosine 偏离的本质区别

### 方向 3 · LLM-as-judge 的偏差与校准
- 我们用独立 AI 裁决输出质量（M8 指标）。已知漏洞：可变分母（删组件→核验条目变少→难项退出分母→分数假性抬高）、judge bias、position bias、contamination。
- 关键词线索：LLM-as-a-judge bias, judge position bias, self-preference bias, evaluation contamination, variable denominator in scoring, rubric calibration, "calibrating LLM judges"
- 要找：这些偏差的标准处理方式、固定分母/覆盖率指标是不是已有共识做法、评分校准（calibration）的成熟协议

## 产出要求
1. 每个方向：列出 3-5 个关键工作（标题 + 链接 + 一句话结论 + conf 高/中/低）
2. **对照判断**：把我们自研的"hidden state 余弦偏离度 top-k 锁定"方法，和方向 2 的成熟方法对比——我们是重复造轮子、还是确实有 gap？该直接采用哪个成熟方法替代？
3. **给 C3 实验设计的 3-5 条具体修正建议**（基于文献，不是泛泛而谈）
4. 明确标出哪些结论 conf 低、需要进一步核实

## 边界
- 这是纯文献调研，不要跑任何实验、不要改代码
- 找不到的就如实说找不到，别编
- 完成后停下汇报，把完整调研写入 research/interpretability/literature-survey.md