# RV3G3cdx-m4-assert-lint — 阶段工件合并记录（r32）

> origin: ai · 2026-10-31 · 本 goal 的 01/03/04 阶段内容合并于此单文件（执行节奏：任务书规格明确 + 纯仓库内机械落地，按「每步产出可验证」纪律压缩阶段文档为单件；02 = 定义文档 §3 规格本身即研究输入，零新增调研）。
> **负面发现（如实登记）**：本会话启动时已在 `ralph/m4-assert-lint-r32` 分支（runner 桥接预建，非 main），且执行期间外部进程切 main 并 fast-forward merge 该分支——template-v3 已随 a4986d1 落 main，assert-m4-sources.py 工作树残留由 e0c36b3 补收。两文件内容与本记录引用 byte-stable（git show 核验）。

## 阶段 01 — goal 分解

**目标**（queue L64 原文承接）：M4 独立源机判落地轮（r152 U1/U2 承接），按 `bench/rubric-v3/m4-independent-source-definition.md` §3 规格执行三步：U2 schema v3 → U1 assert-m4-sources.py 落盘 → 对现有 packet 实跑回归。

**子任务分解**：
| # | 子任务 | 交付物 | 状态 |
|---|---|---|---|
| G1 | U2 schema v3：evidence-packet-template 增 provider 必填 str + channel 枚举两字段 | `bench/self-opt-tester/r5/evidence-packet-template-v3.md` | ✅ a4986d1 |
| G2 | U1 脚本：nature 枚举校验 / source 归一重复 SIGNAL / D2-D3 关键词扫描 + X3 双条件并联排除 | `bench/self-opt-tester/r5/assert-m4-sources.py` | ✅ e0c36b3 |
| G3 | 实跑回归：v2 存量 packet 降级运行（04.5 W6 时序条件兜底）+ 负样例变异测试 | 本文档 §04 节输出 | ✅ |

**激活前置核查**（W6 时序条件）：`ls bench/self-opt-tester/r5/run5/` = 仅 task-brief.md（Oct 26），无产出文件 ⇒ run5 arena 侧倾向未开跑；arena 在途状态仓库内不可核实（无 ls-remote 权限查 arena 侧），按 W6 既定处置 = 降级运行兜底，不阻塞。

**禁区边界裁定**：任务书步骤文字为「evidence-packet-template 增…两字段」。§3 U2 原文 = 「改 template 属判定语义级变更，走独立候选，本轮不动」（指 r152 当时不动）；m4 定义文档 §5 修订规则允许条款级变更直接 Edit。**裁定**：以**新文件 v3** 承接而非 in-place 改 v2——(a) v2 是 R5.2 冻结先例形态（assert-packet-symmetry.py docstring 引用其填写规范、bench.md L134 索引指向 v2 路径），in-place 改动面大于必要；(b) v3 = v2 超集（P1-P5 与 P6 既有字段逐字不变，唯一变更面 = P6 independent_sources 条目增两字段），旧 packet 按 v2 继续合法、新 run 按 v3 填，双版本共存零破坏；(c) 禁区「不改其他冻结断言脚本、不动 scorers/」两条均满足（template 不在冻结断言脚本清单，scorers/ 零触碰）。此读法偏离任务书字面（「增字段」vs「新文件」）如实登记于此，供 04.5 复核。

## 阶段 03 — 动作分解（实施要点）

**G1 template-v3 设计决策**：
- P6 条目 schema：`provider`（必填 str，一条目一主体，多主体拆条须与 D2(γ) 一致——同检索行为同通道多 URL 仍是 1 源，拆条不加分；无法确定 = `"unresolved"` + notes 登记，禁空串）+ `channel`（四值枚举 web-search / llm-receipt / local-measured / file-read）。
- nature-channel 映射约束（冲突 = SIGNAL 非 FAIL）：transcription ⊆ {llm-receipt, file-read} / local-measured ⊆ {local-measured, file-read} / external ⊆ {web-search, llm-receipt}。
- 头部声明三件套：v3=v2 超集关系 / W6 时序前置条件成文 / 消费方（下轮 packet 组装者 + assert-m4-sources.py 完整实跑模式）。
- 选填字段节澄清同名异义：run 级 `channel`（自由文本执行通道描述，v2 既有）≠ P6 条目级 `channel`（四值枚举采集通道）。

**G2 脚本判定语义**（权威源 = 定义文档 §3 U1 (a)(b)(c) + 04.5 W2 双条件并联）：
- (a) nature ∈ {external, local-measured, transcription} = **FAIL 级**（exit 1）。
- (b) source 归一 = 小写 + 去日期括号（半角/全角 `(2026-06-18)` 型）+ 空白折叠；同 run 内归一后重复 = **SIGNAL**（疑似同源拆条，D2(γ)/回测 M1 首个实证用例预注册）。
- (c) 三类扫描：transcription ⇒ D2(β) 自动排除 SIGNAL；`转引|经\s*\S+\s*blog|二手` 命中 ⇒ D3 折减标记 SIGNAL（**只标折不改值**——0.7 暂定待成璐裁定，脚本不把 0.7 当硬阈值写入任何判定，符合定义文档 D3 ⚠ 注记）；X3 = conf=null **且** 负向关键词（不可达/无源/unverified/无外部/无网络）才自动排除，单独任一 = SIGNAL 人工复核（W2 双条件并联）。
- 双模式自动切换：packet 任一条目含 provider/channel 键 ⇒ v3 完整实跑（追加 provider 必填非空 str + channel 枚举 + nature-channel 映射冲突检查）；否则 v2 降级运行（跳过 provider 维度，SIGNAL 声明 U3 激活条件未满足）。
- exit 语义对齐 r5 既有脚本惯例（assert-packet-audit.py 范式）：exit 0 = FAIL 级全过（SIGNAL signal-only 不参与 exit code）/ exit 1 = 存在 FAIL。

## 阶段 04 — 执行验证（实跑输出）

### V1 — v2 存量 packet 降级运行回归（任务书指定对象）

命令：`python3 bench/self-opt-tester/r5/assert-m4-sources.py`（缺省对象 = evidence-packet-r4-v2.json）

```
=== evidence-packet-r4-v2.json [v2 降级运行（provider 维度跳过，U3 激活条件未满足）] ===
SIGNAL ...: schema-version — packet 无 provider/channel 字段 ⇒ 降级运行...
[PASS] ×11 nature ∈ enum（run1[0-1] / run2[0-6] / run3[0-1] 全过）
SIGNAL run1[0] D2-beta-exclude — nature=transcription ⇒ 上轮回执转录，自动排除
SIGNAL run1[1] X3-exclude — conf=null 且负向通道关键词命中 ⇒ 双条件并联成立，自动排除
SIGNAL run2[2] D3-transit-mark — 转引标记命中 '转引'
SIGNAL run2[4] D3-transit-mark — 转引标记命中 '经 arihantdeva blog'
SIGNAL run2[5] D3-transit-mark — 转引标记命中 '转引'
SIGNAL run3[1] X3-exclude — conf=null 且负向通道关键词命中 ⇒ 双条件并联成立，自动排除
=== 0 FAIL / 7 SIGNAL（1 packet）===
PASS（SIGNAL 为 signal-only 报告，不参与 exit code）
exit=0
```

**与 r152 回测 S1 逐条对账**（loop-artifacts/stages/04/RV3G3cdx-m4-ops-backtest.md）：
| 回测判定 | 脚本输出 | 一致？ |
|---|---|---|
| run1[0] 排除 D2(β) | D2-beta-exclude | ✓ |
| run1[1] 排除 X3 | X3-exclude（双条件成立） | ✓ |
| run2[2][4][5] 计入【D3 折减】 | D3-transit-mark ×3 | ✓ |
| run2[3] 同源拆条风险（M1，回测未做字符串归一比对，预注册为 U1 首个实证用例） | **source-dup 未触发**——见下方局限登记 | △ |
| run3[1] 排除 X3 | X3-exclude | ✓ |

**M1 局限如实登记**：run2[0] source = "augmentcode.com guide (2026-06-18); neelmishra.github.io; ai-tldr.dev (2026-06-13)"（三 URL 分号拼接），run2[3] source = "augmentcode.com guide（同 E1 页）"（单 URL + 中文括注）。两者**整串归一后不相等**（前者含另外两个域名，后者含「同 E1 页」括注）⇒ 整串精确匹配检不出这对同源。回测 M1 的「应命中」预期基于**主体名级**归一（augmentcode.com 出现于两条），超出 §3 U1(b) 规格字面（「source 归一（小写 + 去日期括号）重复」= 整串归一）。脚本忠实实现规格字面，主体名级检测 = 规格外增强，导出候选承接（不代扩）。保守计数不受影响（回测已将 [3] 并入 web 簇）。

### V2 — 负样例变异测试（构造 v3 坏 packet，/tmp/bad-packet-v3.json）

五条目覆盖全部检查面：bogus-nature / 空 provider / 大小写+日期括号归一重复对 / conf=null 单条件 / 负向关键词双条件 / transcription+web-search 映射冲突。

```
=== bad-packet-v3.json [v3 完整实跑] ===
[FAIL] runX[1] nature ∈ enum — got 'bogus-nature'
[FAIL] runX[2] provider 必填非空 str — got ''
SIGNAL runX[1] source-dup — 与 [0] 归一后相同（'a.com'…）
SIGNAL runX[2] X3-review — 仅单条件命中（conf_null=True, kw=False）
SIGNAL runX[3] X3-exclude — 双条件并联成立
SIGNAL runX[4] D2-beta-exclude
SIGNAL runX[4] nature-channel-conflict — transcription vs web-search
=== 2 FAIL / 5 SIGNAL（1 packet）===
exit=1
```

六项预期行为全部命中（FAIL×2 拦截 + SIGNAL×5 各分支逐一触发），exit 1 按预期。

### V3 — 禁区与回归基线

- 冻结断言脚本零改动：`git status` 确认 ablation/scripts/ 与 r5/ 既有脚本 0 diff；十五脚本复跑 exit 分布 = 13×0 + 1×1（assert-kappa-receipt.py，SIGNAL κ<0.6 常态，r30 收口已知态）+ 1×2（assert-closure-checklist.py，手动工具无参调用语义，r148 已知态）——与本 goal 改动前基线一致，零漂移。
- scorers/ 目录零触碰（git status 无该路径条目）。
- template-v2 零触碰（新文件 v3 承接，见 §01 边界裁定）。

## 残余 blocked-on-external（导出候选承接）

U3 完整实跑首验 = 下一轮 run 按 template-v3 产出含 provider/channel 的 packet 后首次盲判（检验 r152 回测「完备性验证非预测验证」W4 登记的外推效力）——已导出 queue 候选 `RV3G3cdx-m4-u3-first-blind-judge`。W6 时序条件仍挂（arena 侧在途状态仓库内不可核实）。