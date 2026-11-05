# 阶段 02.5：对抗性交叉核对 — RV3G4-prior-source-assert

> 对象：02 工件的设计判断（J1-J4 + §3 设计结论）· 分支 ralph/rv3g4-prior-source-assert · 2026-10-30

## A1 · 「signal-only 是空防护——provenance 块可以手填两个假 judge_id，脚本照样 PASS」？

**攻击**：脚本只验元数据存在性和 artifact 可解析，不验 p̃ 数值真的来自两个独立过程。Lead 可以自己写一个 judge-blindtest-r1.json 然后登记两个 source，机判全绿但独立性是假的。
**回应**：(a) 本 goal 的授权范围是 G4 导出的「最小机械化版本」——它解决的是「纸面协议零防护力直到被执行」（S3 降档教训），即让 provenance 成为**必须显式落盘、可机判、漂移即 FAIL** 的结构，而不是让单源文件无声通过；(b) 检查②的 byte-exact 条款（blind-reestimate 条目 judge_id == judge-blindtest-r1.json:judge 实际字段）封死了「手写假 judge_id 而 artifact 不存在或内容不符」的路径——artifact 必须真实存在且其 judge 字段与登记一致；(c) 残余风险诚实登记：同一人先后跑两次估计并都登记为独立源，脚本无法识别（需要时间戳/会话指纹级证据，超出 assert 职责）。家族隔离 + 盲性真实性归 04.5 人工复核项 + rubric-v3 遗留 #1（≥3 独立 LLM 服务盲测）闭环。
**判定**：部分成立 → 采纳 byte-exact 条款 + 残余风险登记（R5 进 04 日志）。

## A2 · 「追加 p_tilde_provenance 到冻结件 prior-estimates.json 违反冻结纪律，应该开新文件」？

**攻击**：runner 硬规则「冻结数据只读，要改必须开新文件 + APPROVALS.md 登记」。开新文件（如 prior-estimates-provenance.json）才是合规路径，往原文件加键就是篡改冻结件。
**回应**：APPROVALS.md 登记已预注册（J4），登记理由充分：(a) provenance 语义上**属于** prior-estimates.json 自身的元数据（描述本文件的生成源），拆到新文件会造成「元数据与本体分离」的二义性（两处漂移风险，同 RV3B1psf 02.5 A4 的双源问题）；(b) 改动 = 纯新增顶层键，nodes.* 及所有被消费字段零触碰，消费侧回归（assert-w2-formula / assert-w3w4-recompute 重跑 exit 0）提供机判证明；(c) 若坚持开新文件，则 assert 脚本要跨文件 join，未来任何一侧移动/改名都会断链——单文件自包含更稳。APPROVALS 登记满足硬规则的登记义务，「开新文件」是登记时的可选处置之一而非唯一选项。
**判定**：失败（登记 + 纯新增 + 消费侧回归三重保障）。

## A3 · 「N_MIN=2 但两源同族（都是 Qwen），脚本 PASS 会误导下游以为独立性达标」？

**攻击**：rubric-v3 遗留 #1 明确要 ≥3 个**独立 LLM 服务**盲测 p̃。现在双源同族却给 PASS，下游引用「assert-prior-source.py PASS」时可能误读为独立性检验通过。
**回应**：(a) 脚本输出首行强制标注「SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict」——PASS 的语义边界写在输出里，不是留给读者猜；(b) D2 note 显式声明 `family-independent: false`（双源均 Qwen 家族）——事实层不粉饰；(c) N_MIN=2 是 G4 导出原文「≥N」的最小落地值，≥3 异族标准由遗留 #1 另开 goal 跟踪，两者在 revision-log/g4 文档中互相指向，不会混淆。
**判定**：失败（语义边界三处显式声明）。

## A4 · 「artifact 相对 ROOT 解析——prior-estimates.json 自己作为 primary 的 artifact，等于『自己证明自己』，循环论证」？

**攻击**：primary source 的 artifact 指向 prior-estimates.json 本身，脚本检查「artifact 存在」永远为真，这条检查对 primary 无信息量。
**回应**：承认——primary 条目的 artifact 检查确实只是格式校验（防手滑写错路径），不是独立性证据。primary 的独立性依据是任务书链（TASK-ablation.md L27 指定 Lead 主会话执行估计）+ 本文件即产物本身（自我指认合理：它就是那个估计过程的输出）。脚本职责是「登记的来源可定位、可追溯」，不是「证明历史过程真实发生」——后者超出机判能力，归 04.5 人工复核。此限制写入 04 日志 R6。
**判定**：部分成立 → 限制登记（不阻塞：检查目标本就是可追溯性而非历史真实性）。

## A5 · 「检查②要求 blind-reestimate 条目 judge_id 与 judge-blindtest-r1.json:judge byte-exact——但该字段是人写的描述字符串，未来换 judge 重跑 blindtest 后旧 provenance 就 FAIL 了，脚本变成一次性锁死」？

**攻击**：byte-exact 绑定当前 judge 描述文本，blindtest 文件一旦更新（比如 batch2 换模型重跑），provenance 必须同步改，否则 assert FAIL——这是合理的吗？
**回应**：这正是期望行为——provenance 描述的是**当前落盘 p̃ 值的实际生成源**。blindtest 文件更新 = p̃ 值来源变化 = provenance 必须重新登记（哪个 judge 产出了当前这些值）。锁死不是缺陷，是防漂移：静默换源不更新登记 = 审计链断裂，FAIL 是对的。更新流程 = 改 blindtest + 同步改 provenance + 重跑 assert，三步都在 runner 常规操作内。
**判定**：失败（防漂移语义正确）。

## 汇总

| # | 攻击 | 判定 |
|---|------|------|
| A1 | signal-only 可被假 judge_id 绕过 | 部分成立 → byte-exact 条款 + 残余风险 R5 登记 |
| A2 | 追加冻结件应开新文件 | 失败（APPROVALS 登记 + 纯新增 + 消费侧回归） |
| A3 | 双源同族 PASS 误导下游 | 失败（SIGNAL ONLY 输出 + note 声明 + 遗留 #1 分轨） |
| A4 | primary artifact 自我指认循环 | 部分成立 → 限制登记 R6（可追溯性 ≠ 历史真实性） |
| A5 | byte-exact 锁死未来换源 | 失败（防漂移是期望行为） |

**02.5 verdict：pass**（A1/A4 两项部分成立已登记进 04 日志风险表）。
