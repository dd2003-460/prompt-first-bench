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
## 实验结果 (2026-11-04, n=2/臂×题, 60 runs, all post-fix)

**60 runs 完成** (S0–S5 × Q1-Q5 × r1/r2)，scoring.md 已生成（含 per-dimension + per-question 分解）。

| 区间 | Δ (avg total) | 判定 |
|------|--------------|------|
| S0→S1 (目标分解) | +0.043 | 正贡献 |
| **S1→S2 (信息调研)** | **+0.100** | **最大增益点**（M1 +0.285, M6 +0.600） |
| S2→S3 (行动分解) | -0.065 | 负效应：冗余规划稀释已有 sources |
| S3→S4 (执行验证) | +0.032 | 小幅正 |
| S4→S5 (终审) | +0.012 | 微正 |

**核心发现**：autoresearch 系统的价值集中在 **stage 02（信息调研）**——给模型真实搜索能力是整条曲线最大增益（+0.100）。规划（01/03）和审查（04.5）的边际收益远小于"给工具"。之前 S1→S2 为负是因为"要求调研但没给工具"；给了 ego-browser 后翻转为最大正增益。

**设计启示**：如果只能选一个阶段投入工程资源，选 stage 02（给模型真实搜索/调研能力）。

**限制**：n=2 方向性；judge=被评模型自身 (conf≤0.7)；D1=N/A（Python 3.9 vs GPT Researcher 3.10+）。

**下一步**：n≥4 复确认 → 异源 judge（Gemini via ego-browser，需重新登录）→ 论文初稿。
