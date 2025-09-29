/*
For maps 

put(key,value) - store something
get(key,value) - lookup something

just a a lookupp table 

*/

List<String> names = new List<String>{'A', 'B','C'};
List<String> levels = new List<String>{'T1', 'T2','T3'}


//lets build a lookup table here 
Map<String,String> book = new Map<String>();
for(Integer i = 0; i< names.size(); i++){
    book.put(names[i],levels[i])

}

String whatLevel = book.get('B') // returns T2



//============================

Map<Id,Contact> contactByAccountId = new Map<Is,Contact>();
for (Contact con: [SELECT Id, AccountId FROM Contact WHERE AccountId IN:accountIds]){
    contactByAccountId.put(con.AccountId,con) // ID -> Contact
}

for(Account acc: accounts){
    Contact relatedContact = contactByAccountId.get(acc.Id)
}

//===============================================================




List<Opportunity> opps = [SELECT Id,Name, AccountId FROM Opportunity];
List<Account> accounts = [SELECT Id, Name FROM Account WHERE Id IN: accountIds];

Map<Id, String> accountNameById = new Map<Id,String>();

for(Account acc: accounts){
    accountNameById.put(acc.Id, acc.Name)
}

String accountName = accountNameById.get(someAccountID);

// ===========================================================


// what if one account has multiple contacts 

// each account points to a list of contacts --> one to many relationship 


 Map<Id,List<Contact>> contactsByAccountId = new Map<Id,List<Contact>>();

 for(Contact con: allContacts){
    // check --> does this account already have a list in our map 
    if(!contactByAccountId.containsKey(con.AccountId)){
        contactByAccountId.put(con.AccountId, new List<Contact>>()); // no list exist yet - create an empty one 
    }

    contactByAccountId.get(con.AccountId).add(con);// add this contact to the accoutns list 
 }


//===========================================

/*

Opportuniteis > 50k
stage - proposal 
want to know the account name of each of these opportunities 

*/

// define class - static cz i dont return anything
public class findOpportunties{

    public static void findOpportunties(){

    
    List<Opportunity> allOpps = [SELECT Id, Name, Amount, StageName, AccountId FROM Opportunity];
    List<Opportunity> filterOpps = new List<Opportunity>();

    for(Opportunity opp: allOpps){
        if(opp.Amount > 500000 && opp.StageName == 'proposal'){
            filterOpps.add(opp);
        }
    }

    // collected all the accountIds
    Set<Id> accountIds = new Set<Id>();
    for(Opportunity opp: filterOpps){
        accountIds.add(opp.AccountId)
    }

    List<Account> accounts = [SELECT Id, Name FROM Account WHERE Id IN:accountIds];

    Map<Id, String> accountNameById = new Map<Id, String>();

    for(Account acc: accounts){
        accountNameById.put(acc.Id, acc.Name)
    }

    for(Opportunity opp: filterOpps){
        String accountName = accountNameById.get(opp.AccountId);
        System.debug(opp.Name + '- Account' + accountName)
    }

    }

}