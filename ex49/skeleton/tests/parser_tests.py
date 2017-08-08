# test files
from nose.tools import *
from ex49.ex49 import *

def test_peek():
    wl =  [('stop','the'),('noun','princess')]
    assert_equal(peek(wl), 'stop')

def test_match():
    wl =  [('stop','in'),('noun','princess')]
    assert_equal(match(wl, 'stop'), ('stop','in'))
    wl =  [('stop','in'),('noun','princess')]
    assert_equal(match(wl, 'noun'), None)

def test_skip():
    wl =  [('stop','in'),('noun','princess'),('stop','the'),('direction','north'),('stop','of'),('noun','bear')]
    skip(wl, 'stop')
    assert_equal(wl, [('noun','princess'),
                      ('stop','the'),
                      ('direction','north'),
                      ('stop','of'),
                      ('noun','bear')])

def test_parse_verb():
    wl =  [('stop','in'),('verb','go'),('direction','north')]
    assert_equal(parse_verb(wl), ('verb','go'))
    assert_raises(Exception, parse_verb, [('stop','the'), ('noun', 'bear')] )


def test_parse_object():
    wl1=  [('stop','the'),('direction','north')]
    wl2 =  [('stop','the'),('noun','bear')]
    assert_equal(parse_object(wl1), ('direction','north'))
    assert_equal(parse_object(wl2), ('noun', 'bear'))
    assert_raises(Exception, parse_object, ['verb','kill'] )

def test_parse_subject():
    wl = [('verb', 'kill'), ('stop','the'), ('noun','bear')]
    subj = ('noun', 'princess')
    result = parse_subject(wl, subj)
    assert_equal(result.subject, 'princess')
    assert_equal(result.verb, 'kill')
    assert_equal(result.object, 'bear')

def test_parse_sentence():
    wl = [('stop','the'),
          ('noun', 'prince'),
          ('verb', 'kill'),
          ('stop', 'the'),
          ('noun', 'bear')]
    result = parse_sentence(wl)
    assert_equal(result.subject, 'prince')
    assert_equal(result.verb, 'kill')
    assert_equal(result.object, 'bear')
    assert_raises(Exception, parse_sentence, [('conterj', 'and')]  )


#assert_raises(Exception, parse_verb, [('stop','the'), ('noun', 'bear')] )
#assert_raises("Expected a noun or direction next.", parse_noun, ['verb','kill'] )
#assert_raises("Expected a verb next.", parse_sentence, [('conterj', 'and')]  )
