def masterSolvePartPartWhole(question):
    keyJoinTypes=["ሸጠ","አካፈለ","ጫነ","ሰጠ","ጨመረ","አሰቀመጠ","ተከለ","ደመረ"]
    
    AWP=[{"በፀጋው":"NNP","7":"CD","ብርቱኳኖች":"NNP","አሉት":"VBZ"},{"በእውነት":"NNP","3":"CD","ተጨማሪ":"NNP","ብርቱኳኖችን":"NNP","ሰጠችው":"VBD"}]
    AWP2=[{"ሩት":"NNP","12": "CD","ጌጦች":"NNP","አሉአት":"VBZ"},{"5":"CD","ለርብቃ":"NNP","ሰጠች":"VBD"},{"ሩት":"NNP","ስንት":"ADJ","ጌጦች":"NNP","ይቀሩአታል":"VBZ","?":"QUESM"}]

    AWP3=[{"6":"CD","ወንዶችና":"NNP","7":"CD","ሴቶች":"NNP","በእጅ-ኳስ":"NNP","ቡድን":"NNP","ውስጥ":"PRP","አሉ":"NNP"},{"በአጠቃላይ":"NNP","ቡድኑ":"NNP","ስንት":"ADJ","ልጆችን":"NNP","ይዞአል":"VBZ","?":"QUESM"}];
    possessionKeys=["አሉት","አሉአት","አሉ","ይዞአል","አሉ"];
    transferKeys=["ሰጠችው","ሰጠች"];
    #STEP 1: Identifying owners
    FirNNP="";
    SecNNP="";
    fval="NNP"
    amo="CD"
    FDict=AWP3[0];
    #SecDict=AWP3[1];
    for name,val in FDict.items():
        if val==fval:
            FirNNP=name
            break
    i=0;
    for name,val in FDict.items():
        if i==2:
            break
        if val==fval:
            SecNNP=name
            i=i+1;            
    #step 2: Identify objects and amount
    amount1=0;
    amount2=0;
    i=0;
    for obj,val in FDict.items():
        if val==amo:
            amount1=int(obj)
            break;
    for obj,val in FDict.items():
        if i==2:
            break
        if val==amo:
            amount2=int(obj)
            i=i+1;
    #step 3: Final NLP answer
    OWNER1Obj=amount1+amount2;
    FinAns="NLP Answer= ቡድኑ "+str(OWNER1Obj)+" ልጆችን "+possessionKeys[3]+"::"
    return FinAns

#print(masterSolveJoin("በፀጋው ሰባት ብርቱኳኖች አሉት፡፡ በእውነት 3 ተጨማሪ ብርቱኳኖችን ሰጠችው፡፡ በፀጋው በአጠቃላይ ስንት ብርቱኳኖች ይኖሩታል?"))
