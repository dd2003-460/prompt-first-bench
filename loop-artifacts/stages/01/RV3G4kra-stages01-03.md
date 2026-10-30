# 阶段 01-03 合并工件 — RV3G4-kappa-receipt-assert（小 goal 压缩六阶段：01/02/02.5/03 判定一次落盘，04/04.5 独立）

> origin: ai · 2026-10-30 · 参考同族结构 assert-prior-source.py（r130/r135 验证过）。

## 01 拆解 + schema 提案

| # | 因素 | 口径预注册 |
|---|------|-----------|
| F1 (schema) | 最小回执格式 | g5 C2 四字段为底线，按 DRAFT v2 R5 条款（换位双判 + κ≥0.6 + 长度去偏）补全语义：<br>`kappa-receipt.json` = { `gate`: "role-swap-dual-judge"（固定值，防误用其他方法名）, `kappa_value`: float ∈ [0,1]（条目层二值 Cohen's κ，DRAFT v2 R-02 口径）, `method`: str 非空（κ 计算说明，如 "Cohen kappa on item-level binary scores, n_items=N"）, `judges`: [str, str]（恰两个非空 ID——换位双判定义即两 judge；Fleiss'κ 多 judge 场景属 R5.2-third-scorer 范围，本 schema 不覆盖）, `length_debias_check`: "pass"\|"na"+note（R5 第三要件；当前消融无长度去偏执行 → 允许 "na" 但必须带 note 说明）, `scored_artifact`: str（被门禁保护的评分文件相对路径，可解析） } |
| F2 (三分支) | 断言语义 | ① 回执缺失/不可读 → **FAIL exit 1**（g5 C2「缺失 → FAIL」+ 队列原文「缺回执 = 评分无效」）；② schema 违例（字段缺/类型错/judges≠2/scored_artifact 不可解析）→ **FAIL exit 1**；③ κ<0.6 → **SIGNAL**（exit 0，g5 C2 原文「κ<0.6 → SIGNAL」——门禁阈值判断留人工裁决，脚本只暴露数值） |
| F3 (目标数据) | 对哪个目录跑 | 脚本接受 argv[1] = 评分目录（默认 `bench/rubric-v3/ablation`），在其中找 `kappa-receipt.json`。参数化而非硬编码——未来 batch2 新域评分目录可直接复用 |
| F4 (当前真实状态) | 预期输出 | ablation 目录**没有** kappa-receipt.json（g4 S3 实证「未见任何门禁执行回执」）→ 实跑预期 = FAIL exit 1。**这是正确行为**：脚本的职责就是把「κ 门禁 unverified」从人工判断变成机判事实。不为绿而造回执（伪造门禁回执 = 比无回执更严重的审计污染） |

**F1 取舍说明**：g5 C2 只列了四字段（gate_passed/kappa_value/method/judges）。本提案把 `gate_passed` 拆掉——理由：gate_passed 是 kappa_value ≥ 0.6 的派生布尔，存两份 = 未来漂移源（值改了忘改布尔）；改为脚本现场比较 kappa_value 与 0.6 阈值（阈值常量 KAPPA_MIN=0.6 写死在脚本，引用 DRAFT v2 R5）。新增 length_debias_check 与 scored_artifact 两字段 = R5 三要件完整映射 + 回执与被保护对象的绑定（防回执张冠李戴，同 r104 sourcepath 严格模式思路）。此为**提案扩展**，超出 g5 C2 最小集的部分在 04.5 需反方核验是否过度设计。

## 02 研究（一手验证）

```
$ ls bench/rubric-v3/ablation/kappa-receipt.json
ls: No such file or directory          # F4 预期确认：当前无回执
$ grep -n "换位双判\|κ≥0.6" DRAFT-rubric-v3-v2.md
16: ...judge 校准门禁沿用 C3 v3 的 R5（换位双判 + κ≥0.6 + 长度去偏），评分前不过门禁不开评
208: ...κ 在条目层（二值）计算（v2 R-02）
```
门禁三要件（换位双判/κ≥0.6/长度去偏）与条目层二值 κ 口径均有 DRAFT v2 原文锚点，schema 字段与其一一对应，无虚构条款。

## 02.5 对抗核验

| # | 攻击 | 裁决 |
|---|------|------|
| A1 | "F1 拆掉 gate_passed 是擅自改 g5 C2 schema——提案权在 runner 吗？" | **驳回（提案义务明确）**。g5 C2 原文自带「需最小 schema 提案」——schema 不存在，提案是本 goal 的交付物之一，不是越权。拆 gate_passed 的理由（派生量双写漂移）记录在 F1，04.5 再攻一次 |
| A2 | "对真实数据输出 FAIL 就收口，等于给仓库留一个常红脚本——CI 噪音" | **部分成立，接受**。本仓无 CI（ralph loop 手动收口验证），且该 FAIL 是**待办事实的显式呈现**：κ 门禁执行本身挂 P2/R5.2-third-scorer（外部阻塞）。脚本红了 = 提醒「此处有未闭环协议」，与 X5 unverified 登记同功能。若成璐裁定应降级为 SIGNAL，改一行分支即可（回退成本低）——但默认取 g5 C2 原文的 FAIL 语义，不擅自放宽 |
| A3 | "length_debias_check 允许 'na'——那这个字段形同虚设，填 na 就永远过" | **成立（设计上接受）**。当前消融确实没做长度去偏（无第二 judge 可换），强制 "pass" 会逼出假数据；"na"+必填 note = 如实登记缺口。字段的防护价值在未来：一旦有人声称做了去偏，必须写 "pass" 且 method 里能对上。防的是**虚假声明**，不是**真实缺席** |
| A4 | "judges 恰两个写死——Fleiss'κ（≥3 judge）场景来了脚本要改" | **驳回（范围切割明确）**。docstring 显式声明本 schema 覆盖 DRAFT v2 R5 的两 judge 换位双判；≥3 judge Fleiss'κ 属 R5.2-third-scorer 范围（外部阻塞中），届时扩展 judges 为 ≥2 列表 + κ 方法字段区分 Cohen/Fleiss 即可，改动面小 |

## 03 行动表

| # | 行动 | 验证 |
|---|------|------|
| J1 | schema 提案落盘（本文件 F1 节即为提案正文，另在脚本 docstring 内嵌一份机器可读版） | 04 工件引用 |
| J2 | assert-kappa-receipt.py 落地（三分支 + argv 参数化 + KAPPA_MIN=0.6 常量） | 语法检查 + 首跑 |
| J3 | 真实数据实跑：默认 ablation 目录 → 预期 FAIL exit 1（回执缺失） | 输出落盘 04 |
| J4 | 变异测试 M1-M4：/tmp 沙盒——(M1) 合法回执 κ=0.72 → PASS exit 0；(M2) 缺 method 字段 → FAIL；(M3) κ=0.45 → SIGNAL exit 0；(M4) judges 单元素 → FAIL | 四场景行为表 |
| J5 | 冻结面 git status | 仅新脚本 + 工件 |

**01-03 判定：pass（schema 提案完成且每字段有 DRAFT/g5 原文锚点；F4 预期 FAIL 定位为本 goal 的核心产出而非缺陷；A2/A3 边界如实登记，口径封闭）。**