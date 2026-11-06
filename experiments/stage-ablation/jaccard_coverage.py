#!/usr/bin/env python3
"""D-face: Jaccard coverage of pfb S5 output vs gold tree leaves.

For each gold leaf node, check if the pfb output covers it (keyword match).
Coverage = covered_leaves / total_gold_leaves.
Acceptance: coverage >= 0.70 per D3 quantitative gate.
"""
import re, os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
PFB = os.path.dirname(os.path.dirname(HERE))

def extract_gold_leaves(gold_path):
    with open(gold_path) as f:
        content = f.read()
    leaves = {}
    for line in content.split('\n'):
        m = re.search(r'(N-\d+(?:\.\d+)*).*?(leaf\s+\S+)', line)
        if m:
            node_id = m.group(1).strip()
            desc_start = line.find(node_id) + len(node_id)
            desc_end = line.rfind('leaf')
            desc = line[desc_start:desc_end].strip().strip('|').strip()
            leaves[node_id] = desc
    return leaves

def keyword_match(leaf_desc, output_text):
    """Check if a gold leaf's key terms appear in the pfb output."""
    # Extract meaningful keywords from leaf description
    # Remove numbers and units, keep Chinese terms and English acronyms
    text_lower = output_text.lower()
    
    # Find all CJK phrases (2+ chars) and English acronyms (2+ chars)
    cjk_terms = re.findall(r'[\u4e00-\u9fff]{2,}', leaf_desc)
    eng_terms = re.findall(r'[A-Z][a-zA-Z0-9]{1,}', leaf_desc)
    
    # Also extract key numeric values
    nums = re.findall(r'\d+\.?\d*', leaf_desc)
    
    matched = []
    not_matched = []
    
    for term in cjk_terms:
        if term in text_lower or term in output_text:
            matched.append(term)
        else:
            not_matched.append(term)
    
    for term in eng_terms:
        if term.lower() in text_lower:
            matched.append(term)
        else:
            not_matched.append(term)
    
    # A leaf is "covered" if at least 50% of its key terms are found
    total = len(cjk_terms) + len(eng_terms)
    if total == 0:
        return False, [], []
    ratio = len(matched) / total
    return ratio >= 0.5, matched, not_matched

def compute_coverage(runs_dir, qid, gold_path):
    leaves = extract_gold_leaves(gold_path)
    results = {}
    
    for f in sorted(os.listdir(runs_dir)):
        if not f.endswith('.json'): continue
        full = os.path.join(runs_dir, f)
        with open(full) as fh:
            data = json.load(fh)
        
        if data.get('qid') != qid: continue
        rep = data.get('rep', '?')
        output = data.get('output_text', '')
        
        covered = 0
        details = {}
        for nid, desc in leaves.items():
            is_covered, matched, not_matched = keyword_match(desc, output)
            details[nid] = {
                'desc': desc[:50],
                'covered': is_covered,
                'matched': matched[:5],
                'missing': not_matched[:5]
            }
            if is_covered:
                covered += 1
        
        coverage = covered / len(leaves) if leaves else 0
        results[f'{qid}-r{rep}'] = {
            'coverage': round(coverage, 4),
            'covered': covered,
            'total': len(leaves),
            'details': details
        }
    
    return results

if __name__ == '__main__':
    runs_dir = sys.argv[1] if len(sys.argv) > 1 else 'runs-d-face'
    gold_q6 = os.path.join(PFB, 'bench/rubric-v3/ablation/gold-Q6.md')
    gold_q7 = os.path.join(PFB, 'bench/rubric-v3/ablation/gold-Q7.md')
    
    print(f"=== D-face Jaccard Coverage ===")
    print(f"Runs dir: {runs_dir}")
    
    for qid, gold in [('Q6', gold_q6), ('Q7', gold_q7)]:
        print(f"\n--- {qid} ---")
        res = compute_coverage(runs_dir, qid, gold)
        if not res:
            print("  No runs found")
            continue
        for key, val in sorted(res.items()):
            status = "✅ PASS" if val['coverage'] >= 0.70 else "❌ FAIL"
            print(f"  {key}: {val['coverage']:.3f} ({val['covered']}/{val['total']}) {status}")
            
            # Show missed leaves
            missed = [nid for nid, d in val['details'].items() if not d['covered']]
            if missed:
                print(f"    Missed: {', '.join(missed[:8])}{'...' if len(missed)>8 else ''}")
    
    # Summary
    all_covs = []
    for qid, gold in [('Q6', gold_q6), ('Q7', gold_q7)]:
        res = compute_coverage(runs_dir, qid, gold)
        for key, val in res.items():
            all_covs.append(val['coverage'])
    
    if all_covs:
        import statistics
        mean = statistics.mean(all_covs)
        print(f"\n=== Overall ===")
        print(f"Mean coverage: {mean:.3f} (n={len(all_covs)})")
        print(f"D3 gate (≥0.70): {'PASS ✅' if mean >= 0.70 else 'FAIL ❌'}")