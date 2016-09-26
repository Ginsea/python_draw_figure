#!/usr/bin/env python
#coding:UTF-8

import argparse
import sys
import os
import time
global rds
rds= os.getcwd()

def ltime():
    return time.strftime("%H:%M:%S",time.localtime(time.time()))

def opt():
    args = argparse.ArgumentParser(usage="%(prog)s[options]")
    args.add_argument("--ins",help="Input file which format as script head showing")
    args.add_argument("--num",help="The number of classes")
    args.add_argument("--ous",help="Output figure file")
    return args.parse_args()

def loadfile(inf,num):
    tmpdir = {}
    sys.stdout.write("[{0}] Load file \n".format(ltime(),os.path.basename(inf)))
    if num not in [2,3,4,5]:
        exit("[{0}] Error in --num options".format(ltime()))
    elif num == 2:
        list1 =[]
        list2 = []
        name1 = ""
        name2 = ""
        for line in open(inf,"r"):
            ele = line.strip().split("\t")
            if len(ele) < 2:
                exit("[{0}]Error, No two rows in your file\n".format(ltime()))
            if line.startswith("#"):
                name1 += ele[0][1:]
                name2 += ele[1]
            elif not line.startswith("#"):
                try:
                    list1.append(ele[0])
                except IndexError:
                    continue
                try:
                    list2.append(ele[1])
                except IndexError:
                    continue
        if name1 == "" or name2 == "":
            exit("[{0}] The first line should use '#' as the first character".format(ltime()))
        area1 = len(list1)
        area2 = len(list2)
        n12 = len(set(area1) & set(area2))
        tmpdir["area1"] = area1
        tmpdir["area2"] = area2
        tmpdir["n12"] = n12
        tmpdir["name1"] = name1
        tmpdir["name2"] = name2
        return tmpdir
    elif num == 3:
        list1 = []
        list2 = []
        list3 = []
        name1 = ""
        name2 = ""
        name3 = ""
        for line in open(inf,"r"):
            ele = line.strip().split("\t")
            if line.startswith("#"):
                name1 += ele[0][1:]
                name2 += ele[1]
                name3 += ele[2]
            elif not line.startswith("#"):
                try:
                    list1.append(ele[0])
                except IndexError:
                    continue
                try:
                    list2.append(ele[1])
                except IndexError:
                    continue
                try:
                    list3.append(ele[2])
                except IndexError:
                    continue
        area1 = len(list1)
        area2 = len(list2)
        area3 = len(list3)
        n12 = len(set(list1) & set(list2))
        n13 = len(set(list1) & set(list3))
        n23 = len(set(list2) & set(list3))
        n123 = len(set(list1) & set(list2) & set(list3))

        if name1 == "" or name2 == "" or name3 == "":
            exit("[{0}] The first line should use '#' as the first character".format(ltime()))

        tmpdir["area1"] = area1
        tmpdir["area2"] = area2
        tmpdir["area3"] = area3
        tmpdir["n12"] = n12
        tmpdir["n13"] = n13
        tmpdir["n23"] = n23
        tmpdir["n123"] = n123
        tmpdir["name1"] = name1
        tmpdir["name2"] = name2
        tmpdir["name3"] = name3
        return tmpdir
    elif num == 4:
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        name1 = ""
        name2 = ""
        name3 = ""
        name4 = ""
        for line in open(inf,"r"):
            ele = line.strip().split("\t")
            if line.startswith("#"):
                name1 += ele[0][1:]
                name2 += ele[1]
                name3 += ele[2]
                name4 += ele[3]
            elif not line.startswith("#"):
                try:
                    list1.append(ele[0])
                except IndexError:
                    continue
                try:
                    list2.append(ele[1])
                except IndexError:
                    continue
                try:
                    list3.append(ele[2])
                except IndexError:
                    continue
                try:
                    list4.append(ele[3])
                except IndexError:
                    continue

        tmpdir["area1"] = len(list1)
        tmpdir["area2"] = len(list2)
        tmpdir["area3"] = len(list3)
        tmpdir["area4"] = len(list4)
        tmpdir["n12"] = len(set(list1) & set(list2))
        tmpdir["n13"] = len(set(list1) & set(list3))
        tmpdir["n14"] = len(set(list1) & set(list4))
        tmpdir["n23"] = len(set(list2) & set(list3))
        tmpdir["n24"] = len(set(list2) & set(list4))
        tmpdir["n34"] = len(set(list3) & set(list4))
        tmpdir["n123"] = len(set(list1) & set(list2) & set(list3))
        tmpdir["n124"] = len(set(list1) & set(list2) & set(list4))
        tmpdir["n134"] = len(set(list1) & set(list3) & set(list4))
        tmpdir["n234"] = len(set(list2) & set(list3) & set(list4))
        tmpdir["name1"] = name1
        tmpdir["name2"] = name2
        tmpdir["name3"] = name3
        tmpdir["name4"] = name4
        return tmpdir
    elif num == 5:
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        name1 = ""
        name2 = ""
        name3 = ""
        name4 = ""
        name5 = ""
        for line in open(inf,"r"):
            ele = line.strip().split("\t")
            if line.startswith("#"):
                name1 += ele[0][1:]
                name2 += ele[1]
                name3 += ele[2]
                name4 += ele[3]
                name5 += ele[4]
            elif not line.startswith("#"):
                try:
                    list1.append(ele[0])
                except IndexError:
                    pass
                try:
                    list2.append(ele[1])
                except IndexError:
                    pass
                try:
                    list3.append(ele[2])
                except IndexError:
                    pass
                try:
                    list4.append(ele[3])
                except IndexError:
                    pass
                try:
                    list5.append(ele[4])
                except IndexError:
                    pass
        tmpdir["area1"] = len(list1)
        tmpdir["area2"] = len(list2)
        tmpdir["area3"] = len(list3)
        tmpdir["area4"] = len(list4)
        tmpdir["area5"] = len(list5)
        tmpdir["n12"] = len(set(list1) & set(list2))
        tmpdir["n13"] = len(set(list1) & set(list3))
        tmpdir["n14"] = len(set(list1) & set(list4))
        tmpdir["n15"] = len(set(list1) & set(list5))
        tmpdir["n23"] = len(set(list2) & set(list3))
        tmpdir["n24"] = len(set(list2) & set(list4))
        tmpdir["n25"] = len(set(list2) & set(list5))
        tmpdir["n34"] = len(set(list3) & set(list4))
        tmpdir["n35"] = len(set(list3) & set(list5))
        tmpdir["n45"] = len(set(list4) & set(list5))
        tmpdir["n123"] = len(set(list1) & set(list2) & set(list3))
        tmpdir["n124"] = len(set(list1) & set(list2) & set(list4))
        tmpdir["n125"] = len(set(list1) & set(list2) & set(list5))
        tmpdir["n134"] = len(set(list1) & set(list3) & set(list4))
        tmpdir["n135"] = len(set(list1) & set(list3) & set(list5))
        tmpdir["n145"] = len(set(list1) & set(list4) & set(list5))
        tmpdir["n234"] = len(set(list2) & set(list3) & set(list4))
        tmpdir["n235"] = len(set(list2) & set(list3) & set(list5))
        tmpdir["n245"] = len(set(list2) & set(list4) & set(list5))
        tmpdir["n345"] = len(set(list3) & set(list4) & set(list5))
        tmpdir["n1234"] = len(set(list1) & set(list2) & set(list3) & set(list4))
        tmpdir["n1235"] = len(set(list1) & set(list2) & set(list3) & set(list5))
        tmpdir["n1245"] = len(set(list1) & set(list2) & set(list5) & set(list4))
        tmpdir["n1345"] = len(set(list1) & set(list3) & set(list4) & set(list5))
        tmpdir["n2345"] = len(set(list2) & set(list3) & set(list4) & set(list5))
        tmpdir["n12345"] = len(set(list1) & set(list2) & set(list3) & set(list4) & set(list5))
        tmpdir["name1"] = name1
        tmpdir["name2"] = name2
        tmpdir["name3"] = name3
        tmpdir["name4"] = name4
        tmpdir["name5"] = name5
        return tmpdir
def write2r(inf,num,ous):
    sys.stdout.write("[{0}] Write to venn.r\n".format(ltime()))
    try:
        out = open("{0}/tmp/venn.r".format(rds),"w")
    except:
        os.mkdir("{0}/tmp".format(rds))
        out = open("{0}/tmp/venn.r".format(rds), "w")
    out.write("library(VennDiagram)\n"
              "jpeg(file='{0}',width=700,height=480)\n".format(ous))
    if num == 2:
        valuedir = loadfile(inf, 2)
        out.write("draw.pairwise.venn({0},{1},{2},category = c({3},{4}),cat.cex = rep(1,2),"
                  "col=rep('black',2),euler.d = TRUE,scaled = TRUE,ext.text = TRUE,lwd = c(3,3),"
                  "fill = rainbow(2))\n"
                  "dev.off()\n".format(valuedir["area1"],valuedir["area2"],valuedir["n12"],valuedir["name1"],valuedir["name2"]))
        sys.stdout.write("[{0}] Venn.r have been done!\n".format(ltime()))
    elif num == 3:
        valuedir = loadfile(inf, 3)
        out.write("draw.triple.venn({0},{1},{2},{3},{4},{5},{6},cateory = c('{7}','{8}','{9}'),cat.cex=rep(1,3),"
                  "col=rep('black',3),euler.d = FALSE, scaled = FALSE,lwd=c(3,3,3),"
                  "fill = rainbow(3))\n"
                  "dev.off()\n".format(valuedir["area1"],valuedir["area2"],valuedir["area3"],valuedir["n12"],valuedir["n23"],valuedir["n13"],valuedir["n123"],
                                     valuedir["name1"],valuedir["name2"],valuedir["name3"]))
        sys.stdout.write("[{0}] Venn.r have been done!\n".format(ltime()))
        out.close()
    elif num == 4:
        valuedir = loadfile(inf, 4)
        out.write("draw.quad.venn({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},"
                  "category=c({15},{16},{17},{18}),cat.cex=rep(1,4)),col=rep('black',4),lwd=rep(3,4),fill=rainbow(4))\n"
                  "dev.off()\n".format(valuedir["area1"],valuedir["area2"],valuedir["area3"],valuedir["area4"],valuedir["n12"],valuedir["n13"],valuedir["n14"],
                                     valuedir["n23"], valuedir["n24"], valuedir["n34"],valuedir["n123"],valuedir["n124"],valuedir["n134"],valuedir["n234"],
                                     valuedir["n1234"],valuedir["name1"],valuedir["name2"],valuedir["name3"],valuedir["name4"]))
        sys.stdout.write("[{0}] Venn.r have been done!\n".format(ltime()))
        out.close()
    elif num == 5:
        valuedir = loadfile(inf, 5)
        out.write("draw.quintuple.venn(area1 = {0},"
                  "area2 = {1},"
                  "area3 = {2},"
                  "area4 = {3},"
                  "area5 = {4},"
                  "n12 = {5},"
                  "n13 = {6},"
                  "n14 = {7},"
                  "n15 = {8},"
                  "n23 = {9},"
                  "n24 = {10},"
                  "n25 = {11},"
                  "n34 = {12},"
                  "n35 = {13},"
                  "n45 = {14},"
                  "n123 = {15},"
                  "n124 = {16},"
                  "n125 = {17},"
                  "n134 = {18},"
                  "n135 = {19},"
                  "n145 = {20},"
                  "n234 = {21},"
                  "n235 = {22},"
                  "n245 = {23},"
                  "n345 = {24},"
                  "n1234 = {25},"
                  "n1235 = {26},"
                  "n1245 = {27},"
                  "n1345 = {28},"
                  "n2345 = {29},"
                  "n12345 = {30}"
              "category=c({31},{32},{33},{34},{35}),cat.cex=rep(1,4)),col=rep('black',4),lwd=rep(3,4),fill=rainbow(4))\n"
              "dev.off()\n".format(valuedir["area1"], valuedir["area2"], valuedir["area3"], valuedir["area4"],
                                   valuedir["area5"], valuedir["n12"], valuedir["n13"],
                                   valuedir["n14"], valuedir["n15"], valuedir["n23"], valuedir["n24"],
                                   valuedir["n25"], valuedir["n34"], valuedir["n35"],
                                   valuedir["n45"], valuedir["n123"], valuedir["n124"], valuedir["n125"],
                                   valuedir["n134"],valuedir["n135"],valuedir["n145"],valuedir["n234"],
                                   valuedir["n235"], valuedir["n245"], valuedir["n345"], valuedir["n1234"],
                                   valuedir["n1235"], valuedir["n1245"], valuedir["n1345"], valuedir["n2345"],
                                   valuedir["n12345"],valuedir["name1"],valuedir["name2"],valuedir["name3"],valuedir["name4"],valuedir["name5"]))
        sys.stdout.write("[{0}] Venn.r have been done!\n".format(ltime()))
        out.close()
    else:
        sys.stderr.write("[{0}] Error with num options".format(ltime()))
        exit(1)
def runr():
    os1 = os.system("Rscript {0}/tmp/venn.r".format(rds))
    if os1:
        sys.stderr.write("[{0}] Error for Rscript\n".format(ltime()))
        sys.exit(1)
    else:
        sys.stdout.write("[{0}] Get figure successfully".format(ltime()))
def main():
    args = opt()
    if args.ins == None or args.num == None or args.ous == None:
        os.system("python {0} -h".format(sys.argv[0]))
        exit("[{0}] Error: Incomplete Options".format(ltime()))

    inf = args.ins
    num = int(args.num)
    ous = args.ous
    write2r(inf,num,ous)
    runr()

if __name__ == "__main__":
    main()
