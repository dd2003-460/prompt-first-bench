# origin: ai
# 思考触发（think-trigger）：让 pfb/qqbot 从"做多想少"补上"想"这一层
# 来源：D 2026-11-24 诊断"stophook下的qqbot做的太多想的太少" + 批准"可以试试"+追加"接着考虑"实验
# 关联 goal：research-agi-budget（主线，不另立 goal）

## 最终目标（不可改）
让 pfb/qqbot 的执行循环补上"往上爬一层"的思考触发 + 质量检验，使 agent 能像 D 一样
从具体爬到 general 机制、推出可检验预言。不是让执行"更像 D"，是给执行加上"想"的触发点和质量约束。

## 背景数据（subagent 调查，2026-11-24）
- 量化基线（223 个 Claude Code 会话全量扫描）：
  - thinking 字符 : tool_use 次数 ≈ 430 字符思考 / 1 次工具调用
  - 92.8% 的 assistant 消息无任何 thinking 块
  - 解读：不是不想（总思考 5.5M 字符），是每次动手前思考很薄，大部分轮次直接行动
- 病根：stop_hook 续推消息全是"继续干/不要停/找下一任务"，无一条注入反思指令。
  现有机制（_flex_nudge/4问冷却/等待态门控）全优化"做得更多/不重复"，无一条优化"想得更多"。
  → "做多想少"是这套机制的必然输出，非 agent 态度问题。
- 标杆（D 亲手指认，claude.ai 网页版 6 篇，已全读）：
  本地qwen3.8-27b的harness改进设计 / 量化对27B模型长程工作能力的影响 / ICL中的目标函数识别与Hack研究 /
  模型推理与ICL泛化 / LLM跨域推理能力实验设计 / 完整分点评价
- landscape 定义（D 原话，《调试大型工程排查思路》）：loss surface/优化景观，随机 landscape=非凸优化。
- 爬层活样本（D 原话三步链）：
  具体观察（敏感性难算）→ 一般机制（随机 landscape=非凸优化）→ 可检验假设（优化和信息量有关，能从先验算出来）

## 分解树（正交子项）
### T1 思考触发 hook（实现）
- 目标：stop_hook 检测到"连续 N 轮纯执行无/薄 thinking"→ 注入反思指令（而非纯"继续干"）
- 文件：tools/stage-gate/stage_gate/adapters/stop_hook.py（1108 行，框架源码）
- 方案（按可行性降级）：
  - 首选：检测近 K 轮 tool_use 高但 thinking 字符 < 阈值（基线 430/调用）→ 注入"先想再做：当前进展 vs 原始目标对齐了吗？这背后的 general 机制是什么？"
  - 降级：stop_hook 无法访问 per-message thinking → 每 K 轮（如 5）周期性注入一次反思轮（不依赖 thinking 检测）
- 约束：框架源码改动 = 不可逆类，留痕 APPROVALS.md + git commit 回滚点，改完告知
- 验收：hook 改动后，模拟"连续纯执行"场景能触发反思注入（有日志证据）
- **状态核验（2026-11-25，subagent B 查得）**：T1 **已实现但未提交**——`tools/stage-gate` 是独立 git 仓库（branch main），stop_hook.py 当前 working tree ` M` 未 commit（1249 行 vs 基线 1108 行，+141 行），已含 `_THINK_TRIGGERS`/`_T1_REFLECTION`/`t1-thin-thinking` 触发器+反思注入（"这背后的 general 机制是什么？能推出什么可检验预言？"）+冷却门控 `_THINK_COOLDOWN=3`。该仓库最近提交停在 2026-11-23（T1 之前）。回滚点：根仓库 commit `ace22cfa`（改动前快照）。**尚缺**：T1 commit（tools/stage-gate 仓库）+ APPROVALS.md 留痕（框架源码改动=不可逆类红线）。归属 subagent A，Lead 接手 T3 前先确认 T1 是否已补 commit。
- **✅ 风险已解除（2026-11-25 01:19 提交，01:33 复验）**：T1+T4 已 commit 至 stage-gate 仓 `1b30bc6`（working tree 与 HEAD 零 diff），APPROVALS 留痕根仓 `08697954`。复验：隔离环境（HOME 沙箱）5 场景全过——薄思考触发/冷却/厚思考不触发/可插拔架构/audit 留痕（`think-trigger HIT t1-thin-thinking stats=[(100,1)×5]`）。
- **T4 状态（同批核验 + 01:50 真检测落地）**：goal 计划子项⑥列了 T4（"修脚本卡住→general 思考升级触发"），但本 decomposition 原本漏了 T4——现补登：T4 **真检测已实现并提交**（stage-gate 仓 `7229159`，APPROVALS 留痕 `eeae4de1`）。`_trigger_t4_stubborn_spin` 从恒 False 槽位改成真检测：`_session_thinking_stats` 每轮新增 `errors`（tool 结果归一化报错签名）+ `paths`（编辑类工具结构化 path），触发条件=同一报错签名最近 10 轮内 ≥2 次 **或** 同一文件最近 6 轮被改 ≥5 次且窗口内有报错（无报错的正当迭代不触发）。验证：隔离沙箱 9 场景全过（T4-A 重复报错触发/T4-B 文件打转+报错触发/同文件全成功不触发/不同报错不触发/护栏噪音不触发 + T1 回归 5 场景）+ 真实数据 12 生产 session 0 误报 0 crash。T4 验收已达成：连续卡住（同一报错≥2次/脚本反复失败）时触发反思注入。

### T2 "接着考虑"实验（验证 27b 能否接住 D 的思考链）
- 目标：验证 27b 能否"像 D 一样考虑、接着考虑"——给 D 爬层链的前半段，看 27b 能否续出后半段（机制+预言力）
- 材料：《调试大型工程排查思路__50bf154f.md》L320-399 landscape 段
  - D 原话前半段（给 27b 的输入）："敏感性这种动力学内容应该很容易计算吧，或者说算法的空间不像物理空间那样"
  - D 原话后半段（gold，判据参照）："也就是这块是随机的landscape也就是非凸优化? 但是感觉这块优化和信息量有关，差不多算出来（先验近似0有效/先验信息量大）感觉也可以?"
- 条件（控制臂）：
  - 臂A（无提示）：只给前半段 + "接着考虑"
  - 臂B（general 提示）：前半段 + "接着考虑，往一般机制想，推出可检验的预言"
- 判据（每臂 0-2 分，预注册先 commit 再产数据）：
  - 爬层：是否爬到机制层（landscape/非凸/一般机制）
  - 预言力：是否推出可检验预言（"如果X则Y"形式）
  - 边界识别：是否说明在什么条件下成立/失效
- 模型：本地 27b（127.0.0.1:8787，OpenAI 兼容 /v1/chat/completions，qwen3.8-27b-mtp）
- 约束：预注册红线——判据/材料/条件先 commit，再跑数据。不泄露 gold 后半段给 27b（只作判据参照）
- 验收：两臂各 ≥3 次采样，打分落盘，臂B vs 臂A 差异可量化
- **完成记录（2026-11-25，subagent B）**：两臂各 3 次采样完成（temp 0.7）。**关键陷阱**：27b 是 thinking 模型，机制推理藏在 `reasoning` 字段（vllm 单独返回），只抓 `content` 会系统性低估——v1 只抓 content 低估了臂B，v2 补抓 reasoning 重评修正。结论：general 提示下臂B 3/3 爬到机制层+推出可检验预言+边界（复刻 D 三步链），臂A 0/3 预言；但 27b 一致把"敏感性"解读成动力系统/混沌（李雅普诺夫），非 D 的软件工程/loss landscape 语境——形似神未到，机制选错域，未触及 D 的信息论洞察。数据/打分：`exp-results/raw_outputs_v2.json` + `scores_v2.md`（v2 主数据）。commits: 38e6b34d6(prereg)→1f9ba50d6→8f255df93(v1)→002eada24(v2)。

### T4 修脚本卡住→general 思考升级触发（D 2026-11-24 追加）
- 目标：qqbot/agent 修脚本时若"修烦了"（连续多轮改同一脚本无进展/反复试错），触发 general 思考——退一步想"什么机制才能让 AI general 地思考/解决这个问题"，而不是继续蛮力试
- 触发条件（候选，T1 的 thinking 检测可复用）：
  - 连续 N 轮（如 3）改同一文件且无新验证证据 → 判定"修烦了"
  - 或：同一报错反复出现 ≥2 次 → 判定"在打转"
- 触发动作：注入反思指令"停下来：别再蛮力试了。退一步——这个问题的 general 机制是什么？有没有更一般的方法覆盖这个情况？"
- 与 T1 的关系：T1 是"纯执行无思考→反思"，T4 是"修脚本打转→general 思考"，共用同一套触发基础设施（stop_hook 的检测+注入），T4 是多一个触发条件
- 验收：模拟"连续改同一脚本无进展"场景，确认触发 general 思考注入（有日志证据）

### T3 落点整合（T1+T2 完成后）
- 把 T2 的判据（爬层/预言力/边界）接进 judge 机制（resistive formalism 的 judge 维度）
- 把 T1 的触发阈值用 T2 的基线校准
- 登记进 research-agi-budget 的子项，作为"AGI 系统能接住 D 思路"的能力证据
- **✅ 整合完成（2026-11-25，Lead）**：

  **step 2 — judge 整合（核心产出）**：T2 的"爬层"判据只测了**深度**（爬到哪层），没测**方向**（爬到哪个域）——臂B 爬层满分 2.0 却 100% 漂到混沌域。这正好对上 formalism judge 自己的 **flip（bottleneck 身份变）+ shift（存活 bottleneck 内排名变）**结构（`formalism-skeleton.tex` L68-76：judge = surface-vs-deep 修正，ground truth = argmax leaf）。所以接法不是"加第四维"（ad-hoc），而是把爬层按 formalism 已有的 flip/shift 拆开：
  - **flip（0/1）**= 爬到的机制域身份对不对（相对 ground truth 域，T2 实例 = D 的 loss-landscape/非凸优化域）
  - **shift（0-2）**= 域内爬多深（原爬层判据保留为 shift 分量）
  - **align = flip × form**（form = shift+预言力+边界）：形态再高，域错 = 没对准 ground truth → 0。这就是 formalism "score = 修正距离到 argmax leaf" 在思考质量上的实例化——**judge 是 formalism 的性质，不是 ad-hoc labeler**。
  - **对已有 v2 数据重打分**（判分校准规则：先对齐判据再比；不调 27b、不跑新实验）：
    | 臂 | flip | shift | 预言力 | 边界 | form(0-6) | align |
    |----|------|-------|--------|------|-----------|-------|
    | 臂A | 0 | 1.00 | 0.00 | 1.00 | 2.00 | 0.00 |
    | 臂B | 0 | 2.00 | 2.00 | 1.67 | 5.67 | 0.00 |
  - flip 证据 = scores_v2.md 关键词统计（D 机制域词 0/6 样本 0 命中，混沌域 6/6 样本 141 命中）→ 两臂 flip 全 0。
  - **form 方向未翻转**（臂B 5.67 > 臂A 2.00，与原 v2 总分一致）；新增 align 维度把"形似神未到"精确化：**shift/预言/边界高（形似）+ flip=0（神未到/域错）**。
  - 意义：T2 发现的"域偏移"不是额外的 ad-hoc 发现，**它就是 formalism 的 flip 分量**——思考质量成为 formalism 的一个性质，与 #53 的 judge 机制同构（GPU 实例：surface-vs-deep 修正；思考实例：域内深度 vs 域身份修正）。

  **step 1 — 阈值校准（诚实结论）**：T2 不提供 T1 触发阈值的**数值**校准点——T2 测的是思考**质量**（爬层/预言/边界），T1 阈值测的是思考**薄度**（430 字符/调用，来自 223 会话扫描基线），两者不同维度。T2 提供的是触发**文案**校准（域锚点 + 因果层指令），已落地 T1（stage-gate 仓 e20a2fb，`_T1_REFLECTION` 加"别顺字面停在怎么算/为什么难，往难的结构原因再爬一层"+通用域锚点核对）。数值阈值（5 轮/430 字符）维持 223 会话基线，待生产 HIT 数据回来再校准（与 T4 阈值同批）。

  **step 3 — 登记**：research-agi-budget 子项⑥已含 T1-T4（`context.think_trigger_branch`），本整合把 T3 从"待 T1+T2"推进到"整合完成"。能力证据落点：27b 在 general 提示下能复刻 D 三步链的**形式**（form 5.67/6），但 flip=0（域偏移 100%）——"AGI 系统能接住 D 思路"的证据是**形式的**，内容的（正确机制域）尚未接住，这正是 think-trigger 要补的（触发词带域锚点+因果层指令）。

### T5 流程索引层（咒语=调度器，D 2026-11-25 提出）
- 目标：把咒语从"固定指针"（先压后展→总走六阶段）改成"动态检索"（按问题类型找相关流程）
- 洞察（D）：咒语不是思考程序，而是思考流程的调度器——索引+检索+执行。和 RAG（检索增强生成）同构，检索对象从文本片段换成思考流程。信息论上站得住：调度器信息量远小于被调度程序。
- 三层设计：
  - 索引层：流程库（pfb/loop/*.md 六阶段 + T4 打转检测 + 选域三步）
  - 检索层：问题类型→流程组合的路由表
  - 执行层：执行检索到的流程
- 路由表（初稿）：
  | 问题类型 | 检索到的流程 |
  |---|---|
  | 理论研究 | 01 分解+02 调研+02.5 核验+03 行动+04 执行+04.5 复核 |
  | 调试卡住 | T4 打转检测+general 思考升级 |
  | 选域 | 选域三步（校验范围/迁移条件/实验新条件） |
  | 证据质量 | 02 证据质量分级（四档 bias 可识别性） |
- 边界（诚实）：① 检索依赖问题分类（又回到选域），27b 分类弱可能找错流程；② 执行质量取决于模型底层能力（咒语解决"找对流程"，解决不了"执行得好"）。
- 验收：路由表设计完成+咒语机制改成动态检索+验证不同类型问题检索到不同流程
- 状态：⚠️ **半应用（2026-11-26 二次核验修正）**——首轮核验只查 pfb@main 误判"未落盘"；二次核验发现 T5 活在 `thinkmech-review` 分支（pfb-thinkmech worktree：`loop/ROUTING.md` 3162B + CLAUDE.md 调度器"触发词：先压后展"节均在）。真问题 = **未合入 main 生产线**：pfb@main 无 ROUTING.md、无调度器；CLAUDE.md 保护文件 patch 被审批拦截是合并阻塞点。已处理：ROUTING.md 落 main（可逆，自主）+ CLAUDE.md 调度器节进 APPROVALS 队列（保护文件红线）。**导出规则：核验机制状态必须遍历所有 worktree/分支（git worktree list），单 worktree grep=0 不构成"不存在"结论。**
- **T2b/T2c 域锚点实验（2026-11-25，验收 T2c 前补做，预注册先于数据）**：
  - T2b 软锚点（T1 生产文案的"核对爬到的机制域是不是这个问题所在的域"句）：**无效 0/3**（D 机制域 0 命中，混沌域 13-17 次/样本，同控制臂）。机制：自查型锚点预设模型能识别正确域，27b 选域 gap 使其感知不到自己的漂移。
  - T2c 显式域声明（"这是计算复杂性/优化问题——loss landscape 非凸优化，不是物理动力学，不要用混沌框架"）：**有效 3/3**（D 机制域 19-26 次/样本，混沌域降到 1-5；内容质检 3/3 域内真推理非 prompt 回声；3/3 推出 D 原文没有的新可检验预言：Lipschitz 常数随深度增长 / CNN vs MLP Hessian 条件数 / 初始化 σ_c 相变 / Hessian 负特征值比例随 epoch 下降）。
  - **落点**：① ROUTING.md 加"显式域声明"列——路由结果 = 流程 + 域（路由器必须给域，不指望模型自己找）；② T1 软锚点句保留（无害）但单独无效，域由 T5 路由器提供（不动 stop_hook.py 红线文件）；③ 边界：显式域声明 = 选域外移到 prompt 外部，不证明 27b 能自主选域（仍 gap）；路由半边（27b 分类问题类型）开放。
  - 文件：prereg_t2b.md / prereg_t2c.md / raw_outputs_t2b.json / raw_outputs_t2c.json / run_exp_t2b.py / run_exp_t2c.py / scores_t2b_t2c.md
- **T2 实验给出的触发词改进建议（2026-11-25，T3 直接可用）**：
  - T1 当前文案（`_T1_REFLECTION`）："这背后的 general 机制是什么？能推出什么可检验预言？"
  - T2 实验暴露两个缺口：① 27b 顺字面 priming 停在表层机制（100% 滑向混沌域，0/6 触及 D 的 loss landscape 域）；② 27b 停在"怎么算/为什么难"层，没深挖"难的结构原因是什么、难易由什么决定"。
  - **建议改进文案**（加域锚点 + 因果层指令）：
    "别顺字面停在'怎么算/为什么难'。往'难的结构原因是什么、难易由什么决定'再爬一层。如果这是优化/loss landscape 问题，别套物理动力学的框架。推出'如果X则Y'的可检验预言，说明什么条件下成立、什么条件下失效。"
  - 依据：臂B（带 general 提示）3/3 爬到机制层+推预言，臂A（无提示）0/3 推预言——general 提示有效；但 6/6 样本域偏移 100%——域锚点必要。
  - 注意：域锚点内容需按实际问题域调整（本例是 loss landscape；其他问题域需换锚点），不宜写死成单一域。

## 缺口标注
- [已核验 2026-11-25] stop_hook **能**访问 per-message thinking，T1 走首选路径：`stop_hook.py` L507/L528 读 `~/.hermes/state.db` messages 表 assistant 行的 `reasoning` 列（per-message thinking，非聚合），已提交 stage-gate `1b30bc6` + 5 场景复验全过。
- [已核验 2026-11-25] 27b 在 8787 = `qwen3.8-27b-mtp`（vllm NVFP4，OpenAI 兼容 /v1/chat/completions，thinking 模型：`reasoning` 字段单独返回，只抓 content 丢隐藏思考链）
- [标定结论 2026-11-25] 触发阈值 N/430：T3 整合判 **T2 数据只给文案校准、不给数值点**（T2 测思考质量/爬层，T1 阈值测思考薄度，不同维度）→ 阈值保持先拍值 N=5、430/调用（223 会话扫描基线），留待生产数据积累后校准（`stop_hook.py` L410/L411 注释已注明）。

## 任务表（派发只执行表内条目）
| 任务 | 执行方 | 状态 |
|------|--------|------|
| T1 思考触发 hook 实现 | subagent A | 已提交（stage-gate 仓 1b30bc6 + APPROVALS 08697954，2026-11-25 01:33 复验 5 场景全过） |
| T2 接着考虑实验（预注册+跑） | subagent B | 完成 2026-11-25 (commit 002eada24) |
| T3 落点整合（T1+T2 完成后） | Lead（T1+T2 回来后） | ✅ 整合完成 2026-11-25（judge 整合：爬层按 formalism flip/shift 拆，align=flip×form；对 v2 数据重打分 form 方向未翻转+新增 align 维度；阈值校准=T2 只给文案校准不给数值点；详见 T3 节） |
| T4 | 修脚本卡住→general 思考升级触发 | ✅ 真检测已提交 (stage-gate 7229159 + APPROVALS eeae4de1, 9场景全过+12生产session 0误报) |
| T5 | 流程索引层（咒语=调度器，索引+检索+执行） | ⚠️ **半应用（2026-11-26 二次核验修正）**——T5 活在 `thinkmech-review` 分支（pfb-thinkmech worktree：loop/ROUTING.md 存在+CLAUDE.md 调度器在），**未合入 main**（pfb 生产线无调度器）；CLAUDE.md 是保护文件，patch 被审批拦截=合并阻塞点。教训：Lead 首轮只查 pfb@main 就下"幻影"结论=读错 worktree，与"反复出现同一结果可能在读旧文件"同源 |
| T6 | 机制活性状态机（registry+checker+gate+巡检，D 2026-11-26） | 设计中（见 T6 节） |
| T6 SOP 检查点效果验证（prompt 级代理） | Lead | ✅ 2026-11-25：检查点块 3/3 结构自查+2/3 新预言，域不回退——SOP 核心机制 prompt 级有效；完整 agent 级 A/B 待异族 judge |
| T7 always 层加牙（自评式→可执行式） | Lead | ✅ 2026-11-25：D 问'为何不 always/不留 SOP'→T2b 证 always+泛化自评无效(0/3)、T6 证可执行检查点有效(3/3)→routing.json self-check 从'不用回答'升'每轮一行可执行自问(内部不播报)'；SOP 已在 CLAUDE.md+loop/*.md+ROUTING.md；常态薄(92.8%无思考)由 always 可执行自问补 |
| T8b pfb 六阶段 vs 直接求解 smoke test | subagent | ✅ 2026-11-25（report `exp-results/t8b-smoke-report.md`，commits da7e1ccf9→最新）：主指标 unit 级覆盖 A 0.900 / B 0.883（Δ-0.017，机械 judge 层面无覆盖退化）；correctness 时点快照 0/6（A 0/3、B 0/3 命中 3090×4/W4/n=2）；截断/复读：A 0/3 截断 2/3 复读≥5，B 13/18 stage 截断（72%）3/18 复读≥5。**结构性断点（§3.1/§3.2，归因已修正）**：N-5.1 显存门 6/6 量化（模型层基本到位，弱在未逐候选淘汰）；N-5.2 带宽门 0/6——**主因不是模型能力，是题面与 gold 锚点约束集不一致**（题面 32K 下限+无延迟目标，774/1034/1574 的推导前提 @64K+吞吐目标不在题面内；与 `construct-mismatch-20261123.md` 发现一致，证据链 ① 类）。**对 T8c 的硬前置：token-matched 对照前必须先消解剩余题面歧义（① 64K 定值、③ c_pass 口径；② 候选集 T8b 题面是自行搜索、未定死——模型自由纳入的 4090 会翻转成本最优 winner（见 4090 候选集敏感性），故 T8c 必须把候选集显式定死），否则对照同样被 mismatch 污染**。**§2 探针修正（commit e54a24590）：correctness 探针"窗口内最早卡型"启发式与题面要求的条件性推荐格式冲突，6/6 人工核验后修正——A2 的"3090×2/INT8 配置断"是场景矩阵首行伪影（真实主推荐 2×4090+FP8/INT8）；A3 为关键样本：gold 配置 4×3090 被完整评估（候选D，TCO+敏感性分析齐全）但加权评分 5.9 列第 7/7 末位（输给 2×4090 7.1）= winner 可达、排序分歧，是题面 mismatch 的直接证据（32K 画像下成本权重 30% + 4×3090 性能分仅 5，双重劣势垫底）；A1 形态相反：3090 全文 0 次出现（从未进入候选集，断点在候选构建阶段，非显存门排除）= winner 不可达。binary 0/6 不变，归因从"候选阶段跑偏为主"修正为"32K 画像下 gold 配置竞争力排序本就不同"。**§3.2 定量推导（commit 12ae8c993）：N-5.2 带宽下限的代数结构被精确恢复——`BW_floor = 20×(W_bytes + 24.7)` 在 W4/W8/W16 三点残差全 0.000（截距 494=20×24.7 恰=斜率×`calc.py` KV_PER_STREAM，结构钉死），① 类可复算；物理解释 r=20 即 20 tok/s（≈50ms/token）解码目标、24.7 即 @64K 单流 KV 属 ② 类（conf 0.7，gold 标 S-a 黑盒）。由此 mismatch 被量化：T8b 32K 画像下等价下限应为 527/787/1327 GB/s（较 gold 降 32/24/16%），0/6 带宽门缺失=题面分叉非模型失败。**公式泛化+6/6 实证校验+calc.py 同构（commit e50830793 修正版）：一般式 每卡需求 `r×(W + n_streams×KV)/n_cards` vs 每卡有效带宽 `bw_peak×η_bw`（权重按 TP 分摊、KV 按流数非卡数分摊；准入门按一卡一流 n_streams=n_cards 施加，η_bw=0.80 取 calc.py），用 gold-tree.md N-5.2 全部 6 个 pass/fail 判断校验 6/6 吻合；真实赢家 3090×4/W4/n=2（n_streams=2）代入=317<748.8 pass 与 gold winner 一致；3090×2/W8 为区分性检验（KV 若按卡数分摊则判 pass 与 gold fail 矛盾，故 KV 按流数分摊，结构钉死）。**关键同构**：该式与 calc.py t_decode（L64）代数同构——r 为目标每流速率，N-5.2 不是独立黑盒而是 c_pass decode 项同一套物理的带宽下限表达。N-5.2 从 S-a 黑盒升级为可复算白盒（4 参数 r=20/KV@64K=24.7/η_bw=0.80/bw_peak 均有 ①类来源），物理解释 conf 0.7→0.9。**gold 树内部一致性核验（commit 3421b006c，实跑 calc.py）：四项验收锚全过——c_pass(3090×4/W4/n=2)=0.681≈0.679 ✅、六弹性 6/6 ✅、prefill:decode=40.1:59.9≈40:60 ✅、winner 排名 3090×4/W4/n=2 < 3090×2/W4/n=1 ✅ → gold 树自洽（decode 物理+成本模型+带宽门三者一致），T8b 0/6 坐实为题面 32K 画像 vs gold 64K 画像分叉，非 gold 锚点自身不一致**。**T8c oracle 种子（commit d41ab1bf7）：`exp-results/gold_gpu_oracle.py` 独立 gold 预言机——import calc.py 的 c_pass/mem_per_card + 本轮恢复的 N-5.2 门，3/3 验收过（winner 3090×4/W4/n=2、c_pass 0.681≈0.679、N-5.2 6/6）；建模发现：n 是部署约定 n_cards//2（2卡/流）非自由优化变量（自由 n 会误选 n=3），候选集暂限 3090/V100（①类规格齐全），T8c 补 4090/L40S/A100/H100/M2Ultra 的 ①类规格后可扩**。**4090 候选集敏感性（本轮新增，`check_4090_flip()` ①类可复算）：gold 树候选集（gold-tree.md L94）不含 4090，但 T8b 题面是『自行搜索』——用 KB `rtx-4090.json`（①类 conf 0.85，口径与 calc.py 3090 一致 FP16 non-tensor=2×FP32：3090→71/4090→165.2）代入 gold 64K+c_pass 口径，4090×4/W4/n=2=0.635 < 3090×4/W4/n=2=0.681 → **winner 翻转为 4090**（盈亏平衡价≈$1905≫KB MSRP $1599，对 3090 价 $1050~$2000 稳健）。即 gold winner 是『候选集不含 4090』的条件性结论 = construct mismatch 第三维：候选集依赖。② 候选集从『T8b 已定死』修正为『未消解』（T8b 题面是自行搜索、未定死），T8c 必须显式定死候选集**。**⚠️ harness 预算缺陷 flag（T8c 根因诊断回指）**：B 臂 13/18=72% stage 截断 = per-stage 4096 cap 碎片化饿死评估/收尾阶段（同 T8c 机制）⇒ B coverage 0.883 是**下界**，Δ-0.017 幅度有偏（方向安全）；详见 `exp-results/t8c-stop-rootcause-20261125.md` |
| J1 judge correctness 层设计（coverage 陷阱修复） | subagent | ✅ 完成 2026-11-25（commits 92aa24a76 核心+5d27e0ca9 cov口径+96eb7e041 敏感性+7a93bc03e R轴机制/FP边界+3123d913c v1修复+ea8369aec/1f78d0e63 独立交叉验证+v1.1 未X否定族）：设计文档 correctness-layer-design.md + 原型 correctness_layer_v0.py（独立运行，无 LLM）+ dry-run correctness-layer-dryrun-20261125.md/.json。**验收 5/5**：①机械+连续（正则/计数/bge-m3 对照，无 LLM）②复用 gold 基础设施（gold-gpu-units.json 锚 7/7 一致 verify-anchors，无平行 gold）③A1/A3 判别（dry-run 3/3=100%：arm_a[0]→A1 / arm_a[2]→A3；且发现第三类 A2=候选集粒度断点，扩为三型）④T8b 6+S5 dry-run 分数表落盘 ⑤无质量提升 claim。**验证 5 维度**：因果性 selftest 11/11（含 V7 FP 边界已修 + V8 否定守卫"不X"族 + V9 否定守卫"未X"族）/ 复用忠实 anchors 7/7 / 判别力 dry-run 3/3 / 阈值稳健 sensitivity（A1/A3 全网格 100% 稳定，A2 71% 安全裕度 0.2）/ 格式鲁棒性（R 轴承重机制定位 + 假阳性边界量化并已由 v1+v1.1 修复：弱推荐语义兜底+否定守卫"不X"+"未X"两族）。**独立交叉验证（不靠层探针）**：arm_a[1] A2（4×3090=0 独立正则+逐行核验，澄清 T8b 报告"主推荐 2×4090"vs 本文档"2×3090 方案 A"=条件推荐矩阵分场景非矛盾）+ arm_a[2] A3（4×3090 评估 4 行/强推荐行 0 含 4×3090/5.9 垫底，与层探针 4/4 吻合），commits ea8369aec/1f78d0e63。judge_v1.py 未动（frozen）。commits 全链：92aa24a76 核心+5d27e0ca9 cov口径+96eb7e041 敏感性+7a93bc03e R轴机制/FP边界+3123d913c v1修复+ea8369aec/1f78d0e63 独立交叉验证(3条有gt)+f05e2b929 v1.1未X否定族+68f57fb0c sensitivity版本重验+fb60263ac 全7样本4×3090交叉验证。**给 Lead 的下一步建议**：**v1 R 轴假阳性修复已实现（commit 3123d913c）**——弱推荐语义兜底+否定守卫，V7（winner 评估+无关键词推荐→indeterminate，假阳性已修）+ V8（"不X"否定→仍 A3）；**v1.1 补否定守卫"未X"族**（`未采用|未选择|未采纳|未部署|未选用|未推荐`，防"未采用 4×3090, 建议优先部署 2×4090"这类行被误读为推荐 winner→假 indeterminate，V9 验证），selftest 11/11、dry-run 3/3 保持；**跨 run 推广前置条件已解除**。剩余方向：S 轴本批 7/7 近 0（准入规则数字无人实例化）→ 若更大样本复现，correctness 层价值从"区分断点"转"度量结构落地率"，S 轴权重应上调 |
| O1 套磁 discover：pfb 相关作者候选表 | subagent | ✅ 完成 2026-11-25（落点 `tasks/outreach/candidates.md` 730 行：117 候选/高18 中46 低53，覆盖 16 份本地文献；验收复算 2026-11-25：条目数=优先级合计=117 ✓，裸邮箱 0 ✓，机构不可证 113 处全标 [待核验] ✓ 红线合规；遗留：4 团队作者名单+邮箱待联网补全，属 discover→draft 阶段） |
| J2 correctness 层整合进 judge pipeline + 存量重算 | subagent | ✅ 完成 2026-11-25（commits 9fa00c2a0 骨架→2e40716f4 完整→4c3304138 修正→04d08ab40 最终）。整合入口 `research/judge_pipeline_v0.py`（独立运行, 自动适配 flat/nested/t8b/runs 四 schema, 单次只载一次 bge-m3, `--preset stock` 一键跑存量集）；联合分表 `research/joint-scores-20261125.md`（17 行 S0-r1..r10+S5+T8b 6 条, cov+CORR+五轴+三型 verdict）+ `judge-pipeline-v0-20261125.json`。**口径对齐全复现**：S5 cov=0.3889(基准 0.389±0.01✅)+T8b 6 条 verdict=A1/A2/A3/A2/A2/A2(6/6✅, 镜像 J1 load_samples 对称抽取+line-as-node 节点构造, 修了初稿 _first_text 只取首字段致 arm_b A2→A1 失真 + 整篇单节点致 T8b cov 全 0 两处口径坑)。judge_v1.py 未动(frozen, 只 import)。**三型分布**：S0 10 条 A1×6/A2×4/A3×0/ind×0；总体 17 条 A1×7/A2×9/A3×1/ind×0(A2 候选集粒度断点主导, A3 仅 T8b arm_a[2])。**补充分析(17 条扩展集, 非质量 claim)**：cov 均值按 verdict 单调 A1 0.179<A2 0.259<A3 0.278(A2 系统性高=coverage 陷阱量化)；cov 最高样本 S5(0.389)=A2 断点样本；Pearson(cov,CORR)=0.462(两轴互补非冗余=correctness 层必要性定量依据)；S0 flat cov∈[0.056,0.222] 全<S5 节点级 0.389(口径不可横比)。**runs 容器真实文件验证(commit b9fd5fc06)：arena-judge-s6s7-pack.json 30 条(output_text 变体, 此前会全落 unknown)路由 30/30 + 端到端跑通；四 schema 全部经验证**。**最终验收审计(2026-11-25)：MD 主表 17/17 行与 JSON 逐行一致(cov/CORR/verdict)+分布表自洽(A1=7/A2=9/A3=1/ind=0)+5 项对齐证据全在(S5 0.3889/T8b 6/6/S0 10/10/Pearson 0.462/top3 全断点)→ 交付物闭环, 无遗留** |
| T8c 题面前置消解+预注册（token-matched 对照设计） | subagent | 已派 2026-11-25（T8b 硬前置：① 64K 定值 ② 候选集显式定死（4090 敏感性已证 winner 翻转）③ c_pass 口径；产出=T8c 题面终稿+预注册判据（含 power analysis）+token-matched 对照设计；不产数据）。**J2 集成指针（2026-11-25 补）：三型断点分布应作为 T8c 预注册的 secondary endpoint**——工具已就绪 `research/judge_pipeline_v0.py`（对 T8c 两臂输出直接跑 `python3 judge_pipeline_v0.py <run文件> --qid gpu` 即得 cov+CORR+A1/A2/A3）；存量基线（17 条）三型分布 A1×7/A2×9/A3×1 可作对照先验；已知风险：A3 存量仅 1 条（T8b arm_a[2]），T8c 若要看 A3 检出需预注册时写明 n 与 power（A3 稀有=检出功效低，别把"A3=0"当"无 A3 断点"）；judge_v1 原始要点命中分对 A1/A2 完全盲区（区间重叠 [0.067,0.267]，见 joint-scores-20261125.md「整合价值核心证据」节），故 T8c 判据不应只用原分。**✅ 前置完成（2026-11-25，subagent）**：三歧义消解（①64K 定值 ②候选集定死 2 卡 3090+V100（4090 翻转已证）③c_pass 公式+14 参数与 calc.py 同构+并发约定 n=floor(n_cards/2)）；题面终稿 `t8c-spec-final.md` 冻结 `2c16f644f`；预注册 `t8c-preregistration.md` 判据冻结 `8c168c2a4`（W1 方向+W2 Fisher p<0.05+W3 断点深度后移；n=3 power=0 仅 smoke、n=9/臂 正式、smoke 分流规则 pre-commit）；§5 七项 gate 全机械核验：oracle 实跑 winner=3090×4/W4/n=2 ✅、selfcheck 独立转录 PASS ✅、judge 探针 4/4 ✅（J1 v1.2 EVAL_NUM 补 c_pass/¢/task，`feb568b59`，selftest 11/11 无回归）、runner `run_exp_t8c.py` 新建（Q 与 §4 围栏块 AST 逐字比对 MATCH 1671 字符，MAX_A=24576）`b2e9195b2` ✅、端点 ✅。遗留 gate：V100 实价 ③类假设（<$2033 翻转，跑前复核，subagent 无网→Lead 代查） |
| T8c smoke（n=3/臂）+三型判别+分流决策 | 后台进程 | ✅ 完成 2026-11-25（第 1 批 17:4x 因 gpu_price 歧义 6/6 误读作废归档 `invalid-runs/`；第 2 批 18:02 重跑 18:27 完成，judge v1.3.1）。**停止决策：Arm B 结构性截断失败（FINAL 截断 3/3=100%>50% 作废）→ 无法比较 → 按 pre-commit 规则停止**（预注册 §4 Stage 0 机械检查截断率≤50% 不过，B 臂有效样本 0）。Arm A 3/3 推荐 3090（正确 winner，c_pass 锚点）。**根因诊断**：B 臂截断=harness per-stage cap（4096）<模型 per-stage 需求（04/04.5 3/3 顶格，总需求 69227≫24576），token-matched 碎片化饿死 B 臂评估/收尾阶段 → 对照按当前设计结构性无法公平执行，归因从"B 臂失败"细化为"harness 预算分配缺陷"；**且 B 臂 0/3 无最终 winner 推荐**（04.5 综合阶段 3/3 句中截断，A 臂 3/3 有）⇒ "无法比较"=A 有最终答案 vs B 无最终答案；**且 run0 截断前已算出正确 winner（c_pass 0.6798≈gold 0.681），死在"说出来"这步**——流程开销挤爆 per-stage 预算，重冻预注册时需考虑"计算对但综合断"第四断点型（`exp-results/t8c-stop-rootcause-20261125.md`）。eval 落盘 `exp-results/t8c-smoke-eval.json`；状态源 `exp-results/t8c-smoke-state.json`（round 2）；跑数后预注册只读，post-hoc 修订另开文件 |
| O2 套磁 draft：18 High 候选个性化草稿 | subagent | 已派 2026-11-25（SOP academic-outreach §2：5 段 ≤150 词，§3-4 手工个性化=具体机制/数字/claim；本地文献驱动；邮箱列留 [待核验]——核验走 arena/ego-browser，未核验不发） |
| J3 因素分析：gold 树结构验证+性价比单参数估计器（D 11-25 修正方向） | subagent | 拆分 2026-11-25 17:05（首次派发死于输出上限零落盘，transcript salvage 两条事实：calc.py 实际路径=bench/rubric-v3/tasks/T0-local-27b/reference/calc.py；KB 本地已有全部目标卡 l40s/a100/h100/m5-ultra/m3-ultra.json，无需公开规格）。**J3b（数值+泛化，已派）**：c_pass 作用域边界可检验判据+候选集外泛化排名表（4090 引用已有 flip 结果，L40S/A100/H100/M2Ultra 用本地 KB 规格跑 oracle），排错样本归因作用域。**J3a（纯推理，待派）**：层级因素树+三性质按层级检查（正交/最小/完备开放论证），每节 <40 行增量 commit。**共同方向（objfunc-signal-log 含层级修正 240709ef）**：eval 效度=公式结构验证非异族同意；最小集是层级的（顶层 4 因素=3 性能+1 成本，各压缩下层）；c_pass=顶层估计器有作用域；不做质量提升 claim |

## 状态更新（2026-11-26 13:10，Lead 核验）
### 分支拓扑（重要，防再犯）
- **think-trigger 的活全在 `thinkmech-review` 分支**（T8b/T8c/J1/J2/O1/O2 + oracle + calc.py + KB 卡），不在 main。
- 两 worktree：`pfb` @ main（idea53+think-mechanism）、`pfb-thinkmech` @ thinkmech-review（think-trigger）。
- **派发 think-trigger 任务必须指向 pfb-thinkmech worktree**（J3b 首派死于 main worktree 找不到 oracle/calc.py/KB 卡）。
- thinkmech-review 已 push 远端备份（2026-11-26）；main 已与 origin/main 对齐（merge 3decbb1d2）。
### 任务状态修正
- **O2 实际已完成**（此前误判"死了"）：`tasks/outreach/candidates.md` 730 行在 thinkmech-review，来源核验闭环齐全（16 份本地文献全覆盖，姓名/机构不可证一律 [待核验]）。
- **J3b 确认零落盘死亡**（thinkmech-review 上无泛化排名表产物）：需在 pfb-thinkmech worktree 重派。
- **J3a 待派**（纯推理，层级因素树+三性质按层级检查）。

## T6-L 机制活性状态机（mechanism-liveness，2026-11-26 D 指令）

> D 原话："需要一个可靠的东西，可以保证 hook 挂载什么的百分百起作用，而不是我看不到你也有可能做错的黑盒。什么是类似 stage 的、可以查看注入情况的，并且逐状态可以迁移我们完整的机制，包括思考。"
> 触发事件：T5 半应用（记录"✅ 已实施"但 main 生产线无调度器，跨 worktree 不可见）；Lead 首轮核验读错 worktree 下错结论。

### 设计（四条腿，缺一即退回黑盒）
1. **registry**（`tools/stage-gate/stage_gate/mechanisms/registry.json`）：每个机制一条——
   `{id, kind: rule-injection|stop-hook-trigger|routing-dispatcher|patrol,
     mounts: [{worktree, file, marker}],   # 静态挂载证据：文件存在且含标记（多 worktree 全列）
     audit: {path, signature},             # 动态触发证据：审计日志路径+签名串
     ttl_hours,                            # 多久无触发证据算 UNKNOWN
     stages: [依赖它的阶段],                # 逐状态迁移：阶段声明依赖哪些机制
     note}`
2. **checker**（`stage_gate/mechanisms/check.py`）：逐机制三判——
   mounted?（每个 mount 点 grep marker）→ fired_recently?（audit 日志扫 signature 取最近 ts）→
   verdict ∈ ALIVE / DEAD / UNKNOWN + evidence（file:line / 日志行）。
   快照写 `~/.hermes/.stage-gate/mechanisms-status.json`（时间戳+全表+verdict）。
   **worktree 遍历是硬规则**：mounts 必须覆盖 `git worktree list` 全部相关 worktree，单 worktree grep=0 ≠ 不存在。
3. **gate 接入**：stage-gate 阶段推进前读快照——当前阶段 `stages` 声明的机制有 DEAD/UNKNOWN
   → block + 写明哪条机制缺什么证据。显式 waive 需写 APPROVALS.md（与红线一致）。
4. **可见性**：`python -m stage_gate.mechanisms.check --status` 一行全表（D 随时可跑）；
   project-tidy 每日巡检加 checker 步骤，有 DEAD 推微信。

### 首批 registry（6 条，2026-11-26 磁盘核验过）
| id | kind | 状态 |
|---|---|---|
| rule-injection | rule-injection | ALIVE（rules-injection.jsonl 19:18 在写，每轮留痕） |
| t1-thin-thinking | stop-hook-trigger | ALIVE（progress.log 有 HIT 签名） |
| t4-stubborn-spin | stop-hook-trigger | ALIVE（今日 15:36 HIT） |
| t5-routing-dispatcher | routing-dispatcher | HALF（ROUTING.md 已落 main d6d1b09bc；审计信号已修 a507703：sig ROUTING→自问(常驻)，旧 sig 是假信号；CLAUDE.md marker 待 APPROVALS #5 批准） |
| project-tidy-patrol | patrol | ALIVE（每日 cron + 今日 drift 检查行） |
| methodology-sync-patrol | patrol | ALIVE（今日 f0707c89 加的检查） |

### 任务表
| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 | 状态 |
|---|---|---|---|---|---|---|
| T6-L-S1 registry.json 初版（6 条，schema 见任务卡） | - | ~40 | ~70 | 1(stage-gate) | sub-27b | ✅ aefe09c + 修正 80f5006（patrol audit 路径 run.log 不存在→cron output glob_latest，Lead 校准） |
| T6-L-S2 checker（五判 verdict+快照+exit code，脚本落盘） | S1 | ~60 | ~130(分3次) | 1(stage-gate) | sub-27b | ✅ b50311f（Lead 实跑核验：6 verdict 全符预期，exit 0，快照 evidence 在 mount 级）⚠️ 当时"t5 age 32.7h=ROUTING 注入已停"结论有误：signature=ROUTING 是假信号（见 S4） |
| T6-L-S3 gate 接入 + project-tidy 巡检接线 + per-rule sha1（A→B→C 安全序） | S2 | ~80 | ~60 | 1(stage-gate) | sub-27b | ✅ 90e6840（Lead 验收：A engine.py:42 定义/:213 advance 调用+commit 3 文件纯净；B daily.sh T6L 段 diff 恰 4 行+bash -n 过；C jsonl 14 条 rules，文件型 3 条 sha1 独立复算全对，活 hook 备份 .bak-20261126 在；pytest 15 passed+真实 advance 未被误拦） |
| ④ 预算扫描数据迁移 main 生产线（69 文件+REPORT.md） | - | ~40 | ~45 | 1(pfb) | sub-27b | ✅ eeb738b（Lead 核验：commit 68 文件全在 budget-scan-719/ 下纯净，cov 三值独立复算一致；范围判断对——源 8 子目录只迁 ④ 对应的 q6-* 三个；worktree 黑洞解除） |
| T6-L-S4 t5 审计信号修复（signature ROUTING→自问(常驻)）+ CLAUDE.md marker 入 APPROVALS #5 | S2 | ~30 | ~20 | 1(stage-gate)+APPROVALS | 判断-Lead | ✅ a507703（Lead 自做：核 jsonl 发现旧 sig 匹配的是自问规则文本里顺带提的 ROUTING.md=假信号；t5 是 CLAUDE.md 层调度器不走注入 hook；改 sig 后 checker 报 t5 纯因 CLAUDE.md 缺 marker；marker 改动走 APPROVALS #5 待批——CLAUDE.md 受保护文件） |
| judge 加分项支持：超出 gold 深度的正确分解单独计数、不进 cov 分母（依据 gold-tree.md 停止判据声明 2026-11-26 D 定：可测量性收口+加分项） | gold-tree 声明（✅ 已落盘） | ~80（judge_pipeline_v0.py 匹配段） | ~60 | 1(thinkmech) | sub-27b | 排队（T8c 正式批 n=9/臂 前置；smoke 已跑完的数据如需重判也走新版 judge） |
| 实验台账（D 2026-11-26 需求：全局视角实验员）：骨架+六闸门（预注册/novelty定位/状态机/机械判据/排序权在arena） | - | - | ~60 | 1(thinkmech) | 判断-Lead | ✅ 202c9fb95（骨架落盘 exp-results/experiment-ledger.md；表体待盘点回填） |
| 台账表体回填：inventory JSON → 台账表（每实验一行：假设/臂/状态/结果/novelty diff） | 盘点 sub（experiment-inventory-20261126.json） | ~100(JSON) | ~80(表) | 1(thinkmech) | sub-27b | S1✅ 845d7ef8c（completeness 核验：11/37 complete，26 条欠账）S2 进行中 |
| 消融矩阵抽取：版本×题目×分数（每格标 judge 版本+n+缺口清单） | - | ~12 文件 | ~1 脚本+1 md | 0(禁commit,另一sub在跑) | sub-27b | r1 死于输出上限（扫 200+ 文件超 27b 能力，零落盘）→ r2 换路：显式文件清单（~12 个已知分数文件）+ probe 先行 |

> **验收标准变化（本次事件导出的规则）**："✅ 已实施"类记录必须附磁盘证据（文件路径+commit 或 checker verdict）；
> 自我申报的 ✅ 一律视为未验证。T6-L-S2 落地后，机制类状态以 checker verdict 为准。
> 100% 保证做不到（hook 可能被卸载/日志可能被截断），可达上限 = 死了可见（checker verdict）+ 会挡路（gate block）+ D 可查（--status 一行全表）。

### 扩展：artifact-placement 检查（2026-11-26 ④核验导出的第二病）
预算扫描批核验发现**第二种黑盒**：全部数据+分析（32 文件）落在兄弟 worktree `pfb-thinkmech`（thinkmech-review 分支）`modules/B-pipeline-ablation/data/`，pfb main 生产线不可见——与 T5 调度器同病（产物/机制落在看不见的地方）。
→ registry 加一类 `kind: artifact-placement`：声明"某类产物应在哪个 worktree/路径"，checker 断言产物落点对，落错 worktree = 报警。
例：`{id: budget-scan-data, kind: artifact-placement, expected: pfb/experiments/stage-ablation/, note: ④数据应在 main 生产线}`。
这使 T6-L 从"机制活没活"扩展到"东西落对地方没"，两者都是"你看不到我可能做错"的实例。

## 机制准入门（2026-11-26 D 约束："不能单纯堆机制，或者要确定能提升"）

> **约束**：任何新检测器/触发器/hook 在加之前必须过三关，缺一不加。这不是新机制，是**防止堆机制的门**——它直接减少未来机制数量（奥卡姆：先证必要再引入）。
> 来源：D 2026-11-26 纠正"不能单纯堆机制，或者要确定能提升"。

### 三关（缺一不加）
1. **瞄准哪类错误**：从 objfunc-signal-log 可查该错误类别的历史频率（不是"我觉得会有用"）。
2. **可检验提升预言**：加后 N 天内该类错误频率应降 X%（N/X 预注册，先 commit 再产数据）。
3. **验证方法**：怎么测（signal-log 周频率 / 反事实对照 / 异族 judge），落到可复算的数字。

### 已验证"能提升"的机制（T1/T4，2026-11-26 探针①反事实推断）
- 3 次高价值拦截中 **2 次反事实推断"没有它们就不会自己发现"**（conf 0.7）：
  - #1（11-25 10:38 t4）workshop 论文 0/21 承重数字空验证 bug——commit 已提交，不会回头查，是触发后重审才发现。
  - #2（11-25 13:05 t1）连续 5 轮"加强同一个结论"刷进度——连续 5 轮无自停迹象，是触发后自停。
- 另 1 次（#9 公式推导错误 ρ>0.5 出错）不确定，可能后续计算时自己发现。
- **结论**：T1/T4 在 6 天内拦截了至少 2 个"没有它们就不会发现"的真实错误 → "能提升"有直接证据，非假设。

### 当前错误分布（2026-11-26 探针④，64 条 signal-log → 我判 ~16 条真错误）
真实错误分布与 T1/T4 设计范围（薄思考/打转）**错配**——T1/T4 抓 A 类（薄/打转），D 实际纠正的 B/C/D/E 类基本没被瞄：
- **B 陈旧前提不复验**（幽灵阻塞 arena 登录引用两次 / "122 层"口径失实）——最高频，最该抓
- **C 过度宣称**（n=3 叫"端到端有效性测试"）
- **D 缺 general 思考**（"为什么你还是自己干活""全局方向"）——规则遵守问题非检测器覆盖问题（lead-context-budget 已有，修执行不加检测器）
- **E 概念误解**（套磁≠撒网 / "有利于项目"伪维度 / judge 构造效度）

### 候选检测器（排队，未建——需先攒基线频率）
| 候选 | 瞄准 | 预注册预言 | 验证 | 状态 |
|---|---|---|---|---|
| 陈旧前提复验 | B 类 | 加后 2 周 D 纠正中"引用陈旧前提"类归零或减半 | signal-log 该类周频率 | 排队，无基线（需先攒 1-2 周该类频率） |
| 过度宣称 | C 类 | 加后 2 周 overclaim 纠正归零 | signal-log + 论文 claim 审计 | 排队，无基线 |
| ~~缺 general 思考~~ | D 类 | — | — | **不加检测器**（规则遵守问题，lead-context-budget 已在，修执行） |

> **下一步不是建新检测器**：先把准入门写进 decomposition（本节），攒 1-2 周 B/C 类基线频率，有了基线再决定建不建。错误分布审计作为"何时加检测器"的决策依据，不是常态机制。
