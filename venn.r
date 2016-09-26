library(VennDiagram)
jpeg(file='test.jpeg',width=700,height=480)
draw.triple.venn(6,6,6,3,4,4,3,cateory = c('name1','name2','name3'),cat.cex=rep(1,3),col=rep('black',3),euler.d = FALSE, scaled = FALSE,lwd=c(3,3,3),fill = rainbow(3))
dev.off()
