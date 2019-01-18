getwd()
setwd("E:/R/Rstudio/project")
install.packages("scholar")
library(scholar)
jn = c("evolution", "methods in ecology and evolution", "Journal of Diabetes Research ","Int J Clin Exp Med"
       "journal of insect science", "molecular biology and evolution")
            
get_impactfactor(jn)

jn <- agrep("plant", scholar:::impactfactor$Journal, ignore.case = T,value = T, max.distance = 0.05)
jn
a<- get_impactfactor(jn)
a<- print(a)
write.csv(a,file = "植物学杂志.doc")
save(b, file="微生物杂志.xlsx")

head(a, n=50)
jn = c("gene","genes","genesis","genome","journal of insect science","current bioinformatics")
get_impactfactor(jn)


library(xlsx)
write.xlsx(a, file = "植物学杂志.xlsx")

insect<- agrep("insect", scholar:::impactfactor$Journal, ignore.case = T, 
               value = T, max.distance = 0.05)
Entomology<- agrep("Entomology", scholar:::impactfactor$Journal, ignore.case = T, 
                   value = T, max.distance = 0.05)
insect_IF<- get_impactfactor(insect)
Entomology_IF<- get_impactfactor(Entomology)
insect_IF1$Journal<- tolower(insect_IF1$Journal) 
Entomology_IF$Journal<- tolower(Entomology_IF$Journal)
insect_journal<- rbind(insect_IF1[1:18,], Entomology_IF[1:43,])

write.xlsx(insect_IF1, "昆虫杂志1.xlsx")
write.xlsx(insect_journal, "insect_journal2.xlsx")

insect_IF1<- insect_IF[-grep("infect",insect_IF$Journal, ignore.case = T),]







