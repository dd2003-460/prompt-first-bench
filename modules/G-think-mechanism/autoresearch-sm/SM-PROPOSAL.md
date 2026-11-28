# SM-PROPOSAL: autoresearch 认知层状态机 v0.1
# origin: ai · 2026-11-25 · 状态: DRAFT（待 D 拍板立项）
# 触发: D 2026-11-25 "autoresearch 经常陷入局部，也没有成熟的批判和工作流程"（信号 S43）
# 动机案例: idea53 审计（pfb/outputs/idea53/ + tasks/idea53-goal/，2026-11-25 只读审计）

## 0. 一句话
不建第四个平行状态机。已有的两台（ralph 管流程、s5 管实验执行）不动，
只补一层**认知层**：claim 生命周期 + 3 条特殊转移（逃逸/批判/失效传播）。
这层治 idea53 暴露的三个病，其余全部复用。

## 1. 现状盘点（本地已有，不重复造）
| 层 | 载体 | 有什么 | 缺什么 |
|---|---|---|---|
| 流程层 | `scripts/ralph_runtime/`（`loop/ralph-state-machine-plan.md`，90+ 测试） | 01→06 阶段机、field 协议、hook 门禁、supervisor、stall 看门狗 | 逃逸转移、常设批判、claim 失效 |
| 执行层 | `pfb/experiments/stage-ablation/s5_state_machine.py`（100KB） | {IDLE,DECOMPOSE,VERIFY,REWORK,STOP} + 目标函数裁决 + 边际增益停止 + 防泄漏 | 只管单次实验内部，不管研究叙事 |
| **认知层** | **无** | — | claim 版本/失效、撞车域对齐、对抗批判、打转检测 |

idea53 三个病全部落在认知层：
- 病1 陷入局部：撞车 5 轮全查旧 claim 域，claim 重构后撞车没跟着换域（无失效传播）
- 病2 没批判：被信息论直算反驳的 claim 走到写作阶段才被事后审计拦下（无前置 gate）
- 病3 没流程：toy model 单调性不成立（A100>5090）进了稿（无状态化验收）

## 2. 认知层状态（6 态，附着在 ralph 阶段之上，不是替代）
```
CLAIM → EVIDENCE → COLLISION → CRITIQUE → TOYMODEL → WRITING
```
每态一个量化门禁（不过不前进）：
- CLAIM: claim 文本 + 可证伪形式（数字/不等式）+ 预注册（时间戳早于数据）
- EVIDENCE: 每个 claim 有 ≥1 独立证据 ref（路径/commit/URL）
- COLLISION: 撞车查询的**域必须 = 当前 claim hash 的域**（见 T3）；≥N 近邻逐一切割
- CRITIQUE: 零上下文对抗者回执（见 T2），可打回任意上游态
- TOYMODEL: 数值自检通过（单调性/守恒/手算锚点复现）
- WRITING: 以上 5 态回执齐全才可写；写完触发提交前终检

## 3. 三条特殊转移（核心，治三个病）
### T1 逃逸（治病1 打转）
- 信号：同一任务连续 k 轮**零新 finding**（finding = 新证据 ref / 新 claim / 新撞车结论，机器计数）
- k≥2 → 强制 structural pivot：禁止在当前子问题继续迭代，必须（a）换分解 或（b）升层（arena/人）
- k≥4 → 升级人工（写 APPROVALS 队列，不阻塞其他可逆工作）
- 偷 ARIS `iteration_log.py` 的零 finding 计数 [待核验: sub 提取中]

### T2 批判（治病2 无反驳）
- 进入 WRITING 前**必须**过零上下文对抗者：独立 subagent/arena，只给 claim+证据，不给叙事
- 双线程：最强拒稿备忘录 vs 逐点辩护（偷 ARIS `kill-argument` + `paper-claim-audit` 结构 [待核验]）
- 裁决：致命伤→打回对应上游态；非致命→带 caveat 前进
- 关键设计：**对抗者与生产者不同上下文**（防确认偏误），这是 idea53 病2 的直接对策

### T3 失效传播（治病1 的根因）
- claim 有版本+hash；任何下游产物（撞车轮/批判回执/toy 结果）记录它基于哪个 claim hash
- claim 修订 → 下游全部标 stale，必须重跑或显式豁免（豁免要理由）
- idea53 回放：claim 第 2 次重构后，5 轮撞车全部应标 stale——这正是当时没发生的

## 4. 偷/不偷清单（ARIS 19.8k★，2026-11-25 调查）
**偷**（认知层直接可用）：
1. `iteration_log.py` 零 finding 计数→强制 pivot（T1 的引擎）
2. `kill-argument` / `paper-claim-audit` 的零上下文对抗结构（T2 的 prompt 骨架）
3. `run_state.py` 的 done≠accepted 分离（"loop can DRIVE, cannot ACQUIT"——执行者不能自己验收）

**不偷**：
- 197 个 skill 库（反压缩；我们要的是 3 条转移不是 197 个入口）
- ARIS 的 orchestrator 地位（它的状态机只是辅助脚本，skill 才是 orchestrator——我们要反过来：状态机是权威，执行是附属）
- codex 仓的 10 阶段 prompt 级流程（散文级状态管理，无文件级机器裁决）

## 5. MVP 范围（最小可验收）
只写 3 个文件 + 1 个 dry-run：
1. `claim_ledger.json` schema + `claim_revise` 命令（T3：修订→下游标 stale）
2. `stagnation.py`（T1：per-task finding 计数 + k 阈值 + pivot 提示生成）
3. `critique_receipt.json` schema + 派发模板（T2：零上下文对抗者任务书 + 回执校验）
4. **dry-run 验收**：把 idea53 时间线（claim 3 次重构 + 撞车 5 轮 + 写作）作为事件序列喂给 1+2，
   断言：claim 第 2 次重构后撞车轮被标 stale（T3 触发）；撞车域漂移被检出（T1 触发）。
   两个断言都过 = 状态机能拦住 idea53 的两个真实事故。

## 6. 验收标准（立项后）
- [ ] dry-run 双断言通过（idea53 事故回放）
- [ ] 下一个真实任务全程走认知层：ledger/stagnation/critique 文件有落盘
- [ ] 至少 1 次 T1/T2/T3 真实触发（或证明未触发是合理的——附计数证据）
- [ ] 打转轮数 vs 基线（idea53 5 轮旧域撞车）可测、可对比

## 7. 开放问题（D 拍板）
1. 认知层放哪：`pfb/modules/G-think-mechanism/autoresearch-sm/`（现 staging）vs workspace `loop/`（canonical，跨项目）？
   倾向：MVP 在 pfb 验证，转正后移 `loop/` 并接入 ralph 阶段门禁。
2. 对抗者用谁：本地 27b subagent（免费、快、弱）vs arena（强、慢、要派发）？
   倾向：MVP 用本地 subagent，CRITIQUE 态失败 2 次自动升级 arena。
3. 6 态是否过细：MVP 只强制 CLAIM/COLLISION/CRITIQUE 三态门禁，其余 3 态软提示？
   倾向：是（先治三个病，不追求全流程覆盖）。
