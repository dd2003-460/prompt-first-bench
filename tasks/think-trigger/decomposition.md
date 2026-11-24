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
- **⚠️ 生产运行中但未提交（2026-11-25 核验，风险升级）**：T1 机制**已在生产跑**——`~/.hermes/.stage-gate/.think-trigger.json` 状态文件 ts=2026-11-25 01:21（本会话收到的 stop_hook 续推消息即来自含 T1 机制的 stop_hook）。但改动在 tools/stage-gate working tree 未 commit → 任何人对该仓库做 git checkout/stash/reset 会**静默丢失 T1+T4 功能**（无报错）。commit 紧迫性高于一般"待提交"。
- **T4 状态（同批核验）**：goal 计划子项⑥列了 T4（"修脚本卡住→general 思考升级触发"），但本 decomposition 原本漏了 T4——现补登：T4 **已实现**（stop_hook.py 含 `t4-stubborn-spin` 触发器 + `_T4_REFLECTION`"别蛮力试了，退一步：这个问题的 general 机制是什么？"），同样在未提交的 working tree 里。T4 验收：连续卡住（同一报错≥2次/脚本反复失败）时触发反思注入。

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

## 缺口标注
- [待核验] stop_hook 能否访问 per-message thinking（决定 T1 走首选还是降级）
- [已核验 2026-11-25] 27b 在 8787 = `qwen3.8-27b-mtp`（vllm NVFP4，OpenAI 兼容 /v1/chat/completions，thinking 模型：`reasoning` 字段单独返回，只抓 content 丢隐藏思考链）
- [待标定] 触发阈值 N（连续几轮）和 thinking 阈值（先拍 430/调用，T2 数据回来再校准）

## 任务表（派发只执行表内条目）
| 任务 | 执行方 | 状态 |
|------|--------|------|
| T1 思考触发 hook 实现 | subagent A | 已实现未提交（2026-11-25 核验，待 commit+APPROVALS） |
| T2 接着考虑实验（预注册+跑） | subagent B | 完成 2026-11-25 (commit 002eada24) |
| T3 落点整合（T1+T2 完成后） | Lead（T1+T2 回来后） | 待 T1+T2 |
| T4 脚本卡住→general 思考升级触发 | subagent A（与 T1 同批） | 已实现未提交（2026-11-25 核验，t4-stubborn-spin 触发器，与 T1 同批 commit） |
