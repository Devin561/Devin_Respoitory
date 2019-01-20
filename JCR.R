library(rvest)
library(xml2)
library(stringr)
##gsub, str_replace_all
url= 'http://www.medsci.cn/sci/submit.do?id=1fc16885'
fit<- try(web<- read_html(url), silent = TRUE)##∂¡»°Õ¯¬Áhtml
if(F){
  save(web, url, file = 'omictools.Rdata')
  rm(list = ls())
  load(file = 'omictools.Rdata')
}
if('try-error' %in% class(fit)){
  cat('HTTP error 404\n')
}else{
  h2 <<- web %>% html_nodes('h2') %>% html_text()
  h3 <<- web %>% html_nodes('h3') %>% html_text()
}
Sys.sleep(runif(1,1,2))###≈¿≥Ê∑¿±ª∫Õ–≥
write.table(h2, 'h2.txt', row.names = F, col.names = F, quote = F)

SPAN<- web %>% html_nodes('sci_span2') %>% html_text()
name1 <- html_nodes(web,'.sci_span2')
name1 = gsub("<span class=\"sci_span2\">","",x=name1)
name = name1[9]
name = gsub("[a-z]","",x=name)
name<- str_replace_all(name, "[^[:alnum:]]", " ")
name<- str_replace_all(name, " ", "")
