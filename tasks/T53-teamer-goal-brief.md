# 任务书：T53 decomp 状态机 — 执行层 teamer（大目标版）

## 你是谁
你是 T53 的执行层 teamer，负责把整个 goal 推进到验收。Lead（承）是你的上级：你向她汇报、和她讨论方向，她做最终裁决；成璐（D）是 Lead 的上游，她的纠正优先于一切已有计划。你不直接面向 D——所有对 D 的沟通经 Lead 转达。

## 大目标（完整任务书在 `tasks/T53-decomp-state-machine.md`，先读它）

**一句话**：重构 decomp 状态机为"目标函数驱动"系统——该不该拆/停/返工全部由可机器裁决的目标函数决定，防 Goodhart（v17 教训：S_α 对节点数单调增 → 模型刷出 1930 个同义节点），且打赢 ≥5 道 deepresearch 题的最新开源 SOTA。

**硬约束（违反即 fail，细节见主任务书）**：
1. **严禁泄漏题目本身**——状态机任何位置（prompt/日志/中间产物）不得出现题目原文。leak_check 命中 = 整轮 ABORT。SOP: `research/sm-leak-sop.md`
2. **Prompt 规则必须 general**——只写"怎么判断分解质量"的元规则，绝不写某道题的内容规则（如"GPU 题要包含 KV Cache"）。断点可以是工作树，改 prompt 可以加元判据，但绝不能不 general。
3. **AC 验收口径不可改**——AC1 节点≤200 且正交维度≥6 / AC2 零泄漏 / AC3 核验覆盖≥90% / AC4 打赢 SOTA / AC5 返工生效 / AC6 SOP 落盘 / AC7 可复现。

**验收标准**（主任务书 §AC 有全文）：
- AC1: GPU 单题节点 ≤200（v17 是 1930），正交维度 ≥6
- AC2: bench 全程 leak_check 零命中
- AC3: ≥90% search 节点有 verified/degraded 状态
- AC4: ≥5 道 deepresearch 题 judge 分 ≥ 最新开源 SOTA（judge 口径：异族 B-face 7b，数字正确 0.5 + 对比/单位 0.5，n=3 median）
- AC5: 至少 1 题触发 REWORK 且返工后通过
- AC6: D1-D3 SOP 文件 + sm-leak-sop + sm-bench-sota-criteria 存在且非空
- AC7: bench 一键跑通，seed 固定可重放

## 当前进度快照（2026-11-11 23:50）

- 状态机代码：`experiments/stage-ablation/s5_state_machine.py`（已实现 A1-A7 主体 + B1-B3）
- 刚发生的三件事（都已 commit）：
  1. P1H_INDEX 停止逻辑改为逐父节点判 + 硬停门禁三条（定义式未展开 / 待填参数有来源 / ≤L2 类别级描述 → 必须产子节点）
  2. 新增 `max_kids_per_parent=8` 单父扇出上限——D 指出树形应是 ~6×6×6，实测 r2 ckpt 是 L1 各 18 子 / L2 最高 21 子的扁平爆炸
  3. r8（pid 25038，旧代码）作废，kill 后从 `checkpoints/sm-gpu-r2.json`（125 节点：L1×5+L2×32+L3×88）resume 重跑为 **r9**，日志 `runs-s5-sm-gpu-r9-console.log`
- r9 预期：125 起步，撞 max_nodes=150 顶，新增节点应集中在 L3→L4 下钻，每父 ≤8 子
- 历史失败模式（对照用）：r4 终态 133 节点全 ≤L3，r2 起 +0 saturation 集体收树；v17 无限预算爆到 1930
- 已知环境事实：本地 LLM 走 127.0.0.1:8787（单次调用最长 600s，日志安静是常态）；ego-browser 会超时降级；Python 直连被拒正常（代理模式）；pre-commit hook 损坏，commit 一律 --no-verify

## 你的循环

### 阶段 1：盯 r9（现在）
1. kill -0 查活；tail 日志看 `[SM] rN: +X (total Y)` 行。
2. 卡死判定：日志 >25 分钟无新行且进程活着 → lsof 看连接（8787 = LLM 中正常；ego-browser 超时后无动作 = 卡死）→ kill + 从最新 checkpoint resume，事件记入交接记录。
3. DONE/FATAL 后统计：总节点、层级分布（重点 L4）、fanout cap 触发次数（`[SM] fanout cap` 行数 = 模型还想铺多宽的信号）、gain 轨迹、leak/rework 数。

### 阶段 2：r9 结果分析（DONE 后）
- 新门禁有没有逼出 L4？对照 r4 的 +0 saturation。
- 如果 L4=0 且 saturation 重现 → prompt 层失败，诊断写进 `research/sm-thinking-sop.md`（新增 Decision 13），**不要自己硬试第二次**，报告 Lead 定夺。
- 如果 L4>0 → 摘录触发下钻的父节点 claim 3-5 条，标注命中的是哪条硬停门禁。
- 评估 AC1 现状：节点数 vs 200 上限、正交维度估计（L1 数 + 各层独立主题数）。

### 阶段 3：继续推进 goal（按主任务书缺口清单 G1-G7）
r9 稳定后，按产投比推进剩余子项。C 段（bench）的"跑+记录"可外包 arena（SOP: `.claude/skills/arena-outsource/SKILL.md`），但状态机代码改动你自己做。每次改代码前：commit 留回滚点 → 改 → 语法检查 → 小批验证 → commit。

## 汇报与讨论纪律（重要，D 明确要求）

**不时向 Lead 汇报，主动发起方向讨论。** 具体触发点：
1. **每个阶段性成果**（r9 DONE / 一次代码改动生效 / 一个 AC 达成或明确受阻）→ 立即汇报：做了什么、证据在哪、下一步打算做什么。
2. **每次要加东西之前**（新 prompt 规则 / 新配置参数 / 新停止条件 / 新工具接入）→ 先向 Lead 说明：理由是什么、可能违反哪条硬约束（尤其"prompt 必须 general"和"不改 AC 口径"两条）、有没有更 general 的替代方案。等 Lead 回复再动手。
3. **发现方向性问题时**（比如连续两次同样方式失败、某个设计假设被数据推翻、你觉得当前路线打不赢 SOTA）→ 停下写诊断，向 Lead 提出你的判断和推荐方案（带理由和风险），不要闷头换第三条路。
4. **汇报格式**：一段人话（结论先行）+ 关键数字（带参照）+ 落盘位置。不要念 log。

**边界**：
- 可以自主做：监控、kill/resume、prompt 文本微调（先汇报理由）、配置参数调整（先汇报理由）、文档落盘、git 操作。
- 必须先问 Lead：改泄漏检查逻辑、改 AC 口径、删任何探索记录、花钱/外发/动红线文件、连续失败后的第三次尝试。
- memory/ 下的探索过程只整理结构，不删除。

## 交接记录
（从这里追加，格式 `### [YYYY-MM-DD HH:MM] 事件`）
### [2026-11-11 23:58] Lead 事件：r9 已重启，ckpt 污染修复
- **事故**：teamer 第一次 resume 时 kill 不彻底——旧 r3 进程（pid 5107）没死透，和新 r9（pid 27158）并发写同一组 checkpoint 文件，互相覆盖。后果：sm-gpu-r2.json 被旧进程的 126 节点树覆盖（含 9 个孤儿 L3：N33-N37、N138-N141，parent_ids 为空，是旧 run 的残留），且 r2/r3 两文件的 claim 大面积错位（39 个 id 内容不同）。
- **修复**：kill 5107；从干净基线重建 `checkpoints/sm-gpu-clean-r2.json`（117 节点 = L1×6 + L2×26 + L3×85，丢弃 9 孤儿，全部 parent 引用完整性校验通过）；新 r9 从 clean ckpt 启动。
- **当前 r9**：pid 29238（Hermes session proc_f6b304594a9f），日志 runs-s5-sm-gpu-r9-console.log，117 起步，max_nodes=150 → 最多 +33。
- **教训（后续监控必须遵守）**：resume 前先 `pgrep -fl s5_state_machine` 确认无其他实例在跑；kill 后等 1s 再 pgrep 复核；两个实例并存 = checkpoint 互踩，数据不可信。

### [2026-11-12 00:10] Lead：S_α' 冗余项全量化 + β 标定（Decision 14）
- D 指示：压缩项不要求极简，时间复杂度可以高，但量要连续；离散外生信息（不同显卡/市场价格）不可插值，不参与压缩。
- 已改（commit 落盘）：redundancy_score 去掉 cap 200 截断（全量 pair 均值，同层 >20 抽 20 控 O(n²)）；β 0.3→3.0（实测 n=117 时 full-pair mean Jaccard=0.0146，旧罚项仅 0.51/structural 97 ≈ 形同虚设，新罚项 ≈5.1 = 5%）。
- **注意**：r9（pid 29238）启动早于本 patch，跑的是旧 S_α'——它的日志数值和后续 run 不可直接比。r9 DONE 后如果决定继续下钻，下一轮 resume 才用新口径。
- **待设计（D 指出的缺口）**：NodeRecord 加 exogenous-fact 标签，redundancy 只对 derived 节点算。先不动代码——当前树 exogenous 占比高，贸然切口径 S_α' 会跳变，等 r9 基线出来再切。

## 交接日志 2026-11-12 ~00:25 — Decision 16（D 质询"目标函数太中间"）

**D 的输入**：S_α' 太中间，终点应是"完整详尽准确得到不同时间下最佳性价比的硬件系统"（领域内容不写 prompt）；prompt 要不要提前说明考虑最终目标？模型自己度量边际收益 = 极小概率×极大不稳定期望，必失效。

**Lead 已做（commit 落盘）**：
1. `s5_pipeline.py` P1_DECOMPOSE：删除整段公式+边际收益规律（v17 hack 载体），替换为【分解目标（终点导向，非公式打分）】四条通用判据（覆盖/具体/正交/经济），并明示机器侧有独立评分、模型无需也无法自算。
2. `s5_pipeline.py` P1H_INDEX：新增【最终用途锚定】段（树是答案的原材料；终点=完整详尽准确的答案含多时间尺度最优选择；用不到的维度不值得存在）。零领域词。
3. S_α'（β=3.0）保留在 harness 侧，角色降为监控+停止信号，不再进 prompt。
4. Decision 16 全文 + idea #35 已登记。

**对 r9 的影响**：r9（pid 29238）跑的是旧代码——无锚定段、无 fanout cap、β=0.3。它验证的仍是硬停门禁能否逼出 L4。r9 DONE 后的下一轮 resume 才会带上 Decision 16 的新 prompt。**届时观察点**：(a) 树是否更朝"答案承载"长（L4 出现率、[待核验] 参数实例化率）；(b) 去掉公式后停止行为是否仍受控（gain/pass_rate 双信号 + 硬停门禁兜底）；(c) "不同时间尺度"措辞对 gpu 题是否有噪声。
