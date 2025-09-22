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




