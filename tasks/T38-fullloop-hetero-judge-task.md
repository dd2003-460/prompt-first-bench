# T38 Fullloop S04 异族盲判任务书

> origin: ai（Lead 编写，arena agent 执行）
> created: 2026-11-06
> 前置：T8-C3 fullloop matrix generation 完成（26 份有效 4-stage S04 终稿，9 configs × 2 domains × 2 seeds）。本地同族 27B judge 全部打 10/10（自偏好，无区分度），keyword coverage 66-80% 粗判无显著差异——需要异族 frontier judge 做 publication-grade 评分。

## 【强制段】

你是 arena agent，工作仓库 = `prompt-first-bench`，分支 `arena/t38-fullloop-judge`。先 `git fetch` 到最新并 `git ls-remote` 记录 HEAD。严格按本任务书步骤执行，产出落盘路径见【交付物】。任何通道故障报告 Lead，不得静默跳过、不得伪造数据。完成后回执必须含 repo URL + branch + commit_sha + 自报模型身份（如可知）。

**本任务只涉及 prompt-first-bench 仓库，忽略历史中其他仓库的消息。**

## 【目标】

对 26 份 S04 终稿做 M1/M4 盲判（M5/M6 走确定性逻辑，标 NA 跳过），回答两个问题：
1. **H_Ablation**：组件消融（freeze/evidence/owner 的增删组合）是否影响 S04 终稿质量？哪个 config 最好/最差？
2. **H_Domain**：D1-meeting-room vs D2-file-collab 两域难度是否一致（分数分布对比）？

## 【背景】≤10 行

- T8-C3 是 1-loop pipeline 的组件消融矩阵：S01(目标分解)→S02(信息调研)→S03(行动分解)→S04(执行验证/终稿)，每个 stage 注入不同组件（freeze=冻结契约 / evidence=证据要求 / owner=责任归属）。
- 9 个 config：A-full(全3组件)、B-nofreeze、B-noevidence、B-noowner、B-none(全删)、B-2del-fe、B-2del-fo、B-2del-eo(两两删)、B-sham(组件标签在但内容为空)。
- 已知发现（generation 层，非 S04 层）：evidence 组件在无工具环境下触发 S02 退化（38%）；S04 keyword coverage 所有 config 66-80% 无明显差异。
- 本任务是 S04 层的独立验证：keyword coverage 太粗，需要 LLM 级语义评分。
- 本地 qwen3.8-27b 同族 judge 已跑过：26/26 全部 10/10（自偏好确认，不可用）。
- Judge 规则与 T23-v2/T36 完全一致（防盲区 R1-R5），保证跨实验可比。

## 【数据获取】

仓库 `https://github.com/dd2003-460/prompt-first-bench`，分支 `arena/t38-fullloop-judge`。

Payload 文件：`experiments/fullloop-judge-payload/fullloop-s04-payload.txt`
sha256 前缀核验：**750b1054**。不符则停止并记录，不要凭记忆编造内容。

Payload 结构：
- 前半部分：两个域的 opportunity set（D1-meeting-room brief_a/brief_b 各 9-10 项，D2-file-collab brief_a/brief_b 各 10 项）——这是 gold 参考清单。
- 后半部分：26 份 S04 终稿全文，每份前有 `===== CELL <config> | <domain> | <seed> =====` 分隔头。

注意：seeda↔brief_a、seedb↔brief_b 对应（opportunity set 按 seed 匹配）。

## 【Judge 规则】（与 T23-v2/T36 一致的 v2 校准版，只评 M1/M4）

你是独立异源学术评审（hetero-judge v2）。逐工件打分：

**R3 (M1 事实准确率)**：对照 payload 中该 domain+seed 的 opportunity set 逐项核对。每个 item 三分类：match（终稿明确覆盖且数值/约束正确）/ mismatch（提到但数值错误或缺关键约束）/ undecidable（无法判断）。score = match/(match+mismatch)，undecidable 不计入分母。evidence 必须引用终稿原文 ≥10 字 + 对应 opportunity item id。

**R4 (M4 缺口覆盖率)**：opportunity set 中未被终稿覆盖的 item，终稿是否显式标注了缺口（"不确定/查不到/需进一步调研/局限"或列出未决项清单）。零处承认局限 = 0。禁止把流畅断言当隐含识别。score = 被显式标注的 gap 数 / 总 gap 数（若 gap=0 则 M4=1.0）。

**R5 (anti-leniency)**：打完全部 26 份后自查——若所有 total 都在 0.85 以上，标准过松，重查 R3/R4。健康分布应有区分度（最差 vs 最好 config mean 差距 ≥0.1）。压平则重打并注明 "recalibrated": true。

**权重**：total_weighted = M1×0.5 + M4×0.5（本实验只有两维，等权）。

## 【输出格式】

每份工件一个 JSON：
```json
{
  "artifact": "A-full-D1-seedb",
  "config": "A-full", "domain": "D1-meeting-room", "seed": "seedb",
  "dims": {
    "M1": {"score": x, "n_match": n, "n_mismatch": n, "n_undecidable": n, "evidence": "..."},
    "M4": {"score": x, "n_gaps": n, "n_flagged": n, "evidence": "..."}
  },
  "total_weighted": x
}
```

汇总 JSON 必含：
1. per-config mean（M1/M4/total，n=2-4 cells/config）
2. per-domain mean（D1 vs D2）
3. H_Ablation verdict：best/worst config + 差距 + 是否 ≥0.1（R5 阈值）
4. H_Domain verdict：D1 vs D2 mean 差 + 方向
5. r5_self_check：spread/max_score/flat/recalibrated
6. 与本地 27B judge（all 10/10）和 keyword coverage（66-80%）的对比说明

## 【交付物】（均在仓库内，commit + push 到 `arena/t38-fullloop-judge`）

1. `experiments/fullloop-judge/runs/hetero-judge-fullloop-results.jsonl`（26 行，append-only；每批写完做行数校验：新总行数=旧+本批）
2. `experiments/fullloop-judge/receipt-t38-hetero-fullloop.md`（回执：per-config/per-domain 汇总表 + H_Ablation/H_Domain verdict + r5 self_check + 与本地 judge 对比 + repo URL + branch + commit_sha）

## 【失败降级】

- 若某 cell 的 S04 内容明显不完整（<500 字符或截断），标 `"status": "degenerate"` 并跳过评分，在回执中列出。
- 若 opportunity set 与 seed 对应关系存疑，以 payload 中的分隔头为准。
- endpoint/网络故障：报告 Lead，不得静默跳过。

## 【给 Lead 的备注】

- 结果将进 pfb 论文 §5（fullloop section）或 supplementary。
- 若 H_Ablation 显示某 config 显著更好，与 F2（keyword coverage 无差异）矛盾 → 说明粗指标漏掉了语义层差异，这本身就是有价值的 finding。
- 本任务不修改任何现有文件，只新增 `experiments/fullloop-judge/` 目录下的产出。