/*

- Bunch of Accounts --> Need to mark each one as "Has Contacts" if it has any contacts 


*/


Set<Id> accountIds = new Set<Id>();
for(Account acc : accounts){
    accountIds.add(acc.Id);
}

Set<Id> accountWithContacts = new Set<Id>();
for(Contact con: [SELCT AccountId from Contact WHERE AccountId IN :accountIds]){
    accountWithContacts.add(con.AccountId)
}

for(Account acc: accounts){
    if(accountWithContacts.contains(acc.Id)){
        acc.Has_Contacts__c = true;
    }
}






/*

>10k closed 
- List of opportunties -- find all the ones >10k

various layers or stages --> check for StageName field to know the status 

*/


List<Opportunity> allDeals = [SELECT Amount from Opportunity];

for(Opportunity d: allDeals){
    if(d.Amount >100000){
        bigDeals.add(d);
    }
}


/*
to identify big accounts
*/


List<Account> allAccounts = [SELECT Industry, AnnualRevenue FROM Account];
List<Account> bigTechAccounts = new List<Account>();

for(Account a: acc){
    if(a.Industry == 'Technology' && a.AnnualRevenue == '1000000'){
        bigTechAccounts.add(a)
    }
}





//  initalise or store some value in the variable 
// List<VariableType> variableName = <SOQL query> or new List<VariableType>();


/*

TTriggers - Automatic
Controller Methods - Manual 
Async Jobs - background 

*/

