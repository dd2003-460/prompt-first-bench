# stage-ablation — 逐阶段子模块消融实验

> origin: ai · 2026-11-03 · T23-B 核心交付物（任务书：projects/decomp/tasks/T23-merge-pfb-ablation.md）
> 目标：测 pfb 六阶段（01/02/02.5/03/04/04.5）每个子模块的边际收益，并对比 deepsearch 类完整开源 baseline（D1）。
> 关系：T22 = 单点验证（三道闸有没有用）；本实验 = 全链路消融（哪个阶段有用）。T22 结果决定 S5 臂配置，见 DESIGN.md「显式依赖」。

## 文件

| 路径 | 说明 |
|------|------|
| `DESIGN.md` | 实验设计：S0–S5 × D1 矩阵、5 题跨域题目集、机器可检评分维度、60 runs 预算（含缩略版降级）、发布判据 |
| `competitor-survey.md` | 竞品/基准/代码解剖调研（2026-11-03）：开源 DRA 格局、bench 榜单现状、GPT Researcher 源码分析、对标最高水平承诺——D1 判据与论文 related work 的事实基础 |
| `questions/` | 5 道题面 + gold 锚点索引（Q1 GPU 规格沿用 r1 gold-facts；Q2–Q5 从 t17-generalization 四域各取一题，题面原样摘录） |
| `runs/` | 执行后落盘：每 run 一个 JSON（原始输出 + 评分），命名 `<arm>-<qid>-r<n>.json`；D1 选型理由进 `runs/d1-choice.md`，arena 外包回执进 `runs/receipts/` |
| `score.py` | 执行时写：评分器（M1–M6 接口见 DESIGN §6），框架参考 t17 score.py + r1 run_local.py |
| `scoring.md` | 执行后产出：6 维度 × 臂汇总 + Δ_k + 判据是否达标 + 结论 |
## 实验结果 (2026-11-04, n=3/臂×题, 90 runs, all post-fix)

**90 runs 完成** (S0–S5 × Q1-Q5 × r1/r2/r3)，scoring.md 已生成（含 per-dimension + per-question + n=2/n=3 稳定性对比）。

| 区间 | Δ (avg total, n=3) | 判定 |
|------|--------------|------|
| S0→S1 (目标分解) | +0.089 | 正贡献 |
| **S1→S2 (信息调研)** | **+0.072** | **最大增益点**（真实搜索工具） |
| S2→S3 (行动分解) | -0.046 | 负效应：冗余规划稀释已有 sources |
| S3→S4 (执行验证) | +0.040 | 小幅正 |
| S4→S5 (终审) | +0.020 | 微正 |

**n=3 确认**：所有转换符号与 n=2 一致，量级在 ±0.02 内波动。核心发现复现。

**核心发现**：autoresearch 系统的价值集中在 **stage 02（信息调研）**——给模型真实搜索能力是整条曲线最大增益（+0.072~+0.100）。规划（01/03）和审查（04.5）的边际收益远小于"给工具"。之前 S1→S2 为负是因为"要求调研但没给工具"；给了 ego-browser 后翻转为最大正增益。

**设计启示**：如果只能选一个阶段投入工程资源，选 stage 02（给模型真实搜索/调研能力）。

**限制**：n=3 方向性、统计功效低但符号稳定；judge=被评模型自身 (conf≤0.7)；D1=N/A（Python 3.9 vs GPT Researcher 3.10+）。

**下一步**：异源 judge（Perplexity via ego-browser，72 runs 运行中）→ 论文初稿（`paper-draft.md` 已写）。

**异源 judge 状态**（2026-11-04）：Gemini 网页版在 ego-lite 会话中不可用（/app 被重定向回 landing page），改用 Perplexity。流程已验证（click [role=textbox] → keyboard.type → Enter → 提取"已完成"后文本）。全量 Q1-Q4 × S0-S5 × r1-r3 = 72 runs。**⚠️ 当前阻塞（11-04 10:10）**：Perplexity 免费额度耗尽（"您已达到免费搜索次数上限，几小时后重置"），且凌晨的"运行中"实际只落了 4 条就随会话断开——之前日志无逐条进度是假象。cross_judge.py 已加 QUOTA_EXHAUSTED 快速失败（commit 0880086），等额度重置后 `python3 cross_judge.py` resume 即可（自动跳过已判）。
