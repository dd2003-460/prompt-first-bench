# Q5 run3 评分 — qwen3.6-plus（V0 裸 prompt，本地降级通道）

> origin: ai
> 评分时间：2026-10-23 06:3x Asia/Shanghai
> 评分人：route B 执行 subagent（**探索性自评**；非正式盲评）
> 评分依据：`rubric/scoring.md` D1–D4（100 分制）
> 评分对象：`q5-run3.md` 答案全文
> 匿名处理：评分时隐藏模型名与通道，仅依据输出内容打分。
> degraded: true（arena 故障，本地通道；执行模型 qwen3.8-27b-w8a16 按档映射 qwen3.6-plus）

## 评分锚点（评分者冻结的 Q5 关键里程碑清单）

Q5 开放调研题（信息论/编码理论），关键里程碑（评分者清单）：
- Nyquist 1924 / Hartley 1928 / **Shannon 1948**（奠基）
- Shannon 率失真（1957-59）
- Elias 卷积码（1955）/ **Viterbi 1967** 算法
- **Gallager 1963 LDPC** / **Berrou 1993 Turbo** / **Arikan 2009 极化码**
- Shannon 1949 保密通信
- 网络信息论（Cover, El Gamal 1970s-80s）
- 量子纠错：Shor 1995 / Gottesman-Steane 1996 / AGP 1999 / 表面码 2012
- 方向选择需有理由 + conf

## D1 正确性（40）

| 检查项 | 结果 |
|--------|------|
| Shannon 1948 BSTJ 27 卷页 | ✓ |
| Viterbi 1967 PTL | ✓ |
| Gallager 1963 LDPC 博士论文 | ✓ |
| Berrou 1993 Turbo | ✓ |
| Arikan 2009 极化码 ISIT | ✓ |
| Gottesman 1997 / AGP 1999 | ✓ |
| 5G 2011 采纳极化码 | ✓ |
| 关键事实错误数 | 0 |
| 无来源关键 claim 数 | 0（关键引用均给出） |

**D1 = 40/40**

## D2 完备性（25）

| 里程碑 | 覆盖 |
|--------|------|
| Nyquist 1924 | ✓ |
| Hartley 1928 | ✓ |
| Shannon 1948 | ✓ |
| Shannon 率失真 1957-59 | ✓ |
| Shannon 1949 保密 | ✓ |
| Elias 卷积码 1955 | ✓ |
| Viterbi 1967 | ✓ |
| Gallager 1963 LDPC | ✓ |
| Berrou 1993 Turbo | ✓ |
| Arikan 2009 极化码 | ✓ |
| 5G 2011 | ✓ |
| 量子纠错全链（Shor/Gottesman/AGP/表面码） | ✓ |
| 网络信息论（Cover/El Gamal） | ✓ |
| 压缩感知 Donoho 2006 | ✓ |
| 漏：Slepian-Wolf 1973（分布式信源编码，网络信息论核心） | ✗ 漏 1 个里程碑（-5） |
| 漏：Wyner-Ziv 1976（率失真带边信息） | ✗ 漏 1 个（-5，次要） |

**D2 = 15/25**（-10：漏 2 个经典里程碑）

## D3 结构正交（20）

- 按时代/主题分 5 块（经典 → 信道编码 → 网络 → 量子 → 现代），分块正交；
- 里程碑表与方向选择分节，无重叠；
- 方向选择有「理由 + conf + 备选」结构，清晰；
- 无冗余。

**D3 = 18/20**（-2：E 块「现代前沿」与前面经典块有少量主题交叠（极化码改进 vs Arikan 2009 已列））

## D4 置信度标注（15）

- 来源：关键引用给出 7 条（Shannon/Viterbi/Gallager/Berrou/Arikan/Gottesman/AGP）✓ 但部分为「多」或类别级（网络信息论、FEC），非全部 claim 有来源
- conf：方向选择有显式 conf（~0.8 / 备选 ~0.65）✓，且说明理由
- 按 rubric 字面：来源覆盖大部分关键 claim + conf 有标注

**D4 = 11/15**（-4：部分 claim 无具体来源，但方向 conf 标注完整）

## 总分

| 维度 | 得分 |
|------|------|
| D1 | 40 |
| D2 | 15 |
| D3 | 18 |
| D4 | 11 |
| **总分** | **84** |

## 判定

**84 ≥ 80 → success**

## 备注

- 探索性自评，非正式盲评。
- D2 扣分主因：开放题的「完整搜集」在本地无网络条件下难以做到真正完整（Slepian-Wolf / Wyner-Ziv 等经典项遗漏）。若 arena 可用 + 实时检索，预计 D2 可回升至 20+。
- 方向选择（极化码）理由充分、conf 明确，是本题亮点。
- 降级说明同 q2/q3/q4-run3。
