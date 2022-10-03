
### 1. HSDecipher
Custom Python scripts packages for the downstream comparative genomics analysis of highly similar duplicates data

### 2. What's HSDecipher?
The software implementation was written in Python 3 using the following custom scripts and platforms: HSD_statistics.py, HSD_categories.py, HSD_add_on.py, HSD_batch_run.py and HSD_heatmap.py

```
# HSD_statistics.py
python3 HSD_Statistics.py <path to HSD species folder> <format of HSD file. e.g., 'txt' or 'tsv'> <output file name. e,g. species_stat.tsv>
```
>HSD_statistics.py is a custom python script that calculating the statistics of HSDs via using a variety of HSDFinder thresholds. The output file will be written in a table with the header: File name; Candidate_HSDs#; Non-redundant_gene_copies#; Gene_copies#; True_HSDs# ;Space# ;Incomplete_HSDs#; Capturing_value; Performance_score;

```
#HSD_categories.py
python3 HSD_categories.py <path to HSD species folder> <format of HSD file. e.g., 'txt' or 'tsv'> <output file name. e,g. species_groups.tsv>

```
>HSD_categories.py a custom python script that counts the number of HSD with 2, 3, and more than 4 categories, which is helpful to evaluate the distribution of HSDs groups. 


```
#HSD_add_on.py
python3 HSD_add_on.py  -i <inputfile> -a <adding_file> -o <output file>
```
>HSD_add_on.py can add the later HSD data on the former HSD, in this way, the HSD canadiate categories can be enlarged. For example, HSDs identified at a threshold of 90%_30aa were added on to those identified at a threshold of 90%_10aa (denoted as “ 90%_30aa+90%_10aa”); any redundant HSDs candidates picked out at this combo threshold were removed if the more relaxed threshold (i.e., 90%_30aa) had the identical genes or contained the same gene copies from the stricter cut-off (i.e., 90%_10aa).


```
#HSD_batch_run.py
python3 batch_run.py -i <inputfolder>
```
> HSD_batch_run.py can do a series of combination thresholds at once. To minimize the redundancy and to acquire a larger dataset of HSD candidates, we processed each selected species with the following combination of thresholds: E + (D + (C + (B +A))). Any HSDs candidates pinpointed at the combo threshold (90%_30aa+90%_10aa) were removed if the minimum gene copy length was less than half of the maximum gene copy length for each HSD, or if HSD candidates had gene copies with incomplete conserved domains (i.e., different number of Pfam domains). After filtering the combo threshold at (90%_30aa+90%_10aa), we added on a more relaxed threshold 90%_50aa (i.e., 90%_50aa+(90%_30aa+90%_10aa)) and then carried out the same HSD candidate removal/filtering process.

>A = 90%_100aa+(90%_70aa+(90%_50aa+(90%_30aa+90%_10aa)))

>B = 80%_100aa+(80%_70aa+(80%_50aa+(80%_30aa+80%_10aa)))

>C = 70%_100aa+(70%_70aa+(70%_50aa+(70%_30aa+70%_10aa)))

>D = 60%_100aa+(60%_70aa+(60%_50aa+(60%_30aa+60%_10aa)))

>E = 50%_100aa+(50%_70aa+(50%_50aa+(50%_30aa+50%_10aa)))

```
#HSD_heatmap.py
python3 HSD_heatmap.py -f <HSD file folder> -k <KO file folder> -r <width of output heatmap> -c <length of output heatmap>
```
HSD_heatmap.py is able to visualize the collected HSDs in a heatmap and compare the HSDs sharing the same pathway function. This can be done inta-specise and inter-speies heatmaps. Pleas find the example reuslts in the Heatmap Folder.


### 3.Limitation
There is a possible steep learning curve for users with limited knowledge of bioinformatics, especially for those who are not familiar with the basic command lines and dash shell in a Linux/Unix environment. We do hope to further develop the tool, making it more user friendly, including trying to remove some of the middle steps. Unfortunately, we are not yet able to provide a “one-click solution” because of the incompatibility of the various data source employed by the tool. That said, we still believe that our tool is comparatively easier to use than some of the other options currently available to scientists. Indeed, presently there are very few tools that can proceed for the downstream comparative genomics of highly similar duplicate gene data. Thus, we believe that our pipeline will provide a well-needed service to the bioinformatics and genomics community.

But due to the limitation of this strategy, it should be noted that there are some large groups of HSD candidates in the database that likely diverged in function from one another. In the database, those putatively diverged HSD groups were labelled as “candidate HSDs” and a warning note was added to suggest users should proceed with caution when working with these types of datasets.

### 4. Reference
1. Xi Zhang, Yining Hu, Zhengyu Cheng, John M. Archibald (2022). HSDecipher: A pipeline for comparative genomic analysis of highly similar duplicate genes in eukaryotic genomes. StarProtocols. doi:upcoming
2. Zhang, X., Hu, Y. & Smith, D. R. 2022. HSDatabase - a database of highly similar duplicate genes from plants, animals, and algae. Database, doi:http:// 10.1093/database/baac086.
3. Zhang, X. & Smith, D. R. 2022. An overview of online resources for intra-species detection of gene duplications. Frontiers in Genetics, http://doi: 10.3389/fgene.2022.1012788.
4. Xi Zhang, Yining Hu, David Roy Smith. (2021). HSDFinder: a BLAST-based strategy to search for highly similar duplicated genes in eukaryotic genomes. Frontiers in Bioinformatics. doi: http://10.3389/fbinf.2021.803176
5. Xi Zhang, Yining Hu, David Roy Smith. (2021). Protocol for HSDFinder: Identifying, annotating, categorizing, and visualizing duplicated genes in eukaryotic genomes DOI: https://doi.org/10.1016/j.xpro.2021.100619
6. Xi Zhang, et.al. David Roy Smith (2021). Draft genome sequence of the Antarctic green alga Chlamydomonas sp. UWO241 DOI:https://doi.org/10.1016/j.isci.2021.102084

### 5. Contact
Usage of this site follows AWS’s Privacy Policy. © Copyright (C) 2021
