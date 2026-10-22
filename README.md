# prompt-first-bench

调研目标：**prompt-first 流程（1-loop）究竟有没有提升？对不同 AI 模型提升如何？**

- 执行通道：LMArena agent mode（arena 读本仓库 `tasks/` 任务书 + `loop/` 阶段定义 + `sop/` 链路 SOP）
- 流程权威源：`loop/prompt-first/00..04.5`
- 链路 SOP：`sop/arena-loop-pipeline.md`
- 评分：`rubric/`（任务内引用）
- 产出：`bench/runs/<task>/<variant>/`（run 输出 + score + summary）

## 研究问题（任务书 001）

1. 拆解任务（01 目标分解的正交+完备+递归原子）对最终成功率的影响
2. 正交完备性对最终成功率的影响（对照：无分解/非正交分解/正交完备）
3. 每个具体要求（02.5 交叉验证 / 逐阶段落盘 / 04.5 反方复核）的边际提升
4. 跨模型差异（arena 会话可用模型 × 变体矩阵）
