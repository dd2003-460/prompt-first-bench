# origin: ai — 阶段 01：目标分解（RV3G3cdx-crossdomain-promptversion-mapping · r153）

## 1. 目标交付物

「题面版本↔gold_nodes 映射表」权威源 + assert-goldrank-crossdomain.py load_batch2 的 C-对照检查，
使「换题面未声明 gold_nodes / 声明与题面版本错配」从静默漏计升级为 fail-loud exit 2。

承接链：r147 M1/M2 docstring↔代码 mismatch 登记 → r150 Y1（键集检查）+Y2（prompt_version C-最小消费：
存在性+非空 str）落地，M1 完整 fail-loud 因「权威源映射表不存在」降级导出本候选（queue L24）。

## 2. 因素分解（正交覆盖）

| # | 因素 | 边界 | 已知/可推导/待研究 |
|---|------|------|--------------------|
| F1 | 映射表的 schema 设计 | 顶层结构 / 每条目字段 / 版本标识命名空间 | 待研究（F1a-F1c 子问题） |
| F2 | 既有域（domain1）条目的内容 | prompt_version 值 / gold 清单 / 溯源锚点 | 可推导（仓库内既有事实，见 §3） |
| F3 | 消费规则（load_batch2 对照语义） | 三分支判定 / exit code / 缺省路径行为 | 待研究（§4 空缺 O1-O4） |
| F4 | 样例矩阵扩展 | 正/负样例集合 / 各出口实证 | 待研究（依赖 F1+F3 定稿） |
| F5 | 回归保障 | byte-exact 无参调用 / 十五脚本基线 / 冻结面 | 已知（前序轮次基线协议直接沿用） |

### F1 递归分解
- F1a 条目粒度：一个 (domain, prompt_version) = 一条目？还是 domain 级单条目？
  → 可推导：batch2 场景 = 「第二域 + 某题面版本」，且同域未来可能有 v3 基础题面修订版；
    粒度取 **(domain, prompt_version) 二元组**，domain 作为分组键。
- F1b 版本标识值域：自由 str vs 受控枚举？
  → 待研究 O1（§4）。倾向：映射表本身即受控词表——表内出现的版本 = 合法版本，
    表外版本 = 未知（SIGNAL），无需另设枚举机制（避免双源漂移）。
- F1c gold 清单载体：节点 ID 列表 vs 指向 gold-tree 文件？
  → 可推导：断言消费的是显式 gold_nodes（ID 列表，r150 Y1 键集检查对象），
    对照检查要求逐元素一致 ⇒ 映射表条目必须内联 **gold_nodes: [str]** 完整清单（自包含，
    不引入文件解析依赖）。gold-tree 文件仅作溯源锚点记录（path + commit hash），不作机判输入。

### F3 递归分解
- F3a 三分支语义（预注册，成璐可推翻项挂 04.5）：
  - B1 声明匹配：pe.prompt_version ∈ 映射表 ∧ pe.gold_nodes == 映射表该版本 gold_nodes（顺序敏感？→ O2）⇒ PASS（零输出或 [PASS] 行）
  - B2 版本未知：pe.prompt_version ∉ 映射表 ⇒ **SIGNAL**（exit 0，指名道姓提示「新域/新版本需建表后重跑」）——
    不代裁：runner 无权替数据提供方裁定新域 gold 清单（同 r150 S4 不代裁原则）
  - B3 清单错配：pe.prompt_version ∈ 映射表 ∧ gold_nodes ≠ 映射表清单 ⇒ **FAIL exit 2**（指名道姓：期望 X 实得 Y）
- F3b 缺省路径：pe.gold_nodes 缺失（沿用 GOLD_DOMAIN1）时是否触发对照？
  → 待研究 O3。倾向：**不触发**（r150 Y1 先例「缺省路径零变化」+ 缺省语义 = 同题面冻结，
    由 batch2 目录约定隐含 domain1；但 prompt_version 声明了非 domain1 版本 + 缺省 gold = 潜在错配 → O4）
- F3c 映射表自身 schema 违例（文件损坏/结构错）⇒ exit 2 ERROR fail-loud（同 load_batch2 既有风格）

## 3. 已知条件（仓库内证据，全部带锚点）

| K# | 事实 | evidence |
|----|------|----------|
| K1 | domain1 gold strict 清单 = ["N-2.1","N-3.2.2","N-2","N-4","N-1.3"]（五处独立落盘一致） | assert-goldrank-threshold.py L25 / assert-gmr-recompute.py L13 / assert-o3-claim-rejudge.py L22 / rejudge/sample-plan.json gold_strict_nodes / AUDIT-report.md L100「r71b 冻结」 |
| K2 | gold 清单冻结事件 = r71b commit ed552c4（口径核对含 N-4/N-1.3） | git log ed552c4 message + AUDIT-report.md L100 |
| K3 | 变体矩阵冻结规则 B10：所有变体共用同一 v3 基础题面；无 diff 记录的变体不得开跑；V0 须同批次重跑 | DRAFT-rubric-v3-v2.md §3.2 L180/L184 |
| K4 | 冻结语义 = 收口 commit 61416b4 的 DRAFT-rubric-v3-v2.md 快照（D1=L219-L236 / D2=L154-L161 行号回填） | revision-log-batch1.md R-10 回填状态节 |
| K5 | 当前 ablation 面题面 = prompt-V0.txt（C9-plain 档，无引导 baseline），TASK-ablation.md 明示 runs-C0-* 用同一 prompt | TASK-ablation.md L12 + prompt-V0.txt 存在（md5 5e9459ac…） |
| K6 | prior-estimates.json 无 prompt_version 字段（第一域数据早于 r150 schema 约定）；declared_gold_node_count=35/identified=31 | prior-estimates.json 顶层键枚举 |
| K7 | 第二域题面未落盘（R-10 冻结的是段落 diff 非 gold 清单）——映射表当前只有 domain1 一个域有权威 gold 来源 | queue L24 激活条件原文 + bench/rubric-v3/ablation/batch2/ 目录不存在 |
| K8 | 现有 load_batch2 对 prompt_version 仅做存在性+非空 str 检查（r150 Y2），gold_nodes 键集检查仅显式声明时生效（r150 Y1） | assert-goldrank-crossdomain.py L228-235 |
| K9 | 七方案合成与 (a)/(b) 判定不消费 gold 清单之外的题面信息 —— 对照检查纯前置门禁，不改判定层 | 脚本 main() 结构 |

## 4. 空缺清单（无法假定，阻塞对应后续判断）

| O# | 空缺 | 阻塞 | 处置 |
|----|------|------|------|
| O1 | domain1 既有 run（runs-C0-*）实际使用的题面在 v3 变体矩阵中的归属：C9-plain 是 V0-baseline 的前身（L1 旧题面，#27 裁定只作外部参照）还是独立的 pre-v3 版本？ | 映射表 domain1 条目应登记几个 prompt_version | 保守口径：登记为独立版本 `pre-v3/C9-plain`（v3 矩阵未开跑、无 run 使用过任何 v3 变体题面——K5/K7 实证）；V0-V3-sham 六变体条目以「未开跑·占位」形态预注册 gold 清单 = domain1 gold（B10 同题面规则 K3 的直接推论），标注 status=pending-run。矛盾登记挂 04.5 + APPROVALS（若成璐认为 C9-plain 不应入表） |
| O2 | gold_nodes 一致性判定顺序敏感 vs 集合相等？ | B1/B3 分支实现 | 倾向 **排序后集合相等**（gold 清单无语义顺序——gmr/top10 计数均按权重排序消费，清单顺序零消费；顺序敏感会把等价声明误杀为 FAIL，fail-safe 方向反向）。挂 04.5 攻击项 |
| O3 | 缺省 gold_nodes（未声明）+ prompt_version 已声明时的对照义务 | F3b 分支 | 保守口径：缺省 = 不触发清单对照（沿用 r150 Y1 缺省零变化先例），但若声明版本 ≠ 该 domain 缺省绑定版本则 SIGNAL（提示「建议显式声明 gold_nodes」）。挂 04.5 |
| O4 | 映射表放哪个目录/文件名？ | F1 落盘位置 | 可推导：bench/rubric-v3/ablation/prompt-version-gold-map.json（与 batch2/ 约定目录同级，load_batch2 可直接引用；不进 scripts/ 防与断言脚本混淆）。无实质二义性，直接执行 |
| O5 | 第二域（batch2）条目何时建？ | 映射表完整性 | 不代裁：batch2 数据到来时由 RV3G3-batch2-arrival-closure 同批建表（queue L24 联动条款原文）；本 goal 只在映射表留 _schema 说明 + domain1 实例 |

## 5. 阶段 02 研究入口（第一批行动）

1. 逐字取证 K1-K9 锚点（Read/grep，byte-exact 摘录入 02 工件）——已完成大半（§3 即取证结果），02 补 K4 冻结快照 diff 核验。
2. 映射表 schema 草案三选一对照（内联 gold 清单 / 引用文件 / 混合）——F1c 已收敛到内联，02 做反方检验。
3. 消费规则三分支 × 缺省路径的真值表穷举（8 组合：{声明版本∈表,∉表,缺失}×{gold 声明,缺省}）——02 落真值表，03 转动作。
4. 失败备用路径：若 O1 保守口径被 04.5 证伪 → 映射表退化为「仅 pending 占位 + 消费规则文档」，对照检查整体延后一轮（降级不阻塞）。

## 6. 判定
分解完成：叶子原子（F1a-F1c/F3a-F3c）、空缺全登记（O1-O5）、02 入口可直接开始。
候选集冻结：映射表条目集合 = {domain1/pre-v3-C9-plain(既有), domain1/v3-V0..V3-sham(占位×6)}，后续增删须 02 显式记录。
