question_list=["how many continent are there?","what is the capital of india?","ng me kaun se course se padha jaata hai?"]
option_list=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling tourism","agriculture"]]
ans_list=[2,1,4]
i=0
while i<len(question_list):mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
i=0
while i<len(mainStr):
    (mainStr).pop()
    print(mainStr[i])
    i=i+1
    print(question_list[i])
    j=0
    while j<len(option_list[i]):
        print(option_list[i][j])
        j=j+1
    a=option_list
    b=ans_list
    lifeline=int(input("enter any choice"))
    if lifeline==5050:
        print(a)
    ans=int(input("enter any choice"))
    if ans==ans_list:
        print("correct",ans)
    else:
        print("wrong",ans)
    i=i+1