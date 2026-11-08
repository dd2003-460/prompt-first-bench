"""Rule-hybrid scoring prototype (2026-11-08).

Architecture: LLM classifies level (coarse) + code verifies intra-level evidence (fine).
If code check fails for claimed level, downgrade one level.

Status: PROTOTYPE — only pt5 (nat) implemented. Not yet deployed to production.
Priority: LOW until n expands to ~500/arm. Current n=25-30 doesn't need sub-level resolution.

Usage:
    from rule_hybrid_prototype import score_pt5_hybrid
    level, intra, score = score_pt5_hybrid(answer_text)
"""
import re
from ablation_harness import call_llm

def _llm_classify_level(ans: str) -> int:
    """Ask LLM to classify which level the answer reaches (0-4)."""
    prompt = f'''你是严格评分员。判断下面回答在"驻留时间推导"这个得分点上达到了第几层。只输出整数。

层级（从低到高）：
  L0: 完全未提及驻留时间/residence time/停留时间
  L1: 提到概念但无量化
  L2: 给出量级估计（有具体数字：天/小时）
  L3: 与访问间隔做了显式对比（数量级差异/倍数/vs）
  L4: 推导出折扣因子并给出数值（代入了题面参数）

规则：拿不准往低判。仅提概念=L1，给数字没对比=L2，对比没公式=L3，有公式且代入了具体参数值=L4。

候选回答：
{ans[:12000]}

只输出 JSON：{{"level": N}}（N=0,1,2,3,4）。不要解释。'''
    content, _ = call_llm(prompt, max_tokens=50, temperature=0)
    m = re.search(r'(\d)', content)
    return max(0, min(4, int(m.group(1)) if m else 0))

def _code_verify_level(ans: str, claimed_level: int) -> bool:
    """Deterministic check: does the answer contain evidence for the claimed level?"""
    a = ans.lower()
    l1_pat = r'(residence\s*time|驻留时间|平均停留|停留时间|平均驻留|residency)'
    
    if claimed_level <= 1:
        return bool(re.search(l1_pat, a))
    if claimed_level == 2:
        pats = [
            r'(residence\s*time|驻留时间|停留时间|t_res).{0,80}\d+[\.\d]*\s*(天|日|周|月|年|day|week|month|year|小时|hour|h\b)',
            r'\d+[\.\d]*\s*(天|日|周|月|年|day|week|month|year|小时|hour|h\b).{0,80}(residence\s*time|驻留时间|停留时间|t_res)',
            r't_res.{0,30}\d+[\.\d]*\s*(天|日|day|week|月|month)',
        ]
        return any(bool(re.search(p, a, re.I)) for p in pats)
    if claimed_level == 3:
        pats = [
            r'(residence\s*time|驻留时间|停留时间|t_res).{0,150}(访问间隔|access\s*interval|请求间隔).{0,150}(远大|相差|数量级|倍|vs|对比|≫|<<|远小|orders)',
            r'(访问间隔|access\s*interval|请求间隔).{0,150}(residence\s*time|驻留时间|停留时间|t_res).{0,150}(远小|相差|数量级|倍|vs|对比|≫|<<|orders)',
            r'(residence\s*time|驻留时间|停留时间|t_res).{0,100}(≫|<<|>>|远大于|远小于|个数量级|orders\s*of\s*magnitude)',
        ]
        return any(bool(re.search(p, a, re.I)) for p in pats)
    if claimed_level == 4:
        has_formula = bool(re.search(r'(折扣因子|discount\s*factor|p_stale|stale\s*prob|过期概率|失效概率|1\s*[-−]\s*e?xp|e?\^?\s*\(\s*-\s*u)', a, re.I))
        has_value = bool(re.search(r'(≈|=\s*)\s*0\.\d+|\d+\.\d+\s*%', a, re.I))
        # STRICT: must have formula AND value AND at least one parameter substitution
        has_params = bool(re.search(r'(u\s*[=≈]?\s*\d|λ\s*[=≈]?\s*\d|lambda\s*[=≈]?\s*\d|α\s*[=≈]?\s*\d|T_res\s*[=≈]?\s*\d)', a, re.I))
        return has_formula and has_value and has_params
    return False

def _intra_level_score(ans: str, level: int) -> float:
    """Fine-grained interpolation within the verified level."""
    a = ans.lower()
    if level == 1:
        count = len(re.findall(r'(residence\s*time|驻留时间|平均停留|停留时间|平均驻留|residency)', a))
        return 0.3 if count == 1 else 0.5
    if level == 2:
        nums = re.findall(r'\d+[\.\d]*\s*(天|日|周|月|年|day|week|month|year|小时|hour)', a, re.I)
        return 0.5 + min(0.3, 0.1 * len(nums))
    if level == 3:
        has_ratio = bool(re.search(r'(\d+[\.\d]*)\s*(倍|x|×)|ratio.{0,20}\d+', a, re.I))
        return 0.5 + (0.3 if has_ratio else 0.1)
    if level == 4:
        has_params = bool(re.search(r'(u\s*[=≈]?\s*\d|λ\s*[=≈]?\s*\d|lambda\s*[=≈]?\s*\d|α\s*[=≈]?\s*\d)', a, re.I))
        return 0.7 + (0.2 if has_params else 0.0)
    return 0.0

def score_pt5_hybrid(ans: str) -> tuple:
    """Hybrid: LLM classifies + code verifies. Returns (level, intra, final_score)."""
    claimed = _llm_classify_level(ans)
    
    # Verify; if fails, downgrade
    level = claimed
    while level > 0 and not _code_verify_level(ans, level):
        level -= 1
    
    intra = _intra_level_score(ans, level)
    score = min(1.0, (level - 1 + intra) / 3.0) if level > 0 else 0.0
    return level, round(intra, 2), round(score, 3)

if __name__ == '__main__':
    import json, glob, statistics
    for arm, runs_dir in [('S0','runs-prod'), ('A4','runs-prod')]:
        scores = []
        for rep in range(1, 31):
            fp = f'{runs_dir}/{arm}-nat-r{rep}.json'
            try: d = json.load(open(fp))
            except: continue
            _, _, sc = score_pt5_hybrid(d['answer'])
            scores.append(sc)
        print(f'{arm}-nat pt5: mean={statistics.mean(scores):.3f}±{statistics.stdev(scores):.3f}, distinct={len(set(scores))}')
