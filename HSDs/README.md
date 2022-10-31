Example of HSDs folder file
--------------------------
HSDFinder generates one output files: 9-column spreadsheet integrating with the information of HSD identifier, gene copies number and Pfam domain.

*Example of the 9-column tab-delimited file:* e.g.,Chlamydomonas_reinhardtii.90_10.txt
```
HSD_identifier  gene_copies AA_length function_type function_identifier function_Description  E-value InterPro_identifier InterPro_description
NP_027422.1	NP_027422.1; NP_849661.1; NP_567636.1	303; 293; 291	Pfam	PF06454; PF06454; PF06454	Protein of unknown function (DUF1084); Protein of unknown function (DUF1084); Protein of unknown function (DUF1084)	5.5E-146; 1.1E-145; 2.1E-143	IPR009457; IPR009457; IPR009457	THH1/TOM1/TOM3 domain; THH1/TOM1/TOM3 domain; THH1/TOM1/TOM3 domain
NP_027543.2	NP_027543.2; NP_001322262.1; NP_001154475.1	606; 603; 684	Pfam	PF03141; PF03141; PF03141	Putative S-adenosyl-L-methionine-dependent methyltransferase; Putative S-adenosyl-L-methionine-dependent methyltransferase; Putative S-adenosyl-L-methionine-dependent methyltransferase	6.2E-75; 5.1E-132; 9.8E-139	IPR004159; IPR004159; IPR004159	Putative S-adenosyl-L-methionine-dependent methyltransferase; Putative S-adenosyl-L-methionine-dependent methyltransferase; Putative S-adenosyl-L-methionine-dependent methyltransferase
```
Column header explanation:
1. `HSD_identifier` Highly Similar Duplicates (HSDs) identifiers: The first gene model of the duplicate gene copies is used as the HSD identifers in default. (e.g. NP_027422.1)
2. `gene_copies` Duplicate gene copies (different genes are seperated by comma)(e.g. NP_027422.1; NP_849661.1; NP_567636.1)
3. `AA_length` Amino acid length of duplicate gene copies (aa)(e.g. 303; 293; 291)
4. `function_type` The protein functional type (e.g., Pfam / PRINTS / Gene3D)
5. `function_identifier` (e.g. PF06454; PF06454; PF06454)
6. `function_Description` (e.g. Protein of unknown function (DUF1084); Protein of unknown function (DUF1084); Protein of unknown function (DUF1084))
7. `E-value` (e.g., 5.5E-146; 1.1E-145; 2.1E-143)
8. `InterPro_identifier` InterPro Entry Identifier (e.g. IPR009457; IPR009457; IPR009457)
9. `InterPro_description` InterPro Entry Description (e.g. THH1/TOM1/TOM3 domain; THH1/TOM1/TOM3 domain; THH1/TOM1/TOM3 domain)
<a name="sec5"></a>
