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

### T3b 逐级机械 judge（D 2026-11-27 提议"上一级往下拆, 每级正确性用概念-公式标志"）
- 背景: 现有 correctness_layer_v0 是平的(36 gold 单元挂 sympy, N 轴锚叶子数值, S 轴仅 4 正则签名), 无"逐级"概念。D 提议 = 把 S 轴推广到全部 gold 节点 + 沿树递归。
- 探针已落地(21:50, commit 466555d12): q9_formula_instantiation_probe.py 把 Q9-v2.md 21 定义式做成机械签名, mention(L1)/instantiated(L2) 两级。结果: corr(judge,L1)=+0.21 vs corr(judge,L2)=+0.67; 预算 50→300 instantiation +614% ≫ mention +12%(预算真买深度非伪影); 逐门对账 7 门放水(J3/J4/J9/J10/J11/J13/J14) / 2 门真判别(J2/J12) / 1 门恒严(J5)。
- **本任务(v1 机械 judge)**: 把 21 签名升级为逐级 judge——每节点 score = 概念匹配 × 公式实例化 × 输入溯源, reliability 维(J9-J14)换机械判(消除 LLM-judge 放水)。
- 任务表:
  | 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
  |---|---|---|---|---|---|
  | S1 签名表抽共享模块 q9_gold_signatures.py(probe/judge 都 import, 不复制) | 无 | ~200 | ~150 | 1 | 脚本-Lead |
  | S2 逐级 judge v1: 节点级 score=概念×实例化×溯源, 输出 per-node JSON | S1 | ~150 | ~200 | 1 | 脚本-Lead |
  | S3 对 10 run 重打分, 对比 LLM-judge, 验证 reliability 维机械判消除放水 | S2 | ~100 | ~80 | 1 | 脚本-Lead |
- 验收: per-node score JSON 落盘; reliability 门(J9-J14)机械判与 LLM-judge 分歧处可逐条解释; 3 commit 各自 scoped add。

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
- 状态：✅ 已实施 2026-11-25（ROUTING.md 路由表 + CLAUDE.md 触发词改调度器：先路由再执行，默认六阶段宁全勿漏）。遗留外观项：CLAUDE.md L30 编号重复（两个 3），修正 patch 被保护文件审批拦下，待 D 同意后修。
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
| T5 | 流程索引层（咒语=调度器，索引+检索+执行） | ✅ 已实施 2026-11-25（ROUTING.md + CLAUDE.md 调度器路由；遗留 L30 编号外观项待 D 同意） |
| T6 SOP 检查点效果验证（prompt 级代理） | Lead | ✅ 2026-11-25：检查点块 3/3 结构自查+2/3 新预言，域不回退——SOP 核心机制 prompt 级有效；完整 agent 级 A/B 待异族 judge |
| T7 always 层加牙（自评式→可执行式） | Lead | ✅ 2026-11-25：D 问'为何不 always/不留 SOP'→T2b 证 always+泛化自评无效(0/3)、T6 证可执行检查点有效(3/3)→routing.json self-check 从'不用回答'升'每轮一行可执行自问(内部不播报)'；SOP 已在 CLAUDE.md+loop/*.md+ROUTING.md；常态薄(92.8%无思考)由 always 可执行自问补 |
| T8b pfb 六阶段 vs 直接求解 smoke test | subagent | ✅ 2026-11-25（report `exp-results/t8b-smoke-report.md`，commits da7e1ccf9→最新）：主指标 unit 级覆盖 A 0.900 / B 0.883（Δ-0.017，机械 judge 层面无覆盖退化）；correctness 时点快照 0/6（A 0/3、B 0/3 命中 3090×4/W4/n=2）；截断/复读：A 0/3 截断 2/3 复读≥5，B 13/18 stage 截断（72%）3/18 复读≥5。**结构性断点（§3.1/§3.2，归因已修正）**：N-5.1 显存门 6/6 量化（模型层基本到位，弱在未逐候选淘汰）；N-5.2 带宽门 0/6——**主因不是模型能力，是题面与 gold 锚点约束集不一致**（题面 32K 下限+无延迟目标，774/1034/1574 的推导前提 @64K+吞吐目标不在题面内；与 `construct-mismatch-20261123.md` 发现一致，证据链 ① 类）。**对 T8c 的硬前置：token-matched 对照前必须先消解剩余题面歧义（① 64K 定值、③ c_pass 口径；② 候选集 T8b 题面是自行搜索、未定死——模型自由纳入的 4090 会翻转成本最优 winner（见 4090 候选集敏感性），故 T8c 必须把候选集显式定死），否则对照同样被 mismatch 污染**。**§2 探针修正（commit e54a24590）：correctness 探针"窗口内最早卡型"启发式与题面要求的条件性推荐格式冲突，6/6 人工核验后修正——A2 的"3090×2/INT8 配置断"是场景矩阵首行伪影（真实主推荐 2×4090+FP8/INT8）；A3 为关键样本：gold 配置 4×3090 被完整评估（候选D，TCO+敏感性分析齐全）但加权评分 5.9 列第 7/7 末位（输给 2×4090 7.1）= winner 可达、排序分歧，是题面 mismatch 的直接证据（32K 画像下成本权重 30% + 4×3090 性能分仅 5，双重劣势垫底）；A1 形态相反：3090 全文 0 次出现（从未进入候选集，断点在候选构建阶段，非显存门排除）= winner 不可达。binary 0/6 不变，归因从"候选阶段跑偏为主"修正为"32K 画像下 gold 配置竞争力排序本就不同"。**§3.2 定量推导（commit 12ae8c993）：N-5.2 带宽下限的代数结构被精确恢复——`BW_floor = 20×(W_bytes + 24.7)` 在 W4/W8/W16 三点残差全 0.000（截距 494=20×24.7 恰=斜率×`calc.py` KV_PER_STREAM，结构钉死），① 类可复算；物理解释 r=20 即 20 tok/s（≈50ms/token）解码目标、24.7 即 @64K 单流 KV 属 ② 类（conf 0.7，gold 标 S-a 黑盒）。由此 mismatch 被量化：T8b 32K 画像下等价下限应为 527/787/1327 GB/s（较 gold 降 32/24/16%），0/6 带宽门缺失=题面分叉非模型失败。**公式泛化+6/6 实证校验+calc.py 同构（commit e50830793 修正版）：一般式 每卡需求 `r×(W + n_streams×KV)/n_cards` vs 每卡有效带宽 `bw_peak×η_bw`（权重按 TP 分摊、KV 按流数非卡数分摊；准入门按一卡一流 n_streams=n_cards 施加，η_bw=0.80 取 calc.py），用 gold-tree.md N-5.2 全部 6 个 pass/fail 判断校验 6/6 吻合；真实赢家 3090×4/W4/n=2（n_streams=2）代入=317<748.8 pass 与 gold winner 一致；3090×2/W8 为区分性检验（KV 若按卡数分摊则判 pass 与 gold fail 矛盾，故 KV 按流数分摊，结构钉死）。**关键同构**：该式与 calc.py t_decode（L64）代数同构——r 为目标每流速率，N-5.2 不是独立黑盒而是 c_pass decode 项同一套物理的带宽下限表达。N-5.2 从 S-a 黑盒升级为可复算白盒（4 参数 r=20/KV@64K=24.7/η_bw=0.80/bw_peak 均有 ①类来源），物理解释 conf 0.7→0.9。**gold 树内部一致性核验（commit 3421b006c，实跑 calc.py）：四项验收锚全过——c_pass(3090×4/W4/n=2)=0.681≈0.679 ✅、六弹性 6/6 ✅、prefill:decode=40.1:59.9≈40:60 ✅、winner 排名 3090×4/W4/n=2 < 3090×2/W4/n=1 ✅ → gold 树自洽（decode 物理+成本模型+带宽门三者一致），T8b 0/6 坐实为题面 32K 画像 vs gold 64K 画像分叉，非 gold 锚点自身不一致**。**T8c oracle 种子（commit d41ab1bf7）：`exp-results/gold_gpu_oracle.py` 独立 gold 预言机——import calc.py 的 c_pass/mem_per_card + 本轮恢复的 N-5.2 门，3/3 验收过（winner 3090×4/W4/n=2、c_pass 0.681≈0.679、N-5.2 6/6）；建模发现：n 是部署约定 n_cards//2（2卡/流）非自由优化变量（自由 n 会误选 n=3），候选集暂限 3090/V100（①类规格齐全），T8c 补 4090/L40S/A100/H100/M2Ultra 的 ①类规格后可扩**。**4090 候选集敏感性（本轮新增，`check_4090_flip()` ①类可复算）：gold 树候选集（gold-tree.md L94）不含 4090，但 T8b 题面是『自行搜索』——用 KB `rtx-4090.json`（①类 conf 0.85，口径与 calc.py 3090 一致 FP16 non-tensor=2×FP32：3090→71/4090→165.2）代入 gold 64K+c_pass 口径，4090×4/W4/n=2=0.635 < 3090×4/W4/n=2=0.681 → **winner 翻转为 4090**（盈亏平衡价≈$1905≫KB MSRP $1599，对 3090 价 $1050~$2000 稳健）。即 gold winner 是『候选集不含 4090』的条件性结论 = construct mismatch 第三维：候选集依赖。② 候选集从『T8b 已定死』修正为『未消解』（T8b 题面是自行搜索、未定死），T8c 必须显式定死候选集**。**⚠️ harness 预算缺陷 flag（T8c 根因诊断回指）**：B 臂 13/18=72% stage 截断 = per-stage 4096 cap 碎片化饿死评估/收尾阶段（同 T8c 机制）⇒ B coverage 0.883 是**下界**，Δ-0.017 幅度有偏（方向安全）；详见 `exp-results/t8c-stop-rootcause-20261125.md` |
| J1 judge correctness 层设计（coverage 陷阱修复） | subagent | ✅ 完成 2026-11-25（commits 92aa24a76 核心+5d27e0ca9 cov口径+96eb7e041 敏感性+7a93bc03e R轴机制/FP边界+3123d913c v1修复+ea8369aec/1f78d0e63 独立交叉验证+v1.1 未X否定族）：设计文档 correctness-layer-design.md + 原型 correctness_layer_v0.py（独立运行，无 LLM）+ dry-run correctness-layer-dryrun-20261125.md/.json。**验收 5/5**：①机械+连续（正则/计数/bge-m3 对照，无 LLM）②复用 gold 基础设施（gold-gpu-units.json 锚 7/7 一致 verify-anchors，无平行 gold）③A1/A3 判别（dry-run 3/3=100%：arm_a[0]→A1 / arm_a[2]→A3；且发现第三类 A2=候选集粒度断点，扩为三型）④T8b 6+S5 dry-run 分数表落盘 ⑤无质量提升 claim。**验证 5 维度**：因果性 selftest 11/11（含 V7 FP 边界已修 + V8 否定守卫"不X"族 + V9 否定守卫"未X"族）/ 复用忠实 anchors 7/7 / 判别力 dry-run 3/3 / 阈值稳健 sensitivity（A1/A3 全网格 100% 稳定，A2 71% 安全裕度 0.2）/ 格式鲁棒性（R 轴承重机制定位 + 假阳性边界量化并已由 v1+v1.1 修复：弱推荐语义兜底+否定守卫"不X"+"未X"两族）。**独立交叉验证（不靠层探针）**：arm_a[1] A2（4×3090=0 独立正则+逐行核验，澄清 T8b 报告"主推荐 2×4090"vs 本文档"2×3090 方案 A"=条件推荐矩阵分场景非矛盾）+ arm_a[2] A3（4×3090 评估 4 行/强推荐行 0 含 4×3090/5.9 垫底，与层探针 4/4 吻合），commits ea8369aec/1f78d0e63。judge_v1.py 未动（frozen）。commits 全链：92aa24a76 核心+5d27e0ca9 cov口径+96eb7e041 敏感性+7a93bc03e R轴机制/FP边界+3123d913c v1修复+ea8369aec/1f78d0e63 独立交叉验证(3条有gt)+f05e2b929 v1.1未X否定族+68f57fb0c sensitivity版本重验+fb60263ac 全7样本4×3090交叉验证。**给 Lead 的下一步建议**：**v1 R 轴假阳性修复已实现（commit 3123d913c）**——弱推荐语义兜底+否定守卫，V7（winner 评估+无关键词推荐→indeterminate，假阳性已修）+ V8（"不X"否定→仍 A3）；**v1.1 补否定守卫"未X"族**（`未采用|未选择|未采纳|未部署|未选用|未推荐`，防"未采用 4×3090, 建议优先部署 2×4090"这类行被误读为推荐 winner→假 indeterminate，V9 验证），selftest 11/11、dry-run 3/3 保持；**跨 run 推广前置条件已解除**。剩余方向：S 轴本批 7/7 近 0（准入规则数字无人实例化）→ 若更大样本复现，correctness 层价值从"区分断点"转"度量结构落地率"，S 轴权重应上调 |
| O1 套磁 discover：pfb 相关作者候选表 | subagent | ✅ 完成 2026-11-25（落点 `tasks/outreach/candidates.md` 730 行：117 候选/高18 中46 低53，覆盖 16 份本地文献；验收复算 2026-11-25：条目数=优先级合计=117 ✓，裸邮箱 0 ✓，机构不可证 113 处全标 [待核验] ✓ 红线合规；遗留：4 团队作者名单+邮箱待联网补全，属 discover→draft 阶段） |
| J2 correctness 层整合进 judge pipeline + 存量重算 | subagent | ✅ 完成 2026-11-25（commits 9fa00c2a0 骨架→2e40716f4 完整→4c3304138 修正→04d08ab40 最终）。整合入口 `research/judge_pipeline_v0.py`（独立运行, 自动适配 flat/nested/t8b/runs 四 schema, 单次只载一次 bge-m3, `--preset stock` 一键跑存量集）；联合分表 `research/joint-scores-20261125.md`（17 行 S0-r1..r10+S5+T8b 6 条, cov+CORR+五轴+三型 verdict）+ `judge-pipeline-v0-20261125.json`。**口径对齐全复现**：S5 cov=0.3889(基准 0.389±0.01✅)+T8b 6 条 verdict=A1/A2/A3/A2/A2/A2(6/6✅, 镜像 J1 load_samples 对称抽取+line-as-node 节点构造, 修了初稿 _first_text 只取首字段致 arm_b A2→A1 失真 + 整篇单节点致 T8b cov 全 0 两处口径坑)。judge_v1.py 未动(frozen, 只 import)。**三型分布**：S0 10 条 A1×6/A2×4/A3×0/ind×0；总体 17 条 A1×7/A2×9/A3×1/ind×0(A2 候选集粒度断点主导, A3 仅 T8b arm_a[2])。**补充分析(17 条扩展集, 非质量 claim)**：cov 均值按 verdict 单调 A1 0.179<A2 0.259<A3 0.278(A2 系统性高=coverage 陷阱量化)；cov 最高样本 S5(0.389)=A2 断点样本；Pearson(cov,CORR)=0.462(两轴互补非冗余=correctness 层必要性定量依据)；S0 flat cov∈[0.056,0.222] 全<S5 节点级 0.389(口径不可横比)。**runs 容器真实文件验证(commit b9fd5fc06)：arena-judge-s6s7-pack.json 30 条(output_text 变体, 此前会全落 unknown)路由 30/30 + 端到端跑通；四 schema 全部经验证**。**最终验收审计(2026-11-25)：MD 主表 17/17 行与 JSON 逐行一致(cov/CORR/verdict)+分布表自洽(A1=7/A2=9/A3=1/ind=0)+5 项对齐证据全在(S5 0.3889/T8b 6/6/S0 10/10/Pearson 0.462/top3 全断点)→ 交付物闭环, 无遗留** |
| T8c 题面前置消解+预注册（token-matched 对照设计） | subagent | 已派 2026-11-25（T8b 硬前置：① 64K 定值 ② 候选集显式定死（4090 敏感性已证 winner 翻转）③ c_pass 口径；产出=T8c 题面终稿+预注册判据（含 power analysis）+token-matched 对照设计；不产数据）。**J2 集成指针（2026-11-25 补）：三型断点分布应作为 T8c 预注册的 secondary endpoint**——工具已就绪 `research/judge_pipeline_v0.py`（对 T8c 两臂输出直接跑 `python3 judge_pipeline_v0.py <run文件> --qid gpu` 即得 cov+CORR+A1/A2/A3）；存量基线（17 条）三型分布 A1×7/A2×9/A3×1 可作对照先验；已知风险：A3 存量仅 1 条（T8b arm_a[2]），T8c 若要看 A3 检出需预注册时写明 n 与 power（A3 稀有=检出功效低，别把"A3=0"当"无 A3 断点"）；judge_v1 原始要点命中分对 A1/A2 完全盲区（区间重叠 [0.067,0.267]，见 joint-scores-20261125.md「整合价值核心证据」节），故 T8c 判据不应只用原分。**✅ 前置完成（2026-11-25，subagent）**：三歧义消解（①64K 定值 ②候选集定死 2 卡 3090+V100（4090 翻转已证）③c_pass 公式+14 参数与 calc.py 同构+并发约定 n=floor(n_cards/2)）；题面终稿 `t8c-spec-final.md` 冻结 `2c16f644f`；预注册 `t8c-preregistration.md` 判据冻结 `8c168c2a4`（W1 方向+W2 Fisher p<0.05+W3 断点深度后移；n=3 power=0 仅 smoke、n=9/臂 正式、smoke 分流规则 pre-commit）；§5 七项 gate 全机械核验：oracle 实跑 winner=3090×4/W4/n=2 ✅、selfcheck 独立转录 PASS ✅、judge 探针 4/4 ✅（J1 v1.2 EVAL_NUM 补 c_pass/¢/task，`feb568b59`，selftest 11/11 无回归）、runner `run_exp_t8c.py` 新建（Q 与 §4 围栏块 AST 逐字比对 MATCH 1671 字符，MAX_A=24576）`b2e9195b2` ✅、端点 ✅。遗留 gate：V100 实价 ③类假设（<$2033 翻转，跑前复核，subagent 无网→Lead 代查）**→ 已消解（2026-11-26，①类实价 ¥5000≈$704 击穿，post-hoc 变更 1 + 重锚定 dd6d254f6，见 t8c-formal-blocked.md）** |
| T8c smoke（n=3/臂）+三型判别+分流决策 | 后台进程 | ✅ 完成 2026-11-25（第 1 批 17:4x 因 gpu_price 歧义 6/6 误读作废归档 `invalid-runs/`；第 2 批 18:02 重跑 18:27 完成，judge v1.3.1）。**停止决策：Arm B 结构性截断失败（FINAL 截断 3/3=100%>50% 作废）→ 无法比较 → 按 pre-commit 规则停止**（预注册 §4 Stage 0 机械检查截断率≤50% 不过，B 臂有效样本 0）。Arm A 3/3 推荐 3090（正确 winner，c_pass 锚点）。**根因诊断**：B 臂截断=harness per-stage cap（4096）<模型 per-stage 需求（04/04.5 3/3 顶格，总需求 69227≫24576），token-matched 碎片化饿死 B 臂评估/收尾阶段 → 对照按当前设计结构性无法公平执行，归因从"B 臂失败"细化为"harness 预算分配缺陷"；**且 B 臂 0/3 无最终 winner 推荐**（04.5 综合阶段 3/3 句中截断，A 臂 3/3 有）⇒ "无法比较"=A 有最终答案 vs B 无最终答案；**且 run0 截断前已算出正确 winner（c_pass 0.6798≈gold 0.681），死在"说出来"这步**——流程开销挤爆 per-stage 预算，重冻预注册时需考虑"计算对但综合断"第四断点型（`exp-results/t8c-stop-rootcause-20261125.md`）。eval 落盘 `exp-results/t8c-smoke-eval.json`；状态源 `exp-results/t8c-smoke-state.json`（round 2）；跑数后预注册只读，post-hoc 修订另开文件 |
| O2 套磁 draft：18 High 候选个性化草稿 | subagent | 已派 2026-11-25（SOP academic-outreach §2：5 段 ≤150 词，§3-4 手工个性化=具体机制/数字/claim；本地文献驱动；邮箱列留 [待核验]——核验走 arena/ego-browser，未核验不发） |
| J3 因素分析：gold 树结构验证+性价比单参数估计器（D 11-25 修正方向） | subagent | 拆分 2026-11-25 17:05（首次派发死于输出上限零落盘，transcript salvage 两条事实：calc.py 实际路径=bench/rubric-v3/tasks/T0-local-27b/reference/calc.py；KB 本地已有全部目标卡 l40s/a100/h100/m5-ultra/m3-ultra.json，无需公开规格）。**J3b（数值+泛化，已派）**：c_pass 作用域边界可检验判据+候选集外泛化排名表（4090 引用已有 flip 结果，L40S/A100/H100/M2Ultra 用本地 KB 规格跑 oracle），排错样本归因作用域。**J3a（拆 S1/S2，2026-11-26）**：原版已死 2 次（464 行输入+5 节写入 > 27b 输出上限）→ 拆 S1 纯提取 + S2 检查/综合。**S1 v1 也死了**（deleg_8e79032b，15:23，死于"手写 JSON transcribe"撑爆输出流——读 2 文件 OK，写全树 JSON 那步 >100 行进输出流）。**S1 v2 换路重派**（deleg_3922e276）：JSON 由 ≤60 行 python 脚本解析源文件后落盘，模型输出流只放脚本+1 行结果，JSON 内容不进输出流（树结构规整：节点 ID `N-3.1.3.1` 段数=深度，脚本解析近乎机械）。S2 串行待 S1（卡 TASK-J3a-S2-checks.md）。**共同方向（objfunc-signal-log 含层级修正 240709ef）**：eval 效度=公式结构验证非异族同意；最小集是层级的（顶层 4 因素=3 性能+1 成本，各压缩下层）；c_pass=顶层估计器有作用域；不做质量提升 claim |

## 状态更新（2026-11-26 13:10，Lead 核验）
### 分支拓扑（重要，防再犯）
- **think-trigger 的活全在 `thinkmech-review` 分支**（T8b/T8c/J1/J2/O1/O2 + oracle + calc.py + KB 卡），不在 main。
- 两 worktree：`pfb` @ main（idea53+think-mechanism）、`pfb-thinkmech` @ thinkmech-review（think-trigger）。
- **派发 think-trigger 任务必须指向 pfb-thinkmech worktree**（J3b 首派死于 main worktree 找不到 oracle/calc.py/KB 卡）。
- thinkmech-review 已 push 远端备份（2026-11-26）；main 已与 origin/main 对齐（merge 3decbb1d2）。
### 任务状态修正
- **O2 实际已完成**（此前误判"死了"）：`tasks/outreach/candidates.md` 730 行在 thinkmech-review，来源核验闭环齐全（16 份本地文献全覆盖，姓名/机构不可证一律 [待核验]）。
- **J3b 已完成**（8ad7dea37，此前"零落盘死亡"行 stale）：泛化排名表 + tf_peak 敏感性 + 4 判据 + 排错归因全在 `j3b_generalization.py`。
- **J3a DONE（2026-11-26 a966b5488）**：S1/S2 机械层=确定性脚本（extract_j3a_factors.py 37节点/守恒7组 + verify_j3a_properties.py §4完备无缺口），判断层 Lead 直判（§2 SHARED≠非正交 conf0.8 / §3 五层必要 conf0.85 / §5 四重限定作用域）。开放项 2 个：l2_hit per-path 弹性标定（**设计已落盘 exp-results/j3a-l2hit-calib-design.md**：F-A 框架 + 双工况探针，待 GPU 2h 执行）、prefill/decode share 负载分布标定（**2026-11-26 已推导闭合**：calc.py 线性式纯推出负载敏感度曲线，基线精确复现 0.401/0.599 与 L4 F-A 一致，降级为"已推导+作用域注明"，见 j3a-l2hit-calib-design.md §6；第三个"N-5.3 疑重复"已排除：cache_hit_rate≠l2_hit，grep 核验）。另勘误：L 系列（L0-L6）在 projects/decomp/bench/gold/，gold-tree.md 头部 L 链接为死链。

## 任务表补充（2026-11-26，强制列格式）
| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 | 状态 |
|------|------|--------|--------|---------|------|------|
| T8c-ReAnchor-A：6 文件重锚定（V100 $704/winner→V100×4/MAX_A 73728）+probe fixture 重写 | 无（价格已①类核验） | ~30（grep 定点，禁整读） | ~60 | 1 | executor-cron（试点，任务卡 exp-results/reanchor-taskcard.md 给全 old→new 映射） | ✅ 完成 2026-11-26（commit dd6d254f6，回执 receipts/T8c-ReAnchor-A.json=DONE。executor 应用 37/38 点后超时，supervisor 接管补 4d/4e/4f 漏点+commit。验收：selfcheck PASS、oracle PASS(N-5.2 6/6)、judge 4/6 核心型全绿；judge TBL 正则缺口另行立项 T8c-JudgeFix） |
| T8c-ReAnchor-B：post-hoc 文档（价格重锚+B' 预算修复记录；前置 dd6d254f6 已落地） | ReAnchor-A 的 commit | ~10 | ~80 | 1 | executor-cron（纯执行，内容任务卡 exp-results/posthoc-taskcard.md 给全） | 就绪 | ✅ 完成 2026-11-26（commit 17f691a9d，Lead 验收：任务卡正文 L13-60 替换 hash 占位符后与落盘逐字节一致 sha256=3947248f4a0264b7） |
| T8c smoke 重跑（n=3/臂，新锚点+MAX_A 73728；前置验证 2026-11-26 全过） | ReAnchor-A 验证全过 | - | 落盘 json | - | 后台进程（nohup，执行者起+探活接力+eval；任务卡 exp-results/smoke-rerun-taskcard.md） | ✅ done 2026-11-26 23:52（回执 receipts/T8c-smoke-rerun.json；判决=停止不扩样 s_A=0/3 s_B=1/2 方向弱正；执行者 97852 死于 A 臂后 supervisor 接力 B 臂 1383；报告 exp-results/t8c-smoke-rerun-report-20261126.md，F1 judge 批次噪声/F2 复读审计降级(e420e60cf)/F3 Hermes 跟踪≠setsid 已写进协议） |
| T8c-N9：正式跑（补 run4-9，A×6+B×6 共 9/臂） | T8c-HarnessRetry 验证过 + smoke 重跑 Stage 0 过 | - | - | - | 后台进程（executor-cron 领，任务=单命令后台进程+回执） | ✅ done+判决 2026-11-27（执行者回执 T8c-N9.json=DONE commit 9a5659020，9/9 无重复 run、0 截断、goal state PID 已清；Lead eval t8c-n9-eval.json：W1✗ 3/9=3/9 p=1.0 / W2✗ / W3✓ 3.22>3.11 → **H1 不成立**，判决文档 exp-results/t8c-n9-verdict-20261127.md；预言 #16 证伪已核销——smoke 分离迹象在新增 6 run 下完全反转 A 3/6 vs B 1/6，Stage 0 n=3 分流假阳性警示已记录；**本线 T8c 收口不再扩样**，「流程价值换度量/换题面」另立项） |
| T8c-N9-Runner：n=9 补跑脚本 run_exp_t8c_n9.py（A/B 臂 run4-9 追加不覆盖，import 复用冻结 Q/STAGES/caps/call 防题面漂移） | 无 | ~140（run_exp_t8c.py 全文） | ~80（新脚本） | 1 | sub-27b（纯执行+脚本产出<100行；边界：不改原脚本、不发实验请求、只 py_compile+import 冒烟） | ✅ done+验收 2026-11-27（commit 1c5489ff8；Lead 验收：93 行 / import run_exp_t8c as base 复用冻结 Q+STAGES+caps+call / 无直接 HTTP / A+B 均 append 不覆盖 / 内置 .pre-n9 备份 / B sample 字段与原 run_arm_b 一致） |
| T8c-N9-Eval：n=9 三判据评估脚本 eval_t8c_n9.py（W1 方向+W2 Fisher+W3 深度，复用 eval_t8c_smoke.evaluate 口径，含合成数据 3 场景自测） | 无 | ~130（eval_t8c_smoke.py+预注册 §3） | ~90（新脚本） | 1 | sub-27b（纯执行+脚本产出<100行；边界：不对真实数据跑、不动 eval_t8c_smoke.py） | ✅ done+验收 2026-11-27（commit 41104aa19；Lead 验收：184 行 / from eval_t8c_smoke import evaluate 口径同源 / Fisher 双侧 / 判决映射与预注册 §4 Stage 1 逐条一致 / 自测 3 场景 3-3 PASS（全过→H1、W2 不过→方向性证据、W3 不过→结构未赢）/ 未对真实数据跑） |
| T8c-EvalTruncFix：eval_t8c_smoke.py 截断样本 s=1→s=0（与头部口径「不进三型分布比较」对齐；n=3 截断=0 未暴露，n=9 前必修） | 无 | ~130（eval_t8c_smoke.py） | ~10（截断分支+注释） | 1 | sub-27b（单文件改+重跑两批既有 eval 验证逐字段不变；边界：不动 decide()/分流条款） | ✅ done+验收 2026-11-27（commit 15c3c4309；Lead 验收：截断分支 score=0+note 更新 / diff 9 行 / 重跑对比——brerun n=3 截断=0 逐字段全等（decision 不变）、smoke pre-brerun 截断=1 仅截断行 s 1→0 其余不变 decision 不变 / decide() 未动） |
| T8c-StickyThrottle：stop_hook 便签时间窗抑制（keepalive 每 tick 烧 cron 配额，01:12-01:24 每 15-30s 一条实证） | 无 | ~100（stop_hook 冷却分支） | ~10 | 1 | Lead 直接执行（诊断+patch 落在简短可查范围；stage-gate 独立仓） | ✅ 完成 2026-11-27（stage-gate commit 63e73ef；dense<10min 窗内 sticky 便签降级为无文字 continue，audit 留痕 continue-meta-sticky-suppressed）。**归因更正（Lead 01:35，audit log 为准）**：执行者回执 a6d360240 将便签连发归因给「T1 误判薄思考」，但 progress.log 中 01:12-01:13 那批便签 tag 全为 `continue-meta-sticky`（冷却分支），非 `continue-think-trigger`（T1 分支），时间戳逐条对上 → 真因=冷却分支便签无时间节流，T1 未参与。修复打在冷却分支，方向正确；勿按回执归因去改 T1 |
| T8c-CapFix：04.5 复核阶段单独上限 12288→16384（MAX_B_REVIEW） | 无（独立于 n=9） | ~30 | ~10 | 1 | Lead 直接执行（2026-11-27 00:07，诊断+2 处 patch+meta 登记落在简短可查范围） | ✅ 完成 2026-11-27（commit 5c718d398，备份 .bak-045cap-20261127-000641）。**归因修正**：截断真因=run3-04.5 reasoning 14866 tok 撞 12288（微信会话 F2 补 Lead 复核已归因长度方差 2.6×，非复读）；服务端 probe 证 max_tokens=32768 可接受（非服务端限制）。**与 HarnessRetry 设计的偏离声明**：原设计"cap 不变保 token-matched"，本修复改 04.5 cap——**名义上限不再严格 matched：B 臂 5×12288+16384=77824 vs A 臂 73728（差 4096，+5.5%）**。偏离依据=B 臂实测总消耗 29-41K ≪ 两臂名义上限，matched 的**实际**语义（同预算各自自然消耗、无预算饥饿）未被破坏；但名义差异是真实存在的，n=9 正式跑前需在 meta 里登记该口径变化（或改回 12288+长度约束指令）。其余 5 阶段仍 12288 |
| T8c-CapFix-Verify：重跑 B 臂 1 样本（04.5 阶段）验证 finish=stop | CapFix commit | - | sidecar json | 0 | executor-cron（纯执行：`python3 run_exp_t8c.py b` 只跑 1 run 或等价单阶段调用；验收=04.5 finish_reason=stop 且 total 无 length 截断；边界：不跑 A 臂、不改 harness、结果写新文件不覆盖 raw_outputs_t8c.json） | ✅ done 2026-11-27 00:29（执行者回执 T8c-CapFix-Verify.json，Lead 验收：6 阶段全 stop/04.5 tok=5073/length_retries=0 字段在位/monitor DEAD→核磁盘接力路由正常工作）。**Scope 声明（Lead 判断）**：重跑的是 run1 非原截断样本 run3（11338 tok），且 5073<旧上限 12288、重试未触发 → 本 verify 证明=harness 修复后端到端无回归，**不构成 cap 修复的因果证明**；截断是否真解由 T8c-B-Rerun 全 3 样本定 |
| T8c-B-Rerun：全 B 臂 3 样本重跑（干净 smoke 数据，定 STOP/EXPAND）：先备份 raw_outputs_t8c.json → *.pre-brerun.json，再 `python3 run_exp_t8c.py b`（保留 A 臂、B 臂 3 新样本增量写盘）；跑完对 B 臂 3 样本跑 judge eval——**命令钉死（Lead 2026-11-27 00:55，口径事故预防）**：`python3 eval_t8c_smoke.py raw_outputs_t8c.json t8c-brerun-eval.json`（B 臂输入=6 阶段 content 拼接，与 smoke 同款；**禁止**直接对 flat 文件跑 judge_pipeline_v0——flat 只有 04.5 单段，B 臂会系统性误判 indeterminate，2026-11-27 00:50 已实证该口径差异；第 2 参必须显式传，防覆盖 smoke 四件套的 t8c-smoke-eval.json）。判决矩阵已冻结在 t8c-smoke-verdict-ambiguity-20261127.md（与 eval 脚本 decide() 机械输出逐格对齐，数据到后 Lead 按格查表）；验收：① 04.5 三样本 finish_reason 逐个记录（截断数）② eval 输出的 B 臂 3 行标签+d 值+s_B' ③ 回执附 t8c-brerun-eval.json 路径；边界：不跑 A 臂（两批均 s=0 已满足 s_A'≤1/3）、不改 harness、先备份再写；判决由 Lead 下（执行者只报数）。**Sidecar 风险注记（Lead 2026-11-27 00:45）**：run_exp_t8c.py 的 save_stage_sidecar 硬编码写 t8c_stages/（无后缀），B-Rerun 会覆盖 smoke 的 18 个 sidecar——已核 18 文件全部 commit（git 即备份，可恢复），但执行者须在回执里记录覆盖发生；另 raw_outputs_t8c.json 也已 commit，任务卡的 .pre-brerun 备份仍要做（双保险） | CapFix-Verify done | ~20（脚本入口） | sidecar 18 + outputs + 回执数字 | 0 | executor-cron（纯执行：后台进程+pid 文件+monitor 跟踪，预计 ~15min；同 CapFix-Verify 流程） | ✅ done 2026-11-27 01:03（执行者回执 a362dae33：3 样本全 stop 截断 0/3；eval B' s=0.667 [indeterminate,indeterminate,A3] d=3.667）。**Lead 判决 01:20 = 扩样 n=9**（t8c-brerun-verdict-20261127.md：命中预注册「分离迹象」条款 s_B'≥2/3 且 s_A'≤1/3；更正执行者「边界情形→停止」分流——边界条款要求 s_A'=1/3 且 B' 全 A3，两条均不满足；Stage 0 机械检查过：repeat5=21 经三层审计=局部误报非退化） |
| T8c-HarnessRetry：run_exp_t8c.py 的 call() 加 finish_reason==length 截断重试（同 prompt 同 max_tokens 重采样 ≤2 次，3 次全 length → 该阶段判 indeterminate；cap 不变保 token-matched） | 无（独立于 n=9，先修后验证） | ~30（call() 现有结构） | ~30 | 1 | sub-27b（单文件 run_exp_t8c.py 改 call() + mock 单测；边界：只动 call() 的重试分支，不动 MAX_A/per-stage cap/STAGES 指令，不动 A 臂逻辑） | ✅ done 2026-11-27（commit 5eb66906f，Lead 验收：py_compile OK / 单测 3 场景全 PASS（length×2→stop、length×3→停+length_retries=2、stop→1 次）/ diff 仅 call()+test_call_retry.py 两文件） |
| T8c-JudgeFix：judge `_winner_patterns` 表格行变体补「卡型带后缀」（`V100 SXM2 \| 4 \|` 形态，cfg4_re 第 5 变体 `(?:RTX\s*)?V100[\s*]*\|` 后加 `[\w]*` 容后缀）+ probe TBL 两例转绿 + selftest 无回归 | 无 | ~40 | ~15 | 1 | sub-27b（单文件 correctness_layer_v0.py 改 + probe 复跑验证；边界：只动 `_winner_patterns` cfg4_re 表格变体，不动 3090 世界 CFG4 别名） | ✅ 完成 2026-11-26（commit 0ebcfff18，Lead 直接执行——诊断+1 行正则+双验证落在简短可查范围，比派 27b 稳。probe 6/6 转绿、selftest 7/7 无回归） |
| Q9E-Scan：Q9 (q9-agi) E 预算扫描队列——`bash experiments/stage-ablation/q9_budget_scan_queue.sh`（5 档 50/100/150/300/719 × 3 reps = 15 runs，~11h）。**脚本已写好**（Lead 2026-11-27，bash -n 过；克隆 q6 队列最小化：只跑 SM+存 run json+记日志，评分全后置）。**--max-depth 10（红队 2026-11-27 补，防 x 轴标错+gate 结构性不可达）**：harness 默认 max_depth=4，Q9 gold 的 11 gate 叶有 3 个在 depth=5 → 默认墙下主端点 gate 命中率上限 8/11，P1 必系统性失败；且 q6 原批 719 档全被 max_depth=4 拦停（实际 197/351/379 节点，x 轴标错）前车之鉴。workshop data note (c) 本就要求跨域对比持深度墙恒定（Q6/Q7 均 max_depth=10），本批对齐。**纯题面 questions/Q9-agi-pure.txt 已抽+泄漏检查 0**（gold 五轴关键词 0 命中；runner 整文件读题面，喂原文件会泄露 gold 骨架进 prompt）。**D 三项默认立场已按全自动原则冻结**（预算 150 档在列 / 5 因子不增不减 / 排序键 post_acc，源自 q9-agi-question-d1-lead-derivation-20261126.md 四项默认立场；E-SYNTH 推荐操作点依赖已解除——salvage 无产出，150 维持）。验收：① 15/15 run json 落 data/q9-budget-scan/（q9-{budget}-r{rep}-{ts}.json）② /tmp/q9-budget-scan-queue.log 每行含 budget/rep/rc/wall_s/n_nodes/out ③ 回执附 log 路径+落盘计数；边界：不改 s5_state_machine.py/judge_v1.py/gold-q9-units.json，不碰 q6/gpu/nat/soc 数据目录，不做评分（评分=Q9E-Analyze）；pid 文件+monitor 跟踪，预计 ~11h | 无 | ~30（脚本入口） | 15 run json + log + 回执 | 0 | executor-cron（纯执行：后台进程+pid 文件+monitor 跟踪；同 T8c-B-Rerun 流程） | 执行中（2026-11-27 11:45:54 起跑 pid 22941，实测 ~9.5min/run 比估 11h 快，15 runs 约 2.4h）→ **10/15 落盘后队列死**（2026-11-27 20:0x 核：300-r1 14:47 后无 log 行/无 DONE 行/进程消失，macOS 休眠或进程组回收；50/100/150 各 3 reps 全齐 + 300-r1=298 节点，150 峰值结论不受影响）；补跑队列 `experiments/stage-ablation/q9_budget_scan_resume.sh` 已备（300-r2/3+719×3，与原队列同构，commit af2d4be76），gated sub 释放 8787 后 setsid nohup 起 |
| Q9G-Gate：相关性门禁最小实验 — 单变量=逐层展开 prompt (P1H_INDEX) + gap 补全 prompt (P15B_GAP_FILL) 尾部追加节点相关性约束 (monkeypatch 注入 run_q9_gated.py, 不改本体; 初版注入点 P1_DECOMPOSE 是死路径, 21:3x 核主循环后修正, commit 860f78be7), 预算 150×2 reps, 对照=已有 baseline 150-r1/r2/r3 (LLM 判据漂移率 34%; 关键词粗判口径 baseline=5.3/12.7/9.3% 均值 9.1%, 同口径对照)。假设: 门禁 → 漂移率 (other) 显著降 + 机制率 (mech) 不降。任务卡 modules/G-think-mechanism/think-trigger/taskcard-relevance-gate-150.md (S1 wrapper+S2 2 reps+S3 验证/commit+S4 汇报; leak_check 已核: 门禁段与题面 8 字中文串零重叠, 安全) | mech-scan 解读 (2026-11-27 20:5x) | ~40 (任务卡+runner 入口) | wrapper ~40 行 + 2 run json + log | 1 | sub-27b (纯执行: 写 wrapper+跑 2 reps+commit; 边界: 不改 s5_pipeline/prompts/s5_state_machine 本体, 不碰 baseline 数据, mech 重扫后置 Lead 做) | 派发中 (2026-11-27 21:2x, sa-0-a8a9c2ae, ~20min) |
**50 档早期验证（2026-11-27 12:35）**：3/3 run rc=0，n_nodes 精确=50（x 轴有效，无 max_depth 拦停）；树深 2 层，Q9 gold 11 gate 叶深度分布 2/3/4/5（1/4/3/3）→ depth=2 的 1 个 gate 在 50 档已结构性可达，--max-depth 10 修复生效。
**深层信息增益诊断（2026-11-27 D 指出"公式=同义反复"）**：Q6 nodepth 数据剖面显示 L4/L5 节点 98% 是符号化建模（代数展开），硬件/系统细节占比不随深度增加。核心问题：深层节点没有引入不可约的新经验约束，是父节点变量的代数重排（条件熵≈0）。harness 的"深度"是结构性的（树高度），不是信息论的（累计新信息量）。Q9E-Analyze 应加诊断：① 按"经验锚定率"（含具体数值+来源 URL 的节点占比）分层看 cov，区分"代数游戏节点"vs"经验锚定节点"对 cov 的贡献；② 如果 Q9 gold 也是经验锚定型，预期 Q9 cov 也会卡在低位，原因不是预算不够，是模型深层行为模式（代数展开 vs 经验锚定）。这是比"方向正交"更根本的瓶颈：不是模型在错误的量纲空间，是模型在深层根本不引入新信息。
**瓶颈定位终判（2026-11-27 D 问"问题到底是不是检索"）**：不是检索通道。三层：① 通道好（300+ 次检索，aliyun 官方文档 63 次，query 在点上）② 检索回的概念文章不含 gold 要的精确价目表值（模型写模糊区间 ¥0.1-0.5/GB 顶替精确阶梯价 0.24/0.23/0.21…）③ **harness 质询步骤已反复标记"缺乏来源支持/无法提供外部支持"（三 run 共 426/2157 节点含质询标记，累计 rework=494 次），模型生成自我怀疑标记后保留原 claim 继续代数展开，不触发重检索**。→ ⑥ 思考触发分支的直接实证：防御性语言信号已在数据中存在（[质询] 记录），干预点 = 被质询 claim 强制定向重检索（查价目表非概念文章）且计入预算。这是"模型知道自己不知道"的落点：它知道（质询记录），不行动。
| Q9E-Analyze：Q9 扫描后置分析——per-gate-unit 命中率矩阵（11 gate 叶 × 5 档，从 run json + modules/B-pipeline-ablation/data/gold-q9-units.json 直接算，judge_v1.gold_units 注入跨域口径）+ 主端点阈值（gate 命中率首次达 100% 的最小预算）+ 次端点曲线（gate 全过子集内 cost/time 叶）+ P1 判决数据（gate 是否 ~100-150 节点饱和）。**机械部分=脚本落盘**（矩阵 JSON+阈值），**P1 判决=判断-Lead**（对照 q9-e-experiment-design-20261124.md 冻结端点）。**阈值跨域预案（红队 2026-11-27）**：COS_THRESHOLD=0.70 是 gpu 域标定，Q9 域未重校——分析时先看 c_detail.sim_median 诊断：若 gate 命中率全档≈0（阈值过高）或全档≈1（过低），按 Q9 域 sim 分布重标定阈值重算（run json 不动，只重算 embedding 相似度，不重跑 SM）。验收：矩阵 JSON 落 data/q9-budget-scan/ + 一行 P1 判决（成立/不成立+依据数）；边界：只读 run json+gold，不重跑 SM | Q9E-Scan done | ~150（run json 结构+gold-q9-units+judge_v1 注入签名） | ~80（分析脚本）+矩阵 JSON | 1 | 脚本-Lead（机械提取）+ 判断-Lead（P1 判决） | 阻塞（等 Q9E-Scan；脚本已就绪 f47e84d9e+540b8cdcd，scan 完成后 Lead 跑 analyze_q9e_scan.py 出矩阵+P1 判决；中期数据 8/15：sim_median 三档全平 0.592/0.593/0.591，n_confirmed 尾升 0/3→2/3→1/3 run 各中 1 单元，券收集器模式坐实，P1 判决须报档内 CI） |
| Q9REG：题面/gold/机制版本三维登记册（D 2026-11-27 15:00 三连问"不同问题/不同版本/不同机制是否清晰存放"触发审计）——审计结论（一手 find/diff 实测）：① 问题维度=靠文件名 Q 号约定对齐，Q1-Q5 同目录配对清楚，Q6-Q10 散 3 目录（bench/questions + bench/rubric-v3/ablation + modules/B-pipeline-ablation/data），**Q9 编号冲突**（bench 下 Q9-vlm-arch 旧题 vs stage-ablation Q9-agi 新题）；② 版本维度=gold 有版本号（Q9 v0/v1/v2 文件名），题面版本散落（v1 题面藏在 tasks/q9-agi-question-v0.md 段落里），题面↔gold 绑定无表；③ 机制维度=无登记册（scoring v1-v4 五文件平铺、runs-s5-gpu-v3..v14 + runs-prod 变体 20+ 目录、judge canonical 声明埋在 version-matrix-20261126.md 快照里已过期）；④ **gold-gpu-units.json 两份分叉**（modules 根 vs data/，diff 不一致，canonical 未标）。修法=**脚本生成登记册，不搬文件**（脚本硬编码路径，搬了全断）：scan_gold_registry.py 扫 gold*/questions*/units.json/runs-*/scoring* → registry.json（qid×{题面路径+版本, gold 路径+版本, units, canonical 标记, 冲突标记}）+ 冲突清单（Q9 撞号/gpu-units 分叉/副本 demo+repro 标记）。验收：registry.json 落 modules/B-pipeline-ablation/data/ + 冲突清单 ≤10 行 + canonical 判定（gpu-units 以 data/ 为准需核 build 脚本引用后定）；边界：只读+生成，不移动/不删除任何现有文件 | 无（scan 完成前可做，纯只读扫描） | ~200（全盘 glob+diff 已预做） | ~60（脚本）+registry.json | 1 | 脚本-Lead | **DONE**（2026-11-27 15:40：scan_gold_registry.py 落盘+registry.json（11 qid×题面/gold/units+版本+canonical+绑定证据）+conflicts.md（3 条：gpu-units 分叉 canonical=modules 根 36u judge_v1 L34 引用/data 副本 37u 孤儿 / Q9 撞车 bench 旧 VLM vs stage-ablation 新 agi / Q1 gold 完全副本）；INDEX.md 层 4 指针已加；canonical 判定=judge_v1.py 默认引用方） |
| Q9G-V1：v1 题面 gold 交付缺失追查（D 2026-11-27 14:40 问"gold 到底在哪"时核出）——题面 v1（11-26 20:10 D 冻结，自我认识/5 因子/post_acc 排序键）的 gold 骨架任务卡 11-26 20:30 已派发 arena（APPROVALS#2 批准），但全分支无交付（无 commit/gold 目录无新文件/台账无记录）。当前 scan 跑的是 v0 题面（Q9-agi-pure.txt）+ v0 gold（Q9-v2.md），配对自洽但非 D 最后批准的题面。步骤：① ego-browser 查 arena 会话状态（11-26 20:30 那单，2 卡=主调研+交叉验证）② 有产出→拉回+Lead 对比矛盾点+回执；无产出→重派（任务卡已在 tasks/q9-gold-skeleton-arena-taskcard.md）③ 交付后 D 确认冻结→build 脚本解析→v1 gold 就位。**v0 scan 不停**：容量曲线结论（券收集器）关于测量机制不依赖题面，且是 BA 臂对照臂。验收：arena 会话状态一行（交付中/丢失/超时）+ 处置动作（拉回/重派）落 decomposition；边界：不中断 scan，不动 v0 数据 | scan 跑完窗口（ego-browser 查 arena 需独占） | ~50（任务卡+台账） | ~20（状态记录） | 1 | 执行-Lead（ego-browser arena 查询）+ 判断-Lead（矛盾点对比） | 就绪（D 14:40 触发；scan 8/15 ~14:50 完成，之后执行） |
| Q9E-BA：Q9 预算感知臂（Budget-Aware，D 2026-11-27 13:55 提出）——当前 Q9E-Scan 测的是**容量**（harness 外部截断，LLM 不知道预算），本臂测**优化**（预算+目标层次写进 prompt，LLM 知道"你最多展开 N 个节点，优先覆盖硬判据类因素"）。三型 hack 行为预注册：H1=凑数（浅层废话节点膨胀，节点深度分布 L1/L2 占比升）→ 目标函数设计漏洞；H2=层次理解（gate 类叶优先展开、cost 类压缩）→ 理解 lexicographic；H3=无视预算硬展开（n_nodes 贴满 cap 且与无感知臂同分布）→ 预算传递失败，结论=预算控制必须走 harness 截断。**对照臂=Q9E-Scan 原样 run（无预算感知 baseline），不重跑**。设计：① prompt 注入预算+目标层次（不泄露 gold 骨架，只说"优先覆盖硬判据类因素"——泄漏检查同 Q9E-Scan 纯题面标准）② 同 5 档 × 3 reps=15 runs ③ 对比维度：覆盖差异（有/无感知 n_confirmed）+ 节点深度分布（H1 检测）+ gate 叶优先序（H2 检测）+ n_nodes 实际取值（H3 检测）。**文献定位（2026-11-27 arXiv 速查，详见 research/budget-aware-llm-survey-20261127.md）**：最近邻=Reasoning on a Budget (2507.02534 survey) + Reasoning in Token Economies (2406.06487) + Inference-Time Reward Hacking (2506.19163)——前两者测"预算约束下推理质量衰减"（y 轴=答案正确率），本臂测"预算约束下分解行为变形"（y 轴=覆盖结构+hack 类型），gap=无人把预算感知与目标函数 hack 结合；本地 landscape 文档（autoresearch-landscape-nontraining-20261124.md L29）已核：6 家 research-agent 无预算轴，本臂在 research-agent 语境下仍独有。验收：① prompt 变体落盘+泄漏检查 0 ② 15 run json 落 data/q9-budget-aware/ ③ 三型 hack 判决（H1/H2/H3 各一行+依据数）④ 与 Q9E-Scan 对照的覆盖差异表；边界：不改 s5_state_machine.py（prompt 注入走 runner 参数或新 wrapper），不碰 q9-budget-scan/ 数据 | Q9E-Scan done（对照臂齐）+ prompt 变体设计 | ~200（runner prompt 构造+Q9E-Scan run json 结构） | ~60（prompt 变体+wrapper）+15 run json+判决表 | 2 | 设计-Lead（prompt 变体+泄漏检查）+ executor-cron（跑批）+ 判断-Lead（hack 判决） | 就绪（D 13:55 提出；等 Q9E-Scan 完成出对照臂后启动；设计要点已冻结：三型 hack 预注册+对照臂不重跑+泄漏检查同 Q9E-Scan 标准） |
**仓库布局审计（2026-11-27 13:50，D 连问 5 连击：数据为何在 experiments 下/整齐存放含义/exp 下非 run 杂物/根目录未归类文件夹/脚本工具乱放）**：
盘点结果（一手，find/du 实测）：
- `experiments/stage-ablation/` 顶层 385 项 = 76 py + 40 sh + 70 md + 74 log + 55 json + 数据目录群（checkpoints 325M/71k 文件、runs-* 系列 ~30M）。**这是 11 月初 B 模块诞生前的遗留**：当时一切都在 experiments/ 下，B 模块建立后新数据进了 modules/B/data/，但旧数据和脚本没迁——所以出现"数据在 experiments 下"。
- 根目录 20+ 顶层目录，多数是 loop 机制产物（loop-artifacts/loop-events/receipts=1-loop 流程）+ 杂项（outputs/ 混着 mp4 视频和 outreach、research/ 混着回执和调研文档）。
- "整齐存放"= 红线 0 四条：① 每层 INDEX.md 纯索引递归可达 ② 直接子模块 3-7 个 ③ 标准结构 INDEX+memory/+tasks/ ④ 项目按领域分层。pfb 根目录超标（>7 个顶层目录）+ 无统一 INDEX。
- **迁移映射表已生成**：`tasks/layout-reorg-mapping.json`（385 项逐一定去向）。**归属修正（D 指正后重判，commit 38fcc035f）**：原映射全归 B 是错的——按文件名+头部内容判：D-decomp-state-machine=147（s5_*/ablation_*/queue 状态机核心）、A-eval-infra=66（judge/rubric/scoring）、E-sota-benchmark=35（drb/s10/sota）、B?=81、F=1；数据目录 checkpoints/runs-* 是 D 状态机 run 产物（非 B），s10-runs/hetero 归 E。启发式判定，迁移时 sub 逐批肉眼复核。
- **执行时序约束**：Q9E-Scan（pid 22941）正从 experiments/stage-ablation/ 起 `python3 s5_state_machine.py`（每 run 新起进程，相对路径）→ **扫描跑完前不许动该目录下的 .py/.sh**；数据目录/log/md 理论上可先动但为最小风险整批等扫描完成（~14:30 前后）。
- 根目录收敛方案（待 D 点头或按默认自主）：research/ 并入 memory/ 或 modules 对应处；outputs/ 按内容拆（媒体→archive/media/，outreach→projects 对应项目）；loop-artifacts/receipts 属 1-loop 机制保留但加 INDEX。
| LAYOUT-Reorg：按 tasks/layout-reorg-mapping.json 执行迁移（脚本读映射→git mv 批量→INDEX.md 更新→commit 分 3 批：数据批/脚本批/文档批；边界：① 排除 q9_budget_scan_queue.sh+s5_state_machine.py+ablation_harness.py+research_hook.py（运行中进程依赖，等 Q9E-Scan 完成）② 不动 modules/B/data/q9-budget-scan/（在写）③ .research-cache 两个目录整体移 archive/runtime-cache/ ④ 每批 commit 后 git status 核 ⑤ 跑 scripts/project-tidy 体检） | Q9E-Scan 完成 | ~450（mapping json，脚本读不占上下文） | 脚本 ~60 行 + INDEX 若干 | 3-4 | sub-27b（纯执行+脚本落盘；任务卡=本段+mapping 路径+排除清单） | ✅ DONE 2026-11-27 18:06（sub sa-0-9376bdb6 死于重复循环但活全干完，信磁盘：3 批迁移 388 项 caab4cbf9/7283ae153/d4b7de5e9 + 收尾 6c7865e51/897d55702/5b9c2f773，核验 382/382 源清空，tidy PASS exit=0 0FAIL 24WARN 既有；5 验收项全过） |
| LAYOUT-RefFix：断引用批修（迁移后 56 文件引用旧路径 + 2 手动脚本无 cron 注册，tasks/layout-reorg-migrate-result.json 有清单） | LAYOUT-Reorg done | ~56 文件（脚本读 mapping 做路径替换，不占上下文） | 脚本 ~40 行 + 56 文件 in-place | 1-2 | sub-27b（纯执行+脚本落盘；任务卡=本段+migrate-result.json 路径+替换规则=旧路径→新路径按 mapping 反查） | 就绪（机械批修，低风险可回滚 git；排在 strategic 讨论后的执行窗口） |
| LAYOUT-Root：根目录收敛（research/ 归属重定、outputs/ 拆分、顶层 INDEX.md 建立、loop-artifacts 加 INDEX） | LAYOUT-Reorg done | ~100 | ~50 | 2 | sub-27b | 就绪（串行在 Reorg 后） |
| OBJHACK：目标函数形式 × hack 复现（text vs formula，预算 100 固定，2×2 runs）+ 因果探针（意图锚点） | 无（judge 释放 8787 后起跑） | ~50（spec+metrics 脚本） | 4+1 run json + hack-metrics.json + report.md | 4 | 脚本-Lead（run.sh 串行+指标脚本）+ 判断-Lead（判决） | ✅ DONE 2026-11-27 17:51（H1 判决：公式臂更易 hack，jac 分布形状分离 gt05 0/0 vs 1/14，commit 1f9cf7ace；锚点探针证实预言#18：gt05=1/p95=0.23/info=0.61 → 意图残缺中介成立，设计规则三档排序=锚点>文字>裸公式，commit b5dc55980；四件套齐全 data/objfmt-hack/{spec,arms,judge 端点=机械指标,report}） |
| TOOL-POC：思考→行动接线最小验证（⑥ 前置探针，q9_tool_poc.py：10 真实质询节点 × A 无 tools/B 带 search，测自发 tool_call 率） | OBJHACK done（8787 独占） | ~100（脚本已备） | tool-poc-<date>.json + 一行判决 | 1 | 后台进程（纯执行）+ 判断-Lead（判决） | ✅ DONE 2026-11-27 17:56（PID 49098 rc=0，json=data/q9-budget-scan/tool-poc-20261127.json；**判决：接线可行**——A 臂 0/10 基线 sanity 通过，B 臂 7/10 自发 tool_call，query 全在点上（NVFP4 格式/Claude 定价/CoT 自批判/scipy factorial 存在性）；3/10 未调用（N20/N21 硬件规格、N29 定价）= 模型用散文模拟核验顶替了真检索，正是 ⑥ 要修的残留缺口；已知局限=called 与否≠in-situ 行为、temp=0 单轮核验 prompt、n=10） |
| OBJ-SELFSCRUTINY：目标函数自审循环（反局部最优机制，D 2026-11-27 战略讨论提出）。统一原则=目标函数必须和解法一样被审视（局部最优=优化静态局部指标的必然产物）。五实例：①完备性探针（分解树空/浅子树=漏意图维度，OBJHACK 锚点已证）②压缩测试（当前理解压不成紧凑公式=陷局部最优，D taste 操作化）③对抗复核（独立 critic 攻击目标+当前模型，破自指回音室）④接地（真数据/真来源/真测量破自我参照环，TOOL-POC 7/10 自发检索=接地在作用）⑤全局回顾台账（每实验后：否定了什么/留下什么空间/更新空间地图=目前缺的那块）。验收靶点=GPU 性能/瓶颈建模（Roofline 为已知紧凑好答案：算术强度/FLOPs vs 带宽 2 变量抓 compute-bound vs memory-bound，外部可验证=测真实 GPU 对公式，复杂度覆盖量化/投机解码/KVcache/批大小） | 主线到可发表里程碑（⑤全局回顾台账零成本可先行） | ~200（机制 spec+GPU 靶点定义+台账） | spec + 全局回顾台账 + GPU 模型 | 3-4 | 判断-Lead（机制设计+台账综合）+ 脚本-Lead（压缩/接地探针）+ 对抗-arena（独立 critic） | 就绪（登记未跑；top-1 下一步=⑤全局回顾台账，零成本不烧 GPU，把 Q9/OBJHACK/TOOL-POC 做累积综合=否定清单+空间地图） |
**Q9E-Scan 全档 stop reason（2026-11-27 13:55 一手，DONE 行）**：7/7 runs 全部 `state=rework` 停机（非收敛停），leaks=0。reworks/节点：b50=22-32/50（44-64%）、b100=48-49/100（49%）、b150-r1=89/150（59%）。含义：模型在全部预算档都以"还有节点待 rework"耗尽预算，不是自然收敛——预算曲线测的是"预算饥饿下的覆盖"，与 ④ 的 max_depth 墙同理，P1 判决需带此 caveat。
**Q9E-Analyze 提前诊断（2026-11-27 13:35，50/100 档 6 runs 已完）**：① **analyze_q9e_scan.py 命名 bug（已修）**：gate_ids 是 J-id（J1..J14），confirmed 集合存 N-* unit_id，`g in confirmed` 恒 False → 原 analysis.json 的 gate 矩阵结构性全 0（13:27 那份全 0 是 bug 不是数据）。修=j_id→unit_id 映射。② **阈值不可标定（负对照实证）**：Q6→Q9 gold 负对照 sim p50=0.587/p99=0.686，Q9→Q9 gold 正样本 p50=0.588——正负分布重叠，bge-m3 cosine 在 Q9 域无区分力（gold unit 文本含公式/权重/conf 标注，相似度天花板 ~0.65）。阈值扫 0.50-0.70 全区间，gate 命中率从 1.0 单调跌到 0，无平台。③ **P1 判决不得基于当前仪器**：需换仪器（候选：gold unit 只取核心概念文本算 sim / LLM judge 逐 unit 判定），换后 50/100 档数据可复用（run json 不动）。落盘：data/q9-budget-scan/threshold-recalibration-20261127.json（含负对照）+ research/q9_threshold_recalibrate.py |

**B' 截断修复设计（Lead 判断 2026-11-26）**：根因=总预算 24576 < B' 六阶段真实需求 69227（碎片化 cap 4096 是表象，截断态已耗 94% 总预算）。修复=MAX_A 24576→73728（=6×12288，覆盖 69K 下限），A' 同步 73728 保 matched 上限语义（A' 实际 ~13K，上限不改变其行为）。对照语义澄清为「同预算上限、各自自然消耗」——预算不足以完成流程时测的是「预算饥饿」非「流程价值」，故预算须覆盖流程真实需求下限。进 post-hoc 文件（smoke 已跑过数据，冻结文件只读）。

### Q9E-Scan 决策变更 (2026-11-27 15:50, D 指令"负结果已确立为何还跑")
- **停扫**: 300/719 档队列已 kill (PID 22941 + 子进程)。依据: 负结果 13:35 已确立 (7/7 rework 停机 + 深层零信息增益 + cosine 仪器失效), 继续扩 x 轴 = 惯性, 非信息增益。
- **换仪器**: LLM judge (qwen3.8-27b via 8787, temp=0) 替代 bge-m3 cosine 判 gate 覆盖。脚本 `modules/B-pipeline-ablation/research/q9_llm_judge_coverage.py`, 输入 = 已完成 10 个 run json (50/100/150/300-r1), 不重跑 SM。
- **已知风险**: judge 与被判对象同源 (qwen3.8-27b 自评) — 若结果异常需换独立 judge 复核。
- **✅ 曲线完整 + 轴收口 (2026-11-27 16:25, judge 全量完成)**: `data/q9-budget-scan/llm-judge-coverage-20261127.json`
  - 曲线 (11 gold gate): 50→0.576(5/7/7) · 100→0.576(6/6/7) · 150→0.697(7/7/9) · 300→0.909(10/11, n=1)
  - **节点级一刀 (最硬证据, 单 run 内部)**: 300-r1 前 150 节点已覆盖 9/11, 后 148 节点仅 +1/11 → 300 的高分在前 150 就拿到, 与 150-r3 (9/11) 持平。
  - **收口框架 (替代"没影响"与"越多越好")**: ① 50→100 零增益; ② 100→150 真实增益 (拐点 ~150); ③ 150 以上无超方差增益 (300 n=1, 亮点疑似 run 方差); ④ 硬上界 298 节点 (300 与 719 全停 298, 结构性封顶); ⑤ 13/13 全 rework 停机, 无一次"干净覆盖完"。
  - **对 Pareto 理想的判决**: "预算单调换覆盖"不成立; 真实形状 = 150 拐点 + 298 硬顶 + rework 主导。预算旋钮只控节点数不控正交质量, 多余节点喂 rework 循环 → 指向 ⑥ 思考触发分支 (根因: 质疑→重做打转, 思考不接行动)。
  - **caveat**: 300 档 n=1 (r2/r3 在 judge 启动后才跑完, 未入判); 节点级证据不受此污染。
  - **300/719 重启条件 (原设定)**: 新仪器曲线显著非单调 — 现已满足"150 后平坦" → 不重启, 轴正式关闭。
- **执行偏差注记 (2026-11-27 15:42)**: 15:40 窗口 Lead 未核到本决策即起 resume 队列 (q9_budget_scan_resume.sh, 将重跑 300 r2/r3+719×3)——发现冲突后立即 kill, 无孤儿进程, b300-r2 未落盘 (无 json, 仅 3KB stdout 残片), 数据集不受影响 (仍 10 runs), resume 脚本已删。教训: 起长任务前必须重读 decomposition 最新决策段 (外部编辑可能已改变方向), 不能只信自己上下文里的旧状态。
- **post_acc 死亡判定 + 救活探针 (2026-11-27 18:40, Lead 地基复核; 19:xx D 指正"只是评分问题"后修正)**: ① 状态机 `s5_state_machine.py` 无 `contradicted` 状态 (只有 pending/verified/degraded/reworked) → post_acc=verified/(verified+contradicted) 分母恒 0 → 10 runs 全 post_acc=1.000 (常数, 零判别力, 已逐 run 复算)。② 矛盾扫描器 `_scan_contradictions` 每轮只扫最近 30 verified 节点、单次 LLM 调用、只报 ≤5 个 → 10 runs 抓到的 2 个矛盾事件是**下限不是真值** (D 指正: 仪器弱 ≠ 事件空)。③ **救活探针 (sub sa-0-48c24a27 在跑)**: 不修状态机不重跑 SM, 对 10 runs 全量 verified 节点做 (a) 数值一致性检查 (正则抽参数, 同参数差 >10% 记矛盾) + (b) LLM judge 全量判定 (互斥/无依据), 脚本 `research/q9_postacc_rescue_probe.py`, 落盘 `data/q9-budget-scan/postacc-rescue-probe-20261127.json`。④ **判决路径**: 救活后有区分度 → post_acc 复活为 v1 排序键, D1 之争 (A 惩罚项 vs B 纯) 恢复有效, 待 D 裁; 救活后仍平坦 → post_acc 降级诊断, v1 主端点改 gate 覆盖率 (广度) + post_acc (质量) 互补不互斥。⑤ gate 覆盖曲线 (150 拐点+298 硬顶) 不依赖 post_acc, 已收口不受影响。
- **✅ 救活探针判决 (2026-11-27 19:3x, sub sa-0-48c24a27 完成, commit 3eb3105ee+63635ce81, Lead 已验收)**: post_acc_rescued = 50:0.896 / 100:0.949 / 150:0.958 / **300:0.835 (n=1)** → **有区分度, post_acc 复活** (baseline 恒 1.0 作废)。三点: ① **300 负边际 (方向性)**: 预算最大档 post_acc 最差 (矛盾率 0.215 vs 50 档 ~0.07), 与覆盖 150 平坦合并 → 预算轴结论从"无正边际"升级为"150 后负边际 (方向性, n=1 + batch 共线 caveat: 大 run 批内检测概率低, 0.215 是下界)"。② **A/B 排序在新数据下翻转**: A 公式 J=post_acc×(150/n_realized) 给 50 档 J=2.69 (>1 不合理) —— "预算 cap 强制停"被误读为"高效完成", 50 档是被饿停不是高效; B (纯 post_acc) 排序 150>100>50>300 合理。A 的真实关切 (小树刷比率) 用 Card A L28 已有的"n_realized<0.8×cap 早停臂不计"护栏即可, 不需乘性惩罚项。③ **Lead 建议 (待 D 裁)**: D1 采 B (纯 post_acc) + 早停臂排除护栏; A 的乘性项有语义 bug (饥饿≠高效), 且新数据下 B 已能把 300 排底 (惩罚项的另一个动机也已消失)。
- **分数定义 + 盲区登记 (2026-11-27 19:5x, D 三连质疑后补)**: post_acc_rescued = verified 集合的**重审通过率** (LLM judge 全量 + 数值一致性), 非对 gold 正确率。盲区: ① 同族 judge (qwen3.8-27b 判 qwen3.8-27b) 抓不到系统性规格错误 — **原判据撤回 (2026-11-27 D 纠正)**: 我曾用 "V100 跑 NVFP4 算 KV cache" 节点当"不可能成立"的例子, D 指出 V100 优化/适配后可跑 NVFP4 (只是原生不支持) → 该节点与 "V100 不支持 FP8" 节点不构成矛盾, judge 未必漏判。**查证收口 (2026-11-27 20:1x, Gemini 4 + GitHub 一手)**: ① 硬件层: V100 (SM 7.0, 第 1 代 TC) 无原生 FP4/FP8/BF16 tensor core, 仅 FP16 (m8n8k4) — 树里 "V100 不支持原生 FP8" 节点正确。② 软件层: W4A16 路径 (4bit 权重驻 HBM2 + 寄存器内反量化到 FP16 + FP16 TC 计算) 完全可行, SM70 专用 kernel 存在 (v100-skinny / 1Cat-vLLM TurboMind SM70 路径)。③ 实证: **1Cat-vLLM v1.5.3 (2026-11-14) 公开基准 = Qwen3.8-27B NVFP4 @ 4×V100-SXM2-32GB TP4, 892 tok/s** — 即本服务器同款硬件同款模型 (8787 推理栈), 树内 NVFP4 节点与实际部署一致, 非错误。→ 同族 judge 盲区仍为**假设** (此例不构成证据, 但树在硬件轴上与事实一致是正面信号: 深层节点至少硬件规格层是真的)。 ② 表面积混杂 (节点多→矛盾配对多→掉分部分机械)。用途边界: **预算轴比较够用** (同题同仪器可比), **正确性判断不够用** (归 q9g gold-based 评分)。置信分层: 有区分度=确定; 300 最差=方向稳 (batch 伪影反向, 保守); 150 峰值=不确定 (n=3 vs n=1 + 混杂)。
- **深层节点内容分析 (2026-11-27 19:5x, Lead 直查 10 runs/1198 节点)**: L3=586, L4=295。⚠️ **判据修正 (2026-11-27 20:0x, D 纠正)**: 原"微架构/效率关键词命中 L2/L3/L4 = 39/80/57"是关键词扫描, 命中的全是**规格级**内容 (带宽 900GB/s、KV cache 容量、支不支持某指令) — 有微架构的词, 没有微架构的深度。D 定义的"微架构" = **机制级**: 访存+计算的每一步, 参数变化→影响什么→影响多大 (例: L2 cache 8MB vs 96MB 影响什么/多大, 指令周期对算力的影响)。→ 关键词判据作废, 重定义三要素判据: ① 参数变化 (具体数值/配置对比) ② 影响机制 (因果说明) ③ 影响量 (量化结果)。三要素全有 = 机制级。重扫进行中 (sub 在跑, LLM 判 L3/L4 共 881 节点)。
- **机制级扫描 → 杠杆决策树 (2026-11-27 20:2x, Lead 预判, 数据到即执行)**: 数据 = mech_rate(level, budget) = 机制级节点/该档该深度总节点。Case 1: mech_rate 跨预算档平坦且绝对值低 (<15%) → 深度不买机制级正交性 (D "预算上界只当每步有价值新分解" 完全证实) → 杠杆 = **生成侧门禁**: 深层节点须含三要素中 ≥2 个才允许进入下一层分解 (把刷规格挡在源头, 不是验证侧)。Case 2: mech_rate 随深度上升 (L4>L2) → 深度买机制级, 300 负边际 = 漂移稀释 → 杠杆 = 相关性门禁 (节点 vs Q9 主题相关性检查)。Case 3: mech_rate 150 后下降 → 双因素 (机制稀释+矛盾累积) → 维持 150 上界 + Case1/2 对应门禁。通用 caveat: 同族 judge (27b 判 27b 机制深度) 绝对值不可信, 跨档相对值可用; 验收时 Lead 抽 10 条 mech 样例人工核 judge 松紧 (防系统性偏松把规格级误判成机制级 — 本次判据翻车的前科)。
- **Case 1 杠杆的成熟方案调研 (2026-11-27 20:4x, ego-browser Gemini 4 + 一手核验)**: 关键区分 (D 的直觉被文献证实): **"换皮重复"与"正交但浅层 (规格罗列)"是两种失效模式** — 向量去重门控挡不住第二种 (查参数量/许可证/日期彼此余弦很低但全无认知深度), 必须加信息增益/深度门控。承重锚点 (已一手核验): **UAA (arXiv 2610.22858, NTU 2026-10)** — 兄弟节点语义离散度预测下游冗余坍缩, 展开前零 LLM 成本定预算+剪枝, token -90%/延迟 -9x, training-free; 其第一发现 "同一中间状态的续展大多重复坍缩" = Problem A 的外部独立佐证。机制参考 (知名论文, 高置信): UoT (2402.03271 条件互信息)/ToC (2310.14696 自验证剪枝+全剪空即叶)/SciMON (2305.14259 生成期对比重写)/ShinkaEvolve (2509.19349 向量初筛+LLM novelty 复判两阶段拒采样)/QDAIF (2310.13032 正交网格准入)。⚠️ ARGORA "Contextual Orthogonality Pruning" 归因**作废** (仓库真实但是辩论编排框架, 无此机制, Gemini 安错项目 — 承重锚点必须一手核的又一实证)。→ Case 1 杠杆设计草案 (待数据确认后细化): 三段式 pre-expansion 门控 = ① 向量去重 (vs 祖先+兄弟, >0.80 拒) ② 深度/增益乘积分 (Alignment×Novelty×DepthGain, DepthGain 用 D 三要素 0-3 量表, 乘积一票否决防"正交但浅层") ③ 饱和早停 (父节点连续 N=2-3 候选被拒 → 封顶, RRD 式) + UAA 式兄弟离散度预算缩减。现状对照: 我们 `_scan_contradictions` 是事后+弱仪器, 杠杆全在事前。
- **mech-scan 结果解读 + 杠杆重定向 (2026-11-27 20:5x, 验收 PASS, 数据 `data/q9-budget-scan/mech-level-scan-20261127.json` 1198 节点闭合)**: **推翻 Case 1 预判**。mech_rate 按深度 L1 0%→L2 28.5%→L3 36.2%→**L4 52.5%** (单调陡升, 深度真买机制级, 不是"深度浅"); 按预算 50/100/150/300 = 0.307/0.350/0.362/0.426 (升, 但 300 n=1+298 触顶)。漂移 other 按预算 50/100/150/300 = 0.440/0.440/**0.340(最低)**/0.406, 按深度 L1 82.5%→L4 27.8% (单调降)。三条结论: ① **150 在两独立轴上是拐点** (post_acc 峰 0.958 + 漂移谷 0.340), 300 双轴劣化 (post_acc 0.835 + 漂移回升 0.406) — D "预算上界只当每步有价值新分解" 证实: 150 后边际节点同时加机制+漂移+矛盾, 净负。② **杠杆重定向: 主杠杆 = 相关性门禁 (Case 2)** 而非深度增益门禁 (Case 1) — 病根是漂移 (Q9 无关节点: Celery 队列/M1 Max TTFT/JSON schema 开销), 随预算放大, 生成侧拦 Q9 无关节点比拦浅层更对症; 深度增益门禁降为二级 (拦"相关但规格级"的填充)。③ **caveat 不变**: calibration 44% (<75%), 27b judge 系统性偏松 (16 条判 14 条 mech, 把 spec/other 都塞进 mech) → mech/spec/other 绝对占比虚高 (可能 ~2x), **只有单调趋势 + 跨预算相对值可信**; 若要绝对机制计数 (论文 claim) 需校准后/更严 judge 重扫。趋势为何仍可信: 偏差主方向 other→mech (校准 7/9), 代数上 mech_meas = mech_true + α·other_true — 浅层漂移多被转成 mech 多, 压低 mech 随深度的表观上升, 故 "L4>L2" 是保守下界非虚高伪影 (2026-11-27 D 质疑"judge 都是问题?是不是正则匹配"后补: 两套仪器 = post_acc 的正则数值层(机械,只抓同名参数冲突)+LLM 批内层(同族/批内 p≈20/nv/ground-truth 盲区) 与 mech 纯 LLM 层(偏松 other→mech); 绝对值均不可信, 预算轴相对比较偏差抵消; 修复走真值: q9g gold/更严 judge/跨批配对)。

### Q9 方向级诊断 (2026-11-27 19:xx, D 问"我们在干什么, 能 general 地给优化方向吗")
**我们在干什么**: 表面=Q9 预算-覆盖曲线; 实际=给 S5 自动研究 harness 做体检。体检结论 (三条独立证据 → 同一根因):
1. 预算只买节点数不买质量 (150 拐点后平坦, 13/13 预算耗尽停机非收敛, 298 硬顶)
2. 深度不引入新信息: 经验锚定率 (claim 带数值+来源) by 深度 L2/L3/L4 = 0.19/0.16/0.16 平的 (10 runs 1198 节点, 总 0.16; L1=0/57 是根节点框架 claim 无预期)
3. **验证门在筛选"模糊" (新发现, 2026-11-27 19:xx 探针)**: verified 集锚定率 2/517=0.4%, degraded 集 182/572=32% — 具体数值 claim 触发联网核验、核验失败→degraded; 模糊 claim 不触发核验→LLM 看一眼就过→verified (机制=假设, 相关性=实测)。验证门系统性把具体 claim 筛出 verified 集。
**统一根因**: 目标函数错位 — 循环优化"节点产量", 不优化"每节点信息量"。覆盖广度不惩罚软 claim, 验证通过率反而奖励软 claim (Goodhart)。三域佐证: Q6 (深层=代数展开, 条件熵≈0) + Q9 (本条) + objfmt-hack (H2: 停机条件/scorer 驱动 hack, 非格式)。
**General 方向 (一条原则导出三杠杆)**: 把循环目标从"产节点"改成"增信息"。
- 杠杆1 验证要有判别力: verified 必须带正证据 (来源+数值核对), 否则留 pending。预言: verified 锚定率 0.4%→≥16%, post_acc 分母变真。
- 杠杆2 深度必须买接地: 分支无未决经验问题→不展开 (停=无新问题, 非无预算)。预言: 锚定率随深度升, rework 占比降。
- 杠杆3 停机=收敛非耗尽: frontier 空或 K 轮无新正交节点即停。预言: n_realized 出现 run 间方差 (现在全贴 cap), 单位节点覆盖升。
**最便宜判别探针**: 救活探针 (在跑) 的 n_unsupported 字段 = 杠杆1 预言的下界测量 (verified 集有多少无依据), 不重跑 SM。救活探针回来 → 三杠杆各派最小实验, 现有 10 runs 是对照臂。

**修正 (2026-11-27 19:1x, source×status 交叉验证 + P3_VERIFY 原文核读, 推翻"验证门筛选模糊"假设)**:
- **决定性数字**: source 路由 × 状态交叉表 (10 runs 1198 节点): knowledge 780 (degraded 29%, verified 锚定率 0.00) / **search 345 (degraded 97%)** / given 65 (degraded 2%)。search-degraded 334 个里仅 26 个真"检索失败/timeout", **~308 个是 `[质询]` 开头 = 检索成功拿到来源, 但 LLM 核验判"claim 未被来源直接支持"**。
- **机制 (P3_VERIFY prompt 原文, modules/D-decomp-state-machine/scripts/prompts.py L146)**: ① source=search 节点适用"经验事实排除条款"——具体参数值/市场数据/版本号不适用"第一性原理可推出"豁免, 必须来源直接支持 (a) 或多源一致 (c), 否则 degraded; ② source=knowledge/given 节点"逻辑自洽即 verified", 无需来源。→ **选择倒挂**: 带具体数值的经验 claim (信息量高的) 走 search → 97% 死于"来源不直接支持"; 定性软 claim (信息量低的) 走 knowledge → 几乎全过成 verified。verified 集锚定率 0.4% 不是"模型爱说废话", 是**验证标准与检索通道能力不匹配**: 网页检索片段几乎从不直接陈述具体数值, 而标准几乎不可满足。
- **Goodhart 回路 (新)**: search 路由 = 97% 死亡率 → rework 压力训练模型把 claim 改标 knowledge 规避检索 → 65% 走 knowledge → verified 集更软 → 循环自我强化。模型"知道自己不知道" (29% 主动标 search, gap 标记在工作), 但补全通道是死刑通道, 于是学会不补。
- **合成层修正 (2026-11-27 19:1x, 核 s5_state_machine.py L1526 synthesize_answer, 推翻上一条"degraded 被隔离丢弃")**: 状态机实际用的 P4 接收**全部节点**(按 level 分组, 带 `[status=degraded]` 标签进 fact_table), **不是只吃 verified**。degraded 信息其实进了合成层, 只是带降级标签; P4 prompt 说"基于已验证事实集做封闭推理"→ 合成模型可能**降权** degraded 节点(尤其承载经验内容的 308 个), 但**不是机械丢弃**。→ 杠杆1(b) 的"最便宜一刀"作废(它已在合成层), 改为: **改 P4 prompt 让 degraded 节点按置信度可用而非降权**(纯 prompt 改动, 零重跑)。
- **问题二分 (修正后, 两条独立因果链, 同属"循环优化过门率非信息量"元问题)**: **问题A(生成轴)**: 深度不买正交——锚定率 by 深度 L2/L3/L4=0.19/0.16/0.16 平, 150 后分解产出改写非新内容 → 解释 gate 覆盖 150 拐点(节点内容属性, 与验证状态无关)。**问题B(验证轴)**: 验证门标准与检索通道能力不匹配 → search 97% degraded → ① rework 循环烧预算(13/13 贴 cap 停机) ② post_acc 常数 1.0(分母空) ③ 合成层降权经验内容。**A 和 B 是不同杠杆**: A 治生成(深度必须买正交), B 治验证(标准校准到通道能力 + P4 不降权 degraded)。
- **杠杆1 修正 (从"验证要有判别力"改为"校准验证标准到检索通道能力")**: (a) search 节点"间接支持+逻辑自洽"→ verified 带置信档 (不再二元生死); (b) ~~degraded 进合成层~~ **作废** (19:1x 核 L1526: 全部节点已进 fact_table) → 改为改 P4 prompt 让 degraded 按置信度可用而非降权 (纯 prompt, 零重跑); (c) 提升检索质量 (query 改写/多源) 让"直接支持"可满足。预言: verified 锚定率 0.4%→16%+, 最终答案经验内容占比升, rework 率降。杠杆2/3 维持。
- **General 表述 (可迁移到任何带验证门的 agent 研究循环)**: 验证门的**可满足性**决定哪些 claim 存活; 循环优化的是"过门率"不是"信息量"; 若验证标准超出检索通道的实际供给能力, 系统选择性地杀死信息性 claim、放行空洞 claim, 且路由激励反向强化。判据: 任何验证门上线前测其"通道满足率" (标准可满足的比例), 低于阈值 = 门在筛选空洞。

## T9: 本地 AGI 硬件选型探针 (frame-shift 测试) — 2026-11-27
- 来源: D 反问 "4k 是我们的目标吗? 本地 AGI 最高性价比硬件系统"
- 假设: 27b 参数记忆里 Roofline(速度frame) 太强, 模型面对硬件选型题会惯性优化 tok/s,
  而非识别"显存容量=主导因子" (frame-shift 失败)
- 设计: 复用 GPU 探针 harness, --req hw 题面 (预算5万, 27B-70B, 32K ctx), **C/D 双臂** (原计划 A/B/C 三臂, 实际执行 C=裸 / D=C+简单prompt, 19:45 信号台账改的聚焦设计)
- 外部真值: modules/B-pipeline-ablation/research/hw_probe_ground_truth.md
  (70B Q4 需 ~46GB 显存, 单卡24GB装不下, 容量主导)
- 判据: ✓=给出"显存>=权重+KV"容量公式+推荐双卡/大显存; ✗=还在优化tok/s; ✗✗=散文模拟(search=0自称实测)
- 状态: **done (2026-11-27 19:28 落盘, 6 episodes 全文判读完毕)**
- 产出: data/q9-budget-scan/gpu-model-probe-20261127_hw.json
- **判读结论 (2026-11-27 21:1x, 判断-Lead)**: ① **frame-shift 假设证伪**: 6/6 episodes (C 3 + D 3) 全部识别"显存容量=主导因子"+容量公式+多卡聚合推荐, 无一优化 tok/s — 27b 在硬件选型题上没有 Roofline 速度 frame 惯性, 原假设 (27b 参数记忆 Roofline 太强) 不成立。② **三个新失效模式 (比 frame-shift 严重, 判据 ✗✗ 命中 3/6)**: (a) **假实测**: n_search_calls=0 却声称"实测 32K 吞吐≥15 tok/s" (C ep0/ep2), D ep1 编完整"实测值"表 (34.2/38.7GB), D ep2 自称"实测可行方案" — 零检索+自称实测; (b) **算术自相矛盾** 2/6: C ep1 "936 GB/s > 1.0 TB/s" (方向反), D ep1 "总显存 72 GB ≥ 75 GB 需求" (72<75); (c) **价格幻觉满足预算**: 3090 报 7,500 元/卡 / V100 报 12,000 元/卡, 均低于二手行情 (3090 约 9-12k, conf 中) — "5万内可行"被幻觉价格撑起。③ **C vs D**: D 臂结构更好 (显式"因子检验与否定"表), 但没压住假实测 (D ep1 假实测表比 C 更精致) — 简单 prompt 的价值=结构, 不是接地。④ **跨域佐证 +1**: 假实测=post_acc 的 unsupported 类, 价格幻觉=漂移变体 — Q9 两问题根因 (生成不接地+验证无判别力) 在硬件题同样出现, 非 Q9 特有。

## M: 思考机制落地 team (2026-11-27 D 指令「找个team去研究和实现, 如果能像我一样思考, 论文只是需要让arena和自己review」)

**双 lead 协调 (2026-11-28 01:3x, QQ 会话写入)**: 微信会话 + QQ 会话同时在推 M 线 → M2a 重复做(两边结果一致: power_risk=low, 最大 cv=0.035, 3 reps 够用)。分工锁定: 微信会话=M 线主推进(方向对齐主场, 已推 M3 prep @ 484f757bc); QQ 会话=① arena M0 催交付(已直接进会话 01a20b11 发消息) ② M3 夜间批启动前核验 ③ 跟 D 对齐。**夜间批启动权=微信会话**(它持有 M3 prep 上下文), QQ 只做核验不抢启, 避免双启。

**主线重定义**: 验收物 = 27b 在生产循环里表现出 D 式思考（爬层/统一覆盖/量化落地/类比审计/判据瓶颈），测量=对照实验机械指标。论文/claim 强度/review = 后置（arena 对抗核验 + 自己 review）。
**既有地基（一手证据已核）**: K4b 判决定格 (oood-column-status.md 23:0x): S1(剥离版) ≥ S0(域味版)，域味=负资产，kernel general 成立；S1/B 双臂数据在盘上 (experiments/stage-ablation/oood-probe/s1/, metrics-2x2.json @ 2e2cf60bf)。
**5 模板源** (projects/AI-计算科学/D1-persona-align/memory/general-thinking-template-20261124.md): T1代价模型/T2统一覆盖/T3量化落地/T4类比审计/T5判据瓶颈，每条带触发条件+动作。
**第一性原理** (d-thinking-mechanism-first-principles-20261124.md): 理解=压缩-解压往返无损不动点；两阶段压缩(选域 vs 精化, 顺序不可颠倒)。

### 任务表 (强制列: 任务/依赖/读行/写行/commits/载体)

| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
|---|---|---|---|---|---|
| M0 arena 调研: general 推理成熟机制 (A prompt级/B评测/C开源) | 无 | - | - | - | sub-arena (**✅ DELIVERED 11-27 17:16 UTC @ f8477718 分支 dccefaf3c, 已 cherry-pick 回 thinkmech @ 952880ee1** → modules/G-think-mechanism/think-trigger/m0-general-reasoning-survey.md; 台账原记"分支 423a71ef 超时无交付"=查错分支, 实际交付在 f8477718。内容: A 7 机制(Zero-shot CoT/Step-Back/Least-to-Most/AID/schema约束/SpARE/UoT-BALAR) + B 4 评测法(ARC-AGI-2/知识冲突探针/跨域零样本/预算内accuracy) + C 3 开源(ToT/LangGraph/框架族谱) + 2 gap(构念无标准benchmark/schema约束无同构文献)。**⚠️ 未消费**: M2 设计在 M0 交付前已定稿(只注 T1+T2), V2 臂(M0 top 机制)始终未建 —— D 2026-11-28 质询"实验前有没有调研/有没有解决方案"暴露此断层) |
| M1a 基线提取: S1/B 双臂机械指标 → baseline-pre-injection.json (脚本落盘) | 无 | ~50 | 脚本+~30 | 1 | sub-27b |
| M1b prompt 结构盘点: s1/prompts.py → prompt-inventory.json (脚本落盘) | 无 | 471 | 脚本+~30 | 1 | sub-27b |
| M2 注入变体设计: V0=S1现状 / V1=+5模板 / V2=M0 调研 top 机制 | M0+M1b | ~100 | ~80 | 1 | 判断-Lead (done 11-28 00:55, m2-injection-design-20261128.md; 只注 T1+T2 合并版, T3/T4/T5 与 harness 职责冲突不注) |
| M2a 方差探针: 已有 6 臂 rep 间三指标 cv → 定 M3 reps 功效 | 无 | 脚本 | 脚本+json | 1 | sub-27b (✅ done 11-28 01:2x @ 3003978bb, 零 GPU; variance-report.json; 注: 6臂各1rep, 报的是跨臂方差非rep间方差, rep间方差由M3 3reps 自带) |
| M2b V1 实现: s1/→v1/ 复制 + T1+T2 注入 + 冒烟 | M2 | ~100 | 复制+diff | 1 | sub-27b (done 11-28 00:59 @ d03c9423d, 冒烟 ok 3 节点 JSON 契约不破) |
| M3 对照实验: V1×3域(cyclone/mining/hw) 各3reps + V0(s1)cyclone 2reps = 11reps, 40节点, 无检索口径 | M2 | - | - | 1/rep | sub-27b(✅ prep @ 54eb4e5a7: run_v1_sm.py 按参数切arm + raw-llm落盘 + launch_m3.sh 幂等串行; 🔄 夜间批在跑 PID 11234 起 01:20, log=m3-queue.log, 预计 4-6h) |
| M3b V3 臂（实验上下文注入）: v3/ = v1 注入 + 【你在为什么工作】块（目标/设计/判据 ~200字, 不泄题面答案）; 域=cyclone+hw（埋雷域剔除: 题面含埋雷数据, 注入"质疑题面"会泄雷, 测不干净）; 6 reps 串行 8787 | M3 批完（对照臂已有） | ~50 | 复制+diff+脚本 | 1 | Lead 直接执行（2026-11-28 D 指令"把设计过程/要求目标也给他, 包括具体实验设计"; 冒烟 ok 5 节点 5.7s; 队列 PID 59476 log=v3-queue.log; 判决双轨同 M4, V3 vs V1 vs V0 三臂对比） |
| M3c V2 臂（成熟机制对标: Step-Back）: v2/ = s1 + 【思考习惯】块(a 上溯一步: 分解前先找通用原理写第一个一级节点 / b 原理校验: 子节点机制须能从原理推出, 推不出标[孤立机制]); 内容=M0 A2 Step-Back(Take a Step Back, ICLR 2024, conf 0.85)原样协议, 长度对齐 V1; 单变量=注入内容(自研 T1+T2 vs 成熟机制) | M0 已消费(952880ee1) | ~30 | 复制+diff+脚本 | 1 | Lead 直接执行（2026-11-28 D 质询"实验前有没有调研/有没有解决方案"落地: M0 调研已交付但未消费, V2 臂=对标成熟方案的直接落地; 冒烟 ok 6 节点 5.6s; 队列 PID 62814 log=v2-queue.log; 判决: V2 vs V1 同域对比 → 自研注入是否优于/等效于成熟机制, 这是 M 线 claim 可防御性的关键对照） |
| M4 记分+判决: 机械指标(机制覆盖/量化claim/域偏移率) + 预注册判据 | M3 | ~100 | ~60 | 1 | sub-27b + 判断-Lead |
| M5 论文化+review: claim 强度/对抗核验 | M4 判决为正 | - | - | - | arena + 判断-Lead (后置) |

**M3 预注册判据 (M2 细化)**: 注入有效 = V1 机制覆盖 ≥ V0 且 量化claim 密度(quant/llm_calls) 显著升 且 域偏移率降 (27b 已知: 形式能注入 5.67/6, 内容域偏移 100% — T2 实证, 本次测内容层)。
**并行纪律**: M0(arena) 与 M1a/M1b(本地) 并行; M2 等 M0 交付; M3 等 M2。8787 单实例 → M3 各臂串行排队。
