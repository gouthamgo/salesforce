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


//==========================================


Account newAccount = new Account();
newAccount.Name = 'ACME'
newAccount.Industry = 'Tech'

insert newAccount;

System.debug(newAccount.Id);

// ===================

/*
create primary contact from every account of anuual revenue of >50k 
*/


List<Account> allAccounts = [SELECT Id, Name, AnnualRevenue FROM Account];

List<Account> filterAccs = new List<Account>();

for(Account acc: allAccounts){
    if(acc.AnnualRevenue > 50000){
        filterAccs.add(acc)
    }
}
// now i got my filtered accounts

List<Contact> newContacts = new List<Contact>();
for(Account acc: filterAccs){
    Contact newContact = new Contact();
    
    newContact.LastName = 'Primary Contact';
    newContact.AccountId = acc.Id;
    newContacts.add(newContact);
}

insert newContacts;


//===================================================

/*
Opportunites >100k
StageName == High Value to be set 

*/


public static void markHighOpps(){

    // Query
    List<Opportunity> bigOpps = [SELECT Id, Amount, StageName FROM Opportunity WHERE Amount > 100000]

    for(Opportunity opp: bigOpps){
        opp.StageName = 'High Value';
    }

    update bigOpps;

}


/// ===================================

List<Contact> oldContacts = [SELECT Id FROM Contact WHERE CreatedDate < LAST_YEAR];

delete oldContacts;

// ==========================

/* Relationship Queries 

Parent to child queries --> One Account --> Many Contacts 
*/


Account acc = [SELECT Id,Name, (SELECT Id, LastName FROM Contacts) FROM LIMIT 1];

List<Contact> contacts = acc.Contacts;


// child to parent 

List<Contact> contacts = [SELECT Id, LastName, Account.Name, Account.Industry FROM Contact];

for(Contact con: contacts){
    System.debug(con.LastName + 'works at' + con.Account.Name);
}


//==========================================


/*
find acconts --> revenue > 20k in Tech Industry 
for each of those accounts - get all their current contacts 
create a copy of each contact ( same last name + email but add "-Backup" to LastName)
Link the new copied contacts to the same accounts 


*/


