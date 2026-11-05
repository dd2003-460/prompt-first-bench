# 阶段 03 — RV3G3cdx-closure-checklist-assert 动作分解（补记）

| # | 动作 | owner | 依赖 | 产出/验收 |
|---|------|-------|------|-----------|
| A1 | 脚本落盘 `bench/rubric-v3/ablation/scripts/assert-closure-checklist.py`（三项检查 + exit 三分支 + docstring 预注册判定语义 byte-stable） | agent | - | 文件存在；docstring 含 (a)(b)(c) 规则全文与豁免子句 |
| A2 | 正样例实跑 ×3（16b063f / 0bb55ce / 9f48d94，各自真实 goal 短名） | agent | A1 | 全 PASS exit 0 |
| A3 | 负样例构造 ×2（独立分支 tmp/closurecheck-neg-samples：N1 漏翻复刻 / N2 幻影候选）+ 实跑 | agent | A1 | 全 FAIL exit 1，FAIL 行指名道姓 |
| A4 | exit 2 路径实证（不存在 hash / 无 queue diff commit） | agent | A1 | exit 2 + [ERROR] 信息 |
| A5 | 冻结面零修改核验 + 七脚本回归基线维持 | agent | A1-A4 | git status 冻结文件 0 diff；既有脚本 exit 序列不变 |
| B4 | **预注册不执行**：接入门禁（pre-commit hook / CI）——本轮只交付工具，避免改变所有后续收口行为；接入 = 未来独立 goal | user(裁定) | A1 | 登记不阻塞 |