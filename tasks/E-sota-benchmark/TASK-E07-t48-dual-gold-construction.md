# T48: Dual Gold Construction (B2 信息边界重构)

## 强制段
你是 LMArena agent，本任务只涉及 prompt-first-bench/main。先 git pull 获取最新代码。严格按仓库内 `loop/prompt-first/` 阶段执行（01→02→02.5→03→04→04.5）。产出落盘路径见【交付物】。通道故障报告 Lead 不得静默跳过。

## 【目标】
独立构建第二棵 gold tree（同域：本地 27B 推理硬件选型），作为 rubric-v3 O3 构念效度的双 gold 对照，消除单源偏置宣称限制。

## 【背景】
- 当前 gold tree: `bench/rubric-v3/ablation/gold-tree.md`（31 节点，由 pfb 作者构建）
- 题面: `bench/rubric-v3/ablation/formal-matrix/prompt-V1-full.txt`（66 行，含候选集构造规则+边界声明要求）
- 宣称前置条件（DRAFT-rubric-v3-v2.md §O3 R-06）：在双 gold 或异源第三 judge 闭环前，O3 数字不得作为独立证据对外宣称
- 本任务走「双 gold」路径：你独立调研并构建一棵新 gold tree，与既有 gold 对比，报两 gold 命中差值作为同源偏置上界

## 【SOP 索引】
- `loop/prompt-first/01-goal-decomposition.md`
- `loop/prompt-first/02-information-research.md`
- `bench/rubric-v3/DRAFT-rubric-v3-v2.md`（rubric 定义 + O3 判据）
- `bench/rubric-v3/ablation/gold-tree.md`（参考格式，但内容必须独立推导）

## 【实验设计】
1. **输入**：prompt-V1-full.txt 的题面部分（"我要在本地跑一个 27B..."到末尾），不含候选集构造规则和边界声明要求（这些是评分维度指令，不是题面本身）
2. **你的任务**：像被试一样回答该题——独立调研、独立拆树、独立给出结论。不许看 gold-tree.md 的内容（只看其格式结构作为输出模板参考）
3. **输出格式**：与 gold-tree.md 相同的树形结构（根→子→叶，每节点标 SHARE + 可查/可调/黑盒 + 量法），但所有数值和判断必须来自你自己的调研
4. **搜索预算**：不设上限，直到每个分支都有带来源的证据或显式黑盒声明
5. **禁止**：不得引用 gold-tree.md 中的任何数值；不得访问 calc.py

## 【验收标准】
- [ ] 产出文件存在且非空（≥50 行）
- [ ] 树结构完整：有根节点、≥3 层深度、≥8 个叶子
- [ ] 每个叶子有：数值/区间 + 来源（URL 或 "黑盒+估计范围"）
- [ ] 有瓶颈判定（哪支影响最大 + 为什么）
- [ ] 有矛盾清单（≥1 条或显式"无"+证明查过 ≥2 独立来源）
- [ ] 与 gold-tree.md 的节点重叠率计算（Lead 后续做，你只需交付树）

## 【失败降级】
- arena 沙箱无 web 工具 → 用 arXiv API + 直访厂商页面（NVIDIA/AMD/Intel 规格页）
- 某分支确实搜不到 → 标黑盒 + 给区间 + 写获取路径，不硬编
- 超时 → 先交骨架（主干+一级子节点），叶子标注"待补"

## 【交付物】
- `bench/rubric-v3/ablation/dual-gold/gold-tree-independent.md` — 你的独立 gold tree
- `bench/rubric-v3/ablation/dual-gold/receipt-dual-gold.md` — 回执（repo URL + branch + commit_sha + 搜索来源列表）

## 【给 Lead 的备注】
- 本任务是 RUBRIC-V3-FULL-AUDIT-B2-FULL-FIX 的双 gold 路径执行
- 完成后 Lead 做：① 节点重叠率计算 ② 用两 gold 分别对 21 份正式矩阵 run 打分 ③ 报命中差值 = 同源偏置上界 ④ 更新 DRAFT §O3 宣称前置条件状态
- 边界：你只负责建树，不负责评分（评分是 Lead 用 rubric 脚本做的）
