# -*- coding:utf-8 -*-
class ParseError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, object):
    # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

# word list are a list of tuples
def peek(word_list): # 找出第一个词type
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

## skip the first continuous elements which match word_type
def skip(word_list, word_type):# word_list changes each loop
    while peek(word_list) == word_type:
        match(word_list, word_type)  # no return

def parse_verb(word_list):
    skip(word_list, 'stop') #过滤掉从第一个开始的连续个「stop」类词

    if peek(word_list) == 'verb':
        return match(word_list, 'verb') #如果找到verb,word_list会自动减少一个
    else:
        raise ParseError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParseError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list) # subj来自外部
    obj = parse_object(word_list)

    return Sentence(subj,verb,obj) # 返回sentence类

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParseError("Must start with subject, object, or verb not: %s" %start)
