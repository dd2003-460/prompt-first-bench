# origin: ai — 阶段 04.5：终局反方复核（RV3G3cdx-crossdomain-promptversion-mapping · r153）

> 攻击项 = 02.5 X6 预登记 A-1~A-8 + 04 执行偏差 D-a~D-d。逐项以「试图推翻」姿态复核，
> 结论三态：驳回（攻击不成立）/ 部分成立（处置 W#）/ 成立（必须回炉）。

## A-1 · O1 C9-plain 归属推论（映射表把既有 8 run 题面标为 `pre-v3/C9-plain` archived-reference）

**攻击**：TASK-ablation.md L12 只说 prompt-V0.txt 是「C9-plain 档」，L1 原始任务书不在本仓——
「C9-plain ≠ v3 变体矩阵成员」是基于 #27 裁定文本的推论，若 C9-plain 实际就是 V0-baseline 的旧名，
则映射表制造了虚假版本分裂，V0-baseline 条目变成重复登记。

**复核**：#27 裁定原文（DRAFT v2 §3.2 L180）明确区分两物：「V0 必须在 **v3 题面**上同批次重跑
（#27：不得复用 L1 旧题面数据进配对检验，**L1 C9-plain 只作外部参照**）」——裁定文本自身就把
C9-plain 与 V0 当作两个不同对象处理（一个要重跑、一个只作参照）。若二者同名同物，该句自相矛盾。
推论方向与裁定文本一致，且映射表 status 字段已把两者区隔（archived-reference vs pending-run），
即便成璐裁定归属应改，消费逻辑零影响（gold_nodes 相同，仅 label 变更一行 diff）。

**判定：驳回**（推论有裁定文本锚点支撑；残余不确定性已挂 APPROVALS 供复核，不阻塞）。

## A-2 · r71b vs r71 冻结事件选择（frozen_at_commit = ed552c4）

**攻击**：ed552c4 是「口径核对」commit（复算确认计数不变），不是 gold 清单首次落盘事件——
登记它会让审计者误以为 gold 树在该 commit 才存在。

**复核**：映射表登记的是**口径冻结事件**（strict 集含 N-4/N-1.3 的五节点口径何时成为裁定事实），
非文件创建事件——AUDIT-report.md L100「（r71b 冻结）」即此语义的既有引用锚点，本表沿用仓库自己的
表述惯例。字段名 frozen_at_commit + note 字段写明「口径冻结事件 = r71b」，无歧义空间。
且该字段机判零消费（纯审计锚点），即便改选 r71 也是单行 diff。

**判定：驳回**。

## A-3 · T4 收窄是否漏报（仅 M[P]≠GOLD_DOMAIN1 时 SIGNAL）

**攻击**：M[P]==GOLD_DOMAIN1 且 G 缺省时静默 PASS——若未来 GOLD_DOMAIN1 常量本身被改（第一域
口径演进），缺省路径会静默跟随新常量而映射表绑定旧清单，对照失效无人知晓。

**复核**：GOLD_DOMAIN1 改动 = 十五脚本之一（assert-goldrank-threshold.py 等）同步改动 + 冻结面
APPROVALS 登记的重型事件，不可能静默发生；且该场景下「缺省值==新常量≠绑定清单」恰恰是 T4-SIGNAL
分支（M[P]≠GOLD_DOMAIN1 成立）会报出的情形——攻击场景与静默分支互斥。真正的风险面是
「映射表绑定清单滞后于第一域口径演进」，那是建表方的维护责任（batch2-arrival-closure goal 职责），
非检查器缺陷。

**判定：驳回**。

## A-4 · T6 降级 vs fail-loud 目标冲突（表缺失 = INFO exit 0）

**攻击**：goal 标题是「fail-loud 协议承接」，表缺失却降级放行——若有人恶意删表绕过错配检查，
断言照样 exit 0，fail-loud 形同虚设。

**复核**：02.5 X3 已论证正交性（fail-loud 对象 = 数据错配，非工具能力缺失）。补充本轮实证：
T6 分支输出 `[INFO] gold-map: ...absent → 对照检查跳过` ——**降级是可见的**（stdout 留痕），
非静默吞掉；恶意删表场景下 git status/diff 本身就会暴露权威源文件消失，不存在「无声绕过」。
先例对齐：--lint-only 模式「目录不存在 = SIGNAL」同款降级哲学（既有 docstring 明文）。

**判定：驳回**。

## A-5 · 对照检查放主模式导致 --lint-only 用户失去对照能力

**攻击**：数据提供方用 --lint-only 自验时拿不到 gold-map 对照结果，可能带着错配数据落盘，
直到主模式首跑才暴露——对照能力入口错位。

**复核**：X4 约束的代价是真实的，但替代方案（lint 模式也触发对照）会破坏 11 既有样例的 byte-exact
输出（其 prompt_version="DRAFT-v2-frozen" 不在映射表 ⇒ 全部新增 [SIGNAL] 行）——byte-exact 回归
是本仓库硬验收线，不可破。折中已在 README 固化：r153 新增 4 样例标注「主模式消费」，数据提供方
自验 SOP = lint 查 schema + 主模式 --dir 查对照（两步均有现成命令）。第二域数据到来时
batch2-arrival-closure goal 可评估是否给 lint 模式加独立 --check-goldmap 开关（导出候选，见 queue）。

**判定：部分成立 → W1**（README 已注明双步 SOP；lint 模式对照开关挂候选，不阻塞收口）。

## A-6 · 排序后集合相等 vs 顺序敏感（O2）

**攻击**：sorted-set 比较忽略声明顺序——若下游某消费者依赖 gold_nodes 顺序（如按序计分），
等价集合的不同排列会通过检查但产生不同结果。

**复核**：grep 全仓 gold_nodes 消费点：load_batch2 内 `nid in gold`（集合成员测试）、
top10_gold_count 的 `sum(nid in gold ...)`、hit-matrix 键集循环——**全部是 O(1) 成员测试或遍历，
零顺序依赖**。Y1 检查同为键集成员语义。顺序在现有消费链中信息量为零，顺序敏感只会误杀等价声明。

**判定：驳回**（消费链零顺序依赖获 grep 实证）。

## A-7 · 映射表 _schema 版本号机制是否过度设计

**攻击**：只有一个消费方、只有一个版本的 _schema 字段是仪式性冗余。

**复核**：sample-plan.json 已有 schema_version 先例（仓库惯例）；映射表是**跨 goal 扩展的活文件**
（第二域条目将由 batch2-arrival-closure 追加），schema 演进时（如 versions 增 domain 路由字段——
多域期升级已在本轮代码注释中预注册）旧消费方凭 _schema 值即可拒读而非误读。成本 = 一行字符串，
收益 = 演进期的防误读保险。非过度设计。

**判定：驳回**。

## A-8 · 六变体占位条目是否应入表（vs 只登记 C9-plain）

**攻击**：V0..V3-sham 尚无 run 数据，其 gold_nodes 是 B10 推论非实测——入表会把「推论」伪装成
「登记事实」，污染权威源的证据等级。

**复核**：B10 推论的证据链（DRAFT v2 L180 原文 + 冻结快照 61416b4 + §4 补丁区零 gold 语义）在
02 A3 已闭合到 byte-exact 级；status=pending-run 字段显式标记「尚未开跑」，报告层可区分推论与实测
（02 A7 字段必要性论证第 3 条）。不入表的代价 = 六个变体开跑后首跑全部落 T3 SIGNAL（未登记），
数据提供方须先回来改表才能过检——把机械推论的确认成本转嫁给数据流，违背「零改动接入」设计目标。

**判定：驳回**（status 字段已承担证据等级区分职责）。

## D-a · 初版后缀查询缺陷（完整 pv 直查修复）

**攻击**：修复后的「单域期取唯一 domain」在多域期会变成隐性错误源——prefix 路由靠
domain_id.startswith(family) 匹配，若第二域 id 不以 family 前缀命名（如 `decomp-hw-27b-batch2`
对 family `v3`），路由 miss ⇒ 误落 SIGNAL。

**复核**：多域期 prefix 路由只是**过渡形态**——代码注释已明文「第二域条目到来后由
batch2-arrival-closure goal 升级为显式 domain 字段路由」，且歧义时走 SIGNAL 不代裁（fail-safe 方向：
宁可提示不可错判）。当前单域期该分支不可达（len(domains)==1 先行短路）。风险已被协议化移交，
非遗留缺陷。

**判定：驳回**（过渡形态 + fail-safe 方向 + 协议化移交三重覆盖）。

## D-b · bound 类型违例分支 NameError 潜伏（ver→pv 修复）

**攻击**：该分支仅在映射表自身损坏时触达——修复是否正确？

**复核**：T7b 实跑验证（04 A3 留档）：临时注入 gold_nodes="not-a-list" ⇒ exit 2 且错误消息正确
指名 `domains.decomp-hw-27b.versions.pre-v3/C9-plain.gold_nodes`——变量引用正确、文案完整。

**判定：驳回**（实证闭合）。

## D-c · N6 样例数据修正（N-5.3→N-5 + nodes/hit-matrix 同步）

**攻击**：为让样例触达 gold-map 分支而扩充样例数据（nodes 增 N-5、hit-matrix 增 cell）——
是否为了凑出口而扭曲样例语义？

**复核**：N6 的断言对象是「显式声明 gold 与映射表绑定不一致 ⇒ exit 2」，触达该分支的必要条件是
通过 Y1 键集检查——样例 nodes 键集本来就不含 N-5.3（它是 lint 样例的最小数据集，非真实第二域镜像）。
扩充 N-5 保持样例自洽（Y1 通过 → gold-map 分支成为首个失败点），断言语义未变。负样例「最小改动
触达目标分支」是既有用例构造惯例（neg-goldnode-not-in-nodes 同款思路的反向应用）。

**判定：驳回**。

## D-d · 主模式 --dir 参数化新增

**攻击**：main() 新增 --dir 解析扩大了 CLI 攻击面——`--dir` 出现在 --lint-only 之后的位置会被
两种模式同时解析吗？

**复核**：--lint-only 分支在 main() 顶部 `return`，其后的 --dir 解析代码不可达；--lint-only 自身的
base_dir 解析逻辑零改动（11 样例 byte-exact 实证）。无参调用 main_dir=None ⇒ load_batch2(None)
与改前逐字节一致（A4(i) 实证）。两模式参数空间不相交。

**判定：驳回**。

## 处置汇总

| 攻击项 | 判定 | 处置 |
|--------|------|------|
| A-1 | 驳回 | APPROVALS 复核项保留（非阻塞） |
| A-2 | 驳回 | — |
| A-3 | 驳回 | — |
| A-4 | 驳回 | — |
| A-5 | 部分成立 | **W1**：README 双步 SOP 已固化；lint 模式 --check-goldmap 开关挂 queue 候选 |
| A-6 | 驳回 | — |
| A-7 | 驳回 | — |
| A-8 | 驳回 | — |
| D-a | 驳回 | 多域路由升级挂 batch2-arrival-closure 联动条款（代码注释已预注册） |
| D-b | 驳回 | T7b 实证闭合 |
| D-c | 驳回 | — |
| D-d | 驳回 | — |

## verdict: **pass**

八攻击 + 四执行偏差全闭合：七驳 + 一部分成立（W1 处置已落地/挂候选）+ 四驳回。
无成立级攻击，无需回炉。收口条件满足。