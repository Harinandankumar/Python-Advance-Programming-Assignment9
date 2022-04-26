#!/usr/bin/env python
# coding: utf-8

# 1. YouTube offers different playback speed options for users. This allows
# users to increase or decrease the speed of the video content. Given the
# actual duration and playback speed of the video, calculate the playback
# duration of the video.
# Examples
# playback_duration(&quot;00:30:00&quot;, 2) ➞ &quot;00:15:00&quot;
# playback_duration(&quot;01:20:00&quot;, 1.5) ➞ &quot;00:53:20&quot;
# playback_duration(&quot;51:20:09&quot;, 0.5) ➞ &quot;102:40:18&quot;
# 
# 
# 
# 
#         
#         
#         
#         
#         
#         
# Ans:-

# In[1]:


def playback_duration(in_time,playback_speed):
    time = in_time.split(":")
    time_in_secs = (3600*int(time[0])+60*int(time[1])+int(time[2]))/playback_speed
    f_time_in_hours = str(int(time_in_secs/3600)) if time_in_secs > 3600 else '00'
    f_time_in_mins = str(int((time_in_secs%3600)/60)) if (time_in_secs)%3600 > 60 else '00'
    f_time_in_secs = str(int((time_in_secs%3600)%60)) if ((time_in_secs)%3600)%60 > 0 else '00'   
    output = f'{f_time_in_hours}:{f_time_in_mins}:{f_time_in_secs}'
    print(f'playback_duration{in_time, playback_speed} ➞ {output}')
    
playback_duration("00:30:00", 2)
playback_duration("01:20:00", 1.5)
playback_duration("51:20:09", 0.5) 


# 2. We needs your help to construct a building which will be a pile of n cubes.
# The cube at the bottom will have a volume of n^3, the cube above will have
# volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
# Given the total volume m of the building, can you find the number of cubes n
# required for the building?
# In other words, you have to return an integer n such that:
# n^3 + (n-1)^3 + ... + 1^3 == m
# Return None if there is no such number.
# Examples
# pile_of_cubes(1071225) ➞ 45
# pile_of_cubes(4183059834009) ➞ 2022
# pile_of_cubes(16) ➞ None
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def pile_of_cubes(in_volume):
   out_volume = 0
   output = 0
   for cube in range(1,in_volume):
       out_volume += pow(cube,3)
       if in_volume <= out_volume:
           output = cube if in_volume == out_volume else None
           break
   print(f'pile_of_cubes({in_volume}) ➞ {output}')

pile_of_cubes(1071225)
pile_of_cubes(4183059834009)
pile_of_cubes(16)


# 3. A fulcrum of a list is an integer such that all elements to the left of it and all
# elements to the right of it sum to the same value. Write a function that finds
# the fulcrum of a list.
# To illustrate:
# find_fulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
# // Since [3, 1, 5] and [4, 6, -1] both sum to 9
# Examples
# 
# find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4
# find_fulcrum([9, 1, 9]) ➞ 1
# find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0
# find_fulcrum([8, 8, 8, 8]) ➞ -1
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def find_fulcrum(in_list):
    output = -1
    for ele in in_list:
        index_of_ele =in_list.index(ele)
        if sum(in_list[:index_of_ele]) == sum(in_list[index_of_ele+1:]):
            output = ele
            break
    print(f'find_fulcrum({in_list}) ➞ {output}')
        
find_fulcrum([3, 1, 5, 2, 4, 6, -1])
find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3])
find_fulcrum([9, 1, 9])
find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3])
find_fulcrum([8, 8, 8, 8])


# 4. Given a list of integers representing the color of each sock, determine how
# many pairs of socks with matching colors there are. For example, there are 7
# socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of
# color 2. There are three odd socks left, one of each color. The number of
# pairs is 2.
# Create a function that returns an integer representing the number of matching
# pairs of socks that are available.
# Examples
# sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3
# sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4
# sock_merchant([]) ➞ 0
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def sock_merchant(in_list):
    paired_socks = {}
    output = 0
    for ele in in_list:
        if ele in paired_socks:
            paired_socks[ele]+=1
        else:
            paired_socks[ele]=1
    for pair in paired_socks.values():
        output += pair//2
    print(f'sock_merchant({in_list}) ➞ {output}')
    

sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90])
sock_merchant([])


# 5. Create a function that takes a string containing integers as well as other
# characters and return the sum of the negative integers only.
# Examples
# negative_sum(&quot;-12 13%14&amp;-11&quot;) ➞ -23
# # -12 + -11 = -23
# negative_sum(&quot;22 13%14&amp;-11-22 13 12&quot;) ➞ -33
# # -11 + -22 = -33
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[6]:


import re
def negative_sum(in_string):
    pattern = '-\d+'
    output = sum([int(ele) for ele in re.findall(pattern,in_string)])
    print(f'negative_sum("{in_string}") ➞ {output}')
    
negative_sum("-12 13%14&-11")
negative_sum("22 13%14&-11-22 13 12")

