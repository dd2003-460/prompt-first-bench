# T53-B12 阶段 03：动作分解（执行前计划）

- 上游：02 调研 + 02.5 裁定
- 本阶段只排动作，不写结果

## 1. 动作清单（按依赖排序）

| # | 动作 | 产物 | 依赖 | 可离线？ |
|---|---|---|---|---|
| A1 | 选 3 道新题并写题面 + gold 要点 | `questions/T53-B12-new3-questions.md` | — | ✅ |
| A2 | 建 L1 公开分表 + 三层可比性定义 | `sm-bench-sota-criteria.md` v3 | A1（题→bench 映射） | ✅ |
| A3 | 探测生成端 8787 / judge 1234 / 出网 | 探测记录（04 §1） | — | ✅ |
| A4 | 若 A3 通：注册 qid 进 `ablation_harness.QUESTIONS` | 代码改动 | A3 | ❌ 需端点 |
| A5 | 若 A3 通：`s5_pipeline.py --qs … --reps 3` | `runs-s5-sm-b12/` | A4 | ❌ |
| A6 | 若 A3 通：B-face n=3 median | 分数 | A5 | ❌ |
| A7 | 若 A3 通：L0 对照（LangGraph react agent 同模型同 hook） | 对照分 | A5 | ❌ |
| A8 | 若 A3 不通：写 blocked run 记录（分数 null）+ 阻塞证据 | `runs-s5-sm-q*.json` | A3 | ✅ |
| A9 | 更新 bench report §6 五题表 | `s5-sm-bench-report.md` | A2/A8 | ✅ |
| A10 | 机检 AC1–AC6 | `verify-t53-b12.py` | A1/A2/A8/A9 | ✅ |

## 2. 分支处置（A3 两种结局）

- **通** → 走 A4–A7，报告出分数差，AC3/AC4 满分。
- **不通** → 走 A8–A10，AC3 记 `null + blocked`，报告写明"0/5 可判"，并把 A4–A7 作为 Lead 侧待办。
  这条分支**不是失败**，任务书"降级"节允许：只降通道不降流程。

## 3. 风险

1. 注册遗漏 → E17 静默回退 gpu 题（历史事故，报告 #11）→ 必须在命令前显式校验 `QUESTIONS` 含新 qid。
2. 单次 synthesis 方差（报告 #18/#19：同树 0.857↔1.0）→ n=3 median 偏低，建议 n≥5。
3. 自建题 gold 未核 → 判分前须由人复核，否则"数字正确"那 0.5 分不可信。
