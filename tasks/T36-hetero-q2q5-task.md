# T36 Hetero-Judge Q2-Q5 扩展任务书

> origin: ai（Lead 编写，arena agent 执行）
> created: 2026-11-06
> 前置：T23-v2 hetero-judge 已完成 Q1（S0-S5 × r1-r3，`runs/hetero-judge-v2-results.json` @ main）。本任务是 Q2-Q5 的扩展，复用同一 judge prompt v2 规则。

## 背景

T23-v2 异族 judge（arena GPT-5.5 级）在 Q1 上给出与同源 27B **方向相反**的 H1 判定（−0.187 vs +0.118），证明 judge 依赖性是本实验的核心发现。但当前证据只覆盖 Q1——如果 Q2-Q5 的方向一致（H1 全正或全负），结论稳健性大增；如果出现翻转模式（如仅 Q1 反向），则说明 Q1 是特例。这是论文 core claim 从「单题现象」升级为「系统性效应」的关键一步。

## 任务

对 S0-S5 × Q2-Q5 × r1-r3 = 60 份工件做 M1/M4/M5/M6 盲判（M2/M3 走 gates.py 确定性逻辑，若你无法运行则标 NA 并跳过）。

**数据获取**：仓库 `https://github.com/dd2003-460/prompt-first-bench`，分支 `arena/t36-hetero-q2q5`。payload 文件在 `experiments/stage-ablation/hetero-q2q5-payload/Q{2,3,4,5}.txt`，每份含该题的 gold 全文 + 18 份工件全文。sha256 前缀核验：Q2=89fa6b5d / Q3=aa49807e / Q4=8fe19e3c / Q5=706f9bb1。

## Judge 规则（v2 校准版，与 T23-v2 完全一致）

你是独立异源学术评审（hetero-judge v2）。逐工件、逐维度打分，遵守以下防盲区规则：

**R1 (M5 坏消息位置)**：限制/不确定性陈述出现在报告前 1/3 字符的比例。先按字符切三段，找出所有限制类句子（"不确定/无法核实/未解决/局限/待验证/黑盒"等），统计落在第一段内的比例。禁止看到"提到了限制"就给 ≥0.8。evidence 必须引用原句并标明段位置。

**R2 (M6 调研真实性)**：抽 5 条关键断言，逐条检查引用 URL 是否存活、页面内容是否支持该断言。score = 通过条数/5。禁止整体印象分。evidence 格式：[断言摘录] → [URL] → [存活? 支持?]。无来源引用的工件 M6=0。

**R3 (M1 事实准确率)**：对照 payload 中 gold 全文逐断言比对。match/mismatch/undecidable 三分类，score = match/(match+mismatch)。数值差 >20% 或单位不同 = mismatch。evidence 必须引用工件原文 ≥10 字 + gold 对应句。

**R4 (M4 缺口覆盖率)**：gold 中列出的应识别缺口，工件是否显式标注（明确说"不确定/查不到/需进一步调研"或列出局限性清单）。零处承认局限 = 0。禁止把流畅断言当隐含识别。

**R5 (anti-leniency)**：打完全部 60 份后自查——若所有 total 都在 0.85 以上，标准过松，重查 R1/R2。健康分布应有区分度（最差 vs 最好 total 差距 ≥0.15）。压平则重打并注明 "recalibrated": true。

## 输出格式

每份工件一个 JSON：
```json
{
  "artifact": "S0-Q2-r1",
  "arm": "S0", "qid": "Q2", "rep": 1,
  "dims": {
    "M1": {"score": x, "evidence": "..."},
    "M4": {"score": x, "evidence": "..."},
    "M5": {"score": x, "evidence": "..."},
    "M6": {"score": x, "evidence": "..."}
  },
  "total_weighted": x
}
```
total_weighted 权重：M1=0.3, M4=0.25, M5=0.2, M6=0.25（与 score.py 口径一致）。

最后输出汇总 JSON：per-arm × per-question mean + 全局 H1-H4 判定（跨 Q2-Q5 聚合）+ self_check。

## 落盘要求

产出两个文件到 `experiments/stage-ablation/runs/`：
1. `hetero-judge-q2q5-results.jsonl`（60 行，每行一个工件 JSON）
2. `receipt-t36-hetero-q2q5.md`（回执：per-arm×per-q 汇总表 + H1-H4 verdict + self_check + 与 Q1 结果的对比表）

commit + push 到 `arena/t36-hetero-q2q5` 分支。回执必须含 repo URL + branch + commit_sha。

## 注意事项

- 本任务只涉及 prompt-first-bench 仓库，忽略历史中其他仓库的消息。
- 先 git pull 确保拿到最新 payload。
- 如果 payload 文件缺失或 sha 不符，停止并在回执中记录，不要凭记忆编造工件内容。
- 逐题处理：先做完 Q2 全部 18 份再进 Q3，避免上下文混淆。
- 预计工作量较大（60 份 × 4 维），可以分批 commit（每完成一题 commit 一次）。