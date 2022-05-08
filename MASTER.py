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


import hm
def masterSolveJoin(question):

    hm.AF('E:/AQA/PUB AVE 2/python implementation/test.txt','E:/AQA/PUB AVE 2/python implementation/testo.txt', raw=True)

    sDict1={};
    sDict2={};
    raw_words=[];
    filtered_words=[];
    words=[];
    with open("E:/AQA/PUB AVE 2/python implementation/test.txt",encoding="utf-8") as file_in1:
        for lin in file_in1:
            #print(lin);
            words=lin.split();
        for wo in words:
            #if wo!=',':
            filtered_words.append(wo);
    with open("E:/AQA/PUB AVE 2/python implementation/testo.txt") as file_in:
        lines = []
        sentDict={};
        for line in file_in:
            lines.append(line)
            detLine=0;
            dkey='';
            dMng='';
        j=0;
        for i in range(len(lines)):
            st=lines[i].split();            
            if detLine==1:
                indx=lines[i].find("pos");
                #print(lines[i][indx:indx+5]);
                dKey=lines[i][indx+4:indx+5];
                sentDict[dMng]= dKey;
                j=j+1;
            if st[0]=='-':
                #print(st[1]);
                dMng=st[1];
                detLine=1;
            else:
                detLine=0;            
            i=i+1;        
        fl=0;
        #del sentDict[','];
        sentDict_val2=sentDict.values();
        sentDict_val = [];
        for el in sentDict_val2:
            sentDict_val.append(el);
        sentDictUpdate={};
        q=0;
        for kl in filtered_words:
            sentDictUpdate[kl]=sentDict_val[q];
            q=q+1;
        print(sentDict);
        print(sentDictUpdate);
        for k,m in sentDictUpdate.items():
            if k!=',' and fl==0:
                km=m;
                if k.isdigit()==True:
                    km='CD';
                if km=='n':
                    km='NNP';
                elif km=='v':
                    km='VBZ';
                sDict1[k]=km;
            elif k!=',' and fl==1:
                km=m;
                if k.isdigit()==True:
                    km='CD';
                if km=='n':
                    km='NNP';
                elif km=='v':
                    km='VBZ';
                sDict2[k]=km;
            elif k==',':
                fl=1;   
        #print(kl);
   # print(sentDict);
       # print(sDict1);
        #print(sDict2);
    st2='በፀጋው ሰባት ብርቱኳኖች አሉት እንዲሁም በእውነት 3 ተጨማሪ ብርቱኳኖችን ሰጠችው በፀጋው በአጠቃላይ ስንት ብርቱኳኖች ይኖሩታል'
    keyJoinTypes=["ሸጠ","አካፈለ","ጫነ","ሰጠ","ጨመረ","አሰቀመጠ","ተከለ","ደመረ"]    
   # AWP=[{"በፀጋው":"NNP","7":"CD","ብርቱኳኖች":"NNP","አሉት":"VBZ"},{"በእውነት":"NNP","3":"CD","ተጨማሪ":"NNP","ብርቱኳኖችን":"NNP","ሰጠችው":"VBD"}]
    AWP=[{},{}];
    AWP[0]=sDict1;
    AWP[1]=sDict2;

    #own1=AWP[0]["በፀጋው"]
    possessionKeys=["አሉት"];
    transferKeys=["ሰጠችው"];
    #STEP 1: Identifying owners
    FirNNP="";
    SecNNP="";
    fval="NNP"
    amo="CD"
    OWNER1="";
    OWNER2="";
    FDict=AWP[0];
    SecDict=AWP[1];
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
        if y in AWP[0].keys():
            PE1=1;
            TR=0;   #flag to indicate if the second sentence contains transfer words
    for x in transferKeys:
        if x in AWP[1].keys():
            TR=1;            
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
    OWNER1Obj=amount1+amount2;
    FinAns="NLP Answer= "+OWNER1+" "+str(OWNER1Obj)+" "+object1+" "+possessionKeys[0]+"::"
    return FinAns
print(masterSolveJoin("በፀጋው ሰባት ብርቱኳኖች አሉት፡፡ በእውነት 3 ተጨማሪ ብርቱኳኖችን ሰጠችው፡፡ በፀጋው በአጠቃላይ ስንት ብርቱኳኖች ይኖሩታል?"))

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

