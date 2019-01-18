setwd("E:/GEO")
getwd()
phenotype_file<- read.table('TCGA-BRCA.GDC_phenotype.tsv.gz', header = T, sep = ' ',
                            quote = '')
phenotype_file <- read.csv('TCGA-BRCA.GDC_phenotype.csv')
head(phenotype_file)
phenotype_colnames <- as.data.frame(colnames(phenotype_file))
table(phenotype_file$breast_carcinoma_estrogen_receptor_status)##雌激素受体(ER)
table(phenotype_file$breast_carcinoma_progesterone_receptor_status)##黄体酮受体(PR)
table(phenotype_file$lab_proc_her2_neu_immunohistochemistry_receptor_status)## 人类表皮生长因子受体(HER2)
colnames_num<- grep('receptor_status',colnames(phenotype_file))
phenotype_colnames<- colnames(phenotype_file)[colnames_num]
eph<- phenotype_file[,colnames_num[1:3]]

tnbc_rownum<- apply(eph, 1, function(x) sum(x=='Negative'))
tnbc_sample<- phenotype_file[tnbc_rownum==3,1]
save(tnbc_sample,file = 'tnbc_sample.Rdata')


library(readr)
a=read.delim('TCGA-BRCA.htseq_counts.tsv',sep = '\t',header = T,na.strings = "NA")
library(data.table)
a=fread('TCGA-BRCA.htseq_counts.tsv',sep = ' ',header = T)
a=as.data.frame(a)
a[1:4, 1:4]
rownames(a)=a[,1]
a=a[,-1]
genes=rownames(a)
a[1:4,1:4]

a= 2^a-1


load('tnbc_sample.Rdata')
tnbc_p=substring(tnbc_sample, 1,12)
all_p=substring(colnames(a),1,12)
paired_p= names(table(all_p)[table(all_p)==2])
need_p = intersect(tnbc_p, paired_p)
exprSet= a[,all_p %in% need_p]
tmp=apply(exprSet, 1, function(x){
  sum(x==0)<10
})
exprSet=exprSet[tmp,]


save(exprSet,file = 'tnbc_paired_exprSet.Rdata')

Rdata_dir='.'
load(file=file.path(Rdata_dir,'tnbc_paired_exprSet.Rdata'))
dim(exprSet)

group_list=factor(ifelse(as.numeric(substr(colnames(exprSet),14,15))<10, 'tumor','normal'))
table(group_list)
exprSet = ceiling(exprSet)

if(T){
  
  library(DESeq2)
  
  
  
  (colData <- data.frame(row.names=colnames(exprSet), 
                         
                         group_list=group_list) )
  
  dds <- DESeqDataSetFromMatrix(countData = exprSet,
                                
                                colData = colData,
                                
                                design = ~ group_list)
  
  tmp_f=file.path(Rdata_dir,'TCGA-KIRC-miRNA-DESeq2-dds.Rdata')
  
  if(!file.exists(tmp_f)){
    
    dds <- DESeq(dds)
    
    save(dds,file = tmp_f)
    
  }
  
  load(file = tmp_f)
  
  res <- results(dds, 
                 
                 contrast=c("group_list","tumor","normal"))
  
  resOrdered <- res[order(res$padj),]
  
  head(resOrdered)
  
  DEG =as.data.frame(resOrdered)
  
  DESeq2_DEG = na.omit(DEG)
  
  
  
  nrDEG=DESeq2_DEG[,c(2,6)]
  
  colnames(nrDEG)=c('log2FoldChange','pvalue')  
  
}


load(file = 'tnbc_paired_exprSet.Rdata')

load('TCGA-BRCA-mRNA-DEG_results.Rdata')

exprSet[1:4,1:4]

exprSet=log2(edgeR::cpm(exprSet)+1)

pheatmap::pheatmap(exprSet[rownames(head(DESeq2_DEG)),])


if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("DESeq2", version = "3.3")
source("http://bioconductor.org/biocLite.R")
biocLite("BiocManager")
biocLite("DESeq2")
BiocManager::install("DESeq2", version = "3.8")
