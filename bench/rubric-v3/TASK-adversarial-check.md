# 对抗核验任务书 — rubric-v3 草案

> origin: ai · 2026-10-29 · 供 arena agent mode 执行
> 对象：`bench/rubric-v3/DRAFT-rubric-v3.md`（pfb 仓 rubric-v3 分支）
> 角色：你是审稿人，任务是**找这个评分标准测不出东西或测出假东西的地方**。不是夸它设计得巧。

## 背景（你需要的最小上下文）

- pfb = prompt-first 六阶段 pipeline（目标分解→信息调研→交叉验证→行动分解→执行验证→终审），要证明"这套流程比无引导/开源框架 prompt 产出更好"
- decomp L1 消融已证明：输出契约是前提（Δ=10.63/20）、草稿区核心、scratch/template 不显著——那是单步 prompt 组件消融
- 本 rubric 是下一步：评整个 pipeline 的终态产出（outcome）+ 全程行为（process），双层分开报
- 域第一格 = 27B 本地推理硬件选型（gold 树在 decomp 仓 bench/gold/，可对照）

## 六个质询方向（逐条给结论 + 证据）

### Q1 循环论证检查
O3 用 gold 节点命中计分，但 gold 本身是 Lead（我）写的。如果 rubric 和 gold 同源，"命中 gold"可能只测了"像不像我写的"而不是"好不好"。找出所有这样的同源依赖，给出解耦方案（或证明不可解耦）。

### Q2 维度独立性
O1-O4 和 P1-P4 共 8 个维度，哪些实际上高度相关（比如 O2 矛盾深度高的 run 大概率 P4 也高）？相关的话分开报还有意义吗？用 decomp L1 已有数据（bench/runs/ablation-L1/ 下 11 变体 × 33 plans）做相关性预检——能算的先算，不能算的说清需要什么数据。

### Q3 判据机械性
逐条检查 §1-§2 每个档位的判据：judge 拿着两条不同质量的产出，能不能在不查外部资料的情况下稳定打出不同分？标出所有"需要 judge 自由裁量"的判据，给出机械化改写建议。重点查 O2 的 L3 判定和 P4 的边界类型三分类。

### Q4 候选空间完备性指令（§4）的漏洞
这是给被测 prompt 加的"维度自选+两端覆盖+低先验深评"通用规则。攻击它：
- 模型会不会形式合规实质敷衍（每维度列几个名字但不真搜）？怎么从产出里检测敷衍？
- "划分维度由被测者自选"会不会被钻空子——选两个退化的维度（比如把代际拆成"新/旧"两档）让"覆盖两端"变成 trivially satisfied？给出检测判据
- "搜索不设上限 + 2h wall-clock"在实操中会怎样？给一个最坏情况的时长估计和触发率预测
- 这个指令本身会不会泄漏答案（提到"低先验候选必须纳入"就暗示了冷门选项可能最优）？泄漏的话 V1 vs V0 的对比还干净吗？

### Q5 统计设计
§3.3 的 n 估计逻辑：以 L1 效应量为上限估计是否合理？新维度（O1/O2 层级化）的预期效应量应该参考什么？V0 复用还是重跑（开放问题 5）对 power 的影响？给一个具体的 n × runs × 题数矩阵和对应的 MDE。

### Q6 文献对标
搜一下 LLM-as-judge 评分标准的现有实践（rubric design for agent evaluation, process reward model, outcome vs process scoring in RLHF），看这个双层设计有没有已知陷阱。特别关注：process 评分在 LLM judge 下的可靠性证据（有没有论文说过程分噪声大不建议单独用？）。

## 输出格式

```json
{
  "kind": "ralph_web_llm_cross_check",
  "target": "rubric-v3-draft",
  "responses": [
    {"provider_id": "<你的会话标识>", "verdict": "pass|revise|reject",
     "findings": [{"q": "Q1..Q6", "severity": "blocker|major|minor", "issue": "...", "fix": "..."}],
     "observed_at": "<ISO8601 带时区>"}
  ]
}
```

blocker = 不改就不能跑实验；major = 跑了但结论要打折扣；minor = 记录即可。