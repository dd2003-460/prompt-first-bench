# 阶段 04 执行验证 — RV3G4-kappa-receipt-assert

> origin: ai · 2026-10-30 · 对象 `bench/rubric-v3/ablation/scripts/assert-kappa-receipt.py`（新建，唯一代码改动）

## J1 schema 提案

落盘于 01 工件 F1 节 + 脚本 docstring 内嵌机器可读版。字段集 = g5 C2 四字段的改造映射：

| g5 C2 原字段 | 本提案处置 | 理由锚点 |
|---|---|---|
| gate_passed | **删除**（派生量双写 = 漂移源；阈值判断由脚本现场执行 KAPPA_MIN=0.6） | DRAFT v2 R5 阈值原文 |
| kappa_value | 保留（float ∈ [0,1]，条目层二值口径） | DRAFT v2 R-02 |
| method | 保留（非空 str） | g5 C2 |
| judges | 保留（恰 2 非空 str；Fleiss'≥3 范围切割声明） | DRAFT v2 R5 换位双判 |
| —（新增）gate | 固定值 "role-swap-dual-judge" | 防方法名混用 |
| —（新增）length_debias_check/note | R5 第三要件映射；"na"+必填 note | DRAFT v2 R5 三要件 |
| —（新增）scored_artifact | 回执与被保护评分文件绑定 | r104 sourcepath 严格模式思路 |

## J2/J3 真实数据实跑（核心产出）

```
$ python3 assert-kappa-receipt.py
target dir : /Users/a1-6/Desktop/workspace/pfb/bench/rubric-v3/ablation
[FAIL] ① kappa-receipt.json exists — not found at …/kappa-receipt.json → 评分无效（R5 门禁无执行回执）
RESULT: FAIL (1 checks failed)
exit 1
```

**这是预期行为而非脚本缺陷**（01 F4 预注册）：g4 S3 人工判断「κ 门禁无执行回执 → unverified」自此变为机判事实——脚本对当前消融面输出 FAIL exit 1，缺口从台账文字变成可重复执行的验证结果。未伪造回执让脚本转绿（伪造门禁回执 = 比无回执更严重的审计污染）。该 FAIL 的闭环路径 = P2 κ 换位双判实际执行（外部阻塞，R5.2-third-scorer 同阻塞源），届时生成真回执后脚本自然转 PASS。

## J4 变异测试（/tmp 沙盒五场景）

| 场景 | 数据 | exit | 行为 |
|---|---|---|---|
| M1 合法回执 κ=0.72 | 全字段合规 | 0 | PASS + SIGNAL「阈值达标」 |
| M2 缺 method | del method | 1 | `[FAIL] ② method non-empty str — got None` |
| M3 κ=0.45 | kappa_value=0.45 | 0 | SIGNAL「阈值未达 [人工裁决]」（不 FAIL——g5 C2 原文三分支） |
| M4 judges 单元素 | judges=["only-one"] | 1 | `[FAIL] ② judges is list of exactly 2…` |
| M5 na 无 note | length_debias_note="" | 1 | `[FAIL] ② length_debias_note required when check='na'` |

三分支语义全部实证：缺失→FAIL / schema 违例→FAIL / 低 κ→SIGNAL(exit 0)。

## J5 冻结面

```
$ git status --short
?? bench/rubric-v3/ablation/scripts/assert-kappa-receipt.py   (新建)
?? loop-artifacts/stages/01/RV3G4kra-stages01-03.md          (工件)
```

hit-matrix.json / prior-estimates.json / gold-tree.md / stats-*.json / judge-blindtest-r1.json 零触碰；**未创建任何 kappa-receipt.json 假数据**。

## web-llm 交叉核验

unverified 降级——三 provider 登录态失效（同族判据，机械改动边际贡献 ≈ 0）。

## 04 判定

pass——五项验收标准全部满足（schema 提案 / 三分支脚本 / M1-M5 变异实证 / 真实数据 FAIL 如实记录且定位正确 / 冻结面零触碰+零伪造）。