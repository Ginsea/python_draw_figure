#!/usr/bin/env python
#coding:UTF-8
import sys
try:
    import numpy as np
except:
    sys.stderr.write("请安装numpy模块")
    sys.exit(1)
try:
    import matplotlib.pyplot as plt
except:
    sys.stderr.write("请安装matplotlib模块")
    sys.exit(1)
import argparse
import os

def opt():
    parse = argparse.ArgumentParser(usage="%(prog)s[options]")
    parse.add_argument("--infile",help="infile with txt format,force,example file in example/test.txt")
    parse.add_argument("--outfile",default="text.png",help="outfile default text.png")
    return parse.parse_args()

def read_file(txt):
    col1 = []
    std1 = []
    col2 = []
    std2 = []
    label = []
    ylabel = ""
    title = ""
    group1 = ""
    gourp2 = ""
    for line in open(txt,"r"):
        if not line.startswith("#"):
            ele = line.strip().split()
            label.append(ele[0])
            col1.append(float(ele[1]))
            std1.append(float(ele[2]))
            col2 .append(float(ele[3]))
            std2.append(float(ele[4]))
        elif line.startswith("#yabel"):
            ylabel += line.strip().split("\t")[1]
        elif line.startswith("#title"):
            title += line.strip().split("\t")[1]
        elif line.startswith("#label"):
            group1 += line.strip().split("\t")[1]
            gourp2 += line.strip().split("\t")[3]
    return col1,std1,col2,std2,label,ylabel,title,group1,gourp2

def draw_png(txt,ous):
    txtc = read_file(txt)
    col1 = txtc[0]
    std1 = txtc[1]
    col2 = txtc[2]
    std2 = txtc[3]
    xlabel = txtc[4]
    ylabel = txtc[5]
    title = txtc[6]
    group1 = txtc[7]
    group2 = txtc[8]
    N = len(col1)
    ind = np.arange(N)
    width = 0.35
    fig = plt.figure()
    ax = plt.subplot(111)
    rects1 = ax.bar(ind,col1,width,color="r",yerr=std1)
    rects2 = ax.bar(ind+width,col2,width,color="b",yerr=std2)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(xlabel)
    ax.legend((rects1[0],rects2[0]),(group1,group2),loc="upper left")

    for rect in rects1:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,'%d'%int(height),ha="center",va="bottom")


    for rect in rects2:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height), ha="center", va="bottom")

    plt.savefig("{0}".format(ous),width=20,height=10)

def main():
    pargs = opt()
    if pargs.infile == None:
        print("This script can be used to figure a bar with error")
        os.system("python {0} -h".format(sys.argv[0]))
        sys.stderr.write("Error:incomplete options")
        sys.exit(1)
    else:
        ins = pargs.infile
    if pargs.outfile == None:
        draw_png(ins,"test.png")
    else:
        draw_png(ins,pargs.outfile)

if __name__ == "__main__":
    main()
