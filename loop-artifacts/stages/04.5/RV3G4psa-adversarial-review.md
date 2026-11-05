# 04.5 反方复核 — RV3G4-prior-source-assert（r130 · 2026-10-30）

> verdict: **pass**（7 项攻击：5 败 / 2 部分成立已登记，无实质缺陷）

## 攻击清单与裁定

| # | 攻击 | 裁定 |
|---|------|------|
| A1 | 「provenance 块是自我声明——Lead 自己写『我有两个独立源』，机判全绿但独立性是叙事不是事实」 | **部分成立**——承认：脚本验证的是「登记的来源可定位、可追溯、数量达标」，不是「历史估计过程真实独立发生」。缓解三层：(a) blind-reestimate 条目 judge_id 与 judge-blindtest-r1.json:judge byte-exact + artifact 必须真实存在——伪造需要同时造一个内容一致的 blindtest 文件，成本远超直接跑一次盲估；(b) note 显式声明 family-independent: false，不粉饰；(c) 真正的独立性闭环 = rubric-v3 遗留 #1（≥3 独立 LLM 服务盲测 p̃），本 goal 是它的前置机械化。残余风险登记 R5 |
| A2 | 「signal-only 让『PASS』成为误导符号——下游看到 assert PASS 就引用『p̃ 双源独立已验证』」 | **败**——输出首行强制打印「SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict」+ RESULT 行同样带标注；g4 文档 L100 更新文案明确写 signal-only 边界；provenance.note 三处声明语义边界。误读需要同时无视四处显式标注 |
| A3 | 「prior-estimates.json 的 json.dumps indent=2 重写可能改变既有字段的序列化形态（键序/空格/Unicode 转义），冻结件 diff 超出『纯新增』声明」 | **败**——git diff --stat 实测 +17/-1：+17 = p_tilde_provenance 块 17 行，-1 = 文件尾换行规范化。json 模块 round-trip 保持插入序（Python dict 有序），既有键序不变；ensure_ascii=False 与原文件中文直写一致。消费侧回归 assert-w2-formula.py + assert-w3w4-recompute.py 双双 exit 0 提供数值层证明 |
| A4 | 「N_MIN=2 且两源同族，这个 assert 对当前数据零增量信息——本来就知道只有 Qwen 一个家族」 | **部分成立**——对**当前**数据确实如此（已知事实的机判固化）。价值在三个前瞻场景：(a) 未来任何单源 prior 文件（比如 batch2 新域重估只跑了一个 judge）会被拒收，而不是无声通过——这正是 S3 降档教训要防的；(b) 盲性漂移检测：blindtest 文件被换源而不更新 provenance 时 FAIL（02.5 A5 论证过这是期望行为）；(c) 为遗留 #1 的 ≥3 异族标准预留升级路径（改 N_MIN 常量 + 加家族字段即可）。零增量 ≠ 负价值，防护力体现在未来而非现在 |
| A5 | 「APPROVALS.md 登记后 runner 自行执行 = 自我审批，登记形同虚设」 | **败**——登记的目的不是阻止执行（那是红线操作才有的效力），而是**留痕 + 给成璐可审计的决策点**：APPROVALS 条目写明理由/影响面/回退方式，成璐可 revert 单 commit 推翻。runner 硬规则原文是「要改必须开新文件 + APPROVALS.md 登记」——登记义务已履行；「开新文件 vs 原文件追加」是处置选择，02.5 A2 已论证原文件追加更优（避免元数据二义性）。若成璐裁定应走新文件路径，revert 成本低（单 commit） |
| A6 | 「artifact 用仓库相对路径——prior-estimates.json 的 primary artifact 指向自己，而 blindtest 指向 sibling 文件；未来 ablation/ 目录重组（改名/移动）两条 artifact 都断，脚本 FAIL 变成维护税」 | **败**——断链即 FAIL 是期望行为：provenance 的语义就是「这些 p̃ 值来自这两个具体文件」，文件移动 = 来源定义变化 = 必须重新登记。维护税是真实的但很小（改两行字符串 + 重跑脚本），且方向正确——静默断链才是审计灾难。对比选项「按内容 hash 引用」会把脚本复杂度推高一个量级，边际收益低 |
| A7 | 「note 里写『primary = Lead 主会话 qwen3.8-27b』——但 prior-estimates.json 落盘时的 Lead 模型未必是 qwen3.8-27b（工作区模型配置可变），这是未经验证的事实断言」 | **败（措辞层面已自限）**——note 的家族声明针对的是**当前可核实的环境事实**（本工作区模型配置 = qwen3.8-27b，blindtest judge 字段自声明同模型）；primary 的 judge_id 字段用的是角色描述「lead-main-session (original judge, TASK-ablation.md L27)」而非模型名，模型归属只在 note 里作为家族隔离判断的依据陈述。若未来发现落盘时模型不同，note 修订即可（provenance 块本就是活文档，assert 不锁 note 文本） |

## 数字层独立重算

- prior-estimates.json 顶层键数：10 → 11（+p_tilde_provenance）✓
- nodes 键数：35（不变）✓
- independent_sources 条数：2；judge_id 去重数：2 ≥ N_MIN=2 ✓
- blind-reestimate judge_id == judge-blindtest-r1.json:judge：byte-exact True（python == 验证）✓
- assert-prior-source.py：exit 0，8/8 PASS ✓
- 变异测试 M1-M4：全部 exit 1 + 恢复后 exit 0 ✓
- 消费侧回归：assert-w2-formula.py exit 0 + assert-w3w4-recompute.py exit 0 ✓
- git diff --stat prior-estimates.json：+17/-1（纯新增块 + 尾换行）✓

## 定性结论核对

- G4 导出授权链完整：g4-vulnerability-crosscheck.md L100 候选原文 → queue 条目 → 本 goal ✓
- signal-only 边界四处显式声明（脚本 header/输出行/g4 文档/provenance note）✓
- 家族隔离事实不粉饰：family-independent: false 落盘 ✓
- 冻结数据修改走 APPROVALS 登记路径 + 回退方式声明 ✓
- 其他冻结件（judge-blindtest/hit-matrix/stats-*/gold-tree）零修改 ✓

## verdict

**pass**——无实质缺陷；A1/A4 两项部分成立已登记（R5 残余风险 + 前瞻价值说明），不阻塞收口。
