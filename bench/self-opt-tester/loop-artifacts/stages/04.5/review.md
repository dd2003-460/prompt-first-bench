# 04.5 反方复核 — self-optimization-tester

> origin: ai · 2026-10-23 · 找矛盾 + 验证假设（§3.0 链路）

## 假设 1：§3.0 链路可驱动自主循环
- 支持证据：本任务在零指令情况下按 8 步顺序推进，每步产出落盘。
- 反方证据（漏洞）：
  1. **步骤0 隐含但链路未写**：create_goal 是链路前提（"goal 生命周期"起点），但 §3.0 的 8 步从"找到目标"开始，未说明 goal 如何创建 + subagent/非顶层环境 create_goal 不可用 → 本次卡住一次。
  2. **arena 通道与执行者能力不匹配**：链路假设"让 arena 走 loop"，但未写"执行者无浏览器控制权时如何驱动 arena"（pfb 中转模式的实际操作 = 本地 push + arena 侧拉取，但 SOP 未把这条写成标准动作）。
  3. **"conf ≥ 0.7 迭代"无终止操作定义**：迭代 = 再发一轮 arena 任务？还是本地再读？§3.0 只给阈值不给动作。
  4. **bench 无指标定义落点**：§3.0 说"0.9 比例指标"，但指标清单/权重/baseline 选取规则在哪定义未指明（本次自定，下轮 agent 会重复自定 → 漂移风险）。

## 假设 2：token 效率 bench 可比
- 漏洞：外部开源 baseline 本环境不可得（web_search 禁用 + 无浏览器）→ "高于开源 baseline ≥10%"在降级通道下**不可机器验证**，只能锚 pfb 自有 rubric。验收标准 2 的"开源 baseline"需要 ego-browser 环境才成立。

## 矛盾记录
- AGENTS.md"联网只走 ego-browser" vs 本环境无浏览器 → 冲突按降级方案处理（已在 02/02.5 如实标注），非模板缺陷，属环境约束。

## 漏洞清单（供 bench 与 report）
V1 goal 创建前提缺失（subagent 不可用）
V2 arena 驱动动作未标准化（中转模式缺 SOP 动作序列）
V3 conf 迭代无操作定义
V4 bench 指标/baseline 无固定落点
V5 验收标准 2 在降级通道不可机器验证

## 判定
pass（漏洞 5 条，均有证据；conf 迭代目标：下轮用 ego-browser 环境复核 V5 → conf 0.7）
