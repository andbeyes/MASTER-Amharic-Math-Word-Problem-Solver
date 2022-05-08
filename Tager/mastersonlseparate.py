def masterSolveSeparate(question):
    keyJoinTypes=["ሸጠ","አካፈለ","ጫነ","ሰጠ","ጨመረ","አሰቀመጠ","ተከለ","ደመረ"]
    
    AWP=[{"በፀጋው":"NNP","7":"CD","ብርቱኳኖች":"NNP","አሉት":"VBZ"},{"በእውነት":"NNP","3":"CD","ተጨማሪ":"NNP","ብርቱኳኖችን":"NNP","ሰጠችው":"VBD"}]
    AWP2=[{"ሩት":"NNP","12": "CD","ጌጦች":"NNP","አሉአት":"VBZ"},{"5":"CD","ለርብቃ":"NNP","ሰጠች":"VBD"},{"ሩት":"NNP","ስንት":"","ጌጦች":"NNP","ይቀሩአታል":"VBZ","?":"QUESM"}]
    
    possessionKeys=["አሉት","አሉአት"];
    transferKeys=["ሰጠችው","ሰጠች"];
    #STEP 1: Identifying owners
    FirNNP="";
    SecNNP="";
    fval="NNP"
    amo="CD"
    FDict=AWP2[0];
    SecDict=AWP2[1];
    for name,val in FDict.items():
        if val==fval:
            FirNNP=name
            break
    for name,val in SecDict.items():
        if val==fval:
            SecNNP=name
            break
    PE1=0;   #flag to indicate if the first sentence contains possessionKeys
    for y in possessionKeys:
        if y in AWP2[0].keys():
            PE1=1;
    TR=0;   #flag to indicate if the second sentence contains transfer words
    for x in transferKeys:
        if x in AWP2[1].keys():
            TR=1;
    OWNER1="";
    OWNER2="";
    if PE1==1 and SecNNP!=FirNNP and TR==1:
        OWNER1=FirNNP;
        OWNER2=SecNNP;
    #OWNER1 and OWNER2 are identified
    #step 2: Identify objects and amount
    object1="";
    object2="";
    amount1=0;
    amount2=0;
    for obj,val in FDict.items():
        if val==fval:
            object1=obj
        if val==amo:
            amount1=int(obj)
    for obj,val in SecDict.items():
        if val==fval:
            object2=obj
        if val==amo:
            amount2=int(obj)
    #step 3: Final NLP answer
    OWNER1Obj=amount1-amount2;
    FinAns="NLP Answer= "+OWNER1+" "+str(OWNER1Obj)+" "+object1+" "+possessionKeys[1]+"::"
    return FinAns

#print(masterSolveJoin("በፀጋው ሰባት ብርቱኳኖች አሉት፡፡ በእውነት 3 ተጨማሪ ብርቱኳኖችን ሰጠችው፡፡ በፀጋው በአጠቃላይ ስንት ብርቱኳኖች ይኖሩታል?"))
