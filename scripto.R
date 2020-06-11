
results <- read.table("D:/Bulk data/nightact/guess.txt", quote="\"", comment.char="")
View(results)
names(results)=c("time","r1","r2","r3","r4","r5","day","hour")

summary(results)

R=data.frame()
for (i in 2:6) {R1=results[c(i,7,8)];R1["floor"]=i-1;names(R1)=c("light","day","hour","floor");R=rbind(R,R1)}
attach(R); head(R)

par(mfrow=c(3,2))
for (f in 1:5) {SL=light[floor==f];SH=hour[floor==f];barplot(table(SL,SH),main=paste("floor",f))}
par(mfrow=c(1,1))


library(ggplot2) # plotting package for R
library(tidyverse)
R=as.tibble(R)

summarize(group_by(R,day),m=mean(light))

ggplot(R, aes(x=hour,y=light,colour=floor))+geom_point(size=2, alpha=0.4,colour=floor)+stat_smooth(aes(colour=floor))
 

