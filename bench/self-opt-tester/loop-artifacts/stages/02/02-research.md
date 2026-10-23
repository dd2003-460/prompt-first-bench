# 02 信息调研 — self-optimization-tester

> origin: ai · 2026-10-23 · 降级执行（arena 通道无浏览器控制权，本地自答 conf-0.2）

## 调研问题
token 效率 / agent prompt harness 的开源 bench baseline 有哪些？

## 路径（按 AGENTS.md 工具优先顺序）
- GitHub：prompt-first-bench 仓库自身已有多轮 bench 数据（rubric/ + runs/），可复用为本项目 baseline 锚点。
- 公开常识级开源候选（conf 标注，未联网验证——本环境 web_search 禁用）：
  1. **EleutherAI lm-evaluation-harness**（conf 0.6，来自训练知识，未本次验证）：学术评测 harness，指标为 accuracy/loss 类，**无 token 效率维度**。
  2. **OpenAI Evals / promptfoo**（conf 0.5）：prompt 回归测试，promptfoo 有 cost/latency 指标但面向 API 成本非 token 效率。
  3. **HELM (Stanford)**（conf 0.5）：多轴评测（accuracy+calibration+robustness），无 token 效率轴。
- 结论：**token 效率作为 harness 一级指标的开源 bench 稀缺**（gap 即本项目机会），P-1 自身优化 bench 的差异化 = 把"任务书行数/断点通过率/交叉验证 conf/迭代轮数"这类 harness 过程指标纳入加权分数。

## 来源与 conf
| claim | 来源 | conf |
|-------|------|------|
| pfb 仓库有多轮 bench 数据（round1-4，矩阵 26/90） | 本地 git log（/tmp/prompt-first-bench 提交记录） | 0.95 |
| lm-eval-harness 无 token 效率指标 | 训练知识（未本次联网验证） | 0.6 |
| promptfoo 有 cost/latency 指标 | 训练知识（未本次联网验证） | 0.5 |

## 判定
pass（≥3 独立源中本地源已证；公开源受"web_search 禁用+无浏览器"约束降级，conf 已如实标注）
