import os
import sys

root = sys.argv[1]
folder = os.listdir(root)
folder.sort()
result_list = []
for file in sorted(folder):
    file_paths = os.path.join(root, file)
    if not os.path.isdir(file_paths) and file.split('.')[-1] == 'txt':
        false_positive = 0
        space = 0
        hsd = 0
        score = 0
        gene_list = []
        with open(file_paths, 'r') as f:
            lines = f.readlines()
            for line in lines:
                items = line.split('\t')
                if len(items) > 4:
                    is_space = True
                    domain_list = items[4].split('; ')
                    cur_domain = domain_list[0].split(', ')
                    for domain in domain_list:
                        temp_domain = domain.split(', ')
                        if not sorted(temp_domain) == sorted(cur_domain):
                            false_positive += 1
                            break
                        if not domain == "":
                            is_space = False
                    if is_space:
                        space += 1
                    hsd += 1
                    gene_list += items[1].split('; ')
        true_positive = hsd-false_positive
        precision = true_positive*100/hsd
        score = (true_positive+hsd-space)/(false_positive+1)
        gene_list_non_repeat = list(set(gene_list))
        result_list.append(".".join(file.split('.')[:-1]) + '\t' + str(hsd) + '\t' + str(len(gene_list_non_repeat)) +
                           '\t' + str(len(gene_list)) + '\t' + str(true_positive) + '\t' + str(space) + '\t' +
                           str(false_positive) + '\t' + str(precision) + '\t' + str(score))
with open(os.path.join(root, 'result.tsv'), 'w') as out:
    out.write("name\tHSD\tGene-non-repeat\tGene-num\tTP\tSpace\tFP\tPrecision\tScore\n")
    for r in result_list:
        out.write(r + '\n')

#file.split('.')[0]
#".".join(file.split('.')[:-1])