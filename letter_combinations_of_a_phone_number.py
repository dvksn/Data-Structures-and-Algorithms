def get_all_possible_string(result_list, curr_str, digits, dict_letter, curr_digit_index, length):
        if curr_digit_index == length:
            result_list = result_list + [curr_str]
            return result_list
        for val in  dict_letter[digits[curr_digit_index]]:
            temp_str = curr_str + val
            result_list = get_all_possible_string(result_list, temp_str, digits, dict_letter, curr_digit_index+1, length)
            
        return result_list
    
class Solution:
            
            
    def letterCombinations(self, digits: str) -> List[str]:
        result_list = []
        length = len(digits)
        if(length==0):
              return result_list
        dict_letter = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g','h', 'i'],
                      '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], 
                       '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'],
                       '9':['w','x', 'y','z']}
        
        result_list = get_all_possible_string(result_list, '', digits, dict_letter, 0,
                                              length)
        return result_list
