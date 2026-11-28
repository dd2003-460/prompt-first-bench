# N353: HumanEval 原始基准仅包含 Python 语言测试用例 (N=164)，不存在官方的 Java 或 JavaScript 子集；声称的 'Δ_lang 

- **status**: verified
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

HumanEval 原始基准仅包含 Python 语言测试用例 (N=164)，不存在官方的 Java 或 JavaScript 子集；声称的 'Δ_lang ≈ 8%' 差异源于非官方衍生版本 (如 Multilingual HumanEval) 或错误引用，在标准 HumanEval 语境下，非 Python 语言的通过率为 0% 或未定义

## Corrected Claim

HumanEval 原始基准仅包含 Python 语言测试用例 (N=164)，不存在官方的 Java 或 JavaScript 子集；声称的 'Δ_lang ≈ 8%' 差异源于非官方衍生版本 (如 Multilingual HumanEval) 或错误引用，在标准 HumanEval 语境下，非 Python 语言的通过率为 0% 或未定义

## Evidence

[rework-angle r1] 来源[1][2][3]均确认HumanEval包含164个Python编程问题，且未提及官方Java/JS子集，结合常识可知非Python语言在原始基准中无定义，逻辑自洽且来源支持核心事实。

## Search Query

Multilingual HumanEval Java JavaScript pass rate delta
