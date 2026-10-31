for f in ['ppl-mandiri-siklus1.html', 'ppl-mandiri-siklus2.html', 'ppl-mandiri-siklus3.html', 'ppl-mandiri-siklus4.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'data-lucide="youtube"' in c:
        print(f'Found data-lucide="youtube" in {f}')

