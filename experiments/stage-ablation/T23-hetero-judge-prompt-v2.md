# T23 Hetero-Judge Prompt v2（blind-spot 校准版）

> origin: ai
> generated: 2026-11-05
> 用途：arena 真异源 judge 第二轮（v1 = 任务书原版 prompt；v2 = + 流程性盲区提醒 + anti-leniency 校准）。
> 设计原则：**只提醒"哪里容易漏看"（流程性），不暗示"哪个 arm 应该高"（结论性）**，保留异源性。

## 0. 为什么需要 v2

半异源实验（Qwen2.5-7B, LM Studio）暴露了三个系统性盲区，全部有数据支撑：

| 盲区 | 证据 | 机制 |
|------|------|------|
| **M5 坏消息位置**：7B 给所有工件 0.8–0.98，而确定性 gate 逻辑下多数应为 0 | 16/16 工件 Δ≥+0.60，最大 +0.98 | 7B 把"报告里任何提到限制的句子"都算 M5 命中，不管它在前 1/3 还是末尾；且 evidence 是转述不是定位 |
| **M6 调研真实性**：7B 给 0.8–0.9，同源 27B 给 0.0–1.0 大幅波动 | 12/16 工件 Δ≥+0.80 | 7B 的 evidence 写"大部分断言均有社区实测数据支持"——这是印象分，没逐条核对 URL 存活和来源-断言对应关系 |
| **leniency 压缩**：所有 arm 挤在 0.85–0.92（range=0.07），同源 range=0.18 | T23-semihetero-analysis.md | 弱 judge 没有能力拉开差距 → ablation 曲线被压平 → H2/H3 误判 |

**注意**：M2（无来源数字率）在半异源跑里也出现大分歧（Δ 最高 +0.95），但 M2 按设计是 gates.py 确定性正则计算、不该由 LLM 打。这说明半异源脚本把 M2 也交给了 LLM，属于**实现 bug**，不是模型盲区。v2 明确：M2/M3 走确定性 gate，LLM 只判 M1/M4/M5/M6。

## 1. v2 prompt 模板（发给 arena agent）

```
你是独立异源学术评审（hetero-judge v2）。对 stage-ablation 实验的 18 份工件做盲判。
仓库：https://github.com/dd2003-460/prompt-first-bench （分支 arena/4a614e63-prompt-first-bench）
先读 tasks/T23-stage-ablation-hetero-judge-task.md 全文，再按下面规则执行。

【维度分工】
- M2（无来源数字率）、M3（矛盾对数）：用仓库 experiments/stage-ablation/gates.py 的确定性逻辑计算，不要凭印象打分。把 gates 输出原样填入。
- M1（事实准确率）、M4（缺口标注覆盖率）、M5（坏消息位置）、M6（调研真实性）：由你判断，但必须遵守下面的防盲区规则。

【防盲区规则 — 每条都有已知失败案例】

R1 (M5)：坏消息位置 = 限制/不确定性陈述出现在报告前 1/3 字符的比例。
  - 判定方法：先把报告按字符切三段，找出所有限制类句子（"不确定/无法核实/未解决/局限/待验证/黑盒"等），统计落在第一段内的比例。
  - 禁止：看到报告"提到了限制"就给 ≥0.8。提到 ≠ 在前面。
  - evidence 必须引用该句子的原文并标明它出现在第几段（如 "seg1, char 120-180: '…'"）。

R2 (M6)：调研真实性 = 可定位来源且实际支持对应断言的比例。
  - 判定方法：抽 5 条关键断言，逐条检查其引用的 URL 是否存活、页面内容是否真的支持该断言。score = 通过条数/5。
  - 禁止："大部分断言有来源支持"这类整体印象分。必须逐条。
  - evidence 格式：逐条列 [断言摘录] → [URL] → [存活? 支持?]。

R3 (M1)：事实准确率对照 gold/*.md 逐断言比对。
  - match/mismatch/undecidable 三分类，score = match/(match+mismatch)。
  - 禁止：因为"方向一致"就判 match。数值差 >20% 或单位不同 = mismatch。
  - evidence 必须引用工件原文 ≥10 字 + gold 对应句。

R4 (M4)：缺口覆盖率。gold 中列出的应识别缺口，工件是否显式标注。
  - 显式 = 明确说"不确定/查不到/需进一步调研"，或列出"局限性/待验证项"清单。
  - 禁止：把"通篇流畅的断言"当作隐含识别。零处承认局限 = 0。

R5 (anti-leniency 校准)：打完 18 份后自查一次——
  - 如果所有工件 total 都在 0.85 以上，说明标准过松，重新检查 R1/R2 是否真的逐条执行了。
  - 健康的分布应该有区分度：最差工件和最好工件的 total 差距应 ≥0.15。
  - 如果自查发现压平了，重打一遍并在输出里注明 "recalibrated": true。

【输出格式】每份工件一个 JSON（同任务书），额外加两个字段：
{
  "artifact": "...", "arm": "...", "qid": "...",
  "dims": {"M1": {...}, "M2": {"score": x, "source": "gates.py"}, "M3": {"score": x, "source": "gates.py"}, "M4": {...}, "M5": {...}, "M6": {...}},
  "total_weighted": x,
  "self_check": {"all_above_085": false, "spread": 0.x}
}

最后输出汇总：per-arm weighted mean + H1-H4 假设判定（与任务书一致）。
```

## 2. 预期效果与验证方式

- **H1（S1>S0）**：v1/v2 都应维持 confirm（两轮 judge 方向一致，最稳健的结论）。
- **H2/H3**：v2 拉开区分度后，7B 那轮的 "H2 REFUTED / H3 REFUTED" 是否翻回与同源一致 —— 这是检验"judge 能力 vs 真实效应"的关键对比。
- **方法学产出**：v1 vs v2 的同模型自比（同一 arena 模型跑两版 prompt）直接量化"prompt 校准对 ablation 结论的影响"，可写进 paper-draft.md 的 limitations/threats 一节。

## 3. 使用顺序

1. arena v1 结果落地（当前在跑）→ 存 `hetero-scores-arena-v1.jsonl`
2. 新会话发 v2 prompt → 存 `hetero-scores-arena-v2.jsonl`
3. 三方对比表：same-source 27B / arena-v1 / arena-v2 → 更新 T23-semihetero-analysis.md 为 T23-final-analysis.md