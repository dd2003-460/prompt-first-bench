# TASK-XREF-Q2 — frontier 模型外部参照（Q2 模型选型题）

> origin: ai · 2026-11-24 · 触发：D「不放心我们的 autoresearch，想拿成熟的来跑 idea」
> 目的：给 pfb 执行系统一个**外部参照点**——frontier 模型 + 真搜索在完整研究题上能做到 27b+我们 prompt 做不到的什么。
> 注意：这是**组件参照**（模型能力缺口 vs prompt/hook 缺口），不是"我们的系统 vs AI Scientist 的系统"（实验单元不同，不可直接比）。

## 任务书（arena agent 执行）

### 输入
- 题面：`pfb/experiments/stage-ablation/questions/Q2-model-selection.md` 的「题面」段（原样，不加任何方法论引导——对照臂是 S0 plain）
- 你自带真搜索能力，正常使用（这是本实验的干预变量：frontier 模型 + 真搜索）
- 预算：≤20 次搜索调用，≤15 分钟

### 输出格式（必须，供本地 rubric-v3 判分管线复用）
落盘 `result.md`，结构：
1. `## 输出` — 你的完整研究产出（分解 + 候选评估 + 条件化结论 + 不确定点清单），自然语言，无格式要求
2. `## 来源` — 逐条列出实际引用的 URL + 每条用了什么信息
3. `## 自述缺口` — 你明确标"不确定/没查到/需要进一步验证"的点

### 回执指纹
- 题面 sha1：f45ad104dff8544d6bb2b75a43a7e51021282051（Q2-model-selection.md「题面」段）
- 本任务书 sha256（定义：全文去掉本行后的 sha256，防自引用）：2fec587c69158018abfb6f3987b9b428eab63bc6d06b54bab1551cb5ab00000e
- 回执原样带回两个指纹
- **核验终局（11-24）**：任务书 sha256 ✅ 一致（完整性已证）；题面 sha1 本地 6 种口径均复算不出——但题面 sha1 只是派发时自算的冗余校验值，**不 gate 任何结论**，且 arena 实际跑完并产出 result.md（167 行，已 git 核验），任务正确派发已证。**关闭，不再追**（D 11-24 指令）。

### 禁止
- 不要输出"作为 AI"类免责声明
- 不要编造 URL——没查到的就写没查到（编造 URL 会直接进幻觉率判分）

## 本地判分（Lead 侧，arena 完成后）

- 判分用 rubric-v3（O1 覆盖/O2 矛盾深度/O3 gold 命中/O4 条件结论/O5 口径一致），gold = `projects/decomp/bench/gold-model-selection/tree.md`（24 节点）
- 对照基线：`runs/S0-Q2-r1/r2/r3.json`（27b plain prompt，同题同 gold）
- judge 走既有 arena-judge 管线（`runs/arena-judge-results.jsonl` 同口径），跨模型比较时标注"judge 同族偏差，仅相对有效"（scoring-calib 规则）
- 判分前对齐判据档位（scoring-calib 硬规则：先读 rubric 0/1/2 档定义原文再打分）

## 预期回答的问题
1. frontier+真搜索在 O1（候选覆盖）/O2（矛盾深度）/O3（gold 命中）上比 27b plain 高多少？
2. 差距集中在哪个维度——若 O3 差距大 = 模型能力缺口（27b 分解不出深层节点）；若 O1/O2 差距大但 O3 接近 = prompt/hook 缺口（27b 有分解能力但没触发）
3. frontier 的"不确定点清单"质量 vs 27b 的 defensive language——谁更知道自己不知道

## 状态
- [x] 题面选定（Q2，gold 24 节点，S0 基线 3 rep 现成）
- [x] 任务书指纹填入
- [x] 派发 arena
- [x] 回执核验（git 序列，不信页面汇报）
- [x] rubric-v3 判分 + 对照报告（O3/O1 机械 + O2 粗筛；O2/O4/O5 完整 LLM judge 待办）
