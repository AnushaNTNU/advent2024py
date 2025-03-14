#!/usr/bin/python3
#======================================
#   Day6 Advent of the code
#   
#======================================
#
# Guard moves: 
#   If there is something directly in front of you:
#     turn right 90 degrees.
#   Otherwise, 
#     take a step forward.
#
#
# Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
#
# --------------------------
# general approach:
#  * load text file
#  * find starting position and heading
#  * track moving
#
#  structures: 
#    * map
#    * traced path

# symbols
symbs = {'free':'.','obstacle':'#','visited':'X','guard':'^'}

# default direction of the guard
defdi = [0,-1]

fpath_input1 = '../inputs/day6.dat'


def loadmap (fname):
  # loads the map from a file
  fi = open(fname,'r')
  lmap = []
  for aline in fi.readlines():
    lmap.append(list(aline[:-1]))
  fi.close()
  return lmap


def countsym(lmap, sym):
  nunique = 0
  for liy in lmap:
    nunique+= liy.count(sym)
  return  nunique 



def findpos (lmap):
  ax0 = 0
  ay0 = 0
  for liy in lmap:
    if symbs['guard'] in liy:
      ax0 = liy.index(symbs['guard'])
      break
    else:
      ay0+=1
  return  [ax0,ay0] 


def walk (lmap, pos0, dir0):
  # walks the guard
  #  * lmap: map of the labyrinh
  #  * pos0: coordinates of starting position
  #  * dir0: starting heading of the guard
  #
  nposmax = 1000000
  # initialize
  poss = [pos0]
  bounds = [[0,len(lmap[0])],[0,len(lmap)]]
  [ax,ay] = pos0
  [dix,diy]=dir0
  lmap[ay][ax]=symbs['visited'] 
  npos = 0
  while(npos<nposmax): # prevent infinite loop
    # print(" ({}, {})".format(ax,ay))   ##debug
    # within map?
    if (((ax+dix)<bounds[0][0])|((ax+dix)>=bounds[0][1])|((ay+diy)<bounds[1][0])|((ay+diy)>=bounds[1][1])):
      break
    # try step
    if (lmap[ay+diy][ax+dix]==symbs['obstacle']):
      # if obstacle, turn right 90 deg
      if(dix==1):
        dix= 0
        diy= 1
      elif(diy==1):
        dix =-1
        diy = 0
      elif(dix==-1):
        dix = 0
        diy = -1
      else:
        dix = 1
        diy = 0 
    else:
      # just make forward step
      ax   +=dix
      ay   +=diy
      # count step and mark position
      npos +=1   
      lmap[ay][ax]=symbs['visited']      
  # return map
  return lmap
  

# test it 
themap = loadmap('day6test.dat')
# find position
apos0 = findpos(themap)

# simple walk
lmap_test = walk(themap,apos0,defdi)


print("Test result: {} steps".format(countsym(themap,symbs['visited'])))

print("Now let us try it with a bigger map:")
# now with a bigger map
themap = loadmap(fpath_input1)
# find position
apos0 = findpos(themap)

lmap1 = walk(themap,apos0,defdi)


print("Result first part: {} steps".format(countsym(themap,symbs['visited'])))
print("verified")



