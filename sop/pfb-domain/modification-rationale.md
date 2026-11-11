# 机制修改 SOP：为什么改 / 正交性 / 依据

> origin: ai · 2026-11-12 · D 指令："你们的修改和退出思路——修改想理由，理论计算/外信息貌似容易缺，比如你单加规则貌似没什么全局视角（为什么加，和其他规则是不是正交影响）。这个要写到科研sop"

## 为什么有这条 SOP

状态机迭代了 14 轮，每轮都在加规则（fanout cap、硬停门禁、structural test、contribution threshold…）。问题：**单条规则各自看都有道理，但叠在一起没有全局视角**——新规则和旧规则可能冲突、冗余、或者互相抵消。r13 的教训就是典型：quotient 边检测规则单独看合理，但它让 90% 的边走了 frontier 采样路径，导致树结构变形。不是那条规则错了，是它和已有的 fanout cap 叠加后产生了预期外的交互。

所以每条机制修改必须回答三个问题才能进代码：

## 三问（缺一不可）

### Q1: 为什么加？（动机）

二选一，必须写明：
- **实证证据**：哪次 run 的哪个数据点暴露了这个缺口？引用具体文件 + 行号或节点 id。例："r13 runs-s5-sm-gpu.json 中 quotient 边占 90%，导致 L3 层全是 frontier 采样锚点而非真实维度分解。"
- **理论推导**：从目标函数 U(T) 或代理锥架构推出"缺少 X 会导致 Y 被 hack"。写出推导链，哪怕只有三行。例："cost(T) 按节点数一视同仁罚 → 商边的 frontier 采样天然节点多 → 不区分边类型 = 错罚结构必需 → Goodhart 方向 = 模型学会少拆商边。"

**禁止**："感觉应该加" / "业界都这么做"（除非附具体来源）/ "为了更 robust"。

### Q2: 和现有规则正交吗？（正交性检查）

列出当前生效的所有机制（见下方清单），逐条判断：
- **独立**：新规则的触发条件和效果范围与它无交集。
- **交互**：两者同时生效时行为如何？是互补（一个管 A 面一个管 B 面）还是冲突（同一条边上给相反指令）？
- **冗余**：新规则的效果是否已被某条旧规则覆盖？如果是，不加。

**判定标准**：如果去掉新规则，旧规则集合的行为不变 → 冗余（不加）。如果加上新规则，某条旧规则在特定条件下失效 → 冲突（需要明确优先级或修改旧规则）。

### Q3: 外部依据是什么？（支撑）

三类可接受：
- **文献**：arXiv ID / DOI + 一句话说明它支持了哪个环节。
- **已有实验**：本项目内哪次 run 的数据支持（引用 checkpoint/jsonl 路径）。
- **第一性原理**：从信息论/MDL/Goodhart 定理推出的逻辑链（写出来，不引用）。

**没有外部依据怎么办**：标 `[待验证]`，先跑最小实验拿数据再定参数值。规则可以先进代码但参数用保守默认值，实验数据回来后再标定。**禁止凭直觉定阈值然后当确定值用。**

## 退出条件（什么时候删规则）

每条规则加入时必须同时写明它的**死亡条件**——什么情况下这条规则应该被移除：
- 它解决的问题已被更上游的机制覆盖（例：如果 MDL 压缩目标真的实现了，手动 fanout cap 可能冗余）。
- 连续 N 次 run 中它从未触发（N=3，dead code）。
- 它与新规则冲突且新规则严格更强（证明后删旧的）。

没写退出条件的规则 = 永久债务。

## 当前生效机制清单（正交性检查的对照表）

| # | 机制 | 位置 | 作用 | 加入轮次 | 退出条件 |
|---|------|------|------|---------|---------|
| M1 | L1 skeleton prompt（只输出顶层正交维度 3-7 个） | P1_L1_SKELETON | 防止 L1 下钻到参数级 | r1 | MDL 目标实现后若自动约束则删 |
| M2 | fanout cap 8（max_kids_per_parent） | _decompose_layer | 限制单父节点子项数 | r4 | 贡献度阈值（M5）若已足够约束则删 |
| M3 | 硬停门禁（stop_rounds=3, necessary criterion） | round loop | 防止无限扩展 | r4 | — |
| M4 | verify_threshold 0.6 + degraded 状态 | verification | 软失败不阻断 | r2 | — |
| M5 | contribution threshold 0.10（信息论 I(child)） | stopping | 边际贡献 < ε 则停止展开 | r12 | 若 LLM-judge 版本替代则换 |
| M6 | structural test for edge type（操作标记检测） | edge classification | 区分 cartesian vs quotient | r14 | 若 LLM-judge 边分类替代则换 |
| M7 | quotient frontier sampling（cap 4） | edge expansion | 商边有限采样不穷举 | r14 | 若 cost(T) 区分边类型则调参 |
| M8 | S_α' 过程监控（early stopping + divergence） | monitoring | 不发散才继续 | r12 | — |
| M9 | U(T) 终点验收（机器侧，不进 prompt） | acceptance | Goodhart 防线 | r12 | — |
| M10 | Goodhart 纪律（reward 不进 prompt） | architecture | 结构性防 hack | r10 | 永不出退（架构约束） |

## 修改流程（操作步骤）

1. **写决策条目**：在 `research/sm-thinking-sop.md` 追加 Decision N，包含 Q1/Q2/Q3 完整回答。
2. **更新本文件的机制清单**：新增/修改/删除对应行。
3. **代码改动**：小步改，一次只动一个机制，跑 smoke test（3 节点小树）确认不炸。
4. **落盘证据**：git commit message 格式 `M{编号}: {一句话} (Decision {N})`。
5. **索引**：在本文件顶部 changelog 加一行日期+编号。

## Changelog

- 2026-11-12: 初版（D 指令触发）。机制清单 M1-M10 从 sm-thinking-sop.md Decisions 1-24 提取。