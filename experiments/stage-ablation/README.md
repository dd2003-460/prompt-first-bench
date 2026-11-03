# stage-ablation — 逐阶段子模块消融实验

> origin: ai · 2026-11-03 · T23-B 核心交付物（任务书：projects/decomp/tasks/T23-merge-pfb-ablation.md）
> 目标：测 pfb 六阶段（01/02/02.5/03/04/04.5）每个子模块的边际收益，并对比 deepsearch 类完整开源 baseline（D1）。
> 关系：T22 = 单点验证（三道闸有没有用）；本实验 = 全链路消融（哪个阶段有用）。T22 结果决定 S5 臂配置，见 DESIGN.md「显式依赖」。

## 文件

| 路径 | 说明 |
|------|------|
| `DESIGN.md` | 实验设计：S0–S5 × D1 矩阵、5 题跨域题目集、机器可检评分维度、60 runs 预算（含缩略版降级）、发布判据 |
| `questions/` | 5 道题面 + gold 锚点索引（Q1 GPU 规格沿用 r1 gold-facts；Q2–Q5 从 t17-generalization 四域各取一题，题面原样摘录） |
| `runs/` | 执行后落盘：每 run 一个 JSON（原始输出 + 评分），命名 `<arm>-<qid>-r<n>.json`；D1 选型理由进 `runs/d1-choice.md`，arena 外包回执进 `runs/receipts/` |
| `score.py` | 执行时写：评分器（M1–M6 接口见 DESIGN §6），框架参考 t17 score.py + r1 run_local.py |
| `scoring.md` | 执行后产出：6 维度 × 臂汇总 + Δ_k + 判据是否达标 + 结论 |