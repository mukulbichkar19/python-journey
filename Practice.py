from collections import Counter
import heapq
# Frequency Counting
# Given a string, find the first non-repeating character and return its index. If it doesn’t exist, return -1.
def first_non_repeating(input):
    count_map = Counter(input)
    for character in input:
        if(count_map[character] == 1):
            return character

#Given an integer array, find the top k frequent elements.
def top_k_frequent(input):
    int_count_map = Counter(input)
    topk = sorted(int_count_map.items(), key=lambda item:item[1], reverse=True) #Needs work

#Check if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_map_str1 = Counter(str1)
    char_map_str2 = Counter(str2)
    for k,v in char_map_str1.items():
        if k not in char_map_str2 and v != char_map_str2[k]:
            return False
    
    return True

#Given a string, group all anagrams together.
def group_anagrams(input):
    sorted_word_anagram_map = {}
    for word in input:
        key = tuple(sorted(word)) 
        if key in sorted_word_anagram_map:
            sorted_word_anagram_map[key].append(word)
        else:
            sorted_word_anagram_map[key] = [word]
    
    for k, v in sorted_word_anagram_map.items():
        print("Anagrams are: ", v)

# Set Usage
# Given two integer arrays, find their intersection (unique elements only).
def set_intersection(set1, set2):
    if set1 is None:
        return set2

    if set2 is None:
        return set1

    return set(set1).intersection(set(set2))

# Given an array, check if it contains duplicate elements.
def check_duplicates(input_lst):
    if len(input_lst) == 0:
        return False

    unique_elements = set()
    for n in input_lst:
        if n in unique_elements:
            return True
        unique_elements.add(n)
    
    return False

# Sorting with Containers
def sort_characters_by_freq(input_str):
    word_count_map = Counter(input_str)
    word_count_freq = sorted(word_count_map.items(), key=lambda item:item[1], reverse=True)
    for k,v in word_count_freq:
        print(k,'::',v)

# Given a list of tuples (name, score), sort by score descending, then name ascending.
def custom_sort_tuples(lst_of_tuples):
    for name, score in lst_of_tuples:
        print(name, score)
    sorted_by_score = sorted(lst_of_tuples, key = lambda tup:tup[1], reverse=True)
    sorted_by_name = sorted(sorted_by_score, key = lambda tup:tup[0])

# Given a list of intervals, merge all overlapping intervals.
def merge_overlapping_intervals(lst_of_intervals):
    sorted_intervals_by_start_time = sorted(lst_of_intervals, key=lambda tup:tup[0])
    st = sorted_intervals_by_start_time[0][0]
    end = sorted_intervals_by_start_time[0][1]
    merged_intervals = []
    for index in range(1, len(sorted_intervals_by_start_time)):
        if sorted_intervals_by_start_time[index][0] <= end:
            end = max(end, sorted_intervals_by_start_time[index][1])
        else:
            merged_intervals.append((st, end))
            st = sorted_intervals_by_start_time[index][0]
            end = sorted_intervals_by_start_time[index][1]
    merged_intervals.append((st, end))
    print('Merged Intervals: ', merged_intervals)

# Heap-Based Problems
# Find the k largest elements in an array.
def find_k_largest(lst, k):
    if len(lst) == 0:
        return None
    # Option 1: Using Heapify
    # heapq.heapify(lst)

    # updated_k = len(lst) - k
    
    # while updated_k != 0:
    #     heapq.heappop(lst)
    #     updated_k -= 1

    print('kth largest element is: ',heapq.heappop(lst))
    # Alternative Solution: Maintain a min heap of size k 
    min_heap = []
    for n in lst:
        heapq.heappush(min_heap, n)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    print('k largest elemt is: ', heapq.heappop(min_heap))
    

def k_smallest(lst, k):
    if len(lst) == 0:
        return None
    
    # Option 1: Using Heapify
    # heapq.heapify(lst)
    # k_ele = None
    # while k != 0:
    #     k_ele = heapq.heappop(lst)
    #     k -= 1
    
    # return k_ele

    # Option 2: Using max-heap of size k 
    max_heap = []
    for n in lst:
        heapq.heappush(max_heap, -n)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    return heapq.heappop(max_heap) * -1



def main():
    print('Inside main')
    print(f'First non-repeating character found: {first_non_repeating('rainbow')}')
    print(f'Top K elements from input array: {top_k_frequent([1,2,1,1,3,4,5,2,5,3,5])}')
    print(f'Are Strings Anagrams: {are_anagrams('iceman','mytasa')}')
    print(f'Group Anagrams: {group_anagrams(["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"])}')

    print('-----------------------------------------------------------------------------------')
    print(f'Intersection of 2 integer arrays is {set_intersection([1,2,3,4,5], [2,3,5,9,8,10])}')
    print(f'Does the list contain duplicates: {check_duplicates([1,2,3,4,5,2,1,3])}')
    print(f'The input string count map: {sort_characters_by_freq('eerttee')}')
    print(f'The custom sort of tuples: {custom_sort_tuples([('Akash', 10),('Deep', 109), ('Salu', 98), ('Bhanu', 87)])}')
    print(f'The overlap of intervals is: {merge_overlapping_intervals([(1,3),(2,4),(6,8),(9,10)])}')
    print('-----------------------------------------------------------------------------------')
    print(f'The kth largest element is: {find_k_largest([1,3,4,56,89,109,199,904,891], 3)}')
    print(f'The kth smallest element is: {k_smallest([1,3,4,56,89,109,199,904,891], 4)}')

main()