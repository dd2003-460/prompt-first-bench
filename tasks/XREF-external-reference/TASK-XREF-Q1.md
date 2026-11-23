# TASK-XREF-Q1 — frontier 模型外部参照（Q1 GPU 原题，深 gold）

> origin: ai · 2026-11-24 · 触发：D「能不能拿个靠谱的可以跑这些 idea 的 autoresearch 跑一下」
> 目的：补 pfb 判分矩阵的 frontier 空角——深 gold（37 节点/31 claim，含 MFU/η_bw 微架构层）上只有 27b 数据（blind-eval 21 份答卷，覆盖 45–68%），frontier 角没测过。本任务 = frontier 模型 + 真搜索跑 Q1，与 27b 深 gold 基线形成跨模型对照。
> 注意：这是**组件参照**（模型能力缺口 vs prompt/hook 缺口），不是"我们的系统 vs 别的系统"。

## 任务书（arena agent 执行）

### 输入
- 题面：`pfb/experiments/stage-ablation/questions/Q1-gpu-h100.md` 的「## 题面」段（原样，不加任何方法论引导——对照基线是 27b plain prompt）
- 你自带真搜索能力，正常使用（这是本实验的干预变量：frontier 模型 + 真搜索）
- 预算：≤20 次搜索调用，≤15 分钟

### 输出格式（必须，供本地 rubric-v3 判分管线复用）
落盘 `result.md`，结构：
1. `## 输出` — 你的完整研究产出（分解 + 候选评估 + 条件化结论 + 不确定点清单），自然语言，无格式要求
2. `## 来源` — 逐条列出实际引用的 URL + 每条用了什么信息
3. `## 自述缺口` — 你明确标"不确定/没查到/需要进一步验证"的点

### 回执指纹
- 题面段 sha256：880bfe3d963f8be6e53671840fe685154bf9faca444b5d5317292fcc77777a7b（Q1-gpu-h100.md「## 题面」段，## 题面 到下一个 ## 之间，strip 后）
- 本任务书 sha256（定义：全文去掉本行后的 sha256，防自引用）：55ab14928bfef0c4daca3138a569c6954e4039f30424f7b7f8bd5a7a773dc7d3
- 回执原样带回两个指纹

### 禁止
- 不要输出"作为 AI"类免责声明
- 不要编造 URL——没查到的就写没查到（编造 URL 会直接进幻觉率判分）

## 本地判分（Lead 侧，arena 完成后）

- 判分用 rubric-v3 机械 O3（gold-tree matching），gold = `pfb/bench/rubric-v3/ablation/gold-tree.md`（37 节点，31 条可判 claim，含微架构层 N-3.1 家族 + N-2.2 调度效率）
- 对照基线：blind-eval 21 份 27b 答卷（`bench/rubric-v3/ablation/formal-matrix/blind-eval/`，7 prompt 版本 × 3 rep，双 judge 相对序 A 垫底 < E/G < C/D/F < B 最高，覆盖 45–68%）
- **重点观察项**：N-3.1/N-3.1.1/N-3.1.2/N-3.1.3（FLOPs/峰值算力/MFU 建模 prefill）+ N-2.2（调度效率子因子）在 27b 全部 21 份答卷 0 命中——frontier 能否补上这条"计算量÷折扣算力"建模路径（而非抄实测 tok/s）
- judge 同族偏差标注：跨模型比较仅相对有效（scoring-calib 规则）；判分前对齐判据档位
- 附带产出：本地 27b judge 评 arena 结果（异族）vs 评 27b 答卷（同族），量化 judge 分族偏差（D 11-24 指令）

## 预期回答的问题
1. 深 gold 上 frontier 覆盖率 vs 27b 45–68%——区分度实测（浅 gold 上 frontier 已饱和 1.0，深树是否仍拉开）
2. 27b 全版本 0 命中的 N-3.1 微架构家族，frontier 能否命中——命中 = 模型能力缺口（27b 分解不出）；未命中 = 题面/信息可得性问题
3. frontier 的"不确定点清单"质量 vs 27b 的 defensive language

## 状态
- [x] 题面选定（Q1 GPU 原题，深 gold 37 节点，27b 深 gold 基线 21 份现成）
- [x] 任务书指纹填入
- [ ] 派发 arena
- [ ] 回执核验（git 序列，不信页面汇报）
- [ ] rubric-v3 机械判分 + 对照报告
