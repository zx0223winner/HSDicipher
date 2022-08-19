import os
import sys

if len(sys.argv)!=4: #if the input arguments not 4, showing the usage.
    print("Usage:python3 HSD_Statistics.py <path to HSD species folder> <format of HSD file. e.g., 'txt' or 'tsv'> <output file name. e,g. species_stat.tsv>")
    sys.exit()

root = sys.argv[1]
folder = os.listdir(root)
folder.sort()
result_list = []
for file in sorted(folder):
    file_paths = os.path.join(root, file)
    if not os.path.isdir(file_paths) and file.split('.')[-1] == sys.argv[2]:
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
        precision = round(true_positive*100/hsd,2)
        score = round((true_positive+hsd-space)/(false_positive+1),2)
        gene_list_non_repeat = list(set(gene_list))
        result_list.append(".".join(file.split('.')[:-1]) + '\t' + str(hsd) + '\t' + str(len(gene_list_non_repeat)) +
                           '\t' + str(len(gene_list)) + '\t' + str(true_positive) + '\t' + str(space) + '\t' +
                           str(false_positive) + '\t' + str(precision) + '\t' + str(score))
with open(os.path.join(root, sys.argv[3]), 'w') as out:
    out.write("File_name\tCandidate_HSDs#\tNon-redundant_gene_copies#\tGene_copies#\tTrue_HSDs#\tSpace#\tIncomplete_HSDs#\tCapturing_value\tPerformance_score\n")
    for r in result_list:
        out.write(r + '\n')

#file.split('.')[0]
#".".join(file.split('.')[:-1])