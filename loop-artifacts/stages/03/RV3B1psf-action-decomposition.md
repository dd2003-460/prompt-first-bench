# 阶段 03：行动分解 — RV3B1-prompt-side-freeze

> 依据：02 §2 判断 + 02.5 verdict pass（A1 缓解并入）· 分支 ralph/rv3b1-psf

## 行动表

| # | 行动 | 对象 | 具体改动 | 验证方式 |
|---|------|------|----------|----------|
| A1 | D2 段写入 02.5 附录区 | `loop/prompt-first/02.5-cross-check.md` | 文末新增小节「## 附录 · 冻结件：D2 边界类型声明段（rubric-v3 V0/V3 消融删除对象，非本 loop 规则）」——含来源标注（DRAFT v2 L155-L160 正文 6 行）+ 代码块承载的逐字原文 + 用途说明（prompt 组装脚本读取此副本；权威定义仍在 DRAFT v2） | assert 检查① byte-exact diff |
| A2 | §4.4 新建 V3-sham 替换段 | `bench/rubric-v3/DRAFT-rubric-v3-v2.md` §4.3 之后 | 新增「### 4.4 V3-sham 替换段（等长中性 · R-09 联动）」：主题 = 引用与脚注格式规范（不含边界类型三类语义、不含候选集/搜索语义），代码块内 6 行正文，总字符数与 D2 正文偏差 ≤10% | assert 检查③ 等长机判 |
| A3 | §3.2 加 V3-sham 行 | DRAFT v2 §3.2 变体矩阵表 | V-sham 行后插入一行：「V3-sham \| P4 边界类型声明要求段（D2）整体替换为等长中性引用格式段（§4.4 全文），其余与 V1 相同 \| 控制 D2 删除的长度/格式效应（R-09 联动）」；既有六行零改动 | assert 检查② 定点断言 + 既有行不变断言 |
| A4 | `[batch2: R-09]` 占位符更新 | DRAFT v2 L164 | 「本 goal 不实施，占位防误用」→「边界类型声明段落写入 prompt + V3 sham 化联动已落地（RV3B1-prompt-side-freeze，rXXX）；可观测三问细化仍待 batch2」 | grep 定点 |
| A5 | assert 脚本 | `bench/rubric-v3/ablation/scripts/assert-psf-freeze.py`（新建） | ① 02.5 附录段 == DRAFT v2 L155-L160（byte-exact）；② §3.2 含 V3-sham 行且既有六变体行文本不变；③ §4.4 存在 + 行数 = 6 + 字符偏差 ≤10% + 黑名单（不含「边界类型」「数学/理论边界」「实操边界」「信息边界」「research_required」等 D2 语义 token） | exit 0 + 变异测试 |
| A6 | revision-log 登记 | DRAFT v2 revision-log（或 revision-log-batch1.md 追加节） | R-09 部分落地条目：D2 写入 02.5 + §4.4 + V3-sham 行，commit hash 留收口时回填 | grep |
| A7 | 六阶段工件 | loop-artifacts/stages/{01,02,02.5,03,04,04.5}/ + prompt-first/ | 本文件 + 04 执行日志 + 04.5 反方复核 + per-goal web-llm 回执 | 文件存在性 |

## 明确不做

- 不改 V3-noboundary / V0 / V1 / V1-align / V2 / V-sham 任何既有行（冻结内容零改动）
- 不改 D1 相关任何内容（§4.1/§4.3 原样）
- 不实施「可观测三问细化」（R-09 的另一半，仍留 batch2）
- 不动 `loop/prompt-first/` 下其他阶段文件（只碰 02.5）
- 冻结数据（prior-estimates/judge-blindtest/hit-matrix/stats-*）零修改

## 顺序依赖

A1 → A2 → A3 → A4（文档侧）→ A5（assert 锚定最终文本）→ A6（log 收口）→ A7（04 汇总实跑输出）。